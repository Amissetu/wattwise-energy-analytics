from pathlib import Path

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from prophet import Prophet

ROOT_DIR = Path(__file__).resolve().parent
DATA_PATH = ROOT_DIR / "cleaned_data_power_consumption.txt"

ZONE_LABELS = {
    "sub_metering_1": "Kitchen",
    "sub_metering_2": "Laundry",
    "sub_metering_3": "HVAC / Water Heating",
}


@st.cache_data
def load_data() -> pd.DataFrame:
    df = pd.read_csv(DATA_PATH, parse_dates=["datetime"], low_memory=False)
    if df.empty:
        return pd.DataFrame(columns=["datetime", "global_active_power", "global_reactive_power", "voltage", "global_intensity", "sub_metering_1", "sub_metering_2", "sub_metering_3"])

    df = df.sort_values("datetime").reset_index(drop=True)
    df["hour"] = df["datetime"].dt.hour
    df["day_name"] = df["datetime"].dt.day_name()
    df["season"] = df["datetime"].dt.month.map(
        {
            12: "Winter",
            1: "Winter",
            2: "Winter",
            3: "Spring",
            4: "Spring",
            5: "Spring",
            6: "Summer",
            7: "Summer",
            8: "Summer",
            9: "Autumn",
            10: "Autumn",
            11: "Autumn",
        }
    )

    def time_band(hour: int) -> str:
        if 5 <= hour < 12:
            return "Morning"
        if 12 <= hour < 17:
            return "Afternoon"
        if 17 <= hour < 22:
            return "Evening"
        return "Night"

    df["time_band"] = df["hour"].apply(time_band)
    return df


@st.cache_data
def build_forecast(df: pd.DataFrame, forecast_days: int) -> pd.DataFrame:
    if df.empty:
        return pd.DataFrame(columns=["ds", "yhat", "yhat_lower", "yhat_upper"])

    daily = (
        df.assign(ds=df["datetime"].dt.floor("D"))
        .groupby("ds", as_index=False)["global_active_power"]
        .mean()
        .rename(columns={"global_active_power": "y"})
        .sort_values("ds")
        .reset_index(drop=True)
    )

    if len(daily) < 2:
        return pd.DataFrame(columns=["ds", "yhat", "yhat_lower", "yhat_upper"])

    model = Prophet(yearly_seasonality=True, weekly_seasonality=True, daily_seasonality=False)
    model.fit(daily[["ds", "y"]])
    future = model.make_future_dataframe(periods=forecast_days)
    forecast = model.predict(future)
    return forecast


def format_kw(value: float) -> str:
    return f"{value:,.2f} kW"


st.set_page_config(layout="wide", page_title="WattWise Energy Analytics", page_icon="⚡")


df = load_data()
if df.empty:
    st.error("The dataset could not be loaded. Please verify the file exists and is readable.")
    st.stop()

min_date = df["datetime"].min().date()
max_date = df["datetime"].max().date()

with st.sidebar:
    st.image("https://images.unsplash.com/photo-1497435334941-8c899ee9e8e9?auto=format&fit=crop&w=1200&q=80", width=280)
    st.title("Controls")

    selected_range = st.date_input("Date range", value=(min_date, max_date), min_value=min_date, max_value=max_date)
    if isinstance(selected_range, tuple) and len(selected_range) == 2:
        start_date, end_date = selected_range
    else:
        start_date = end_date = selected_range

    metric_options = [
        ("Global Active Power", "global_active_power"),
        ("Global Reactive Power", "global_reactive_power"),
        ("Voltage", "voltage"),
        ("Global Intensity", "global_intensity"),
        ("Kitchen", "sub_metering_1"),
        ("Laundry", "sub_metering_2"),
        ("HVAC / Water Heating", "sub_metering_3"),
    ]
    selected_metric_name, selected_metric_col = st.selectbox("Metric", metric_options)

    selected_region = st.selectbox("Region focus", ["All regions", "sub_metering_1", "sub_metering_2", "sub_metering_3"])
    selected_time_band = st.multiselect("Demand segment", ["Morning", "Afternoon", "Evening", "Night"], default=["Morning", "Afternoon", "Evening", "Night"])
    selected_seasons = st.multiselect("Season", sorted(df["season"].dropna().unique().tolist()), default=sorted(df["season"].dropna().unique().tolist()))
    forecast_days = st.slider("Forecast horizon (days)", min_value=7, max_value=120, value=30)

filtered = df[
    (df["datetime"].dt.date >= start_date)
    & (df["datetime"].dt.date <= end_date)
    & (df["time_band"].isin(selected_time_band))
    & (df["season"].isin(selected_seasons))
].copy()

if selected_region != "All regions":
    filtered = filtered[filtered[selected_region].notna()].copy()

if filtered.empty:
    st.warning("No data matches the current filters. Please widen the date range or select more periods.")
    st.stop()

filtered = filtered.sort_values("datetime").reset_index(drop=True)
peak_idx = filtered[selected_metric_col].idxmax()
peak_record = filtered.loc[peak_idx]
peak_time = peak_record["datetime"].strftime("%Y-%m-%d %H:%M")
peak_value = peak_record[selected_metric_col]
mean_load = filtered[selected_metric_col].mean()
total_load = filtered[selected_metric_col].sum()

st.title("WattWise Energy Analytics Dashboard")
st.caption("Interactive analysis of household electricity demand, peak behaviour, and future forecast trends.")

kpis = st.columns(4)
kpis[0].metric("Average load", format_kw(mean_load))
kpis[1].metric("Peak demand", format_kw(peak_value))
kpis[2].metric("Peak time", peak_time)
kpis[3].metric("Total observed load", format_kw(total_load))

overview_tab, patterns_tab, forecast_tab, recommendations_tab = st.tabs(["Overview", "Patterns", "Forecast", "Recommendations"])

with overview_tab:
    trend_fig = px.line(
        filtered,
        x="datetime",
        y=selected_metric_col,
        title=f"{selected_metric_name} over time",
        labels={"datetime": "Date and time", selected_metric_col: selected_metric_name},
        color_discrete_sequence=["#1f77b4"],
    )
    trend_fig.add_vline(x=peak_record["datetime"], line_dash="dash", line_color="red", annotation_text="Peak")
    trend_fig.update_layout(hovermode="x unified", template="plotly_white")
    st.plotly_chart(trend_fig, use_container_width=True)

    left_col, right_col = st.columns(2)

    hist_fig = px.histogram(
        filtered,
        x=selected_metric_col,
        nbins=30,
        title=f"Distribution of {selected_metric_name}",
        labels={selected_metric_col: selected_metric_name},
        color_discrete_sequence=["#7f7fff"],
    )
    left_col.plotly_chart(hist_fig, use_container_width=True)

    box_fig = px.box(
        filtered,
        x="time_band",
        y=selected_metric_col,
        title=f"{selected_metric_name} by demand segment",
        labels={"time_band": "Demand segment", selected_metric_col: selected_metric_name},
        color="time_band",
    )
    right_col.plotly_chart(box_fig, use_container_width=True)

with patterns_tab:
    region_daily = (
        filtered[["datetime", "sub_metering_1", "sub_metering_2", "sub_metering_3"]]
        .assign(date=filtered["datetime"].dt.floor("D"))
        .groupby("date", as_index=False)[["sub_metering_1", "sub_metering_2", "sub_metering_3"]]
        .sum()
    )
    region_line = px.line(
        region_daily,
        x="date",
        y=["sub_metering_1", "sub_metering_2", "sub_metering_3"],
        title="Daily energy use by region",
        labels={"date": "Date", "value": "Energy use (kW)"},
    )
    region_line.update_layout(template="plotly_white", legend_title_text="Region")
    st.plotly_chart(region_line, use_container_width=True)

    heat_data = filtered.groupby(["day_name", "hour"])[selected_metric_col].mean().unstack(fill_value=0)
    ordered_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    heat_data = heat_data.reindex(index=ordered_days, fill_value=0)

    heatmap_fig = go.Figure(
        data=go.Heatmap(
            z=heat_data.values,
            x=heat_data.columns.tolist(),
            y=heat_data.index.tolist(),
            colorscale="YlOrRd",
            hovertemplate="Hour: %{x}<br>Day: %{y}<br>Value: %{z:.2f}<extra></extra>",
        )
    )
    heatmap_fig.update_layout(
        title=f"{selected_metric_name} by hour and day of week",
        xaxis_title="Hour of day",
        yaxis_title="Day of week",
        template="plotly_white",
    )
    st.plotly_chart(heatmap_fig, use_container_width=True)

    scatter_fig = px.scatter(
        filtered,
        x="voltage",
        y=selected_metric_col,
        color="time_band",
        title=f"{selected_metric_name} vs voltage",
        labels={"voltage": "Voltage", selected_metric_col: selected_metric_name},
        hover_data={"datetime": True},
    )
    scatter_fig.update_layout(template="plotly_white")
    st.plotly_chart(scatter_fig, use_container_width=True)

with forecast_tab:
    forecast = build_forecast(filtered, forecast_days)
    if forecast.empty:
        st.info("Not enough data is available in the selected range to generate a stable forecast. Try a broader time window.")
    else:
        forecast_fig = go.Figure()
        forecast_fig.add_trace(go.Scatter(x=forecast["ds"], y=forecast["yhat"], mode="lines", name="Forecast", line=dict(color="#2ca02c", width=3)))
        forecast_fig.add_trace(go.Scatter(x=forecast["ds"], y=forecast["yhat_lower"], mode="lines", line=dict(width=0), name="Lower bound", showlegend=False))
        forecast_fig.add_trace(go.Scatter(x=forecast["ds"], y=forecast["yhat_upper"], mode="lines", line=dict(width=0), name="Upper bound", showlegend=False, fill="tonexty", fillcolor="rgba(44, 160, 44, 0.15)"))
        forecast_fig.update_layout(
            title="Projected future energy demand",
            xaxis_title="Date",
            yaxis_title="Average active power (kW)",
            template="plotly_white",
        )
        st.plotly_chart(forecast_fig, use_container_width=True)

        latest = forecast.iloc[-1]
        st.markdown("### Forecast summary")
        st.write(f"The model projects the next {forecast_days} days to average around {latest['yhat']:.2f} kW, with a likely range of {latest['yhat_lower']:.2f} to {latest['yhat_upper']:.2f} kW.")

with recommendations_tab:
    demand_by_segment = filtered.groupby("time_band")[selected_metric_col].mean().sort_values(ascending=False).reset_index()
    segment_bar = px.bar(
        demand_by_segment,
        x="time_band",
        y=selected_metric_col,
        title="Average demand by segment",
        labels={"time_band": "Demand segment", selected_metric_col: selected_metric_name},
        color_discrete_sequence=["#ff7f0e"],
    )
    st.plotly_chart(segment_bar, use_container_width=True)

    zone_summary = filtered[["sub_metering_1", "sub_metering_2", "sub_metering_3"]].mean().sort_values(ascending=False)
    zone_df = zone_summary.reset_index().rename(columns={"index": "Region", 0: "Average usage"})
    zone_df["Region"] = zone_df["Region"].map(ZONE_LABELS)

    zone_bar = px.bar(
        zone_df,
        x="Region",
        y="Average usage",
        title="Average load by region",
        labels={"Average usage": "Average load (kW)"},
        color_discrete_sequence=["#17becf"],
    )
    st.plotly_chart(zone_bar, use_container_width=True)

    corr = filtered[["global_active_power", "global_reactive_power", "voltage", "global_intensity", "sub_metering_1", "sub_metering_2", "sub_metering_3"]].corr()["global_active_power"].drop("global_active_power")
    corr_df = corr.sort_values(ascending=False).reset_index().rename(columns={"index": "Variable", 0: "Correlation"})

    peak_segment = demand_by_segment.iloc[0]["time_band"]
    top_region = zone_df.iloc[0]["Region"]
    strongest_driver = corr_df.iloc[0]["Variable"]

    st.markdown("### Energy efficiency story")
    st.write(
        f"The highest demand occurs during the **{peak_segment}** period, which suggests that high-load activities are clustered in a short timeframe. "
        f"The strongest driver of active demand is **{strongest_driver}**, pointing to the main source of power spikes. "
        f"The largest recurring contribution comes from **{top_region}**, making it the most important area for efficiency action."
    )

    st.markdown("### Recommended actions")
    st.markdown(
        f"1. Shift discretionary loads away from the **{peak_segment}** period and into off-peak hours.\n"
        f"2. Prioritise efficiency upgrades and smart scheduling in **{top_region}**.\n"
        "3. Monitor voltage and reactive power during peak periods to reduce waste and lower stress on the network.\n"
        "4. Use the forecast to plan seasonal demand management before spikes intensify."
    )

st.markdown("<hr>")
st.caption("Built for WattWise using interactive analytics and forecasting for smarter energy management.")

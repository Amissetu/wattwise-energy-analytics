from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

DATA_FILE = Path(__file__).resolve().parent / "cleaned_data_power_consumption"


@st.cache_data
def load_data(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    df["datetime"] = pd.to_datetime(df["datetime"])
    return df


def format_metric_name(name: str) -> str:
    return name.replace("_", " ").title()


def prepare_filtered_data(df: pd.DataFrame, start_date, end_date) -> pd.DataFrame:
    filtered = df[(df["datetime"].dt.date >= start_date) & (df["datetime"].dt.date <= end_date)].copy()
    if filtered.empty:
        return filtered

    filtered["day_name"] = filtered["datetime"].dt.day_name()
    filtered["hour"] = filtered["datetime"].dt.hour
    filtered["month"] = filtered["datetime"].dt.to_period("M").astype(str)
    return filtered


st.set_page_config(
    page_title="WattWise Energy Dashboard",
    page_icon="⚡",
    layout="wide",
)

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(180deg, #f4fafd 0%, #eef5ff 100%);
    }
    .block-container {
        padding-top: 1.5rem;
    }
    div[data-testid="stMetric"] {
        background: rgba(255,255,255,0.9);
        border: 1px solid #dfeafc;
        padding: 0.8rem;
        border-radius: 0.8rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

df = load_data(DATA_FILE)

with st.sidebar:
    st.header("Dashboard Controls")
    min_date = df["datetime"].min().date()
    max_date = df["datetime"].max().date()

    start_date, end_date = st.date_input(
        "Select date range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date,
    )

    selected_metric = st.selectbox(
        "Choose metric",
        options=[
            "global_active_power",
            "global_reactive_power",
            "voltage",
            "global_intensity",
            "sub_metering_1",
            "sub_metering_2",
            "sub_metering_3",
        ],
        index=0,
    )

    st.markdown("---")
    st.subheader("Insight Focus")
    st.write(
        "Explore usage patterns, peak demand periods, and household energy behaviour over time."
    )

st.title("WattWise Energy Analytics Dashboard")
st.caption("Interactive dashboard built from the cleaned household power consumption dataset.")

filtered_df = prepare_filtered_data(df, start_date, end_date)

if filtered_df.empty:
    st.warning("No data matches the selected date range. Please choose another range.")
    st.stop()

peak_idx = filtered_df[selected_metric].idxmax()
peak_row = filtered_df.loc[peak_idx]
peak_value = peak_row[selected_metric]
peak_time = peak_row["datetime"].strftime("%Y-%m-%d %H:%M:%S")

metric_label = format_metric_name(selected_metric)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Average " + metric_label, f"{filtered_df[selected_metric].mean():.2f}")
col2.metric("Peak " + metric_label, f"{filtered_df[selected_metric].max():.2f}")
col3.metric("Minimum " + metric_label, f"{filtered_df[selected_metric].min():.2f}")
col4.metric("Records", f"{len(filtered_df):,}")

st.info(
    f"The highest {metric_label.lower()} reading is {peak_value:.2f}, recorded on {peak_time}."
)

overview_tab, trend_tab, relationship_tab, narrative_tab = st.tabs(
    ["Overview", "Daily Patterns", "Relationships", "Narrative"]
)

with overview_tab:
    line_fig = px.line(
        filtered_df,
        x="datetime",
        y=selected_metric,
        title=f"{metric_label} Over Time",
        labels={"datetime": "Date/Time", selected_metric: metric_label},
        template="plotly_white",
    )
    line_fig.update_traces(line=dict(width=3))
    line_fig.update_layout(hovermode="x unified", margin=dict(l=20, r=20, t=50, b=20))
    st.plotly_chart(line_fig, use_container_width=True)

with trend_tab:
    hourly_summary = (
        filtered_df.groupby("hour")[selected_metric].mean().reset_index().rename(columns={"hour": "Hour"})
    )
    hourly_fig = px.bar(
        hourly_summary,
        x="Hour",
        y=selected_metric,
        title=f"Average {metric_label} by Hour of Day",
        labels={selected_metric: metric_label, "Hour": "Hour of Day"},
        template="plotly_white",
    )
    hourly_fig.update_layout(margin=dict(l=20, r=20, t=50, b=20))
    st.plotly_chart(hourly_fig, use_container_width=True)

    day_summary = (
        filtered_df.groupby("day_name")[selected_metric]
        .mean()
        .reindex(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
        .reset_index()
    )
    day_summary.columns = ["Day", selected_metric]
    day_fig = px.bar(
        day_summary,
        x="Day",
        y=selected_metric,
        title=f"Average {metric_label} by Day of Week",
        labels={selected_metric: metric_label},
        template="plotly_white",
    )
    day_fig.update_layout(margin=dict(l=20, r=20, t=50, b=20))
    st.plotly_chart(day_fig, use_container_width=True)

with relationship_tab:
    scatter_fig = px.scatter(
        filtered_df,
        x="global_intensity",
        y=selected_metric,
        color="day_name",
        title=f"{metric_label} vs Global Intensity",
        labels={
            "global_intensity": "Global Intensity",
            selected_metric: metric_label,
            "day_name": "Day",
        },
        template="plotly_white",
    )
    scatter_fig.update_layout(legend_title_text="Day", margin=dict(l=20, r=20, t=50, b=20))
    st.plotly_chart(scatter_fig, use_container_width=True)

with narrative_tab:
    st.subheader("Dashboard Narrative")
    st.markdown(
        f"- The selected metric is **{metric_label.lower()}** across the period from **{start_date}** to **{end_date}**.\n"
        f"- The average value during this range is **{filtered_df[selected_metric].mean():.2f}**, with a peak of **{peak_value:.2f}** on **{peak_time}**.\n"
        f"- Trends by hour and weekday help identify when energy demand is highest and when it is comparatively stable.\n"
        f"- Combining the time-series view with relationship charts supports stronger storytelling and better decision-making."
    )

    st.caption(
        "Prepared from the cleaned household power consumption dataset for interactive insight delivery and reporting."
    )

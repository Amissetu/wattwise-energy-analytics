# WattWise Energy Analytics: Energy Consumption and Forecasting

# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Project Overview

WattWise Energy Analytics is a group data analytics project that explores household electricity consumption using historical electricity usage data. The project aims to identify patterns in energy consumption, understand how usage changes by hour, day, month, and year, and highlight periods of high electricity demand.

Our team uses Python and data analysis libraries to clean, transform, and explore the dataset. We use the findings to develop clear visualisations and an interactive dashboard that can help users understand household electricity usage and make more informed decisions about energy consumption.

The project also investigates hypotheses about weekday and weekend consumption, evening peak usage, and the relationship between active power and global intensity.

## Dataset Content

Our project uses the [Electric Power Consumption Dataset from Kaggle](https://www.kaggle.com/datasets/uciml/electric-power-consumption-data-set), which originates from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/235/individual+household+electric+power+consumption).

The dataset contains household electricity measurements collected at one-minute intervals from December 2006 to November 2010. The original dataset contains approximately 2.07 million records.

To make the data more manageable for analysis, our team reduced the minute-level records to hourly averages. The reduction process produced 34,589 expected hourly records before further data cleaning. The cleaned dataset used in the exploratory data analysis contains 34,168 records and seven electrical measurement columns.

The main variables include:

- `global_active_power`: Household active power consumption, measured in kilowatts (kW).
- `global_reactive_power`: Reactive power consumption, measured in kilowatts (kW).
- `voltage`: Average voltage, measured in volts (V).
- `global_intensity`: Average current intensity, measured in amperes (A).
- `sub_metering_1`: Energy recorded by sub-metering system 1.
- `sub_metering_2`: Energy recorded by sub-metering system 2.
- `sub_metering_3`: Energy recorded by sub-metering system 3.

The dataset includes measurements from a single household. Therefore, our findings describe the recorded household rather than all households or regions.

## Business Requirements

Our project addresses the following business requirements:

1. **Understand electricity consumption patterns:** Analyse how household electricity usage changes over time.
2. **Identify peak consumption periods:** Determine the hours, days and months associated with higher average electricity consumption.
3. **Investigate seasonal patterns:** Explore whether electricity usage changes across different seasons and years.
4. **Understand relationships between measurements:** Examine how active power, reactive power, voltage, current intensity and sub-metering measurements relate to each other.
5. **Explore forecasting opportunities:** Assess whether historical patterns and seasonality could support future electricity consumption forecasting.
6. **Communicate actionable insights:** Present findings through clear visualisations and an interactive dashboard to support understanding and energy-efficiency decisions.

## Hypotheses and How to Validate Them

Our team formulated three hypotheses to test using the cleaned household electricity consumption data.

### Hypothesis 1: Weekday and Weekend Consumption

- **Null hypothesis (H0):** There is no statistically significant difference in mean household active power consumption between weekdays and weekends.
- **Alternative hypothesis (H1):** Mean household active power consumption differs between weekdays and weekends.

**Validation:** We compare average active power consumption on weekdays and weekends using an independent two-sample t-test, allowing for unequal variances. We use a significance level of 0.05.

### Hypothesis 2: Evening Peak and Off-Peak Consumption

- **Null hypothesis (H0):** Mean active power consumption during evening peak hours (18:00–22:00) is equal to consumption during off-peak hours.
- **Alternative hypothesis (H1):** Mean active power consumption during evening peak hours is greater than during off-peak hours.

**Validation:** We compare the mean active power readings during evening peak hours with readings during all other hours. The results are assessed using a statistical test at the 0.05 significance level.

### Hypothesis 3: Active Power and Global Intensity

- **Null hypothesis (H0):** There is no statistically significant linear relationship between global active power and global intensity.
- **Alternative hypothesis (H1):** There is a statistically significant positive linear relationship between global active power and global intensity.

**Validation:** We calculate Pearson's correlation coefficient and its p-value to assess the strength, direction and statistical significance of the relationship.

For all three hypotheses, a p-value below 0.05 provides evidence against the relevant null hypothesis. The final conclusions will be based on the actual test results rather than the hypotheses alone.

## Project Plan

Our team follows a structured approach to data collection, preparation, analysis, visualisation and presentation.

### Day 1 – Project Setup and Data Preparation

We agree on the project objectives, select the household electricity consumption dataset, inspect the available variables and establish the project repository. We also begin reducing and preparing the raw data for analysis.

### Day 2 – Exploratory Data Analysis and Interactive Dashboards

We explore electricity consumption over time, investigate missing timestamps and unusual patterns, examine relationships between measurements, and develop visualisations. We also begin designing interactive dashboard features.

### Day 3 – Statistical Testing, Refinement and Documentation

We test our hypotheses, refine the visualisations, validate the results, document the analysis process and update the README. We also prepare the presentation and review the dashboard against the project requirements.

### Day 4 – Final Testing and Presentation

We complete final checks, address identified issues, confirm the project documentation, publish the dashboard if applicable, and present our findings, recommendations and lessons learned.

*These stages describe our planned workflow. We will update the README to reflect the tasks actually completed by the team.*

### Data Management

We manage the data through the following stages:

1. **Collection:** Obtain the original household electricity consumption dataset from Kaggle and identify its UCI source.
2. **Reduction:** Convert minute-level records into hourly averages to reduce the dataset size while preserving useful consumption patterns.
3. **Cleaning and transformation:** Validate date and time fields, convert measurement columns to numeric values, handle invalid entries, check for duplicates and prepare a consistent dataset.
4. **Exploration:** Inspect data types, missing values, timestamp gaps, summary statistics and consumption trends.
5. **Analysis:** Compare consumption across different periods, examine correlations and carry out statistical hypothesis testing.
6. **Visualisation:** Develop charts and dashboard components to communicate the findings.
7. **Documentation and version control:** Record the methods, findings and limitations in the project repository and track changes using GitHub.

We use Python and Jupyter Notebook to support reproducible analysis and keep our processing steps organised.

### Research Methodology

We use a quantitative research approach because the project focuses on numerical electricity measurements collected over time.

Our methods include descriptive statistics, time-series exploration, correlation analysis, visualisation and statistical hypothesis testing. These methods allow us to identify patterns, compare consumption periods and assess relationships between variables.

## Rationale for Mapping Business Requirements to Data Visualisations

We select visualisations based on the questions each business requirement needs to answer.

| Business requirement | Planned visualisation | Rationale |
|---|---|---|
| Understand consumption over time | Time-series line chart | Shows changes in electricity consumption and helps identify peaks, drops and longer-term patterns. |
| Identify high-demand periods | Bar chart of average consumption by hour | Makes it easier to compare consumption at different hours of the day. |
| Compare weekdays and weekends | Bar chart or grouped comparison | Shows differences in average consumption between working days and weekends. |
| Explore seasonal patterns | Monthly and yearly comparison charts | Helps identify recurring changes across months and years. |
| Investigate relationships between measurements | Correlation heatmap and scatter plots | Shows the direction and strength of relationships between electrical measurements. |
| Explore forecasting opportunities | Seasonal decomposition chart and forecasting evaluation | Separates trend, seasonal patterns and residual variation to assess whether forecasting may be useful. |
| Support user exploration | Interactive dashboard filters and charts | Allows users to explore relevant measurements and consumption periods. |

The final visualisations may change during development if another chart type communicates the findings more clearly.

## Analysis Techniques Used

### Data Reduction and Cleaning

We use the Pandas library to load, process and transform the dataset. The original minute-level readings are aggregated into hourly averages, reducing the dataset from approximately 2.07 million records to 34,589 expected hourly records before further cleaning.

We convert measurement columns to numeric values, handle invalid entries and standardise the date and time information. We also check for duplicate timestamps and missing observations.

### Exploratory Data Analysis (EDA)

We use exploratory data analysis to understand the structure, quality and patterns within the dataset before drawing conclusions.

Our EDA includes:

- Checking the number of rows and columns, data types and date range.
- Identifying missing values and duplicate timestamps.
- Checking for missing hourly observations.
- Exploring hourly, daily, weekly and monthly consumption patterns.
- Comparing average consumption by hour, day of the week, month and year.
- Examining relationships between electrical measurements using correlation analysis and scatter plots.
- Exploring seasonality and the potential for future forecasting.

### Descriptive Statistics

We calculate averages and other summary measures to compare electricity consumption across different periods. These summaries help us identify typical consumption levels and periods of unusually high or low demand.

### Correlation Analysis

We use Pearson correlation coefficients and a correlation heatmap to examine linear relationships between electrical measurements. A correlation coefficient ranges from -1 to +1: positive values indicate that two variables tend to move together, while negative values indicate that they tend to move in opposite directions.

Correlation does not establish causation, so we interpret these results carefully.

### Statistical Hypothesis Testing

We use independent two-sample t-tests to compare mean active power consumption between weekdays and weekends and between evening peak and off-peak hours. We use Pearson correlation testing to investigate the relationship between global active power and global intensity.

These tests help us assess whether the observed differences or relationships are statistically significant.

### Time-Series Analysis and Forecasting

We use time-series visualisations and seasonal decomposition to explore trends, recurring seasonal patterns and irregular variation. We also assess whether the available data is suitable for a forecasting approach.

Missing periods and incomplete calendar years can affect forecasting accuracy. Any missing-data treatment used for decomposition must be documented, and forecasting performance should be evaluated using a suitable test period before making claims about predictive accuracy.

### Limitations and Alternative Approaches

The dataset represents one household, so the findings cannot automatically be generalised to other households or geographical regions.

The data also contains missing hourly observations. Our EDA identified 421 missing hours out of 34,589 expected hours, representing approximately 1.22% of the expected timestamps. These gaps may affect comparisons and forecasting.

Aggregating minute-level data into hourly averages makes the dataset smaller and easier to interpret, but it removes some short-term fluctuations. Analysing the original minute-level readings could provide more detailed insights if required.

Correlation analysis identifies associations but does not prove that one measurement causes another to change. More advanced forecasting methods could be considered if they provide measurable improvements over a simple baseline model.

### Use of Generative AI

Our team may use generative AI tools to support project ideation, clarify Python concepts, review code, suggest visualisation improvements and refine documentation.

AI-generated suggestions are reviewed by team members, tested where applicable and checked against the actual dataset and analysis outputs. The team remains responsible for the accuracy, interpretation and presentation of all findings.

We will update this section to name the tools used and describe their actual contributions before submission.

## Ethical Considerations

The dataset contains household electricity measurements rather than direct personal identifiers. However, detailed electricity usage patterns can reveal information about household routines and occupancy.

We consider the following ethical issues:

- **Privacy:** We avoid attempting to identify the household or infer personal details beyond what the data supports.
- **Responsible interpretation:** We do not treat observations from one household as representative of all households.
- **Data quality:** We document missing timestamps and processing decisions that may affect the results.
- **Transparency:** We identify the data source, explain our methods and acknowledge limitations.
- **Responsible use of AI:** We verify AI-assisted code and explanations rather than accepting generated outputs without review.

The dataset is used for educational analysis, and our findings are presented with appropriate limitations.

## Dashboard Design

Our dashboard is intended to help users explore household electricity consumption and understand the main findings without needing to read the entire analysis notebook.

The planned dashboard content includes:

1. **Consumption Overview:** Summary indicators showing key electricity consumption measures.
2. **Consumption Over Time:** Line charts showing changes in active power consumption.
3. **Consumption by Period:** Charts comparing average consumption by hour, day of the week and month.
4. **Relationships Between Measurements:** Visualisations showing relationships between active power, intensity, voltage and sub-metering measurements.
5. **Seasonality and Forecasting:** Visualisations that explain recurring consumption patterns and, if implemented and evaluated, forecast results.
6. **Interactive Exploration:** Suitable filters that allow users to examine selected periods or measurements, where supported by the final dashboard.

We aim to use clear chart titles, readable labels, appropriate units and concise explanations so that users can understand the findings. The final dashboard features and published link will be updated to match the implementation.

## Unfixed Bugs and Known Limitations

We will record any unresolved technical issues discovered during testing and explain their impact.

Known analytical limitations include:

- Missing hourly observations in the cleaned dataset.
- A single-household dataset that limits generalisation.
- Incomplete calendar coverage at the beginning and end of the dataset.
- Potential effects of missing periods on time-series analysis and forecasting.
- The risk of interpreting correlation as causation.

The team will review the notebooks, data-processing steps and dashboard before submission. Any remaining software bugs will be documented separately from these analytical limitations.

## Development Roadmap

Our next steps are to:

- Complete and validate the data-cleaning workflow.
- Finish the exploratory analysis and statistical hypothesis tests.
- Review the visualisations and select those that best answer the business questions.
- Complete the interactive dashboard and test its usability.
- Evaluate forecasting approaches if implemented.
- Finalise the README, data-source references and acknowledgements.
- Review the repository structure and ensure the required files are available.
- Prepare and deliver the final group presentation.

Through this project, we aim to strengthen our skills in Python, data cleaning, statistical analysis, data visualisation, dashboard development, version control and collaborative problem-solving.

## Deployment

The dashboard will be published using the platform selected by our team, such as Power BI Desktop, Tableau Public or a Python-based dashboard application.

**Live dashboard:** To be added once the dashboard has been published and the link has been confirmed.

If a Streamlit application is deployed to Heroku, the final application URL and deployment instructions will be added here.

## Main Data Analysis Libraries

Our project uses Python libraries to prepare, analyse and visualise the household electricity consumption data.

| Library | Purpose |
|---|---|
| [Pandas](https://pandas.pydata.org/) | Loads, cleans, transforms and aggregates the dataset, including hourly and daily summaries. |
| [NumPy](https://numpy.org/) | Supports numerical operations and data processing. |
| [Matplotlib](https://matplotlib.org/) | Creates line charts, bar charts, scatter plots and time-series visualisations. |
| [Seaborn](https://seaborn.pydata.org/) | Creates statistical visualisations, including the correlation heatmap. |
| [SciPy](https://scipy.org/) | Performs statistical tests, including t-tests and Pearson correlation testing. |
| [Statsmodels](https://www.statsmodels.org/) | Supports seasonal decomposition and time-series analysis. |

The final list should reflect the libraries actually used in the submitted notebooks and application.

## Credits

We acknowledge the following sources and resources that supported our project.

### Dataset

- **Kaggle:** [Electric Power Consumption Dataset](https://www.kaggle.com/datasets/uciml/electric-power-consumption-data-set) — the source through which our team accessed the household electricity consumption data.
- **UCI Machine Learning Repository:** [Individual Household Electric Power Consumption](https://archive.ics.uci.edu/dataset/235/individual+household+electric+power+consumption) — the original dataset source and supporting dataset information.

### Technical Documentation

- [Pandas documentation](https://pandas.pydata.org/docs/) — data loading, cleaning, transformation and aggregation.
- [NumPy documentation](https://numpy.org/doc/) — numerical operations.
- [Matplotlib documentation](https://matplotlib.org/stable/) — chart creation and customisation.
- [Seaborn documentation](https://seaborn.pydata.org/) — statistical visualisation.
- [SciPy documentation](https://docs.scipy.org/doc/scipy/) — statistical testing.
- [Statsmodels documentation](https://www.statsmodels.org/stable/index.html) — time-series analysis and seasonal decomposition.
- [GitHub documentation](https://docs.github.com/) — repository management and version control.
- [Code Institute](https://codeinstitute.net/) — the learning framework and hackathon project guidance.

Any additional tutorials, external code, dashboard resources or AI tools that materially contribute to the final project will be acknowledged with specific links before submission.

## Acknowledgements

We would like to thank Code Institute for providing the hackathon framework and learning resources that guided our project.

We also acknowledge our teammates for their collaboration, contributions and shared commitment throughout the project. Working together has allowed us to combine our skills in data preparation, exploratory analysis, statistical testing, visualisation and documentation.

We recognise the support of our instructors and peers in helping us develop our analytical thinking, technical skills and understanding of data-driven problem-solving.

This project represents a collaborative learning experience in which we have applied data analytics methods to a real-world household electricity consumption dataset.


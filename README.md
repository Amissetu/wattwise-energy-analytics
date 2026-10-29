# WattWise Energy Analytics: Energy Consumption and Forecasting

Energy Consumption and Forecasting is a data analytics project that aims to explore electricity consumption patterns, identify periods of high usage and investigate how historical electricity data can help predict future consumption. The project will use data analysis and visualisation techniques to communicate findings and support a better understanding of energy usage.

# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Project Overview

WattWise Energy Analytics is a group data analytics project that explores household electricity consumption. The aim is to understand electricity usage patterns, identify changes in consumption over time, and explore how data analysis can support better energy management and forecasting.

The project uses Python to prepare and analyse electricity consumption data. Statistical tests and data visualisations are used to investigate patterns and communicate findings clearly.

## Dataset Content

The project uses the Electric Power Consumption Dataset from Kaggle, which originates from the UCI Machine Learning Repository.
The original dataset contains household electricity consumption measurements recorded over time, including date, time, global active power, global reactive power, voltage, global intensity and three sub-metering measurements.
The team reduced the original dataset from 2,075,259 minute-level records to 34,589 hourly records. This was achieved by selecting seven electrical measurement columns and calculating hourly averages.
The data preparation process includes converting measurement columns to numeric values, handling invalid values, organising records chronologically and preparing the data for further analysis. The transformation workflow also aims to check date and time values, duplicates and other data quality issues.

## Business Requirements

The project aims to answer the following business questions:

•	How does household electricity consumption change over time?

•	Does average electricity consumption differ between weekdays and weekends?

•	Is electricity consumption higher during evening peak hours than during other hours?

•	What relationship exists between global active power and global intensity?

•	How can charts help users understand household electricity consumption?

•	Can historical electricity consumption data help identify possible future usage patterns?

## Hypothesis and How to Validate

The team formulated three hypotheses for statistical testing.

**Hypothesis 1: Weekday and weekend consumption**

• Alternative hypothesis (H1): Mean global active power differs between weekdays and weekends.

• Validation: Use an independent-samples t-test to compare the mean active power of the two groups.

**Hypothesis 2: Evening peak and off-peak consumption**

• Alternative hypothesis (H1): Mean global active power during evening peak hours (18:00–22:00) is higher than during other hours.

• Validation: Compare the mean active power of peak and off-peak periods using an appropriate statistical test. The test should be one-sided if the aim is specifically to test whether peak-hour consumption is higher.

**Hypothesis 3: Active power and intensity**

• Alternative hypothesis (H1): There is a positive linear relationship between global active power and global intensity.

• Validation: Use Pearson's correlation test to examine the direction and strength of the relationship and assess its statistical significance.

A significance level of 0.05 is used to assess the statistical results. A p-value below 0.05 provides evidence against the relevant null hypothesis. The conclusions will be based on the actual test results rather than assumptions.

## Project Plan

**Day 1 – Project setup and data preparation:** Confirm the project objectives, review the dataset, organise the project files and identify the variables needed for analysis.

**Day 2 – Data cleaning and transformation:** Reduce the dataset, handle invalid values, convert measurement columns to suitable data types and prepare the data for analysis.

**Day 3 – Analysis and visualisation:** Explore consumption patterns, perform statistical tests and develop charts to communicate the results. Investigate forecasting if feasible.

**Day 4 – Finalisation and presentation:** Review the analysis, complete the documentation, check the project files and prepare the final presentation.

The Rationale to Map the Business Requirements to the Data Visualisations

## The visualisations are intended to help answer the business questions and make electricity consumption patterns easier to understand.

• **Line charts:** Show how electricity consumption changes over time.

• **Bar charts:** Compare average consumption between weekdays and weekends or between peak and off-peak periods.

• **Histograms:** Show the distribution of electricity consumption measurements.

• **Scatter plots:** Explore the relationship between global active power and global intensity.

• **Correlation heatmaps:** Summarise relationships between numerical measurements where useful.

• **Forecast charts:** If forecasting is completed, compare predicted consumption with actual values.

The final visualisations will depend on the analysis results and the variables selected for each question.

## Analysis Techniques Used

**Data Reduction**

The original minute-level dataset was reduced to hourly averages using Pandas. Seven electrical measurement columns were retained to support further analysis. This reduced the number of records from 2,075,259 to 34,589.

**Data Cleaning and Transformation**

The data preparation workflow includes:

• Loading the raw dataset using Pandas.

• Combining date and time information into a datetime value.

• Treating invalid measurement values marked with ? as missing values.

• Converting electrical measurements to numeric data types.

• Sorting the records chronologically.

• Aggregating minute-level measurements into hourly averages.

• Preparing transformed and cleaned CSV files for further analysis.

The transformation workflow also identifies checks for date and time validity, duplicate records and invalid rows.

**Exploratory Data Analysis**

Exploratory data analysis uses summary statistics and visualisations to examine the dataset, understand consumption patterns and identify relationships between variables.

**Statistical Testing**

The project investigates three hypotheses using independent-samples t-tests and Pearson's correlation test. These methods help determine whether differences between groups and relationships between measurements are statistically significant.

**Forecasting**

The project explores the potential use of historical electricity consumption data for forecasting. Any forecasting method, model evaluation and results will be documented if this work is completed.

## Ethical Considerations

The project uses an existing household electricity consumption dataset for educational and analytical purposes. The team acknowledges the original data source and aims to interpret the results responsibly.

The analysis will consider data quality, the limitations of the dataset and the difference between statistical association and causation. Statistical results will not be presented as proof that one variable causes another.

## Dashboard Design (Optional)

If an interactive dashboard is developed, it will present the main electricity consumption patterns and relevant analysis results in a clear and accessible format. The final design will depend on the visualisations and features completed by the team.

## Unfixed Bugs

Any outstanding issues identified during development and testing will be documented here. This section will be updated following checks of the notebooks, datasets, analysis and any dashboard or forecasting components.

## Development Roadmap

• Complete and verify data cleaning and transformation.

• Perform exploratory data analysis.

• Complete the three statistical hypothesis tests and interpret the results.

• Develop and refine suitable data visualisations.

• Explore forecasting if feasible within the project scope.

• Review the findings and finalise the project documentation and presentation.

## Deployment (Optional)

Deployment details will be added if the team develops and deploys an interactive application or dashboard.

## Heroku (Optional)

If the project is deployed on Heroku, the live application link and relevant deployment information will be added here.

## Main Data Analysis Libraries

The libraries used in the project should be confirmed against the final code.

• **Pandas:** For loading, cleaning, transforming and analysing tabular data.

• **NumPy:** For numerical operations.

• **SciPy:** For statistical tests, including t-tests and Pearson's correlation.

• **Matplotlib:** For creating charts and visualisations.

• **Seaborn:** For statistical visualisations, if used.

• **Scikit-learn:** For machine learning or forecasting, if used.

## Credits

**Content**

The project uses the Electric Power Consumption Dataset from Kaggle. The dataset originates from the UCI Machine Learning Repository.

The analysis and documentation were developed as part of the Code Institute Data Analytics with AI course group project.

## Media

The Code Institute logo is included in the README template.

Acknowledgements

## Acknowledgements

We would like to thank Code Institute for providing the learning resources and project framework that supported our WattWise Energy Analytics group project.

We acknowledge the contributors of the [Electric Power Consumption Dataset](https://www.kaggle.com/datasets/uciml/electric-power-consumption-data-set) for making the data available for analysis.

We also appreciate the collaboration, contributions and shared efforts of all our team members throughout the project.



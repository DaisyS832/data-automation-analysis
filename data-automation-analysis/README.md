# Data Automation and Analysis Project

## Overview

The goal of this project is to analyze airline performance and identify patterns in flight delays across airlines, routes, and distances. The analysis is designed to support data-driven decision-making by highlighting operational inefficiencies and performance trends within the aviation industry.

The project focuses on analyzing airline performance, delays, and operational patterns using Python and data analysis libraries.

## Data Cleaning and Preparation

The raw dataset was processed to ensure accuracy, consistency, and usability for analysis. Key steps included:

* Removing unnecessary and redundant columns
* Handling missing values by filtering relevant records
* Converting date fields into proper datetime format
* Standardizing airline naming conventions
* Filtering out extreme outliers in delay values
* Selecting only relevant features for analysis

The final cleaned dataset includes the following variables:

* Flight Date
* Airline
* Origin Airport
* Destination Airport
* Departure Delay
* Arrival Delay
* Distance

This streamlined dataset improves both computational efficiency and analytical clarity.

## Data Preview

![Data Preview](images/data_preview.png)

This preview shows a sample of the cleaned dataset after preprocessing. The dataset has been structured to include only relevant variables, ensuring clarity and usability for analysis.

## Analysis and Visualizations

### 1. Top Airlines with Highest Average Arrival Delays

![Airline Delay](images/airline_delay.png)

This visualization highlights airlines with the highest average arrival delays. It reveals clear differences in performance across carriers, allowing identification of consistently delayed airlines.

### 2. Top Airlines by Number of Flights

![Flight Count](images/flight_count.png)

This chart shows airline activity based on total flight volume. Larger carriers dominate flight counts, which provides important context when interpreting delay patterns.

### 3. Top Routes with Highest Average Delays

![Route Delay](images/route_delay.png)

This analysis identifies routes with consistently high delays. A minimum flight threshold was applied to ensure reliability and avoid misleading results from low-frequency routes.

### 4. Distance vs Arrival Delay

![Distance vs Delay](images/distance_vs_delay.png)

This scatter plot examines the relationship between flight distance and arrival delay. The visualization shows that delays are widely distributed and not strongly correlated with distance, though extreme delays appear more frequently on shorter and mid-range flights.

## Key Insights

* Several airlines consistently experience higher average arrival delays, indicating potential operational inefficiencies or scheduling challenges
* High-volume airlines dominate total flight operations, which can significantly influence overall delay distributions
* Certain routes repeatedly show high delays, suggesting route-specific issues such as congestion, weather impact, or airport constraints
* Flight distance is not a strong predictor of arrival delay, as delays are distributed across both short and long-haul flights
* Applying data filtering and thresholds improves the reliability of insights by removing noise from low-frequency or extreme observations

These insights can support airline operations teams, analysts, and decision-makers in identifying areas for performance improvement and optimizing scheduling strategies.

## Business Impact

The results of this analysis can support decision-making in several areas:

* Airline operations teams can identify consistently underperforming routes and prioritize operational improvements
* Scheduling teams can adjust flight timings or resource allocation to reduce delays on high-risk routes
* Analysts can use these patterns to build predictive models for delay forecasting
* Airport authorities can better understand congestion patterns and optimize traffic flow

By transforming raw flight data into structured insights, this project demonstrates how data analytics can contribute to improving efficiency and customer experience in the aviation industry.

## Technologies Used

* Python
* Pandas
* Matplotlib
* Jupyter Notebook
* CSV (data storage)

## How to Run

1. Open the notebook located in the `notebooks/` folder
2. Run all cells to reproduce the analysis and visualizations
3. Output files will be generated in the `outputs/` folder
4. Visualizations will be saved in the `images/` folder

## Project Structure

```
data-automation-analysis/

├── data/
│ ├── raw/
│ │ └── raw_data.csv
│ └── processed/
│ └── cleaned_data.csv

├── notebooks/
│ └── analysis_notebook.ipynb

├── scripts/
│ ├── data_cleaning.py
│ └── analysis.py

├── outputs/
│ ├── avg_delay_by_airline.csv
│ └── top_delayed_routes.csv

├── images/
│ ├── airline_delay.png
│ ├── flight_count.png
│ ├── route_delay.png
│ └── distance_vs_delay.png

├── docs/
│ └── project_summary.md

└── README.md
```

## Data Accessibility

The full dataset used in this project is large and may not display directly within GitHub.

To improve accessibility, a smaller sample dataset (`cleaned_data_sample.csv`) has been included in the `data/processed/` folder. This file contains a subset of the data and allows users to easily preview the dataset structure.

For complete analysis, users can download the full dataset.

## Conclusion

This project demonstrates the ability to clean large datasets, perform structured analysis, and generate meaningful visual insights. The workflow reflects real-world data analytics practices, including data preprocessing, exploratory analysis, and result interpretation.

The findings provide valuable insights into airline performance and delay patterns, which could support operational improvements and decision-making processes in the aviation industry.

## Author

Daisy Sharma

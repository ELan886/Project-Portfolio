# Info Final Project

## Authors
- Eric Lan
- Quinton Baughman
- Mohamed Camara
- Gabrielle Morris

## Date
2024-05-22

## Introduction
This project examines the differences in crime rates between California and Washington, motivated by the significant population difference between the two states and the relevance to the student body at the University of Washington. The study focuses on:
1. Comparing crime rates between California and Washington.
2. Analyzing the 5 most populated counties in each state.
3. Evaluating crime rates by county.
4. Identifying the most prevalent violent crimes.

Understanding where violent crimes are most frequent can help in developing solutions to address these crimes and raising public awareness.

## Data Sources
We used datasets from DATA.GOV, sourced from:
- Washington State Statistical Analysis Center
- California Department of Public Health

These datasets include information on violent and non-violent crimes, population totals, and specific crime types. Our analysis focused on data from 2000 to 2013 and included the following violent crimes: rape, assault, murder, and robbery.

## Datasets
- **Washington State Crime Data:** 1419 rows, 228 columns
- **California State Crime Data:** 49228 rows, 27 columns

The datasets were cleaned and filtered to include relevant data for our analysis. For California, data was reshaped to match the layout of the Washington dataset.

## Methods
1. Filtered the datasets to include relevant columns (year, county, population, and specific crime types).
2. Computed crime rates as the ratio of total crime value for each county divided by its population.
3. Reshaped the California dataset to match the Washington layout.
4. Joined the datasets by year to create representative graphs and analyze crime trends for both states.

## Findings
- **Crime Rate Comparison:** California has an overall higher crime rate compared to Washington.
- **Population Growth:** Both states have experienced population growth from 2000 to 2013.
- **County Analysis:** The most populous counties in California had higher violent crime rates compared to those in Washington, except for rape.
- **Most Prevalent Crime:** Assault was found to be the most prevalent crime overall.

## Summary
From a violent crime standpoint, California is a more dangerous state than Washington. California's higher population and crime rates may contribute to the perception of it being more dangerous. This understanding can help explain why many California students might choose to attend universities in other states.

## Additional Graphs
Graphs comparing the rates of assault, rape, murder, and robbery over the years provide a visual representation of the trends and differences between the two states.

## Future Work
To extend this study, additional datasets including non-violent crimes should be analyzed to compare overall safety on a larger scale.



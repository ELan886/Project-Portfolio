# California Housing Prices Analysis

Introduction

This research project analyzes the California Housing Prices dataset sourced from Kaggle. The dataset, containing around 20,000 blocks of housing from 1997, provides a comprehensive overview of the housing market in various Californian neighborhoods. Variables include geographical coordinates, housing median age, total rooms, total bedrooms, population, households, median income, median house value, and ocean proximity.

The primary goal is to explore how socioeconomic and demographic factors influence house values in California and to develop a predictive linear regression model for housing price forecasts.

Theory and Hypothesis

The research addresses two key questions:

What factors influence housing prices in California?
Is it feasible to construct a linear model for this purpose?
Hypotheses:

H1: There is a positive correlation between median house values and factors like median income, newer housing, and ocean proximity.
H2: There is a negative correlation between median house values and factors such as higher population densities.
Data and Visual Analysis

Data
Initial dataset: 20,640 rows and 17 columns.
Post-cleaning dataset: 19,675 rows and 18 columns.
Key steps:

Elimination of outliers (housing values > $500,000).
Aggregation of distances to major cities into a single variable.
Conversion of categorical variables ('ocean proximity' and 'City') into numeric values.
Descriptive Statistics
Mean, standard deviation, minimum, median, and maximum values for key variables.
Correlation matrix indicating relationships between variables.
Exploratory Data Analysis
Visualizations included:

Scatter plots of median house value vs. median income, distance to coast, and distance to central city.
Distribution histograms for median house value, median income, distance to coast, and distance to city.
Results Discussion
Regression analysis revealed significant predictors:

Positive correlation with median income.
Negative correlation with distance to coast, distance to central city, and population density.
The model explains approximately 59.45% of the variance in median house values.
Conclusion

The study confirms that:

Higher median incomes and proximity to the coast or central cities positively influence house values.
Higher population densities negatively impact house values.
These findings underscore the importance of socioeconomic and demographic factors in shaping California's real estate market. Future research could expand on these insights by incorporating additional data, advanced modeling techniques, and exploring temporal changes in the housing market.

Repository Structure

data/: Contains the dataset used for analysis.
notebooks/: Jupyter notebooks detailing data cleaning, analysis, and model development.
results/: Outputs of the analysis including visualizations and regression models.
README.md: Project overview and instructions.

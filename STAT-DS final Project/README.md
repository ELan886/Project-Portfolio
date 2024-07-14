# HR Analytics Study

## Project Overview

This project is a comprehensive analysis of HR analytics, utilizing a dataset produced by IBM Corporation. The main objective is to identify predictors of monthly income and build appropriate regression models to predict it. The project addresses the following questions:

1. Which numerical factors significantly influence the monthly income of employees?
2. Can a linear regression model be applied to predict the monthly income of employees?
3. Can a more complex model address multicollinearity issues in predicting monthly income?
4. Which model demonstrates superior predictive performance?

## Contributors

- **Eric Lan**: Model full, reduced & complex code, correlation matrix, K-fold-validation, conclusions
  - Email: ericlan@uw.edu
- **Xiaoyu Zhou**: Coordination, models full & reduced code, correlation matrix, K-fold-validation, conclusions
  - Email: xz081302@uw.edu
- **Shelby Ames**: Preliminary presentation, report writing, further reduced model code, figure 6 code, Bonferroni correction code
  - Email: sah2003@uw.edu

## Introduction

HR analytics is a field that enables data-driven decision-making in human resources by analyzing HR processes, organizational performance, and economic benchmarks. The dataset used in this project contains 1480 observations and 38 attributes, with monthly income as the outcome variable.

## Methodologies

- **Data Cleaning**: Removed 57 missing variables.
- **Tools**: R Studio for graphing and plotting.
- **Analysis Techniques**: 
  - Correlation matrices for numerical and categorical variables.
  - Simple and complex regression models (including stepwise regressions and log transformations).
  - Residual plots for analyzing normality, non-constance, heteroscedasticity, and outliers.
  - ANOVA and K-Fold Cross Validation for model performance comparison.

## Data Analysis

### Correlation Analysis
- **Key Findings**: Monthly income has the greatest correlation with total working years and the least with the daily rate. Significant predictors include age, total working years, and years at the company.

### Linear Regression
- **Full Model**: Significant predictors at a 95% confidence level include total working years, job role, job level, distance from home, and department.
- **Reduced Model**: Focuses on significant values from the Bonferroni correction, revealing heteroscedasticity and residual groupings.
- **Further Reduced Model**: Diminishes grouping issues but explains only 57% of the variability in monthly income.

### Stepwise Regression
- **Findings**: Includes additional significant variables (attrition, education, number of companies worked for, and years in current roles) with an R² of 87%. However, it still faces issues like residual groupings and right-skewed distributions.

### Model Performance
- **K-Fold Validation Results**: The stepwise regression model shows the greatest performance with the lowest RMSE and MSE values and the highest R² value of 0.916.

## Conclusions

The stepwise regression model performs the best, but issues such as non-constance and residual groupings remain. Further analysis of variables like salary slab and job level within categories may lead to more accurate predictive models.

## References

- Angrave, D., Charlwood, A., Kirkpatrick, I., Lawrence, M., & Stuart, M. (2016). HR and Analytics: Why HR Is Set to Fail the Big Data Challenge. Human Resource Management Journal, 26:1–11.
- Boudreau, J. W., & Marler, J. H. (2017). An evidence-based review of HR Analytics. The International Journal of Human Resource Management, 28:1, 3-26.
- Tahir, M. (2023). HR Analytics. Kaggle. [Link](https://www.kaggle.com/datasets/mohammadkaiftahir/hr-analytics)


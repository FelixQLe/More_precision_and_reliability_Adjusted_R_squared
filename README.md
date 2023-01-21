### In this repo I will explain the limitations of R-squared, and the importance of Adjusted R-squared in Regession model

R-squared is a statistical measure in regression model, showing how well the model fits a given set of data or how well it will predict a future set of observations (the goodness of fit). 
for example, an R-squared of 100% reveals a model that explains all the variation in the response variable around its mean. Generally, a higher R-squared indicates the better the regression model fits our observations. However, it is not alway the case
#### Limitations of R-squared
- R-squared will increases every time we add an independent vairable to the model, even though our dependent variable is not explained by our new independent variables. A regression model contains more independent variables(with higher R-squared) than another model(lower R-squared) can look like it provides better prediction just because it contains more independent variables, but that is not true, if the model contains more independant variables,but those more independant variables are not bettter explain the dependent variable
- 
- R-squared can not determine the coefficent estimates and predcitions are bias, which we have to assess residual plots

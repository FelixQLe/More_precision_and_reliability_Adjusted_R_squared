### In this repo I will explain the limitations of R-squared, and the importance of Adjusted R-squared in Regession model

R-squared is a statistical measure in regression model, showing how well the model fits a given set of data or how well it will predict a future set of observations (the goodness of fit). 
for example, an R-squared of 100% reveals a model that explains all the variation in the response variable around its mean. Generally, a higher R-squared indicates the better the regression model fits our observations. However, it is not alway the case
#### Limitations of R-squared
1. R-squared will increases every time we add an independent vairable to the model, even nonsense features/variables will always increase R-squared, while adjust R-squared decrease. adding more features/variables to increase goodness of fit of our model using solely measure of R-squared, is a tempted reward that we want to achieve. However, low R-squared does not always mean our model is not a good fit, or Higher R-squared does not always mean our model is a good fit. Hence, A good way to see how goodness of fit our model is, using adjust R-squared together with R-squared. A regression model contains more independent variables(with higher R-squared) than another model(lower R-squared) can look like it provides better prediction just because it contains more independent variables, but that is not true, if the model contains more independant variables,but those more independant variables are not bettter explain the dependent variable
will make our model's predictive power decrease

In this repo I will compare R-squared and Adjust R-squared when we add more independent variables

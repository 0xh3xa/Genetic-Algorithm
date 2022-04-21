### Linear Regression using GA

- Linear regression attempts to model the relationship between two variables by fitting a linear equation to observed data
- We can use linear regression to solve linear equation Y=aX+b, Meanwhile, a is the slope of the line
another representation of Y=mX + b, or Y=&#952;1X + &#952;0

- The most common method for fitting a regression line is the method of least-squares
- For more http://www.stat.yale.edu/Courses/1997-98/101/linreg.htm

<div align="center">
    <img src="../../assets/problems/linear_regression/model.png" alt="neural networks" width="600" style="border: 2px solid tan"/>
</div>

### Goal of Linear regression

To find a continuous or real number and best line fit between Y=aX+b

### Dataset

It's using a naive dataset based on the age and glucose

|Ages | Glucose|
|-----|--------|
|43   | 99|
|21   | 65|
|25   | 79|
|42   | 75|
|57   | 87| 
|59   | 81|
    
The task is find appropriate a and b parameters for Y = aX + b
, and answer a query what would be the value of Y when X = 65

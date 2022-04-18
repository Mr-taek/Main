- 회귀 제곱합 : 가로선과 회귀선간의 차이

- 잔차 제곱합 : 회귀선과 실제값 간의 차이

### 상관관계 구하기

1. cor() : 상관관계 구하기
    - EX
    ```
    cor(cars)
    ```
2. cor.text(x,y) : 피어슨의 상관계수와 t값, p값 을 다 알려줌
    - EX
    ```
    cor.test(cars$speed,cars$dist)
    ```
    ->
    ```
    	Pearson's product-moment correlation

    data:  cars$speed and cars$dist
    t = 9.464, df = 48, p-value = 1.49e-12
    alternative hypothesis: true correlation is not equal to 0
    95 percent confidence interval:
    0.6816422 0.8862036
    sample estimates:
        cor 
    0.8068949 
    ```

3. 상관분석 : corrplot package설치.
    1. corrplot:: (::사용하면 ) 뭐라함
    2. corrplot::corrplot.mixed(cor(mtcars)) -> 히트맵

4. 잔차와 이상치 검사법
    1. fit.cars=lm(dist~speed,data=cars)
    2. summary(fit.cars)
    ->
    ```
    Call:
    lm(formula = dist ~ speed, data = cars)

    Residuals:
        Min      1Q  Median      3Q     Max 
    -29.069  -9.525  -2.272   9.215  43.201 

    Coefficients:
                Estimate Std. Error t value Pr(>|t|)    
    (Intercept) -17.5791     6.7584  -2.601   0.0123 *  
    speed         3.9324     0.4155   9.464 1.49e-12 ***
    ---
    Signif. codes:  
    0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

    Residual standard error: 15.38 on 48 degrees of freedom
    Multiple R-squared:  0.6511,	Adjusted R-squared:  0.6438 
    F-statistic: 89.57 on 1 and 48 DF,  p-value: 1.49e-12
    ```

5. predict()
    - 
    ```
    new_data=data.frame(speed=c(30,31,32))

    predict(fit.cars, newdata=new_data) 
    ```
# PUI2017 HW 5.

This Repository contains the work done for Homework Assignment - 5


## Assignment 1: Test the Z test: 

Worked on my own for this Assignment.


Generated N samples from a Laplace distribution with a chosen mean μ = 100 and standard deviation σ: N(μ, σ) and calculated the mean of each sample (all samples having the same size n). 

Assessed the validity of the Z-test: From samples drawn from the distribution that is subject to test, the z-values calculated follow a N(0,1) distribution (a Gaussian with mean 0 and standard deviation 1). The distribution of z -statistics that was calculated using  is indeed consistent with N(0,1).

### Things Done: 

Plot original distribution

plot at least one of the samples

plot the distribution of z statistics

fit the z-statistics with a gaussian model and assess the goodness of fit with a simple test (AD or KS).

![solarpalette](screenshots/9d.png)

![solarpalette](screenshots/9e.png)

![solarpalette](screenshots/9f.png)

![solarpalette](screenshots/9g.png)

### Null Hypothesis: Laplace Distribution Follows Gaussian Distribution 
### Since the P Value is 0.19 and it is greater than the assumed p value of 0.05 for the hypothesis, the Null Hypothesis cannot be rejected.

### Therefore, Laplace Distribution considering a 1000 Samples follows a Gaussian Distribution.


## Assignment 2: Compare Tests for Goodness of fit
Followed the skeleton notebook [Assignment 2](https://github.com/fedhere/PUI2017_fb55/blob/master/HW5_fb55/Assignment2_instructions.ipynb)

I was stuck on the section where we had to create an array. But with some help from Matt, I understood how to resolve the issue

KS Test:
Null Hypothesis: Binomial & Poisson Distribution can be Approximated for a Gaussian Distribution as the value of mean increases
Binomial: The P Value = 0.0 is less than 0.05 hence the Null Hypothesis cannot be rejected.
Poisson: The P Value = 0.3 is greater than 0.05 hence the Null Hypothesis can be rejected.
AD Test:
Null Hypothesis: Binomial & Poisson Distribution are drawn from a Gaussian Distribution.
Binomial: The statistics AD=15.85 larger than threshold (for alpha=0.05) thresh_0.05 = 0.784 hence the Null Hypothesis cannot be rejected.
Poisson: The statistics AD=0.92 larger than threshold (for alpha=0.05) thresh_0.05 = 0.784 hence the Null Hypothesis can be rejected.

Binomial on a Normal
KS Test: With the increase in the sample size the P-Value increases and KS Statistics reduces. So with Large number of samples Binomial Approximates to a Gaussian Distribution.
AD Test: With the increase in sample size the AD Statistics value decreases and tends to go below the threshold. So with Large number of samples Binomial Approximates to a Gaussian Distribution.
KL Test: With the increase in sample size the KL Statistics value decreases, So the entropy value decreases with increase in the sample size

Poisson on a Normal
KS Test: With the increase in the sample size the P-Value increases and KS Statistics reduces. So with Large number of samples Poisson Approximates to a Gaussian Distribution.
AD Test: With the increase in sample size the AD Statistics value decreases and tends to go below the threshold. So with Large number of samples Poisson Approximates to a Gaussian Distribution.
KL Test: With the increase in sample size the KL Statistics value decreases, So the entropy value decreases with increase in the sample size.

![solarpalette](screenshots/9b.png)

![solarpalette](screenshots/9c.png)



Tested and showed that binomial and Poisson distribution look increasingly more similar to Gaussians as the mean of the distribution increases.


## Assignment 3: investigate linear relationships between fire arm possession, homicides by fire arms, and mass shootings for different countries, considering also the country GDP


Followed instructions in [this_skeleton_notebook](https://github.com/fedhere/PUI2017_fb55/blob/master/HW5_fb55/Assignment3_instructionsUpdated.ipynb) and derived Conclusions drawn from the analysis.

![solarpalette](screenshots/1.png)

![solarpalette](screenshots/2.png)

![solarpalette](screenshots/3.png)

![solarpalette](screenshots/4.png)

![solarpalette](screenshots/5.png)

![solarpalette](screenshots/6.png)

![solarpalette](screenshots/7.png)

![solarpalette](screenshots/8.png)

![solarpalette](screenshots/9.png)

![solarpalette](screenshots/9a.png)





# Barker simulations 
Simulations of Barker frailty at the aggregate level

We develop a discrete variant of a general model for adult mortality influenced
by the delayed impact of early conditions on adult health and mortality. The
discrete variant of the model builds on an intuitively appealing interpretation of
conditions that induce delayed effects and is an extension of the discrete form of the
standard frailty model with distinct implications. We show that introducing delayed
effects is equivalent to perturbing adult mortality patterns with a particular class of
time-/age-varying frailty. We emphasize two main results. First, populations with
delayed effects could experience unchanging or increasing adult mortality even
when background mortality has been declining for long periods of time.
Although this phenomenon also occurs in a regime with standard frailty, the
distortions can be more severe under a regime with Barker frailty. As a
consequence, conventional interpretations of the observed rates of adult mortality
decline in societies that experience Barker frailty may be inappropriate.
Second, the observed rate of senescence (slope of adult mortality rates) in
populations with delayed effects could increase, decrease, or remain steady
over time and across adult ages even though the rate of senescence of the
background age pattern of mortality is time- and age-invariant. This second
result implies that standard interpretations of empirical estimates of the slope of
adult mortality rates in populations with delayed effects may be misleading
because they can reflect mechanisms other than those inducing senescence as
conventionally understood in the literature.

In this project, we simulate a population that undergoes a secular mortality decline over 150 years 
(period). We then construct cohort mortality rates as the diagonals of period rates and construct
50 cohorts. We create 300 copies of each cohort and randomly assign them a value that corresponds to
Barker frailty (values drawn from a Gamma distribution (scale=1, shape=1)). We then create 4 scenarios
1) 10% of copies are affected by Barker frailty (i.e., their Gamma value is within the first decile)
2) 20% of copies are affected by Barker frailty (i.e., their Gamma value is within the second decile)
3) 30% of copies are affected by Barker frailty (i.e., their Gamma value is within the third decile)
4) 40% of copies are affected by Barker frailty (i.e., their Gamma value is within the fourth decile)
In each of these scenarios we apply an excess mortality starting at age 40 with four possible values
ranging from 1.5 to 4 in increments of 0.5

Finally, we compute aggregate measures by averaging values across copies in each cohort. See Palloni and
Beltran-Sanchez (2017) for the appropriate formulas when computing the average values.

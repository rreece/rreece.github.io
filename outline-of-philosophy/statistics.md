Philosophy of statistics
================================================================================

Statistics are *way* important in addressing the problem of induction.

<!-- PAGETOC -->


Issues and positions
--------------------------------------------------------------------------------

### Problem of induction

See the [Outline of the scientific method](scientific-method.html#induction)


### Probability and its related concepts

#### Probability

Probability is of epistemic interest, being in some sense
a measure of inductive confidence.

-   Kolmogorov
-   Carnap: "Probability as a guide in life" [^Carnap1947]

[^Carnap1947]: @Carnap_1947_Probability_as_a_guide_in_life\.


#### Expectation and variance

Expectation:

$$ \mathrm{E}(y) \equiv \int dx \: P(x) \: y(x) \label{eq:expectation} $$

Expectation values can be approximated with a partial sum over some data
or monte carol sample:

$$ \mathrm{E}(y) \approx \frac{1}{n} \sum_s^n y(x_s) \label{eq:expectation_sum} $$

The variance of a random variable, $y$, is defined as

\begin{align}
    \mathrm{Var}(y) &\equiv \mathrm{E}((y - \mathrm{E}(y))^2) \nonumber \\
    &= \mathrm{E}(y^2 - 2 \: y \: \mathrm{E}(y) + \mathrm{E}(y)^2) \nonumber \\
    &= \mathrm{E}(y^2) - 2 \: \mathrm{E}(y) \: \mathrm{E}(y) + \mathrm{E}(y)^2 \nonumber \\
    &= \mathrm{E}(y^2) - \mathrm{E}(y)^2 \label{eq:variance}
\end{align}

The covariance matrix, $\boldsymbol{V}$, of random variables $x_i$ is

\begin{align}
    V_{ij} &= \mathrm{Cov}(x_i, x_j) \equiv \mathrm{E}[(x_i - \mathrm{E}(x_i)) \: (x_j - \mathrm{E}(x_j))] \nonumber \\
           &= \mathrm{E}(x_i \: x_{j} - \mu_i \: x_j - x_i \: \mu_j + \mu_i \: \mu_j ) \nonumber \\
           &= \mathrm{E}(x_i \: x_{j}) - \mu_i \: \mu_j \label{eq:covariance_matrix_indexed}
\end{align}

\begin{equation}
\boldsymbol{V} = 
\begin{pmatrix}
    \mathrm{Var}(x_1) & \mathrm{Cov}(x_1, x_2) & \cdots & \mathrm{Cov}(x_1, x_n) \\
    \mathrm{Cov}(x_2, x_1) & \mathrm{Var}(x_2) & \cdots & \mathrm{Cov}(x_2, x_n) \\
    \vdots & \vdots & \ddots &  \vdots \\
    \mathrm{Cov}(x_n, x_1) & \mathrm{Cov}(x_n, x_2) & \cdots & \mathrm{Var}(x_n)
\end{pmatrix}
\label{eq:covariance_matrix_array}
\end{equation}

Diagonal elements of the covariance matrix are the variances of each
variable.

$$ \mathrm{Cov}(x_i, x_i) = \mathrm{Var}(x_i) $$

Off-diagonal elements of a covariance matrix measure
how related two variables are, linearly.
Covariance can be normalized to give the correlation coefficient between
variables:

$$ \mathrm{Cor}(x_i, x_j) \equiv \frac{ \mathrm{Cov}(x_i, x_j) }{ \sqrt{ \mathrm{Var}(x_i) \: \mathrm{Var}(x_j)  }  } \label{eq:correlation_matrix} $$

which is bounded: $-1 \leq \mathrm{Cor}(x_i, x_j)  \leq 1$.

The covariance of two random vectors is given by

$$ \boldsymbol{V} = \mathrm{Cov}(\vec{x}, \vec{y}) = \mathrm{E}(\vec{x} \: \vec{y}^{\top}) - \vec{\mu}_x \: \vec{\mu}_{y}^{\top} \label{eq:covariance_matrix_vectors} $$


#### Uncertainty

-   Quantiles
-   Practice of standard error
-   Uncertainty quantification


#### Bayes' theorem

-   [Bayes, Thomas (1701-1761)](https://en.wikipedia.org/wiki/Thomas_Bayes)
-   Bayes' theorem

$$ P(A|B) = P(B|A) \: P(A) \: / \: P(B) \label{eq:bayes_theorem} $$

-   Extended version of Bayes theorem
-   Example of conditioning with medical diagnostics


#### Likelihood and frequentist vs bayesian probability

-   frequentist vs bayesian probability
-   Weisberg: ["Two Schools"](https://jonathanweisberg.org/vip/two-schools.html) [^Weisberg2019ch15]  

$$ P(H|D) = P(D|H) \: P(H) \: / \: P(D) \label{eq:bayes_theorem_hd} $$

-   Likelihood

$$ L(\theta) = P(D|\theta) \label{eq:likelihood_def_x} $$

-   Cranmer

>   Bayes's theorem is a theorem, so there's no debating it. It is not the case that
>   Frequentists dispute whether Bayes's theorem is true. The debate is whether the
>   necessary probabilities exist in the first place. If one can define the joint
>   probability $P (A, B)$ in a frequentist way, then a Frequentist is perfectly
>   happy using Bayes theorem. Thus, the debate starts at the very definition of
>   probability. [^Cranmer2015p6]

-   Carnap
    -   "The two concepts of probability" [^Carnap1945b]
-   Royall
    -   "What do these data say?" [^Royall1997p171]
-   We will return to the frequentist vs bayesian debate in the section on the
    ["Statistics Wars"](#statistics-wars).

[^Carnap1945b]: @Carnap_1945_The_two_concepts_of_probability\.
[^Cranmer2015p6]: @Cranmer_2015_Practical_statistics_for_the_LHC\, p. 6.
[^Royall1997p171]: @Royall_1997_Statistical_Evidence_A_likelihood_paradigm\, p. 171--2.
[^Weisberg2019ch15]: @Weisberg_2019_Odds__Ends_Introducing_Probability__Decision\, ch. 15\.


### Foundations of statistics

#### Early investigators

-   [Graunt, John (1620-1674)](https://en.wikipedia.org/wiki/John_Graunt)
-   [Bernoulli, Jacob (1655-1705)](https://en.wikipedia.org/wiki/Jacob_Bernoulli)
    -   *Ars Conjectandi* (1713, posthumous)
    -   First modern phrasing of the problem of parameter estimation [^Edwards1974p9]
    -   See Hacking [^Hacking1971]
    -   Early vision of decision theory:

>   The art of measuring, as precisely as possible, probabilities of things,
>   with the goal that we would be able always to choose or follow in our
>   judgments and actions that course, which will have been determined to be
>   better, more satisfactory, safer or more advantageous. [^Bernoulli1713]

-   [Bayes, Thomas (1701-1761)](https://en.wikipedia.org/wiki/Thomas_Bayes)
-   [Gauss, Carl Friedrich (1777-1855)](http://en.wikipedia.org/wiki/Gauss)
-   [Mill, John Stuart (1806-1873)](https://en.wikipedia.org/wiki/John_Stuart_Mill)
-   [Venn, John (1834-1923)](https://en.wikipedia.org/wiki/John_Venn)
    -   *The Logic of Chance* (1866) [^Venn1888]

[^Bernoulli1713]: Bernoulli, J. (1713). *Ars Conjectandi*, Chapter II, Part IV, defining the art of conjecture [[wikiquote](https://en.wikiquote.org/wiki/Jacob_Bernoulli)].
[^Edwards1974p9]: @Edwards_1974_The_history_of_likelihood\, p. 9.
[^Hacking1971]: @Hacking_1971_Jacques_Bernoullis_Art_of_conjecturing\.
[^Venn1888]: @Venn_1888_The_Logic_of_Chance\.


#### Foundations of modern statistics

-   [Peirce, Charles Sanders (1839-1914)](https://en.wikipedia.org/wiki/Charles_Sanders_Peirce)
    -   Formulated modern statistics in "Illustrations of the Logic of Science",
        a series published in *Popular Science Monthly* (1877-1878),
        and also "A Theory of Probable Inference" in *Studies in Logic* (1883). [^Peirce1883]
    -   With a repeated measures design, introduced blinded, controlled randomized experiments (before Fisher).
-   [Pearson, Karl (1857-1936)](https://en.wikipedia.org/wiki/Karl_Pearson)
-   [Fisher, Ronald (1890-1972)](https://en.wikipedia.org/wiki/Ronald_Fisher)
    -   Fisher significance of the null hypothesis ($p$-values)
        -   On an absolute criterion for fitting frequency curves. [^Fisher1912]
        -   Frequency distribution of the values of the correlation coefficient in samples of indefinitely large population. [^Fisher1915]
        -   On the "probable error" of a coefficient of correlation deduced from a small sample [^Fisher1921] - definition of *likelihood*
        -   *The Lady Tasting Tea* [^Salsburg2001]
-   [Neyman, Jerzy (1894-1981)](https://en.wikipedia.org/wiki/Jerzy_Neyman)
-   [Pearson, Egon (1895-1980)](https://en.wikipedia.org/wiki/Egon_Pearson)
    -   Neyman-Pearson confidence intervals with fixed error probabilities (also $p$-values but considering two hypotheses involves two types of errors)
-   [Jeffreys, Harold (1891-1989)](https://en.wikipedia.org/wiki/Harold_Jeffreys)
    -   objective (non-informative) Jeffreys priors

[^Fisher1912]: @Fisher_1912_On_an_absolute_criterion_for_fitting_frequency\.
[^Peirce1883]: @Peirce_1883_Studies_in_Logic\, p. 126--181.
[^Fisher1915]: @Fisher_1915_Frequency_distribution_of_the_values\.
[^Fisher1921]: @Fisher_1921_On_the_probable_error_of_a_coefficient\.
[^Salsburg2001]: @Salsburg_2001_The_Lady_Tasting_Tea\.


#### Pedagogy

-   Kendall [^Kendall1946]
-   James [^James2006]
-   Cousins [^Cousins2018]
-   Cowan [^Cowan1998]
-   Cranmer [^Cranmer2015]
-   Weisberg [^Weisberg2019]

[^Cousins2018]: @Cousins_2018_Lectures_on_statistics_in_theory_Prelude\.
[^Cowan1998]: @Cowan_1998_Statistical_Data_Analysis and @Cowan_2016_Statistics\. 
[^Cranmer2015]: @Cranmer_2015_Practical_statistics_for_the_LHC\.
[^James2006]: @James_2006_Statistical_Methods_in_Experimental_Particle\.
[^Kendall1946]: @Kendall_1946_The_Advanced_Theory_of_Statistics_VolII\.
[^Weisberg2019]: @Weisberg_2019_Odds__Ends_Introducing_Probability__Decision\.


### Statistical models

#### Parametric models

-   Data: $x_i$
-   Parameters: $\theta_j$
-   Model: $f(\vec{x} ; \vec{\theta})$


#### Canonical distributions

-   Bernoulli distribution
-   Binomial distribution
-   Poisson distribution
-   Normal/Gaussian distribution

$$ N(x \,|\, \mu, \sigma^2) = \frac{1}{\sqrt{2\,\pi\:\sigma^2}} \: \exp\left[\frac{-(x-\mu)^2}{2\,\sigma^2}\right] \label{eq:gaussian} $$

and in $k$ dimensions:

$$ N(\vec{x} \,|\, \vec{\mu}, \boldsymbol{\Sigma}) = (2 \pi)^{-k/2}\:\left|\boldsymbol{\Sigma}\right|^{-1/2} \: \exp\left[\frac{-1}{2}\:(\vec{x}-\vec{\mu})^{\top}\:\boldsymbol{\Sigma}^{-1}\:(\vec{x}-\vec{\mu})\right] \label{eq:gaussian_k_dim} $$

where $\boldsymbol{\Sigma}$ is the covariance matrix
(defined in [@eq:covariance_matrix_indexed])
of the distribution.

-   Central limit theorem
-   $\chi^2$ distribution
-   Univariate distribution relationships [^Leemis2008]
-   TODO: add fig

[^Leemis2008]: @Leemis_2008_Univariate_distribution_relationships\.


#### Mixture models

-   Gaussian mixture models (GMM)
-   Marked poisson
    -   [pyhf model description](https://scikit-hep.org/pyhf/intro.html)
    -   HistFactory [^Cranmer2012]

[^Cranmer2012]: @Cranmer_2012_HistFactory_A_tool_for_creating_statistical\.


### Point estimation and confidence intervals

#### Inverse problems

-   [Inverse problem](https://en.wikipedia.org/wiki/Inverse_problem)
-   estimators
-   regression


#### Bias and variance

The bias of an estimator, $\hat\theta$, is defined as

$$ \mathrm{Bias}(\hat{\theta}) \equiv \mathrm{E}(\hat{\theta} - \theta) = \int dx \: P(x|\theta) \: (\hat{\theta} - \theta) \label{eq:bias} $$

The mean squared error (MSE) of an estimator has a similar formula to variance
([@eq:variance])
except that instead of quantifying the square of the difference of the estimator
and its expected value, the MSE uses the square of the difference of the estimator
and the true parameter:

$$ \mathrm{MSE}(\hat{\theta}) \equiv \mathrm{E}((\hat{\theta} - \theta)^2) \label{eq:mse} $$

The MSE of an estimator can be related
to its bias and its variance by the following proof:

\begin{align}
    \mathrm{MSE}(\hat{\theta}) &= \mathrm{E}(\hat{\theta}^2 - 2 \: \hat{\theta} \: \theta + \theta^2) \nonumber \\
    &= \mathrm{E}(\hat{\theta}^2) - 2 \: \mathrm{E}(\hat{\theta}) \: \theta + \theta^2
\end{align}

noting that

$$ \mathrm{Var}(\hat{\theta}) = \mathrm{E}(\hat{\theta}^2) - \mathrm{E}(\hat{\theta})^2 $$

and

\begin{align}
    \mathrm{Bias}(\hat{\theta})^2 &= \mathrm{E}(\hat{\theta} - \theta)^2 \nonumber \\
    &= \mathrm{E}(\hat{\theta})^2 - 2 \: \mathrm{E}(\hat{\theta}) \: \theta + \theta^2
\end{align}

we see that MSE is equivalent to

$$ \mathrm{MSE}(\hat{\theta}) = \mathrm{Var}(\hat{\theta}) + \mathrm{Bias}(\hat{\theta})^2 \label{eq:mse_variance_bias} $$

For an unbiased estimator, the MSE is the variance of the estimator.

TODO:

-   Accuracy vs precision [^Cowan1998pX]
-   Bias and variance trade-off
-   Note the new deep learning view [^Belkin2019]

[^Cowan1998pX]: @Cowan_1998_Statistical_Data_Analysis and @Cowan_2016_Statistics\, p. X. 
[^Belkin2019]: @Belkin_2019_Reconciling_modern_machine_learning_practice\.


#### Maximum likelihood estimation

A maximum likelihood estimator (MLE) was first used by Fisher [^Aldrich1997]

$$\hat{\theta} \equiv \underset{\theta}{\mathrm{argmax}} \: \mathrm{log} \: L(\theta) \label{eq:mle} $$

Maximizing $\mathrm{log} \: L(\theta)$ is equivalent to maximizing $L(\theta)$,
and the former is more convenient because for data that are
independent and identically distributed (*i.i.d.*)
the joint likelihood can be factored
into a product of individual measurements:

$$ L(\theta) = \prod_i L(\theta|x_i) = \prod_i P(x_i|\theta) $$

and taking the log of the product makes it a sum:

$$ \mathrm{log} \: L(\theta) = \sum_i \mathrm{log} \: L(\theta|x_i) = \sum_i \mathrm{log} \: P(x_i|\theta) $$

Maximizing $\mathrm{log} \: L(\theta)$ is also equivalent to minimizing $-\mathrm{log} \: L(\theta)$, the negative-log-likelihoo (NLL). For distributions that are *i.i.d.*,

$$ L = \prod_i L_i $$

$$ - \log L = - \sum_i \log L_i $$

$$ \Rightarrow \mathrm{NLL} = \sum_i \mathrm{NLL}_i $$

TODO:

-   Least squares from MLE of gaussian models: $\chi^2$
-   Ordinary Least Squares (OLS)
-   interpretation

[^Aldrich1997]: @Aldrich_1997_RAFisher_and_the_making_of_maximum_likelihood\.


#### Variance of MLEs

-   Taylor expansion of a likelihood near its maximum
-   Analytic variance of gaussian likelihoods: $\chi^2$
-   Cram&eacute;r-Rao bound [^Cramer-Rao]
    -   for unbiased and efficient estimators
    -   proof in Rice [^Rice2007p300]
-   Variance of MLEs by the method of $\Delta\chi^2$ or $\Delta{}L$
    -   Invariance of likelihoods to reparametrization
-   Uncertainty of measuring an efficiency
    -   Precision vs recall for classification
    -   Classification and logistic regression
-   TODO:
    -   Explain if/why the Neyman construction would be needed for point estimation.

[^Cramer-Rao]: @Frechet_1943_Sur_lextension_de_certaines_evaluations\,
    @Cramer_1946_A_contribution_to_the_theory_of_statistical\,
    @Rao_1945_Information_and_the_accuracy_attainable\, and
    @Rao_1947_Minimum_variance_and_the_estimation_of_several\.
[^Rice2007p300]: @Rice_2007_Mathematical_Statistics_and_Data_Analysis\, p. 300--2.


#### Bayesian credibility intervals

-   defined, MAP
-   prior sensitivity
    -   Betancourt, M. (2018). [Towards A Principled Bayesian Workflow](https://github.com/betanalpha/jupyter_case_studies/blob/master/principled_bayesian_workflow/principled_bayesian_workflow.ipynb) - ipynb
-   not invariant to reparametrization in general
-   Jeffreys priors are
-   Examples:
    -   Some sample mean
    -   Measuring efficiency 
    -   Bayesian lighthouse
    -   Some HEP fit


### Statistical hypothesis testing

-   Null hypothesis significance testing (NHST)
    -   goodness of fit
    -   Fisher:

>   [T]he null hypothesis is never proved or established,
>   but is possibly disproved, in the course of experimentation. [^Fisher1935p16]

-   Neyman-Pearson theory
    -   probes an alternative hypothesis [^Goodman1999p998]
    -   Type-1 and type-2 errors
    -   Power and confidence
    -   Neyman-Pearson lemma [^Neyman1933]
    -   Neyman construction
-   $p$-values and significance [^Cowan2012]
    -   Coverage
    -   Fisherian vs Neyman-Pearson $p$-values
    -   Flip-flopping and Feldman-Cousins confidence intervals [^Feldman1998]
-   Student's $t$-test
    -   ANOVA
-   Asymptotics
    -   Wilks [^Wilks1938]
    -   Pearson $\chi^2$-test
    -   Wald [^Wald1943]
    -   Cowan _et al_.[^Cowan2011]
-   Frequentist vs bayesian decision theory [^Murphy2012p197]
-   Examples:
    -   Difference of two means: $t$-test
    -   A/B-testing
    -   New physics

[^Cowan2011]: @Cowan_2011_Asymptotic_formulae_for_likelihood_based_tests\.
[^Cowan2012]: @Sinervo_2002_Signal_significance_in_particle_physics and @Cowan_2012_Discovery_sensitivity_for_a_counting_experiment\.
[^Feldman1998]: @Feldman_1998_A_unified_approach_to_the_classical_statistical\.
[^Fisher1935p16]: @Fisher_1935_The_Design_of_Experiments\, p. 16.
[^Goodman1999p998]: @Goodman_1999_Toward_evidence_based_medical_statistics_1_The_P\. p. 998.
[^Murphy2012p197]: @Murphy_2012_Machine_Learning_A_probabilistic_perspective\, p. 197.
[^Neyman1933]: @Neyman_1933_On_the_problem_of_the_most_efficient_tests\.
[^Wald1943]: @Wald_1943_Tests_of_statistical_hypotheses_concerning_several\.
[^Wilks1938]: @Wilks_1938_The_large_sample_distribution_of_the_likelihood\.


### Systematic uncertainties

-   Class-1, class-2, and class-3 systematic uncertanties (good, bad, ugly), Classification by Pekka Sinervo (PhyStat2003) [^Sinervo2013]
-   Not to be confused with type-1 and type-2 errors in Neyman-Pearson theory
-   Profiling and the profile likelihood
    -   Importance of Wald and Cowan _et al_.

[^Sinervo2013]: @Sinervo_2003_Definition_and_treatment_of_systematic\.

![Classification of measurement uncertainties ([philosophy-in-figures.tumblr.com](http://philosophy-in-figures.tumblr.com/post/150371555016/classification-of-measurement-uncertainties)).](img/systematic-uncertainties-sinervo.png){#fig:systematic-uncertainties-sinervo}


### Exploratory data analysis

-   [Tukey, John (1915-2000)](https://en.wikipedia.org/wiki/John_Tukey)
    -   [Exploratory data analysis](https://en.wikipedia.org/wiki/Exploratory_data_analysis)
    -   *Exploratory Data Analysis* (1977) [^Tukey1977]
-   File-drawer effect = Look-Elsewhere Effect (LEE)
-   Stopping rules
    -   validation dataset
    -   statistical issues, violates the likelihood principle
-   "Data science"
    -   Data collection, quality, analysis, archival, and reinterpretation
    -   RECAST

[^Tukey1977]: @Tukey_1977_Exploratory_Data_Analysis\.


### Likelihood principle

-   [Likelihood principle](http://en.wikipedia.org/wiki/Likelihood_principle)
-   The likelihood principle is the proposition that, given a statistical model and a data sample,
    all the evidence relevant to model parameters is contained in the likelihood function.
-   The history of likelihood [^Edwards1974]
    -   Allan Birnbaum proved that the likelihood principle follows from two more primitive
        and seemingly reasonable principles,
        the [conditionality principle](https://en.wikipedia.org/wiki/Conditionality_principle)
        and the [sufficiency principle](https://en.wikipedia.org/wiki/Sufficient_statistic).  [^Birnbaum1962]
    -   Hacking identified the "law of likelihood". [^Hacking1965]
-   Berger & Wolpert. (1988). *The Likelihood Principle* [^Berger1988]
-   Criticisms:
    -   Evans [^Evans2013]
    -   Mayo [^Mayo2014]
-   Gandenberger
    -   "A new proof of the likelihood principle" [^Gandenberger2015]
    -   [gandenberger.org/research](http://gandenberger.org/research/)
    -   [Do frequentist methods violate the likelihood principle?](http://gandenberger.org/2014/04/28/do-frequentist-methods-violate-lp/)
-   [Likelihoodist statistics](https://en.wikipedia.org/wiki/Likelihoodist_statistics)

[^Berger1988]: @Berger_1988_The_Likelihood_Principle\.
[^Evans2013]: @Evans_2013_What_does_the_proof_of_Birnbaums_theorem_prove\.
[^Edwards1974]: @Edwards_1974_The_history_of_likelihood\.
[^Gandenberger2015]: @Gandenberger_2015_A_new_proof_of_the_likelihood_principle\.
[^Hacking1965]: @Hacking_1965_Logic_of_Statistical_Inference\.
[^Mayo2014]: @Mayo_2014_On_the_Birnbaum_Argument_for_the_Strong_Likelihood\.


### "Statistics Wars"

-   Carnap
    -   Sznajder on the alleged evolution of Carnap's views of inductive logic [^Sznajder2018]
-   David Cox
-   Ian Hacking
    -   *Logic of Statistical Inference* [^Hacking1965]
-   Richard Royall
    -   *Statistical Evidence: A likelihood paradigm* [^Royall1997]
-   Jim Berger
    -   "Could Fisher, Jeffreys, and Neyman have agreed on testing?" [^Berger2003]
-   Deborah Mayo
    -   "In defense of the Neyman-Pearson theory of confidence intervals" [^Mayo1981]
    -   Concept of "Learning from error" in *Error and the Growth of Experimental Knowledge* [^Mayo1996]
    -   "Error statistics" [^Mayo2011]
    -   *Statistical Inference as Severe Testing* [^Mayo2018]
    -   [Statistics Wars: Interview with Deborah Mayo](https://blog.apaonline.org/2019/03/07/interview-with-deborah-mayo/) - APA blog
    -   [Review of *SIST* by Prasanta S. Bandyopadhyay](https://ndpr.nd.edu/news/statistical-inference-as-severe-testing-how-to-get-beyond-the-statistics-wars/)
-   Andrew Gelman
    -   Beyond subjective and objective in statistics [^Gelman2017]
    -   [Confirmationist and falsificationist paradigms of science](https://statmodeling.stat.columbia.edu/2014/09/05/confirmationist-falsificationist-paradigms-science/) - Sept. 5, 2014
    -   [Retire Statistical Significance: The discussion](https://statmodeling.stat.columbia.edu/2019/03/20/retire-statistical-significance-the-discussion/)
    -   [Exchange with Deborah Mayo on abandoning statistical significance](https://statmodeling.stat.columbia.edu/2019/09/11/exchange-with-deborah-mayo-on-abandoning-statistical-significance/)
    -   [Several reviews of *SIST*](https://statmodeling.stat.columbia.edu/2019/04/12/several-reviews-of-deborah-mayos-new-book-statistical-inference-as-severe-testing-how-to-get-beyond-the-statistics-wars/)
-   Larry Wasserman
    -   [Statistical Principles?](https://normaldeviate.wordpress.com/2012/07/28/statistical-principles/)
-   Kevin Murphy
    -    Pathologies of frequentist statistics [^Murphy2012ch6]
-   Greg Gandenberger
    -   [An introduction to likelihoodist, bayesian, and frequentist methods (1/3)](http://gandenberger.org/2014/07/21/intro-to-statistical-methods/)
    -   As Neyman and Pearson put it in their original presentation of the frequentist approach,
        "without hoping to know whether each separate hypothesis is true or false,
        we may search for rules to govern our behavior with regard to them, in the
        following which we insure that, in the long run of experience, we shall not
        too often be wrong" (1933, 291). 
    -   [An introduction to likelihoodist, bayesian, and frequentist methods (2/3)](http://gandenberger.org/2014/07/28/intro-to-statistical-methods-2/)
    -   [An introduction to likelihoodist, bayesian, and frequentist methods (3/3)](http://gandenberger.org/2014/08/26/intro-to-statistical-methods-3/)
    -   [An argument against likelihoodist methods as genuine alternatives to bayesian and frequentist methods](http://gandenberger.org/2013/10/21/against-likelihoodist-methods/)
    -   "Why I am not a likelihoodist" [^Gandenberger2016]

[^Berger2003]: @Berger_2003_Could_Fisher_Jeffreys_and_Neyman_have_agreed_on\.
[^Birnbaum1962]: @Birnbaum_1962_On_the_foundations_of_statistical_inference\.
[^Gandenberger2016]: @Gandenberger_2016_Why_I_am_not_a_likelihoodist\.
[^Gelman2017]: @Gelman_2017_Beyond_subjective_and_objective_in_statistics\.
[^Mayo1981]: @Mayo_1981_In_defense_of_the_Neyman_Pearson_theory\.
[^Mayo1996]: @Mayo_1996_Error_and_the_Growth_of_Experimental_Knowledge\.
[^Mayo2011]: @Mayo_2011_Error_statistics\.
[^Mayo2018]: @Mayo_2018_Statistical_Inference_as_Severe_Testing_How\.
[^Murphy2012ch6]: @Murphy_2012_Machine_Learning_A_probabilistic_perspective\, ch. 6.6.
[^Royall1997]: @Royall_1997_Statistical_Evidence_A_likelihood_paradigm\.
[^Sznajder2018]: @Sznajder_2018_Inductive_logic_as_explication_The_evolution\.


### P-value controversy

-   "Why most published research findings are false" [^Ioannidis2005]
-   ASA statement on $p$-values [^Wasserstein2016]
-   [Big names in statistics want to shake up much-maligned P value](http://www.nature.com/news/big-names-in-statistics-want-to-shake-up-much-maligned-p-value-1.22375) [^Benjamin2017]
-   [Hi-Phi Nation, episode 7](https://hiphination.org/episodes/episode-7-hackademics-ii-the-hackers/)
-   Fisher:

>   [N]o isolated experiment, however significant in itself, can suffice
>   for the experimental demonstration of any natural phenomenon;
>   for the "one chance in a million" will undoubtedly occur,
>   with no less and no more than its appropriate frequency,
>   however surprised we may be that it should occur to us.
>   In order to assert that a natural phenomenon is experimentally
>   demonstrable we need, not an isolated record, but a reliable method of
>   procedure. In relation to the test of significance, we may say that a
>   phenomenon is experimentally demonstrable when we know how to conduct an
>   experiment which will rarely fail to give us a statistically significant
>   result. [^Fisher1935p13]

-   Relationship to the LEE
-   [Tukey, John (1915-2000)](https://en.wikipedia.org/wiki/John_Tukey)
    -   [Uncomfortable science](https://en.wikipedia.org/wiki/Uncomfortable_science)
-   Mayo
-   Vox: [What a nerdy debate about p-values shows about science--and how to fix it](https://www.vox.com/science-and-health/2017/7/31/16021654/p-values-statistical-significance-redefine-0005)

[^Benjamin2017]: @Benjamin_2017_Redefine_statistical_significance\.
[^Fisher1935p13]: @Fisher_1935_The_Design_of_Experiments\, p. 13--14.
[^Ioannidis2005]: @Ioannidis_2005_Why_most_published_research_findings_are_false\.
[^Wasserstein2016]: @Wasserstein_2016_The_ASAs_statement_on_p_values_Context_process\.


### Information geometry

-   Balasubramanian, V. (1996). A geometric formulation of Occam's razor for inference
    of parametric distributions. [^Balasubramanian1996]
-   Cranmer

[^Balasubramanian1996]: @Balasubramanian_1996_A_geometric_formulation_of_Occams_razor
    and @Balasubramanian_1996_Statistical_inference_Occams_razor\.


### Machine learning

#### Classical

-   classification vs regression
-   supervised and unsupervised learning
    -   classification = supervised; clustering = unsupervised
-   Hastie, Tibshirani, & Friedman [^Hastie2009]

[^Hastie2009]: @Hastie_2009_The_Elements_of_Statistical_Learning_Data_Mining\.


#### Computer Vision

Computer Vision (CV)

-   Fukushima: neocognitron
-   LeCun: LeNet-5
-   Ciresan: MCDNN
-   Krizhevsky: AlexNet
-   Review: Deep learning [^LeCun2015]
-   *Deep Learning* [^Goodfellow2016]

[^Goodfellow2016]: @Goodfellow_2016_Deep_Learning\.
[^LeCun2015]: @LeCun_2015_Deep_learning\.


#### Natural language processing

Natural language processing (NLP)

-   RNNs and LSTMs
-   Sutskever seq2seq [^Sutskever2014]
-   Review by Stahlberg [^Stahlberg2019]
-   Rationalism and empiricism in artificial intellegence:
    A survey of 25 years of evaluation [in NLP]. [^Church2019]
-   Note that NLP has implications to the philosophy of language and realism
    -   [NLP word representations and the Wittgenstein philosophy of language](http://blog.christianperone.com/2018/05/nlp-word-representations-and-the-wittgenstein-philosophy-of-language/). [^Perone2018]
    -   See also: [Implications for the realism debate](#implications-for-the-realism-debate) below.

[^Church2019]: @Church_2019_A_survey_of_25_years_of_evaluation\.
[^Perone2018]: @Perone_2018_NLP_word_representations_and_the_Wittgenstein\.
[^Stahlberg2019]: @Stahlberg_2019_Neural_machine_translation_A_review\.
[^Sutskever2014]: @Sutskever_2014_Sequence_to_sequence_learning_with_neural\.


#### Reinforcement learning

Reinforcement learning (RL)


### Theoretical machine learning

-   No free lunch theorem
-   Relationship to statistical mechanics [^Bahri2020]
-   Relationship to gauge theory

[^Bahri2020]: @Bahri_2020_Statistical_mechanics_of_deep_learning\.


### Automation

#### Surrogate models

-   "The frontier of simulation-based inference" [^Cranmer2019]


#### AutoML

-   Neural Architecture Search (NAS)
-   AutoML frameworks


#### AutoScience

-   Automated discovery
-   "Learning new physics from a machine" [^DAgnolo2019]
-   "Big data and extreme-scale computing: Pathways to Convergence-Toward a shaping strategy for a future software and data ecosystem for scientific inquiry." [^Asch2018]
    -   Note that this description of abduction is missing that it is normative (i.e. "best-fit").
-   "The End of Theory: The data deluge makes the scientific method obsolete." [^Anderson2008]

![The inference cycle for the process of scientific inquiry. The three distinct forms of inference (abduction, deduction, and induction) facilitate an all-encompassing vision, enabling HPC and HDA to converge in a rational and structured manner. HPC: high- performance computing; HDA: high-end data analysis [@Asch_2018_Big_data_and_extreme_scale_computing_Pathways]. ](img/BDEC-scientific-method.png){#fig:BDEC-scientific-method}


[^Anderson2008]: @Anderson_2008_The_End_of_Theory_The_data_deluge_makes\.
[^Asch2018]: @Asch_2018_Big_data_and_extreme_scale_computing_Pathways\.
[^Cranmer2019]: @Cranmer_2019_The_frontier_of_simulation_based_inference\.
[^DAgnolo2019]: @DAgnolo_2019_Learning_New_Physics_from_a_Machine\.


### Implications for the realism debate

-   Korb [^Korb2001]
-   Williamson [^Williamson2009]
-   Bensusan [^Bensusan2000]
-   See the [Outline on scientific realism](scientific-realism.html)

[^Bensusan2000]: @Bensusan_2000_Is_machine_learning_experimental_philosophy\.
[^Korb2001]: @Korb_2001_Machine_learning_as_philosophy_of_science\.
[^Williamson2009]: @Williamson_2009_The_philosophy_of_science_and_its_relation\.


My thoughts
--------------------------------------------------------------------------------

My docs:

-   [Derivation of the Cram&eacute;r-Rao Bound](http://rreece.github.io/publications/pdf/2009.Reece.Derivation-of-the-Cramer-Rao-Bound.pdf)

My talks:

-   [Likelihood functions for supersymmetric observables](http://rreece.github.io/talks/pdf/2009-09-29-RReece-Likelihood-functions-for-SUSY.pdf)
-   [Primer on statistics: MLE, confidence intervals, and hypothesis testing](http://rreece.github.io/talks/pdf/2018-02-16-RReece-statistics-workshop-insight.pdf)

Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore
eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident,
sunt in culpa qui officia deserunt mollit anim id est laborum.


Annotated bibliography
--------------------------------------------------------------------------------

### Mayo, D.G. (1996). *Error and the Growth of Experimental Knowledge*.

-   @Mayo_1996_Error_and_the_Growth_of_Experimental_Knowledge

#### My thoughts

-   TODO

--------------------------------------------------------------------------------

### Cowan, G. (1998). *Statistical Data Analysis*.

-   @Cowan_1998_Statistical_Data_Analysis and @Cowan_2016_Statistics

#### My thoughts

-   TODO

--------------------------------------------------------------------------------

### James, F. (2006). *Statistical Methods in Experimental Physics*.

-   @James_2006_Statistical_Methods_in_Experimental_Particle

#### My thoughts

-   TODO

--------------------------------------------------------------------------------

### Cowan, G. *et al.* (2011). Asymptotic formulae for likelihood-based tests of new physics.

-   @Cowan_2011_Asymptotic_formulae_for_likelihood_based_tests
-   Glen Cowan, Kyle Cranmer, Eilam Gross, Ofer Vitells

#### My thoughts

-   TODO

--------------------------------------------------------------------------------

### ATLAS Collaboration. (2012). Combined search for the Standard Model Higgs boson.

-   @ATLAS_2012_Combined_search_for_the_Standard_Model_Higgs_boson
-   [arxiv:1207.0319](http://arxiv.org/abs/1207.0319)

#### My thoughts

-   TODO

--------------------------------------------------------------------------------

### Cranmer, K (2015). Practical statistics for the LHC.

-   @Cranmer_2015_Practical_statistics_for_the_LHC

#### My thoughts

-   TODO

--------------------------------------------------------------------------------

### More articles to do

-   *All of Statistics* [^Wasserman2003]
-   *The Foundations of Statistics* [^Savage1954]

[^Savage1954]: @Savage_1954_The_Foundations_of_Statistics\.
[^Wasserman2003]: @Wasserman_2003_All_of_Statistics_A_Concise_Course_in_Statistical\.


Links and encyclopedia articles
--------------------------------------------------------------------------------

<div class="clickmore"><a id="link:encyclopedia_articles" class="closed" onclick="toggle_more('encyclopedia_articles')">
Click to show links
</a></div>
<div id="encyclopedia_articles" class="more">

### SEP

-   [Abduction](http://plato.stanford.edu/entries/abduction/)
-   [Analysis of Knowledge](http://plato.stanford.edu/entries/knowledge-analysis/)
-   [Bayes' Theorem](https://plato.stanford.edu/entries/bayes-theorem/)
-   [Bayesian Epistemology](https://plato.stanford.edu/entries/epistemology-bayesian/)
-   [Carnap, Rudolf (1891-1970)](https://plato.stanford.edu/entries/carnap/)
-   [Causal Models](https://plato.stanford.edu/entries/causal-models/)
-   [Causal Processes](http://plato.stanford.edu/entries/causation-process/)
-   [Dutch Book Arguments](https://plato.stanford.edu/entries/dutch-book/)
-   [Epistemology](http://plato.stanford.edu/entries/epistemology/)
-   [Foundationalist Theories of Epistemic Justification](http://plato.stanford.edu/entries/justep-foundational/)
-   [Hume, David (1711-1776)](http://plato.stanford.edu/entries/hume/)
-   [Identity of Indiscernibles](http://plato.stanford.edu/entries/identity-indiscernible/)
-   [Induction, The problem of](http://plato.stanford.edu/entries/induction-problem/)
-   [Logic and Probability](https://plato.stanford.edu/entries/logic-probability/)
-   [Naturalized epistemology](http://plato.stanford.edu/entries/epistemology-naturalized/)
-   [Peirce, Charles Sanders (1839-1914)](https://plato.stanford.edu/entries/peirce/)
-   [Popper, Karl (1902-1994)](http://plato.stanford.edu/entries/popper/)
-   [Principle of Sufficient Reason](http://plato.stanford.edu/entries/sufficient-reason/)
-   [Probability, Interpretations of](https://plato.stanford.edu/entries/probability-interpret/)
-   [Probabilistic Causation](https://plato.stanford.edu/entries/causation-probabilistic/)
-   [Reichenbach, Hans (1891-1953)](https://plato.stanford.edu/entries/reichenbach/)
-   [Scientific Explanation](http://plato.stanford.edu/entries/scientific-explanation/)
-   [Statistics, Philosophy of](http://plato.stanford.edu/entries/statistics/)

### IEP

-   [Epistemology](http://www.iep.utm.edu/epistemo/)
-   [Hempel, Carl Gustav (1905-1997)](http://www.iep.utm.edu/hempel/)
-   [Hume, David (1711-1776)](http://www.iep.utm.edu/hume-cau/)
-   [Naturalism](http://www.iep.utm.edu/naturali/)
-   [Naturalistic Epistemology](http://www.iep.utm.edu/nat-epis/)
-   [Peirce, Charles Sanders (1839-1914)](https://www.iep.utm.edu/peircebi/)
-   [Reductionism](http://www.iep.utm.edu/red-ism/)
-   [Safety Condition for Knowledge, The](http://www.iep.utm.edu/safety-c/)
-   [Simplicity in the philosophy of science](http://www.iep.utm.edu/simplici/)
-   [William of Ockham (1280-1349)](http://www.iep.utm.edu/ockham/)

### Scholarpedia

-   [Algorithmic probability](http://www.scholarpedia.org/article/Algorithmic_probability)
-   [Universal search](http://www.scholarpedia.org/article/Universal_search)

### Wikipedia

-   [Abductive reasoning](http://en.wikipedia.org/wiki/Abductive_reasoning)
-   [Algorithmic information theory](https://en.wikipedia.org/wiki/Algorithmic_information_theory)
-   [Algorithmic probability](https://en.wikipedia.org/wiki/Algorithmic_probability)
-   [Analysis of variance](https://en.wikipedia.org/wiki/Analysis_of_variance)
-   [Aumann's agreement theorem](https://en.wikipedia.org/wiki/Aumann%27s_agreement_theorem)
-   [Bayes, Thomas (1701-1761)](https://en.wikipedia.org/wiki/Thomas_Bayes)
-   [Bayesian inference](https://en.wikipedia.org/wiki/Bayesian_inference)
-   [Birnbaum, Allan (1923-1976)](https://en.wikipedia.org/wiki/Allan_Birnbaum)
-   [Bootstrapping](http://en.wikipedia.org/wiki/Bootstrapping_(statistics))
-   [Confidence interval](https://en.wikipedia.org/wiki/Confidence_interval)
-   [Cosmic variance](https://en.wikipedia.org/wiki/Cosmic_variance)
-   [Cram&eacute;r-Rao bound](http://en.wikipedia.org/wiki/Cram%C3%A9r%E2%80%93Rao_bound)
-   [Cram&eacute;r, Harald (1893-1985)](https://en.wikipedia.org/wiki/Harald_Cram%C3%A9r)
-   [Data science](https://en.wikipedia.org/wiki/Data_science)
-   [Decision theory](https://en.wikipedia.org/wiki/Decision_theory)
-   [Deductive-nomological model](https://en.wikipedia.org/wiki/Deductive-nomological_model)
-   [Empircism](http://en.wikipedia.org/wiki/Empiricism)
-   [Epistemology](http://en.wikipedia.org/wiki/Epistemology)
-   [Exploratory data analysis](https://en.wikipedia.org/wiki/Exploratory_data_analysis)
-   [Fisher, Ronald (1890-1962)](https://en.wikipedia.org/wiki/Ronald_Fisher)
-   [Frequentist inference](https://en.wikipedia.org/wiki/Frequentist_inference)
-   [Foundations of statistics](https://en.wikipedia.org/wiki/Foundations_of_statistics)
-   [Gauss, Carl Friedrich (1777-1855)](http://en.wikipedia.org/wiki/Gauss)
-   [German tank problem](https://en.wikipedia.org/wiki/German_tank_problem)
-   [Gosset, William Sealy (1876-1937)](https://en.wikipedia.org/wiki/William_Sealy_Gosset)
-   [Graunt, John (1620-1674)](https://en.wikipedia.org/wiki/John_Graunt)
-   [History of probability](https://en.wikipedia.org/wiki/History_of_probability)
-   [History of statistics](https://en.wikipedia.org/wiki/History_of_statistics)
-   [Hume, David (1711-1776)](http://en.wikipedia.org/wiki/David_Hume)
-   [Induction, The problem of](http://en.wikipedia.org/wiki/Problem_of_induction)
-   [Inductive reasoning](https://en.wikipedia.org/wiki/Inductive_reasoning)
-   [Interval estimation](http://en.wikipedia.org/wiki/Interval_estimation)
-   [Inverse probability](https://en.wikipedia.org/wiki/Inverse_probability)
-   [Inverse problem](https://en.wikipedia.org/wiki/Inverse_problem)
-   [Ivakhnenko, Alexey (1913-2007)](https://en.wikipedia.org/wiki/Alexey_Ivakhnenko)
-   [Jeffrey, Richard (1926-2002)](https://en.wikipedia.org/wiki/Richard_Jeffrey)
-   [Jeffreys, Harold (1891-1989)](https://en.wikipedia.org/wiki/Harold_Jeffreys)
-   [Jeffreys prior](https://en.wikipedia.org/wiki/Jeffreys_prior)
-   [Kolmogorov, Andrey (1903-1987)](https://en.wikipedia.org/wiki/Andrey_Kolmogorov)
-   [Kolmogorov complexity](https://en.wikipedia.org/wiki/Kolmogorov_complexity)
-   [Lady tasting tea](https://en.wikipedia.org/wiki/Lady_tasting_tea)
-   [Laplace, Pierre-Simon (1749-1827)](https://en.wikipedia.org/wiki/Pierre-Simon_Laplace)
-   [Likelihood principle](http://en.wikipedia.org/wiki/Likelihood_principle)
-   [Likelihoodist statistics](https://en.wikipedia.org/wiki/Likelihoodist_statistics)
-   [List of important publications in statistics](https://en.wikipedia.org/wiki/List_of_important_publications_in_statistics)
-   [Machine learning](https://en.wikipedia.org/wiki/Machine_learning)
-   [Maximum likelihood estimation](https://en.wikipedia.org/wiki/Maximum_likelihood_estimation)
-   [Mill, John Stuart (1806-1873)](https://en.wikipedia.org/wiki/John_Stuart_Mill)
-   [Misuse of p-values](https://en.wikipedia.org/wiki/Misuse_of_p-values)
-   [Neyman, Jerzy (1894-1981)](https://en.wikipedia.org/wiki/Jerzy_Neyman)
-   [Neyman construction](https://en.wikipedia.org/wiki/Neyman_construction)
-   [Neyman-Pearson lemma](http://en.wikipedia.org/wiki/Neyman%E2%80%93Pearson_lemma)
-   [Ockham, William of (1287-1347)](http://en.wikipedia.org/wiki/William_of_Ockham)
-   [Pearson, Egon (1895-1980)](https://en.wikipedia.org/wiki/Egon_Pearson)
-   [Pearson, Karl (1857-1936)](https://en.wikipedia.org/wiki/Karl_Pearson)
-   [Peirce, Charles Sanders (1839-1914)](https://en.wikipedia.org/wiki/Charles_Sanders_Peirce)
-   [Poisson, Sim&eacute;on Denis (1781-1840)](https://en.wikipedia.org/wiki/Sim%C3%A9on_Denis_Poisson)
-   [Popper, Karl (1902-1994)](https://en.wikipedia.org/wiki/Karl_Popper)
-   [Principle of sufficient reason](https://en.wikipedia.org/wiki/Principle_of_sufficient_reason)
-   [Precision and recall](https://en.wikipedia.org/wiki/Precision_and_recall)
-   [P-value](https://en.wikipedia.org/wiki/P-value)
-   [Rao, C.R. (b. 1920)](https://en.wikipedia.org/wiki/C._R._Rao)
-   [Savage, Leonard Jimmie (1917-1971)](https://en.wikipedia.org/wiki/Leonard_Jimmie_Savage)
-   [Solomonoff, Ray (1926-2009)](https://en.wikipedia.org/wiki/Ray_Solomonoff)
-   [Solomonoff's theory of inductive inference](https://en.wikipedia.org/wiki/Solomonoff%27s_theory_of_inductive_inference)
-   [Statistical classification](http://en.wikipedia.org/wiki/Statistical_classification)
-   [Statistical hypothesis testing](http://en.wikipedia.org/wiki/Statistical_hypothesis_testing)
-   [Statistical inference](http://en.wikipedia.org/wiki/Statistical_inference)
-   [Statistical sensitivity and specificity](http://en.wikipedia.org/wiki/Sensitivity_and_specificity)
-   [Statistical significance](http://en.wikipedia.org/wiki/Statistical_significance)
-   [Statistics](http://en.wikipedia.org/wiki/Statistics)
-   [Statistics, Founders of](http://en.wikipedia.org/wiki/Founders_of_statistics)
-   [Statistics, History of](http://en.wikipedia.org/wiki/History_of_statistics)
-   [Statistics, Mathematical](https://en.wikipedia.org/wiki/Mathematical_statistics)
-   [Statistics, Outline of](http://en.wikipedia.org/wiki/Outline_of_statistics)
-   [Statistics, Philosophy of](https://en.wikipedia.org/wiki/Philosophy_of_statistics)
-   [Student's t-test](https://en.wikipedia.org/wiki/Student%27s_t-test)
-   [Systematic error](http://en.wikipedia.org/wiki/Systematic_error)
-   [Trial and error](https://en.wikipedia.org/wiki/Trial_and_error)
-   [Tukey, John (1915-2000)](https://en.wikipedia.org/wiki/John_Tukey)
-   [Type-I and type-II errors](http://en.wikipedia.org/wiki/Type_I_and_type_II_errors)
-   [Uncomfortable science](https://en.wikipedia.org/wiki/Uncomfortable_science)
-   [Uniformitarianism](http://en.wikipedia.org/wiki/Uniformitarianism)
-   [Unsolved problems in statistics, List of](http://en.wikipedia.org/wiki/List_of_unsolved_problems_in_statistics)
-   [Venn, John (1834-1923)](https://en.wikipedia.org/wiki/John_Venn)
-   [Wilks, S.S. (1906-1964)](https://en.wikipedia.org/wiki/Samuel_S._Wilks)
-   [Wilks's theorem](https://en.wikipedia.org/wiki/Wilks%27_theorem)

### Others

-   [Deep Learning: Our Miraculous Year 1990-1991](http://people.idsia.ch/~juergen/deep-learning-miraculous-year-1990-1991.html) - Schmidhuber
-   [errorstatistics.com](http://errorstatistics.com/) - Deborah Mayo's blog
-   [Graunt, John (1620-1674)](http://statprob.com/encyclopedia/JohnGRAUNT.html) - statprob.com
-   [Peng, R. (2016). A Simple Explanation for the Replication Crisis in Science.](http://simplystatistics.org/2016/08/24/replication-crisis/) - simplystatistics.org
-   [Why is binary classification not a hypothesis test?](https://stats.stackexchange.com/questions/240138/why-is-binary-classification-not-a-hypothesis-test) - stackexchange.com
-   [If the likelihood principle clashes with frequentist probability then do we discard one of them?](https://stats.stackexchange.com/questions/40856/if-the-likelihood-principle-clashes-with-frequentist-probability-then-do-we-disc) - stackexchange.com
-   [Wilks's theorem](https://stephens999.github.io/fiveMinuteStats/wilks.html) - fiveMinuteStats

</div>

<!-- REFERENCES -->



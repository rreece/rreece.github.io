\newcommand*{\trans}{^{\mkern-1.5mu\mathsf{T}}}

Philosophy of statistics
================================================================================

Statistics are *way* important in addressing the problem of induction.

<!-- PAGETOC -->


Problem of induction
--------------------------------------------------------------------------------

A key issue for the scientific method, as discussed in the
[previous outline](scientific-method.html#induction),
is the [problem of induction](scientific-method.html#induction).
Inductive inferences are used in the scientific method
to make generalizations from finite data.
This introduces unique avenues of error not found in purely deductive
inferences, like in logic and mathematics.
Compared to deductive inferences, which are sound and necessarily follow
if an argument is valid and all of its premises obtain,
inductive inferences can be valid and probably (not certainly) sound,
and therefore can still result in error in some cases because the support of
the argument is ultimately probabilistic.

A skeptic may further probe if we are even justified in using the probabilities
we use in inductive arguments. What is the probability the Sun will rise tomorrow?
What kind of probabilities are reasonable?

In this outline, we sketch and explore how the mathematical theory of statistics
has arisen to wrestle with the problem of induction, and how it equips us with
careful ways of framing inductive arguments and notions of confidence in them.


Probability and its related concepts
--------------------------------------------------------------------------------

### Probability

Probability is of epistemic interest, being in some sense
a measure of inductive confidence.

TODO:

-   Kolmogorov
-   Probability vs odds: $p/(p+q)$ vs $p/q$
-   Carnap: "Probability as a guide in life" [^Carnap1947]

[^Carnap1947]: @Carnap_1947_Probability_as_a_guide_in_life\.


### Expectation and variance

Expectation:

$$ \mathrm{E}(y) \equiv \int dx \: p(x) \: y(x) \label{eq:expectation} $$

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

$$ \boldsymbol{V} = \mathrm{Cov}(\vec{x}, \vec{y}) = \mathrm{E}(\vec{x} \: \vec{y}\trans) - \vec{\mu}_x \: \vec{\mu}_{y}\trans \label{eq:covariance_matrix_vectors} $$


### Cross entropy

TODO: discuss the Shannon entropy and Kullback-Leibler (KL) divergence. [^Goodfellow2016p72]

Shannon entropy:

$$ H(p) = - \underset{x\sim{}p}{\mathrm{E}}\big[ \log p(x) \big] \label{eq:shannon_entropy} $$

Cross entropy:

$$ H(p, q) = - \underset{x\sim{}p}{\mathrm{E}}\big[ \log q(x) \big] \label{eq:cross_entropy} $$

Kullback-Leibler (KL) divergence:

\begin{align}
D_\mathrm{KL}(p, q)
    &= \underset{x\sim{}p}{\mathrm{E}}\left[ \log \left(\frac{p(x)}{q(x)}\right) \right] = \underset{x\sim{}p}{\mathrm{E}}\big[ \log p(x) - \log q(x) \big] \label{eq:kl_divergence} \\
    &= - H(p) + H(p, q) \\
\end{align}

See also the section on [logistic regression](#logistic-regression).

[^Goodfellow2016p72]: @Goodfellow_2016_Deep_Learning\, p. 72-73.


### Uncertainty

-   Propagation of error
    -   See Cowan
-   Quantiles
-   Practice of standard error for uncertainty quantification.


### Bayes' theorem

-   [Bayes, Thomas](https://en.wikipedia.org/wiki/Thomas_Bayes) (1701-1761)
-   Bayes' theorem

$$ P(A|B) = P(B|A) \: P(A) \: / \: P(B) \label{eq:bayes_theorem} $$

-   Extended version of Bayes theorem
-   Example of conditioning with medical diagnostics


### Likelihood and frequentist vs bayesian probability

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


Foundations of statistics
--------------------------------------------------------------------------------

### Early investigators

-   [Graunt, John](https://en.wikipedia.org/wiki/John_Graunt) (1620-1674)
-   [Bernoulli, Jacob](https://en.wikipedia.org/wiki/Jacob_Bernoulli) (1655-1705)
    -   *Ars Conjectandi* (1713, posthumous)
    -   First modern phrasing of the problem of parameter estimation [^Edwards1974p9]
    -   See Hacking [^Hacking1971]
    -   Early vision of decision theory:

>   The art of measuring, as precisely as possible, probabilities of things,
>   with the goal that we would be able always to choose or follow in our
>   judgments and actions that course, which will have been determined to be
>   better, more satisfactory, safer or more advantageous. [^Bernoulli1713]

-   [Bayes, Thomas](https://en.wikipedia.org/wiki/Thomas_Bayes) (1701-1761)
-   [Laplace, Pierre-Simon](https://en.wikipedia.org/wiki/Pierre-Simon_Laplace) (1749-1827)
    -   rule of succssion, bayesian
-   [Gauss, Carl Friedrich](http://en.wikipedia.org/wiki/Gauss) (1777-1855)
-   [Mill, John Stuart](https://en.wikipedia.org/wiki/John_Stuart_Mill) (1806-1873)
-   [Venn, John](https://en.wikipedia.org/wiki/John_Venn) (1834-1923)
    -   *The Logic of Chance* (1866) [^Venn1888]

[^Bernoulli1713]: Bernoulli, J. (1713). *Ars Conjectandi*, Chapter II, Part IV, defining the art of conjecture [[wikiquote](https://en.wikiquote.org/wiki/Jacob_Bernoulli)].
[^Edwards1974p9]: @Edwards_1974_The_history_of_likelihood\, p. 9.
[^Hacking1971]: @Hacking_1971_Jacques_Bernoullis_Art_of_conjecturing\.
[^Venn1888]: @Venn_1888_The_Logic_of_Chance\.


### Foundations of modern statistics

-   [Peirce, Charles Sanders](https://en.wikipedia.org/wiki/Charles_Sanders_Peirce) (1839-1914)
    -   Formulated modern statistics in "Illustrations of the Logic of Science",
        a series published in *Popular Science Monthly* (1877-1878),
        and also "A Theory of Probable Inference" in *Studies in Logic* (1883). [^Peirce1883]
    -   With a repeated measures design, introduced blinded, controlled randomized experiments (before Fisher).
-   [Pearson, Karl](https://en.wikipedia.org/wiki/Karl_Pearson) (1857-1936)
-   [Fisher, Ronald](https://en.wikipedia.org/wiki/Ronald_Fisher) (1890-1972)
    -   Fisher significance of the null hypothesis ($p$-values)
        -   On an absolute criterion for fitting frequency curves. [^Fisher1912]
        -   Frequency distribution of the values of the correlation coefficient in samples of indefinitely large population. [^Fisher1915]
        -   On the "probable error" of a coefficient of correlation deduced from a small sample [^Fisher1921] - definition of *likelihood*
        -   *The Lady Tasting Tea* [^Salsburg2001]
-   [Neyman, Jerzy](https://en.wikipedia.org/wiki/Jerzy_Neyman) (1894-1981)
    -   biography by Reid [^Reid1998]
-   [Pearson, Egon](https://en.wikipedia.org/wiki/Egon_Pearson) (1895-1980)
    -   Neyman-Pearson confidence intervals with fixed error probabilities (also $p$-values but considering two hypotheses involves two types of errors)
-   [Jeffreys, Harold](https://en.wikipedia.org/wiki/Harold_Jeffreys) (1891-1989)
    -   objective (non-informative) Jeffreys priors
-   Glivenko-Cantelli-theorem

[^Fisher1912]: @Fisher_1912_On_an_absolute_criterion_for_fitting_frequency\.
[^Peirce1883]: @Peirce_1883_Studies_in_Logic\, p. 126--181.
[^Fisher1915]: @Fisher_1915_Frequency_distribution_of_the_values\.
[^Fisher1921]: @Fisher_1921_On_the_probable_error_of_a_coefficient\.
[^Reid1998]: @Reid_1998_Neyman\.
[^Salsburg2001]: @Salsburg_2001_The_Lady_Tasting_Tea\.


### Pedagogy

-   Kendall [^Stuart2010]
-   James [^James2006]
-   Cousins [^Cousins2018]
-   Cowan [^Cowan1998]
-   Lista [^Lista2016]
-   Cranmer [^Cranmer2015]
-   Cranmer, K. (2020). [Statistics and Data Science](https://cranmer.github.io/stats-ds-book/intro.html).
-   Weisberg [^Weisberg2019]

[^Cousins2018]: @Cousins_2018_Lectures_on_statistics_in_theory_Prelude\.
[^Cowan1998]: @Cowan_1998_Statistical_Data_Analysis and @Cowan_2016_StatisticsIn_CPatrignani_et_alParticle_Data\. 
[^Cranmer2015]: @Cranmer_2015_Practical_statistics_for_the_LHC\.
[^James2006]: @James_2006_Statistical_Methods_in_Experimental_Particle\.
[^Lista2016]: @Lista_2016_Statistical_Methods_for_Data_Analysis_in_Particle\.
[^Stuart2010]: @Stuart_2010_Kendalls_Advanced_Theory_of_Statistics_Vol_2A\.
[^Weisberg2019]: @Weisberg_2019_Odds__Ends_Introducing_Probability__Decision\.


Statistical models
--------------------------------------------------------------------------------

### Parametric models

-   Data: $x_i$
-   Parameters: $\theta_j$
-   Model: $f(\vec{x} ; \vec{\theta})$


### Canonical distributions

#### Bernoulli distribution

$$ \mathrm{Ber}(k; p) = \begin{cases} p & \mathrm{if}\ k = 1 \\ 1-p & \mathrm{if}\ k = 0 \end{cases} \label{eq:bernoulli} $$

which can also be written as

$$ \mathrm{Ber}(k; p) = p^k \: (1-p)^{(1-k)} \quad \mathrm{for}\ k \in \{0, 1\} $$

or

$$ \mathrm{Ber}(k; p) = p k + (1-p)(1-k) \quad \mathrm{for}\ k \in \{0, 1\} $$

-   Binomial distribution
-   Poisson distribution

TODO: explain, another important relationship is

![Relationships among Bernoulli, binomial, categorical, and multinomial distributions.](img/bernoulli-binomial-multinomial.png){#fig:bernoulli-binomial-multinomial}


#### Normal/Gaussian distribution

$$ N(x \,|\, \mu, \sigma^2) = \frac{1}{\sqrt{2\,\pi\:\sigma^2}} \: \exp\left(\frac{-(x-\mu)^2}{2\,\sigma^2}\right) \label{eq:gaussian} $$

and in $k$ dimensions:

$$ N(\vec{x} \,|\, \vec{\mu}, \boldsymbol{\Sigma}) = (2 \pi)^{-k/2}\:\left|\boldsymbol{\Sigma}\right|^{-1/2} \: \exp\left(\frac{-1}{2}\:(\vec{x}-\vec{\mu})\trans \:\boldsymbol{\Sigma}^{-1}\:(\vec{x}-\vec{\mu})\right) \label{eq:gaussian_k_dim} $$

where $\boldsymbol{\Sigma}$ is the covariance matrix
(defined in [@eq:covariance_matrix_indexed])
of the distribution.

-   Central limit theorem
-   $\chi^2$ distribution
-   Univariate distribution relationships

![Detail of a figure showing relationships among univariate distributions. See the [full figure here](http://www.stat.rice.edu/~dobelman/courses/texts/leemis.distributions.2008amstat.pdf) [^Leemis2008].](img/Leemis-univariate-distribution-relationships.png ){#fig:Leemis-univariate-distribution-relationships}

[^Leemis2008]: @Leemis_2008_Univariate_distribution_relationships\.


### Mixture models

-   Gaussian mixture models (GMM)
-   Marked poisson
    -   [pyhf model description](https://scikit-hep.org/pyhf/intro.html)
    -   HistFactory [^Cranmer2012]

[^Cranmer2012]: @Cranmer_2012_HistFactory_A_tool_for_creating_statistical\.


Point estimation and confidence intervals
--------------------------------------------------------------------------------

### Inverse problems

-   [Inverse problem](https://en.wikipedia.org/wiki/Inverse_problem)
-   estimators
-   regression
    -   Accuracy vs precision [^Cowan1998pX]
-   classification
    -   Precision vs recall
    -   Recall is sensitivity
    -   Sensitivity vs specificity
    -   Accuracy


### Bias and variance

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

-   Note the new deep learning view. See [Deep learning](#deep-learning).

[^Cowan1998pX]: @Cowan_1998_Statistical_Data_Analysis and @Cowan_2016_StatisticsIn_CPatrignani_et_alParticle_Data\, p. X. 


### Maximum likelihood estimation

A maximum likelihood estimator (MLE) was first used by Fisher. [^Aldrich1997]

$$\hat{\theta} \equiv \underset{\theta}{\mathrm{argmax}} \: \mathrm{log} \: L(\theta) \label{eq:mle} $$

Maximizing $\mathrm{log} \: L(\theta)$ is equivalent to maximizing $L(\theta)$,
and the former is more convenient because for data that are
independent and identically distributed (*i.i.d.*)
the joint likelihood can be factored
into a product of individual measurements:

$$ L(\theta) = \prod_i L(\theta|x_i) = \prod_i P(x_i|\theta) $$

and taking the log of the product makes it a sum:

$$ \mathrm{log} \: L(\theta) = \sum_i \mathrm{log} \: L(\theta|x_i) = \sum_i \mathrm{log} \: P(x_i|\theta) $$

Maximizing $\mathrm{log} \: L(\theta)$ is also equivalent to minimizing $-\mathrm{log} \: L(\theta)$, the negative log-likelihood (NLL). For distributions that are *i.i.d.*,

$$ \mathrm{NLL} \equiv - \log L = - \log \prod_i L_i = - \sum_i \log L_i $$

$$ \Rightarrow \mathrm{NLL} = \sum_i \mathrm{NLL}_i $$

TODO:

-   Least squares from MLE of gaussian models: $\chi^2$
-   Ordinary Least Squares (OLS)
-   Geometric interpretation

[^Aldrich1997]: @Aldrich_1997_RAFisher_and_the_making_of_maximum_likelihood\.


### Variance of MLEs

-   Taylor expansion of a likelihood near its maximum
-   Analytic variance of gaussian likelihoods: $\chi^2$
    -   Wald approximation
-   Cram&eacute;r-Rao bound [^Cramer-Rao]
    -   for unbiased and efficient estimators
    -   proof in Rice [^Rice2007p300]
-   Variance of MLEs by the method of $\Delta\chi^2$ or $\Delta{}L$
    -   Invariance of likelihoods to reparametrization
-   Uncertainty of measuring an efficiency
    -   Normal/Gaussian/Wald interval
    -   Clopper-Pearson interval [^Clopper1934]
    -   [Rule of three](https://en.wikipedia.org/wiki/Rule_of_three_(statistics)) [^Hanley1983]
    -   Review by Brown, Cai, & DasGupta [^Brown2001]
    -   Precision vs recall for classification, again
    -   Classification and logistic regression

[^Brown2001]: @Brown_2001_Interval_estimation_for_a_binomial_proportion\.
[^Clopper1934]: @Clopper_1934_The_use_of_confidence_or_fiducial_limits\.
[^Cramer-Rao]: @Frechet_1943_Sur_lextension_de_certaines_evaluations\,
    @Cramer_1946_A_contribution_to_the_theory_of_statistical\,
    @Rao_1945_Information_and_the_accuracy_attainable\, and
    @Rao_1947_Minimum_variance_and_the_estimation_of_several\.
[^Hanley1983]: @Hanley_1983_If_nothing_goes_wrong_is_everything_all_right\.
[^Rice2007p300]: @Rice_2007_Mathematical_Statistics_and_Data_Analysis\, p. 300--2.


### Bayesian credibility intervals

-   defined, MAP
-   prior sensitivity
    -   Betancourt, M. (2018). [Towards a principled Bayesian workflow](https://github.com/betanalpha/jupyter_case_studies/blob/master/principled_bayesian_workflow/principled_bayesian_workflow.ipynb) - ipynb
-   not invariant to reparametrization in general
-   Jeffreys priors are
-   Examples:
    -   Some sample mean
    -   Measuring efficiency 
    -   Bayesian lighthouse
    -   Some HEP fit


Statistical hypothesis testing
--------------------------------------------------------------------------------

### Null hypothesis significance testing

-   Null hypothesis significance testing (NHST)
-   goodness of fit
-   Fisher

Fisher:

>   [T]he null hypothesis is never proved or established,
>   but is possibly disproved, in the course of experimentation. [^Fisher1935p16]

[^Fisher1935p16]: @Fisher_1935_The_Design_of_Experiments\, p. 16.


### Neyman-Pearson theory

-   probes an alternative hypothesis [^Goodman1999p998]
-   Type-1 and type-2 errors
-   Power and confidence
-   Neyman-Pearson lemma [^Neyman1933]
-   Neyman construction

Neyman-Pearson test statistic:

$$ q_\mathrm{NP} = - 2 \ln \frac{L(H_0)}{L(H_1)} \label{eq:qnp-test-stat} $$

Background-only Neyman-Pearson test statistic:

$$ q_\mathrm{0} = - 2 \ln \frac{L(b)}{L(\mu\,s + b)} \label{eq:q0-test-stat} $$

![TODO: ROC explainer. ([Wikimedia](https://commons.wikimedia.org/wiki/File:ROC_curves.svg), 2015).](img/ROC-explainer.png){#fig:ROC-explainer}

[^Goodman1999p998]: @Goodman_1999_Toward_evidence_based_medical_statistics_1_The_P\. p. 998.
[^Neyman1933]: @Neyman_1933_On_the_problem_of_the_most_efficient_tests\.


### $p$-values and significance

-   $p$-values and significance [^Cowan2012]
-   Coverage
-   Fisherian vs Neyman-Pearson $p$-values
-   Flip-flopping and Feldman-Cousins confidence intervals [^Feldman1998]

[^Cowan2012]: @Sinervo_2002_Signal_significance_in_particle_physics and @Cowan_2012_Discovery_sensitivity_for_a_counting_experiment\.
[^Feldman1998]: @Feldman_1998_A_unified_approach_to_the_classical_statistical\.


### Student's $t$-test

-   ANOVA
-   A/B-testing


### CLs method

-   Conservative coverage; used in particle physics
-   Junk [^Junk1999]
-   Read [^Read2002]
-   ATLAS [^ATLAS2011]

[^ATLAS2011]: @ATLAS_2011_The_CLs_method_information_for_conference\.
[^Junk1999]: @Junk_1999_Confidence_level_computation_for_combining\.
[^Read2002]: @Read_2002_Presentation_of_search_results_the_CLs_technique\.


### Asymptotics

-   Wilks [^Wilks1938]
-   Pearson $\chi^2$-test
-   Wald [^Wald1943]
-   Cowan _et al_.[^Cowan2011]

[^Cowan2011]: @Cowan_2011_Asymptotic_formulae_for_likelihood_based_tests\.
[^Wald1943]: @Wald_1943_Tests_of_statistical_hypotheses_concerning_several\.
[^Wilks1938]: @Wilks_1938_The_large_sample_distribution_of_the_likelihood\.


### Frequentist vs bayesian decision theory

-   Frequentist vs bayesian decision theory [^Murphy2012p197]

[^Murphy2012p197]: @Murphy_2012_Machine_Learning_A_probabilistic_perspective\, p. 197.


### Examples

-   Difference of two means: $t$-test
-   A/B-testing
-   New physics
    -   [Slides by Me, Ryan Reece: "ATLAS, data reduction, and epistemology"](http://rreece.github.io/talks/pdf/2016-11-29-RReece-ATLAS-Epistemology.pdf)
    -   [Talk by Tommaso Dorigo: "Frequentist Statistics, the Particle Physicists' Way"](https://www.youtube.com/watch?v=NA5u5X23QLo)


Systematic uncertainties
--------------------------------------------------------------------------------

### Sinervo classification

-   Class-1, class-2, and class-3 systematic uncertanties (good, bad, ugly), Classification by Pekka Sinervo (PhyStat2003) [^Sinervo2013]
-   Not to be confused with type-1 and type-2 errors in Neyman-Pearson theory

![Classification of measurement uncertainties ([philosophy-in-figures.tumblr.com](http://philosophy-in-figures.tumblr.com/post/150371555016/classification-of-measurement-uncertainties), 2016).](img/systematic-uncertainties-sinervo.png){#fig:systematic-uncertainties-sinervo}

[^Sinervo2013]: @Sinervo_2003_Definition_and_treatment_of_systematic\.


### Profile likelihoods

-   Profiling and the profile likelihood
    -   Importance of Wald and Cowan _et al_.


### Examples of poor estimates of systematic uncertanties

-   CDF $Wjj$ bump
    -   Phys.Rev.Lett.106:171801 (2011) / [arxiv:1104.0699](https://arxiv.org/abs/1104.0699)
    -   [Invariant mass distribution of jet pairs produced in association with a $W$ boson in $p\bar{p}$ collisions at $\sqrt{s}$ = 1.96 TeV](https://www-cdf.fnal.gov/physics/ewk/2011/wjj/7_3.html)
    -   Dorigo, T. (2011). [The jet energy scale as an explanation of the CDF signal](https://www.science20.com/quantum_diaries_survivor/blog/jet_energy_scale_explanation_cdf_signal-77886).

![Demonstration of sensitivity to the jet energy scale for an alleged excess in $Wjj$ by [Tommaso Dorigo (2011)](https://www.science20.com/quantum_diaries_survivor/blog/jet_energy_scale_explanation_cdf_signal-77886).](img/AnimatedDijet.gif){#fig:AnimatedDijet}

-   Faster-than-light neutrinos.
-   BICEP2 claimed evidence of B-modes in the CMB as evidence of cosmic inflation without accounting for cosmic dust.


Exploratory data analysis
--------------------------------------------------------------------------------

### Introduction

-   [Tukey, John (1915-2000)](https://en.wikipedia.org/wiki/John_Tukey)
    -   [Exploratory data analysis](https://en.wikipedia.org/wiki/Exploratory_data_analysis)
    -   *Exploratory Data Analysis* (1977) [^Tukey1977]

[^Tukey1977]: @Tukey_1977_Exploratory_Data_Analysis\.


### Look-elsewhere effect

-   Look-elsewhere effect (LEE)
    -   AKA File-drawer effect
-   Stopping rules
    -   validation dataset
    -   statistical issues, violates the likelihood principle


### Archiving and data science

-   "Data science"
    -   Data collection, quality, analysis, archival, and reinterpretation
    -   RECAST


Likelihood principle
--------------------------------------------------------------------------------

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

O'Hagan:

>   The first key argument in favour of the Bayesian approach can be called the
>   axiomatic argument. We can formulate systems of axioms of good inference,
>   and under some persuasive axiom systems it can be proved that Bayesian inference
>   is a consequence of adopting any of these systems...
>   If one adopts two principles known as ancillarity and sufficiency principles,
>   then under some statement of these principles it follows that one must adopt
>   another known as the likelihood principle. Bayesian inference conforms to the
>   likelihood principle whereas classical inference does not.
>   Classical procedures regularly violate the likelihood principle
>   or one or more of the other axioms of good inference.
>   There are no such arguments in favour of classical inference. [^OHagan2010]

-   Criticisms:
    -   Evans [^Evans2013]
    -   Mayo [^Mayo2014]
    -   Mayo: [The law of likelihood and error statistics](https://errorstatistics.com/2019/04/04/excursion-1-tour-ii-error-probing-tools-versus-logics-of-evidence-excerpt/) [^Mayo2019]
-   Gandenberger
    -   "A new proof of the likelihood principle" [^Gandenberger2015]
    -   Thesis: [*Two Principles of Evidence and Their Implications for the Philosophy of Scientific Method*](http://d-scholarship.pitt.edu/24634/) (2015)
    -   [gandenberger.org/research](http://gandenberger.org/research/)
    -   [Do frequentist methods violate the likelihood principle?](http://gandenberger.org/2014/04/28/do-frequentist-methods-violate-lp/)
-   [Likelihoodist statistics](https://en.wikipedia.org/wiki/Likelihoodist_statistics)

Mayo:

>   Likelihoods are vital to all statistical accounts, but they are often
>   misunderstood because the data are fixed and the hypothesis varies.
>   Likelihoods of hypotheses should not be confused with their probabilities.
>   ...
>   [T]he same phenomenon may be perfectly predicted or explained by two rival
>   theories; so both theories are equally likely on the data, even though they
>   cannot both be true. [^Mayo2019]

[^Berger1988]: @Berger_1988_The_Likelihood_Principle\.
[^Evans2013]: @Evans_2013_What_does_the_proof_of_Birnbaums_theorem_prove\.
[^Edwards1974]: @Edwards_1974_The_history_of_likelihood\.
[^Gandenberger2015]: @Gandenberger_2015_A_new_proof_of_the_likelihood_principle\.
[^Hacking1965]: @Hacking_1965_Logic_of_Statistical_Inference\.
[^OHagan2010]: @OHagan_2010_Kendalls_Advanced_Theory_of_Statistics_Vol_2B\, p. 17--18\.
[^Mayo2014]: @Mayo_2014_On_the_Birnbaum_Argument_for_the_Strong_Likelihood\.
[^Mayo2019]: @Mayo_2019_The_law_of_likelihood_and_error_statistics\.


"Statistics Wars"
--------------------------------------------------------------------------------

-   Carnap
    -   Sznajder on the alleged evolution of Carnap's views of inductive logic [^Sznajder2018]
-   David Cox
-   Ian Hacking
    -   *Logic of Statistical Inference* [^Hacking1965]
-   Neyman
    -   "Frequentist probability and frequentist statistics" [^Neyman1977]
-   Zech
    -   "Comparing statistical data to Monte Carlo simulation" [^Zech1995]
-   Richard Royall
    -   *Statistical Evidence: A likelihood paradigm* [^Royall1997]
-   Jim Berger
    -   "Could Fisher, Jeffreys, and Neyman have agreed on testing?" [^Berger2003]
-   Deborah Mayo
    -   "In defense of the Neyman-Pearson theory of confidence intervals" [^Mayo1981]
    -   Concept of "Learning from error" in *Error and the Growth of Experimental Knowledge* [^Mayo1996]
    -   "Severe testing as a basic concept in a Neyman-Pearson philosophy of induction" [^Mayo2006]
    -   "Error statistics" [^Mayo2011]
    -   *Statistical Inference as Severe Testing* [^Mayo2018]
    -   [Statistics Wars: Interview with Deborah Mayo](https://blog.apaonline.org/2019/03/07/interview-with-deborah-mayo/) - APA blog
    -   [Review of *SIST* by Prasanta S. Bandyopadhyay](https://ndpr.nd.edu/news/statistical-inference-as-severe-testing-how-to-get-beyond-the-statistics-wars/)
    -   [LSE Research Seminar: Current Controversies in Phil Stat](https://phil-stat-wars.com/2020/05/22/lse-research-seminar-ph500-may-15/) (May 21, 2020)
        -   [Meeting 5](https://phil-stat-wars.com/2020/06/11/meeting-5-june-18/) (June 18, 2020)
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

![The major virtues and vices of Bayesian, frequentist, and likelihoodist approaches to statistical inference ([gandenberger.org/research/](http://gandenberger.org/research/), 2015).](img/gandenberger-thesis-venn-diagram.png){#fig:gandenberger-thesis-venn-diagram}

[^Berger2003]: @Berger_2003_Could_Fisher_Jeffreys_and_Neyman_have_agreed_on\.
[^Birnbaum1962]: @Birnbaum_1962_On_the_foundations_of_statistical_inference\.
[^Gandenberger2016]: @Gandenberger_2016_Why_I_am_not_a_likelihoodist\.
[^Gelman2017]: @Gelman_2017_Beyond_subjective_and_objective_in_statistics\.
[^Mayo1981]: @Mayo_1981_In_defense_of_the_Neyman_Pearson_theory\.
[^Mayo1996]: @Mayo_1996_Error_and_the_Growth_of_Experimental_Knowledge\.
[^Mayo2006]: @Mayo_2006_Severe_testing_as_a_basic_concept_in_a_Neyman_\.
[^Mayo2011]: @Mayo_2011_Error_statistics\.
[^Mayo2018]: @Mayo_2018_Statistical_Inference_as_Severe_Testing_How\.
[^Murphy2012ch6]: @Murphy_2012_Machine_Learning_A_probabilistic_perspective\, ch. 6.6.
[^Neyman1977]: @Neyman_1977_Frequentist_probability_and_frequentist\.
[^Royall1997]: @Royall_1997_Statistical_Evidence_A_likelihood_paradigm\.
[^Sznajder2018]: @Sznajder_2018_Inductive_logic_as_explication_The_evolution\.
[^Zech1995]: @Zech_1995_Comparing_statistical_data_to_Monte_Carlo\.


Replication crisis
--------------------------------------------------------------------------------

### Introduction

-   "Why most published research findings are false" [^Ioannidis2005]

[^Ioannidis2005]: @Ioannidis_2005_Why_most_published_research_findings_are_false\.


### P-value controversy

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
    -   ["Les stats, c'est moi: We take that step here!"](https://errorstatistics.com/2019/12/13/les-stats-cest-moi-we-take-that-step-here-adopt-our-fav-word-or-phil-stat/)
    -   "Significance tests: Vitiated or vindicated by the replication crisis in psychology?" [^Mayo2020]
-   Vox: [What a nerdy debate about p-values shows about science--and how to fix it](https://www.vox.com/science-and-health/2017/7/31/16021654/p-values-statistical-significance-redefine-0005)
-   Karen Kafadar: [The Year in Review ... And More to Come](https://magazine.amstat.org/blog/2019/12/01/kk_dec2019/)

[^Benjamin2017]: @Benjamin_2017_Redefine_statistical_significance\.
[^Fisher1935p13]: @Fisher_1935_The_Design_of_Experiments\, p. 13--14.
[^Mayo2020]: @Mayo_2020_Significance_tests_Vitiated_or_vindicated_by\.
[^Wasserstein2016]: @Wasserstein_2016_The_ASAs_statement_on_p_values_Context_process\.


Classical machine learning
--------------------------------------------------------------------------------

### Introduction

-   classification vs regression
-   supervised and unsupervised learning
    -   classification = supervised; clustering = unsupervised
-   Hastie, Tibshirani, & Friedman [^Hastie2009]
-   *Information Theory, Inference, and Learning* [^MacKay2003]
-   VC-dimension [^Vapnik1994]

[^Hastie2009]: @Hastie_2009_The_Elements_of_Statistical_Learning_Data_Mining\.
[^MacKay2003]: @MacKay_2003_Information_Theory_Inference_and_Learning\.
[^Vapnik1994]: @Vapnik_1994_Measuring_the_VC_dimension_of_a_learning_machine\.


### Logistic regression

TODO: Describe the setup of logistic regression for classification.
Binary classification.

From a probabilistic point of view, [^Murphy2012p21]
logistic regression can be derived from doing maximum likelihood
with a Bernoulli random variable, $y \in \{0, 1\}$, with a probability
$\mu$ that $y = 1$.
The negative log-likelihood of multiple trials is

\begin{align}
\mathrm{NLL}
    &= - \sum_i \log p(y_i | \mu) \nonumber \\
    &= - \sum_i \log\left( \mu_i^{y_i} \: (1-\mu_i)^{(1-y_i)} \right) \nonumber \\
    &= - \sum_i \big( y_i \, \log \mu_i + (1-y_i) \log(1-\mu_i) \big) \label{eq:cross_entropy_loss} \\
\end{align}

which is the **cross entropy loss**.
Note that the first term is non-zero only when the true target is $y_i=1$,
and similarly the second term is non-zero only when  $y_i=0$.
Let us reparametrize the problem in terms of multiple Bernoulli means, $\mu_k$,
where we constrain the total mean probability over classes to be normalized
by defining $\mu_2 = 1 - \mu_1$ and $y_2 = 1 - y_1$, then

$$ \mathrm{CEL} = \mathrm{NLL} = - \sum_i \sum_k \big( y_{ki} \, \log \mu_{ki} \big) \label{eq:cross_entropy_loss2} $$

This readily generalizes from binary classification to classification over many classes,
where now we have an activation, $\mu_k$, for each class.
In the sum over classes, $k$, only one term for the true class contributes [^NoteLabelSmoothing]

$$ \mathrm{CEL} = - \left. \sum_i \log \mu_{ki} \right|_{k\ \mathrm{is\ such\ that}\ y_{ki}=1} \label{eq:cross_entropy_loss3} $$

----------

Logistic regression uses the **logit function** [^Berkson],
which is the logarithm of the odds---the ratio of the chance of success to
failure. Let $\mu$ be the probability of success in a Bernoulli trial,
then the logit function is defined as

$$ \mathrm{logit}(\mu) \equiv \log\left(\frac{\mu}{1-\mu}\right) \label{eq:logit} $$

Logistic regression assumes that the logit function
is a linear function of the explanatory variable, $x$.

$$ \log\left(\frac{\mu}{1-\mu}\right) = \beta_0 + \beta_1 x $$

where $\beta_0$ and $\beta_1$ are trainable parameters.
(TODO: Why would we assume this?)
This can be generalized to a vector of multiple input variables, $\vec{x}$,
where the input vector has a 1 prepended to be its zeroth component in order to
conveniently include the bias, $\beta_0$, in a dot product.

$$ \vec{x} = (1, x_1, x_2, \ldots, x_n)\trans $$

$$ \vec{w} = (\beta_0, \beta_1, \beta_2, \ldots, \beta_n)\trans $$

$$ \log\left(\frac{\mu}{1-\mu}\right) = \vec{w}\trans \vec{x} $$

For the moment, let $z \equiv \vec{w}\trans \vec{x}$.
Exponentiating and solving for $\mu$ gives

$$ \mu = \frac{ e^z }{ 1 + e^z } = \frac{ 1 }{ 1 + e^{-z} } $$

This function is called the **logistic or sigmoid function**.

$$ \mathrm{logistic}(z) \equiv \mathrm{sigm}(z) \equiv \frac{ 1 }{ 1 + e^{-z} }  \label{eq:logistic} $$

Since we inverted the logit function by solving for $\mu$,
the inverse of the logit function is the logistic or sigmoid.

$$ \mathrm{logit}^{-1}(z) = \mathrm{logistic}(z) = \mathrm{sigm}(z) $$

And therefore,

$$ \mu = \mathrm{sigm}(z) = \mathrm{sigm}(\vec{w}\trans \vec{x}) $$

![Logistic regression.](img/logistic-regression.png){#fig:logistic-regression}

From a probabilistic point of view, [^Murphy2012p21]
logistic regression can be derived from doing maximum likelihood
estimation of a vector of model parameters, $\vec{w}$, in a dot product
with the input features, $\vec{x}$, and squashed with a logistic
function that yields the probability, $\mu$, of a Bernoulli random variable, $y \in \{0, 1\}$.

$$ p(y | \vec{x}, \vec{w}) = \mathrm{Ber}(y | \mu(\vec{x}, \vec{w})) = \mu(\vec{x}, \vec{w})^y \: (1-\mu(\vec{x}, \vec{w}))^{(1-y)} $$

The negative log-likelihood of multiple trials is

\begin{align}
\mathrm{NLL}
    &= - \sum_i \log p(y_i | \vec{x}_i, \vec{w}) \nonumber \\
    &= - \sum_i \log\left( \mu(\vec{x}_i, \vec{w})^{y_i} \: (1-\mu(\vec{x}_i, \vec{w}))^{(1-y_i)} \right) \nonumber \\
    &= - \sum_i \log\left( \mu_i^{y_i} \: (1-\mu_i)^{(1-y_i)} \right) \nonumber \\
    &= - \sum_i \big( y_i \, \log \mu_i + (1-y_i) \log(1-\mu_i) \big)
\end{align}

which is the **cross entropy loss**.
Note that the first term is non-zero only when the true target is $y_i=1$,
and similarly the second term is non-zero only when  $y_i=0$.
Therefore, we can reparametrize the target $y_i$ in favor of $t_{ki}$ that
is one-hot in an index $k$ over classes.

$$ \mathrm{CEL} = \mathrm{NLL} = - \sum_i \sum_k \big( t_{ki} \, \log \mu_{ki} \big) \label{eq:cross_entropy_loss2} $$

where

$$ t_{ki} = \begin{cases} 1 & \mathrm{if}\ (k = y_i = 0)\ \mathrm{or}\ (k = y_i = 1) \\ 0 & \mathrm{otherwise} \end{cases} $$

and

$$ \mu_{ki} = \begin{cases} 1-\mu_i & \mathrm{if}\ k = 0 \\ \mu_i & \mathrm{if}\ k =1 \end{cases} $$

This readily generalizes from binary classification to classification over many classes
as we will discuss more below.
Note that in the sum over classes, $k$, only one term for the true class contributes.

$$ \mathrm{CEL} = - \left. \sum_i \log \mu_{ki} \right|_{k\ \mathrm{is\ such\ that}\ y_k=1} \label{eq:cross_entropy_loss3} $$

Again, from a probabilistic point of view, we can derive the use of multi-class cross entropy loss
by starting with the Bernoulli distribution, generalizing it to multiple classes (indexed by $k$) as

$$ p(y_k | \mu) = \mathrm{Cat}(y_k | \mu_k) = \prod_k {\mu_k}^{y_k} \label{eq:categorical_distribution} $$

which is the categorical or multinoulli distribution.
The negative-log likelihood of multiple independent trials is

$$ \mathrm{NLL} = - \sum_i \log \left(\prod_k {\mu_{ki}}^{y_{ki}}\right) = - \sum_i \sum_k y_{ki} \: \log \mu_{ki} \label{eq:nll_multinomial} $$

Noting again that $y_{ki} = 1$ only when $k$ is the true class, and is 0 otherwise, this simplifies
to [@eq:cross_entropy_loss3].

-   [Logistic regression](https://en.wikipedia.org/wiki/Logistic_regression)
    -   Cross entropy loss
    -   Harlan, W.S. (2007). [Bounded geometric growth: motivation for the logistic function](http://www.billharlan.com/pub/papers/logistic/logistic.html).
    -   Heesch, D. [A short intro to logistic regression](http://www.daniel-heesch.com/static/softmax_regression.pdf).
    -   Roelants, P. (2019). [Logistic classification with cross-entropy](https://peterroelants.github.io/posts/cross-entropy-logistic/).
-   [Multinomial logistic regression](https://en.wikipedia.org/wiki/Multinomial_logistic_regression)
    -   Softmax
    -   McFadden [^McFadden1973]
    -   Softmax is really a soft argmax. TODO: find ref.
    -   Softmax is not unique. There are other squashing functions. [^Blondel2020]
    -   Roelants, P. (2019). [Softmax classification with cross-entropy](https://peterroelants.github.io/posts/cross-entropy-softmax/).
    -   Gradients from backprop through a softmax
    -   Goodfellow et al. point out that _any_ negative log-likelihood is a cross entropy
        between the training data and the probability distribution predicted by the model. [^Goodfellow2016p129] 

[^Berkson]: "Logit" was coined by [Joseph Berkson](https://en.wikipedia.org/wiki/Joseph_Berkson) (1899-1982).
[^Blondel2020]: @Blondel_2020_Learning_with_Fenchel_Young_losses\.
[^Goodfellow2016p129]: @Goodfellow_2016_Deep_Learning\, p. 129.
[^McFadden1973]: @McFadden_1973_Conditional_logit_analysis_of_qualitative_choice\.
[^Murphy2012p21]: @Murphy_2012_Machine_Learning_A_probabilistic_perspective\, p. 21.
[^NoteLabelSmoothing]: Note: _Label smoothing_ is a regularization technique that smears the
    activation over other labels, but we don't do that here.


### Clustering

-   Gaussian Mixture Models (GMMs)
    -   Gaussian discriminant analysis
-   Generalized Linear Models (GLMs)
    -   Exponential family of PDFs
    -   Multinoulli $\mathrm{Cat}(x|\mu)$
    -   GLMs
-   EM algorithm
    -   $k$-means
-   [Curse of dimensionality](https://en.wikipedia.org/wiki/Curse_of_dimensionality)
    -   [Stein's paradox](https://en.wikipedia.org/wiki/Stein%27s_example)
    -   [Proof of Stein's example](https://en.wikipedia.org/wiki/Proof_of_Stein%27s_example)
-   [Topological data analysis](https://en.wikipedia.org/wiki/Topological_data_analysis)
    -   Dindin, M. (2018). [TDA To Rule Them All: ToMATo Clustering](https://towardsdatascience.com/tda-to-rule-them-all-tomato-clustering-878e03394a1).


Deep learning
--------------------------------------------------------------------------------

### Introduction

-   Conceptual reviews of deep learning
    -   Lower to higher level representations [^Bengio2009]
    -   "Review: Deep learning" [^LeCun2015]
    -   *Deep Learning* [^Goodfellow2016]
-   Backpropagation
    -   Rumelhart [^Rumelhart1986]
-   Pratical guides
    -   Bengio, Y. (2012). [Practical recommendations for gradient-based training of deep architectures](https://arxiv.org/abs/1206.5533).
    -   Hao, L. et al. (2017). [Visualizing the loss landscape of neural nets](https://arxiv.org/abs/1712.09913).
    -   "Deep learning: A guide for practitioners in the physical sciences" [^Spears2018]
-   Others
    -   "The explanation game: A formal framework for interpretable machine learning" [^Watson2019]
    -   [AIMyths.com](https://www.aimyths.org/)


![Raw input image is transformed into gradually higher levels of representation. [^Bengio2009]](img/bengio-raw-to-higher-rep.png){#fig:bengio-raw-to-higher-rep}

[^Bengio2009]: @Bengio_2009_Learning_deep_architectures_for_AI\.
[^Goodfellow2016]: @Goodfellow_2016_Deep_Learning\.
[^LeCun2015]: @LeCun_2015_Deep_learning\.
[^Rumelhart1986]: @Rumelhart_1986_Learning_representations_by_back_propagating\.
[^Spears2018]: @Spears_2018_Deep_learning_A_guide_for_practitioners\.
[^Watson2019]: @Watson_2019_The_explanation_game_A_formal_framework\.


### Deep double descent

-   Bias and variance trade-off. See [Bias and variance](#bias-and-variance).
-   MSE and model capacity
-   "Reconciling modern machine-learning practice and the classical bias-variance trade-off" [^Belkin2019]
-   "Deep double descent: Where bigger models and more data hurt" [^Nakkiran2019]
-   ["Deep Double Descent"](https://openai.com/blog/deep-double-descent/).  *OpenAI Blog*.
-   Hubinger, E. (2019). [Understanding "Deep Double Descent"](https://www.lesswrong.com/posts/FRv7ryoqtvSuqBxuT/understanding-deep-double-descent). *LessWrong*.

[^Belkin2019]: @Belkin_2019_Reconciling_modern_machine_learning_practice\.
[^Nakkiran2019]: @Nakkiran_2019_Deep_double_descent_Where_bigger_models_and_more\.


### Batch size vs learning rate

Papers:

1.  Keskar, N.S. et al. (2016). [On large-batch training for deep learning: Generalization gap and sharp minima](https://arxiv.org/abs/1609.04836).
2.  Hoffer, E. et al. (2017). [Train longer, generalize better: closing the generalization gap in large batch training of neural networks](https://arxiv.org/abs/1705.08741).
3.  Goyal, P. et al. (2017). [Accurate large minibatch SGD: Training ImageNet in 1 hour](https://arxiv.org/abs/1706.02677).
4.  You, Y. et al. (2017).  [Large batch training of convolutional networks](https://arxiv.org/abs/1708.03888).
5.  You, Y. et al. (2017). [ImageNet training in minutes](https://arxiv.org/abs/1709.05011).
6.  Jastrzebski, S. (2018). [Three factors influencing minima in SGD](https://arxiv.org/abs/1711.04623).
7.  Smith, S.L. (2018). [Don't decay the learning rate, increase the batch size](https://arxiv.org/abs/1711.00489).
8.  Masters, D. & Luschi, C. (2018). [Revisiting small batch training for deep neural networks](https://arxiv.org/abs/1804.07612).
9.  Lin, T. et al. (2020). [Don't use large mini-batches, use local SGD](https://arxiv.org/abs/1808.07217).
10. Golmant, N. et al. (2018). [On the computational inefficiency of large batch sizes for stochastic gradient descent](https://arxiv.org/abs/1811.12941).
11. Arora, S. et al. (2018). [A convergence analysis of gradient descent for deep linear neural networks](https://arxiv.org/abs/1810.02281).
12. McCandlish, S. et al. (2018). [An empirical model of large-batch training](https://arxiv.org/abs/1812.06162).
13. Jastrzebski, S. et al. (2018). [Width of minima reached by stochastic gradient descent is influenced by learning rate to batch size ratio](https://link.springer.com/chapter/10.1007/978-3-030-01424-7_39).
14. You, Y. et al. (2019). [Large-batch training for LSTM and beyond](https://arxiv.org/abs/1901.08256).
15. You, Y. et al. (2019). [Large batch optimization for deep learning: Training BERT in 76 minutes](https://arxiv.org/abs/1904.00962).
16. Zhang, G. et al. (2019). [Which algorithmic choices matter at which batch sizes? Insights from a Noisy Quadratic Model](https://arxiv.org/abs/1907.04164).
17. Li, Y., Wei, C., & Ma, T. (2019). [Towards explaining the regularization effect of initial large learning rate in training neural networks](https://arxiv.org/abs/1907.04595).
18. Jastrzebski, S. et al. (2020). [The break-even point on optimization trajectories of deep neural networks](https://arxiv.org/abs/2002.09572).

Blogs:

-   Shen, K. (2018). [Effect of batch size on training dynamics](https://medium.com/mini-distill/effect-of-batch-size-on-training-dynamics-21c14f7a716e).
-   Chang, D. (2020). [Effect of batch size on neural net training](https://medium.com/deep-learning-experiments/effect-of-batch-size-on-neural-net-training-c5ae8516e57).


### Regularization

Regularization = any change we make to the training algorithm in order to reduce the generalization error but not the training error. [^Mishra2020]

Most common regularizations:

-   L2 Regularization
-   L1 Regularization
-   Data Augmentation
-   Dropout
-   Early Stopping

Papers:

-   Loshchilov, I. & Hutter, F. (2019). [Decoupled weight decay regularization](https://arxiv.org/abs/1711.05101).

[^Mishra2020]: Mishra, D. (2020). [Weight Decay == L2 Regularization?](https://towardsdatascience.com/weight-decay-l2-regularization-90a9e17713cd)


### Computer vision

Computer Vision (CV)

-   Fukushima: neocognitron
-   LeCun: OCR with backpropagation [^LeCun1989]
-   LeCun: LeNet-5 [^LeCun1998]
-   Ciresan: MCDNN
-   Krizhevsky, Sutskever, and Hinton: AlexNet [^Krizhevsky2012]
-   VGG
-   ResNet

[^Krizhevsky2012]: @Krizhevsky_2012_ImageNet_classification_with_deep_convolutional\.
[^LeCun1989]: @LeCun_1989_Backpropagation_applied_to_handwritten_zip_code\.
[^LeCun1998]: @LeCun_1998_Gradient_based_learning_applied_to_document\.


### Natural language processing

Natural language processing (NLP)

-   RNNs and LSTMs
    -   Hochreiter, S. & Schmidhuber, J. (1997). Long short-term memory. [^Hochreiter1997]
-   Backpropagation through time (BPTT)
-   Sutskever seq2seq [^Sutskever2014]
-   Review by Stahlberg [^Stahlberg2019]
-   Rationalism and empiricism in artificial intellegence:
    A survey of 25 years of evaluation [in NLP]. [^Church2019]
-   Transformer
-   Horev, R. (2018). [BERT Explained: State of the art language model for NLP](https://towardsdatascience.com/bert-explained-state-of-the-art-language-model-for-nlp-f8b21a9b6270).
-   GPT-1, 2, 3

[^Church2019]: @Church_2019_A_survey_of_25_years_of_evaluation\.
[^Hochreiter1997]: @Hochreiter_1997_Long_short_term_memory\.
[^Stahlberg2019]: @Stahlberg_2019_Neural_machine_translation_A_review\.
[^Sutskever2014]: @Sutskever_2014_Sequence_to_sequence_learning_with_neural\.


### Reinforcement learning

-   AlphaGo
-   Sutton & Barto [^Sutton2018]

[^Sutton2018]: @Sutton_2018_Reinforcement_Learning\.


Theoretical machine learning
--------------------------------------------------------------------------------

### No free lunch theorem

-   David Wolpert
-   Inductive bias
-   Yudkowsky, E. (2007). "[Inductive bias](https://www.lesswrong.com/posts/H59YqogX94z5jb8xx/inductive-bias)". *LessWrong*.
-   Hamilton, L.D. (2014). "[The inductive biases of various machine learning algorithms](http://www.lauradhamilton.com/inductive-biases-various-machine-learning-algorithms)".
-   Wolpert, D. (2018). [Why do computers use so much energy?](https://blogs.scientificamerican.com/observations/why-do-computers-use-so-much-energy/)
-   [Sante Fe Institute: Thermodynamics of Computation](https://centre.santafe.edu/thermocomp/Santa_Fe_Institute_Collaboration_Platform:Thermodynamics_of_Computation_Wiki)
-   Gerhard Schurz


###  Graphical tensor notation

-   [Penrose graphical notation](https://en.wikipedia.org/wiki/Penrose_graphical_notation)
-   Predrag Cvitanovic
-   [Matrices as Tensor Network Diagrams](https://www.math3ma.com/blog/matrices-as-tensor-network-diagrams)


### Relationship to statistical mechanics

-   Logistic/softmax and Boltzman factors
-   Bahri [^Bahri2020]
-   Halverson [^Halverson2020]
-   Canatar, A., Bordelon, B., & Pehlevan, C. [Spectral bias and task-model alignment explain generalization in kernel regression and infinitely wide neural networks](https://arxiv.org/abs/2006.13198).

[^Bahri2020]: @Bahri_2020_Statistical_mechanics_of_deep_learning\.
[^Halverson2020]: @Halverson_2020_Neural_networks_and_quantum_field_theory\.


### Relationship to gauge theory

-   Cohen


Information geometry
--------------------------------------------------------------------------------

### Introduction

-   "A gentle introduction to information geometry" [^Smith2019]
-   "An elementary introduction to information geometry" [^Nielsen2018]
-   *Information Geometry and Its Applications* [^Amari2016]

[^Amari2016]: @Amari_2016_Information_Geometry_and_Its_Applications\.
[^Nielsen2018]: @Nielsen_2018_An_elementary_introduction_to_information_geometry\.
[^Smith2019]: @Smith_2019_A_gentle_introduction_to_information_geometry\.


### Geometric understanding of classical statistics

-   "A geometric formulation of Occam's razor for inference of parametric distributions" [^Balasubramanian1996a]
-   "Statistical inference, Occam's Razor and statistical mechanics on the space of probability distributions" [^Balasubramanian1996b]
-   *Geometric Modeling in Probability and Statistics* [^Calin2014]
-   Cranmer

[^Balasubramanian1996a]: @Balasubramanian_1996_A_geometric_formulation_of_Occams_razor\.
[^Balasubramanian1996b]: @Balasubramanian_1996_Statistical_inference_Occams_razor\.
[^Calin2014]: @Calin_2014_Geometric_Modeling_in_Probability_and_Statistics\.


### Geometric understanding of deep learning

-   "Geometric understanding of deep learning" [^Lei2018]
-   Cohen [^Cohen2016]
-   Gao, Y. & Chaudhari, P. (2020). [An information-geometric distance on the space of tasks](https://arxiv.org/abs/2011.00613).

[^Cohen2016]: @Cohen_2016_Group_equivariant_convolutional_networks\.
[^Lei2018]: @Lei_2018_Geometric_understanding_of_deep_learning


Automation
--------------------------------------------------------------------------------

### AutoML

-   Neural Architecture Search (NAS)
-   AutoML frameworks


### Surrogate models

-   Autoencoders, latent variables
-   Physical constratints in loss functions
-   "The frontier of simulation-based inference" [^Cranmer2019]


### AutoScience

-   Automated discovery
-   "Learning new physics from a machine" [^DAgnolo2019]
-   "Big data and extreme-scale computing: Pathways to Convergence-Toward a shaping strategy for a future software and data ecosystem for scientific inquiry." [^Asch2018]
    -   Note that this description of abduction is missing that it is normative (i.e. "best-fit").
-   "The End of Theory: The data deluge makes the scientific method obsolete." [^Anderson2008]
-   "Symbolic pregression: Discovering physical laws from raw distorted video." [^Udrescu2020]
-   "Discovering symbolic models from deep learning with inductive biases." [^Cranmer2020]
    -   Video: [Discussion by Yannic Kilcher](https://www.youtube.com/watch?v=LMb5tvW-UoQ)
-   See also: [Artificial intelligence](http://rreece.github.io/outline-of-philosophy/future.html#artificial-intelligence)
    in the [Outline of future studies](http://rreece.github.io/outline-of-philosophy/future.html).

![The inference cycle for the process of scientific inquiry. The three distinct forms of inference (abduction, deduction, and induction) facilitate an all-encompassing vision, enabling HPC and HDA to converge in a rational and structured manner. HPC: high- performance computing; HDA: high-end data analysis. [^Asch2018fig]](img/BDEC-scientific-method.png){#fig:BDEC-scientific-method}

[^Anderson2008]: @Anderson_2008_The_End_of_Theory_The_data_deluge_makes\.
[^Asch2018]: @Asch_2018_Big_data_and_extreme_scale_computing_Pathways\.
[^Asch2018fig]: @Asch_2018_Big_data_and_extreme_scale_computing_Pathways\.
[^Cranmer2019]: @Cranmer_2019_The_frontier_of_simulation_based_inference\.
[^Cranmer2020]: @Cranmer_2020_Discovering_symbolic_models_from_deep_learning\.
[^DAgnolo2019]: @DAgnolo_2019_Learning_New_Physics_from_a_Machine\.
[^Udrescu2020]: @Udrescu_2020_Symbolic_pregression_Discovering_physical_laws\.


Implications for the realism debate
--------------------------------------------------------------------------------

-   Korb [^Korb2001]
-   Williamson [^Williamson2009]
-   Bensusan [^Bensusan2000]
-   Note that NLP has implications to the philosophy of language and realism
    -   [NLP word representations and the Wittgenstein philosophy of language](http://blog.christianperone.com/2018/05/nlp-word-representations-and-the-wittgenstein-philosophy-of-language/). [^Perone2018]
-   See the [Outline on scientific realism](scientific-realism.html)

[^Bensusan2000]: @Bensusan_2000_Is_machine_learning_experimental_philosophy\.
[^Korb2001]: @Korb_2001_Machine_learning_as_philosophy_of_science\.
[^Perone2018]: @Perone_2018_NLP_word_representations_and_the_Wittgenstein\.
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

-   @Cowan_1998_Statistical_Data_Analysis and @Cowan_2016_StatisticsIn_CPatrignani_et_alParticle_Data

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
-   [Analysis of knowledge](http://plato.stanford.edu/entries/knowledge-analysis/)
-   [Bayes' theorem](https://plato.stanford.edu/entries/bayes-theorem/)
-   [Bayesian epistemology](https://plato.stanford.edu/entries/epistemology-bayesian/)
-   [Carnap, Rudolf (1891-1970)](https://plato.stanford.edu/entries/carnap/)
-   [Causal models](https://plato.stanford.edu/entries/causal-models/)
-   [Causal processes](http://plato.stanford.edu/entries/causation-process/)
-   [Confirmation](https://plato.stanford.edu/entries/confirmation/)
-   [Dutch book arguments](https://plato.stanford.edu/entries/dutch-book/)
-   [Epistemology](http://plato.stanford.edu/entries/epistemology/)
-   [Foundationalist Theories of Epistemic Justification](http://plato.stanford.edu/entries/justep-foundational/)
-   [Hume, David (1711-1776)](http://plato.stanford.edu/entries/hume/)
-   [Identity of indiscernibles](http://plato.stanford.edu/entries/identity-indiscernible/)
-   [Induction, The problem of](http://plato.stanford.edu/entries/induction-problem/)
-   [Logic and Probability](https://plato.stanford.edu/entries/logic-probability/)
-   [Naturalized epistemology](http://plato.stanford.edu/entries/epistemology-naturalized/)
-   [Peirce, Charles Sanders (1839-1914)](https://plato.stanford.edu/entries/peirce/)
-   [Popper, Karl (1902-1994)](http://plato.stanford.edu/entries/popper/)
-   [Principle of sufficient reason](http://plato.stanford.edu/entries/sufficient-reason/)
-   [Probability, Interpretations of](https://plato.stanford.edu/entries/probability-interpret/)
-   [Probabilistic pausation](https://plato.stanford.edu/entries/causation-probabilistic/)
-   [Reichenbach, Hans (1891-1953)](https://plato.stanford.edu/entries/reichenbach/)
-   [Scientific explanation](http://plato.stanford.edu/entries/scientific-explanation/)
-   [Scientific research and big data](https://plato.stanford.edu/entries/science-big-data/)
-   [Statistics, Philosophy of](http://plato.stanford.edu/entries/statistics/)

### IEP

-   [Carnap, Rudolf (1891-1970)](http://www.iep.utm.edu/carnap/)
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
-   [Bernoulli, Jacob (1655-1705)](https://en.wikipedia.org/wiki/Jacob_Bernoulli)
-   [Birnbaum, Allan (1923-1976)](https://en.wikipedia.org/wiki/Allan_Birnbaum)
-   [Bootstrapping](http://en.wikipedia.org/wiki/Bootstrapping_(statistics))
-   [Carnap, Rudolf (1891-1970)](http://en.wikipedia.org/wiki/Rudolf_Carnap)
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
-   [Replication crisis](https://en.wikipedia.org/wiki/Replication_crisis)
-   [Rule of three](https://en.wikipedia.org/wiki/Rule_of_three_(statistics))
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

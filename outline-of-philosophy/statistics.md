Philosophy of statistics
================================================================================

Statistics are *way* important in addressing the problem of induction.

<!-- PAGETOC -->


Issues and positions
--------------------------------------------------------------------------------

### Problem of induction

-   How do we infer universals from particulars?
-   Hume [^Hume2007]
    -   Weintraub [^Weintraub1995]
-   Mill
-   Peirce
-   Reichenbach [^Reichenbach1938]
    -   Salmon [^Salmon1963]
-   Good [^Good1988]
-   Hacking [^Hacking2001]
-   Huber [^Huber2007]

[^Hacking2001]: @Hacking_2001_An_Introduction_to_Probability_and_Inductive_Logic\.
[^Huber2007]: @Huber_2007_Confirmation_and_induction\.
[^Hume2007]: @Hume_2007_An_Enquiry_Concerning_Human_Understanding\.
[^Good1988]: @Good_1988_The_interface_between_statistics_and_philosophy\.
[^Reichenbach1938]: @Reichenbach_1938_Experience_and_Prediction and
    @Reichenbach_1940_On_the_justification_of_induction\.
[^Salmon1963]: @Salmon_1963_On_vindicating_induction\,
    @Salmon_1966_The_Foundations_of_Scientific_Inference\,
    @Salmon_1991_Hans_Reichenbachs_vindication_of_induction\.
[^Weintraub1995]: @Weintraub_1995_What_was_Humes_contribution_to_the_problem\.


### Probability and uncertainty

-   Kolmogorov
-   Frequentist vs Bayesian probability
    -   [Bayes, Thomas (1701-1761)](https://en.wikipedia.org/wiki/Thomas_Bayes)
-   Accuracy vs precision [^Cowan1998]


### Early investigators

-   [Graunt, John (1620-1674)](https://en.wikipedia.org/wiki/John_Graunt)
-   [Bayes, Thomas (1701-1761)](https://en.wikipedia.org/wiki/Thomas_Bayes)
-   [Gauss, Carl Friedrich (1777-1855)](http://en.wikipedia.org/wiki/Gauss)
-   [Mill, John Stuart (1806-1873)](https://en.wikipedia.org/wiki/John_Stuart_Mill)
-   [Venn, John (1834-1923)](https://en.wikipedia.org/wiki/John_Venn)
    -   *The Logic of Chance* (1866) [^Venn1888]
-   [Peirce, Charles Sanders (1839-1914)](https://en.wikipedia.org/wiki/Charles_Sanders_Peirce)
    -   Formulated modern statistics in "Illustrations of the Logic of Science" (1877-1878) and "A Theory of Probable Inference" in *Studies in Logic* (1883).
    -   With a repeated measures design, introduced blinded, controlled randomized experiments (before Fisher).
-   [Turkey, John (1915-2000)](https://en.wikipedia.org/wiki/John_Tukey)

[^Venn1888]: @Venn_1888_The_Logic_of_Chance


### Foundations of statistics

-   Ronald Fisher, Jerzy Neyman, Egon Pearson, Harold Jeffreys
    -   Fisher significance of the null hypothesis ($p$-values)
        -   On an absolute criterion for fitting frequency curves. [^Fisher1912]
        -   Frequency distribution of the values of the correlation coefficient in samples of indefinitely large population. [^Fisher1915]
    -   Neyman-Pearson confidence intervals with fixed error probabilities (also $p$-values but considering two hypotheses involves two types of errors)
    -   objective (non-informative) Jeffreys priors
-   Responses
    -   Cox
    -   Berger [^Berger2003]
    -   Mayo
        -   Learning from Error [^Mayo1996]
        -   Error statistics [^Mayo2006]
-   Likelihood principle
    -   Birnbaum
    -   violated by both Frequentists and Bayesians
-   Pedagogy
    -   Kendall [^Kendall1946]
    -   James [^James2006]
    -   Cowan [^Cowan1998]
    -   Cranmer [^Cranmer2015]

[^Berger2003]: @Berger_2003_Could_Fisher_Jeffreys_and_Neyman_have_agreed_on\.
[^Cowan1998]: @Cowan_1998_Statistical_Data_Analysis and @Cowan_2016_Statistics\. 
[^Cranmer2015]: @Cranmer_2015_Practical_statistics_for_the_LHC\.
[^Fisher1912]: @Fisher_1912_On_an_absolute_criterion_for_fitting_frequency\.
[^Fisher1915]: @Fisher_1915_Frequency_distribution_of_the_values\.
[^James2006]: @James_2006_Statistical_Methods_in_Experimental_Particle\.
[^Kendall1946]: @Kendall_1946_The_Advanced_Theory_of_Statistics_VolII\.
[^Mayo1996]: @Mayo_1996_Error_and_the_Growth_of_Experimental_Knowledge\.
[^Mayo2006]: @Mayo_1981_In_defense_of_the_Neyman_Pearson_theory\.


### Statistical hypothesis testing

-   classification
-   Type-1 and type-2 errors in Neyman-Pearson theory
-   Power and confidence
-   Neyman-Pearson lemma [^Neyman1933]
-   Wilks [^Wilks1938] and Wald [^Wald1943]
-   $p$-values and significance [^Cowan2012]
-   Flip-flopping and Feldman-Cousins confidence intervals [^Feldman1998]

[^Cowan2012]: @Sinervo_2002_Signal_significance_in_particle_physics and @Cowan_2012_Discovery_sensitivity_for_a_counting_experiment\.
[^Feldman1998]: @Feldman_1998_A_unified_approach_to_the_classical_statistical\.
[^Neyman1933]: @Neyman_1933_On_the_problem_of_the_most_efficient_tests\.
[^Wald1943]: @Wald_1943_Tests_of_statistical_hypotheses_concerning_several\.
[^Wilks1938]: @Wilks_1938_The_large_sample_distribution_of_the_likelihood\.


### Point estimation and confidence intervals

-   regression
-   MLE: Maximum likelihood estimators, Fisher [^Aldrich1997]
-   Cram&eacute;r-Rao bound [^Cramer-Rao]
-   Asymptotics [^Cowan2011]

[^Aldrich1997]: @Aldrich_1997_RAFisher_and_the_making_of_maximum_likelihood\.
[^Cramer-Rao]: @Frechet_1943_Sur_lextension_de_certaines_evaluations\,
    @Cramer_1946_A_contribution_to_the_theory_of_statistical\,
    @Rao_1945_Information_and_the_accuracy_attainable\, and
    @Rao_1947_Minimum_variance_and_the_estimation_of_several\.
[^Cowan2011]: @Cowan_2011_Asymptotic_formulae_for_likelihood_based_tests\.


### Systematic uncertainties

-   Class-1, class-2, and class-3 systematic uncertanties (good, bad, ugly), Classification by Pekka Sinervo (PhyStat2003) [^Sinervo2013]
-   Not to be confused with type-1 and type-2 errors in Neyman-Pearson theory

[^Sinervo2013]: @Sinervo_2003_Definition_and_treatment_of_systematic\.

![Classification of measurement uncertainties ([philosophy-in-figures.tumblr.com](http://philosophy-in-figures.tumblr.com/post/150371555016/classification-of-measurement-uncertainties)).](img/systematic-uncertainties-sinervo.png){#fig:systematic-uncertainties-sinervo}


### P-value controversy

-   file-drawer effect = look-elsewhere effect
-   [Hi-Phi Nation, episode 7](https://hiphination.org/episodes/episode-7-hackademics-ii-the-hackers/)
-   ASA statement on $p$-values [^Wasserstein2016]
-   [Big names in statistics want to shake up much-maligned P value](http://www.nature.com/news/big-names-in-statistics-want-to-shake-up-much-maligned-p-value-1.22375) [^Benjamin2017]

[^Benjamin2017]: @Benjamin_2017_Redefine_statistical_significance\.
[^Wasserstein2016]: @Wasserstein_2016_The_ASAs_statement_on_p_values_Context_process\.


### Machine learning

-   classification and regression
-   supervised and unsupervised learning
-   Hastie, Tibshirani, & Friedman [^Hastie2009]

[^Hastie2009]: @Hastie_2009_The_Elements_of_Statistical_Learning_Data_Mining\.


### Auto-science

![The inference cycle for the process of scientific inquiry. The three distinct forms of inference (abduction, deduction, and induction) facilitate an all-encompassing vision, enabling HPC and HDA to converge in a rational and structured manner. HPC: high- performance computing; HDA: high-end data analysis.](img/BDEC-scientific-method.png){#fig:img/BDEC-scientific-method}

-   Big data and extreme-scale computing: Pathways to Convergence...
-   Note that this description of abduction is missing that it is normative (i.e. "best-fit").

[^Asch2018]: @Asch_2018_Big_data_and_extreme_scale_computing_Pathways\.


### Implications for the realism debate

-   See the outline on [Scientific realism](scientific-realism.html)
-   Perone, C.S. (2018). [NLP word representations and the Wittgenstein philosophy of language](http://blog.christianperone.com/2018/05/nlp-word-representations-and-the-wittgenstein-philosophy-of-language/).


My thoughts
--------------------------------------------------------------------------------

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

### James, F. (2006). *Statistical Methods in Experimental Physics, 2nd Ed.*

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

### ATLAS Collaboration. (2012). Combined search for the Standard Model Higgs boson in $pp$ collisions at $\sqrt{s}$ = 7 TeV with the ATLAS detector.

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

-   Univariate Distribution Relationships [^Leemis2008]
-   *All of Statistics* [^Wasserman2003]
-   *The Foundations of Statistics* [^Savage1954]

[^Leemis2008]: @Leemis_2008_Univariate_distribution_relationships\.
[^Savage1954]: @Savage_1954_The_Foundations_of_Statistics\.
[^Wasserman2003]: @Wasserman_2003_All_of_Statistics_A_Concise_Course_in_Statistical\.


Links and encyclopedia articles
--------------------------------------------------------------------------------

### SEP

-   [Abduction](http://plato.stanford.edu/entries/abduction/)
-   [Analysis of Knowledge](http://plato.stanford.edu/entries/knowledge-analysis/)
-   [Causal Models](https://plato.stanford.edu/entries/causal-models/)
-   [Causal Processes](http://plato.stanford.edu/entries/causation-process/)
-   [Epistemology](http://plato.stanford.edu/entries/epistemology/)
-   [Foundationalist Theories of Epistemic Justification](http://plato.stanford.edu/entries/justep-foundational/)
-   [Hume, David (1711-1776)](http://plato.stanford.edu/entries/hume/)
-   [Identity of Indiscernibles](http://plato.stanford.edu/entries/identity-indiscernible/)
-   [Induction, The problem of](http://plato.stanford.edu/entries/induction-problem/)
-   [Naturalized epistemology](http://plato.stanford.edu/entries/epistemology-naturalized/)
-   [Popper, Karl (1902-1994)](http://plato.stanford.edu/entries/popper/)
-   [Principle of Sufficient Reason](http://plato.stanford.edu/entries/sufficient-reason/)
-   [Scientific Explanation](http://plato.stanford.edu/entries/scientific-explanation/)
-   [Statistics, Philosophy of](http://plato.stanford.edu/entries/statistics/)

### IEP

-   [Epistemology](http://www.iep.utm.edu/epistemo/)
-   [Hempel, Carl Gustav (1905-1997)](http://www.iep.utm.edu/hempel/)
-   [Hume, David (1711-1776)](http://www.iep.utm.edu/hume-cau/)
-   [Naturalism](http://www.iep.utm.edu/naturali/)
-   [Naturalistic Epistemology](http://www.iep.utm.edu/nat-epis/)
-   [Reductionism](http://www.iep.utm.edu/red-ism/)
-   [Safety Condition for Knowledge, The](http://www.iep.utm.edu/safety-c/)
-   [Simplicity in the philosophy of science](http://www.iep.utm.edu/simplici/)
-   [William of Ockham (1280-1349)](http://www.iep.utm.edu/ockham/)

### Scholarpedia

-   [Algorithmic probability](http://www.scholarpedia.org/article/Algorithmic_probability)

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
-   [Data science](https://en.wikipedia.org/wiki/Data_science)
-   [Decision theory](https://en.wikipedia.org/wiki/Decision_theory)
-   [Deductive-nomological model](https://en.wikipedia.org/wiki/Deductive-nomological_model)
-   [Empircism](http://en.wikipedia.org/wiki/Empiricism)
-   [Epistemology](http://en.wikipedia.org/wiki/Epistemology)
-   [Fisher, Ronald (1890-1962)](https://en.wikipedia.org/wiki/Ronald_Fisher)
-   [Frequentist inference](https://en.wikipedia.org/wiki/Frequentist_inference)
-   [Foundations of statistics](https://en.wikipedia.org/wiki/Foundations_of_statistics)
-   [Gauss, Carl Friedrich (1777-1855)](http://en.wikipedia.org/wiki/Gauss)
-   [German tank problem](https://en.wikipedia.org/wiki/German_tank_problem)
-   [Graunt, John (1620-1674)](https://en.wikipedia.org/wiki/John_Graunt)
-   [History of probability](https://en.wikipedia.org/wiki/History_of_probability)
-   [History of statistics](https://en.wikipedia.org/wiki/History_of_statistics)
-   [Hume, David (1711-1776)](http://en.wikipedia.org/wiki/David_Hume)
-   [Induction, The problem of](http://en.wikipedia.org/wiki/Problem_of_induction)
-   [Inductive reasoning](https://en.wikipedia.org/wiki/Inductive_reasoning)
-   [Interval estimation](http://en.wikipedia.org/wiki/Interval_estimation)
-   [Jeffrey, Richard (1926-2002)](https://en.wikipedia.org/wiki/Richard_Jeffrey)
-   [Jeffreys, Harold (1891-1989)](https://en.wikipedia.org/wiki/Harold_Jeffreys)
-   [Jeffreys prior](https://en.wikipedia.org/wiki/Jeffreys_prior)
-   [Kolmogorov, Andrey (1903-1987)](https://en.wikipedia.org/wiki/Andrey_Kolmogorov)
-   [Kolmogorov complexity](https://en.wikipedia.org/wiki/Kolmogorov_complexity)
-   [Laplace, Pierre-Simon (1749-1827)](https://en.wikipedia.org/wiki/Pierre-Simon_Laplace)
-   [Likelihood principle](http://en.wikipedia.org/wiki/Likelihood_principle)
-   [Machine learning](https://en.wikipedia.org/wiki/Machine_learning)
-   [Maximum likelihood estimation](https://en.wikipedia.org/wiki/Maximum_likelihood_estimation)
-   [Mill, John Stuart (1806-1873)](https://en.wikipedia.org/wiki/John_Stuart_Mill)
-   [Neyman, Jerzy (1894-1981)](https://en.wikipedia.org/wiki/Jerzy_Neyman)
-   [Neyman-Pearson lemma](http://en.wikipedia.org/wiki/Neyman%E2%80%93Pearson_lemma)
-   [Ockham, William of (1287-1347)](http://en.wikipedia.org/wiki/William_of_Ockham)
-   [Pearson, Egon (1895-1980)](https://en.wikipedia.org/wiki/Egon_Pearson)
-   [Peirce, Charles Sanders (1839-1914)](https://en.wikipedia.org/wiki/Charles_Sanders_Peirce)
-   [Poisson, Sim&eacute;on Denis (1781-1840)](https://en.wikipedia.org/wiki/Sim%C3%A9on_Denis_Poisson)
-   [Popper, Karl (1902-1994)](https://en.wikipedia.org/wiki/Karl_Popper)
-   [Principle of sufficient reason](https://en.wikipedia.org/wiki/Principle_of_sufficient_reason)
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
-   [Systematic error](http://en.wikipedia.org/wiki/Systematic_error)
-   [Trial and error](https://en.wikipedia.org/wiki/Trial_and_error)
-   [Turkey, John (1915-2000)](https://en.wikipedia.org/wiki/John_Tukey)
-   [Type-I and type-II errors](http://en.wikipedia.org/wiki/Type_I_and_type_II_errors)
-   [Uncomfortable science](https://en.wikipedia.org/wiki/Uncomfortable_science)
-   [Uniformitarianism](http://en.wikipedia.org/wiki/Uniformitarianism)
-   [Unsolved problems in statistics, List of](http://en.wikipedia.org/wiki/List_of_unsolved_problems_in_statistics)
-   [Venn, John (1834-1923)](https://en.wikipedia.org/wiki/John_Venn)

### Others

-   [errorstatistics.com](http://errorstatistics.com/) - Deborah Mayo's blog
-   [Graunt, John (1620-1674)](http://statprob.com/encyclopedia/JohnGRAUNT.html) - statprob.com
-   [Peng, R. (2016). A Simple Explanation for the Replication Crisis in Science.](http://simplystatistics.org/2016/08/24/replication-crisis/) - simplystatistics.org


<!-- REFERENCES -->



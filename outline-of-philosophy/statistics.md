Philosophy of statistics
================================================================================

Statistics are *way* important in addressing the problem of induction.

<!-- PAGETOC -->


Issues and positions
--------------------------------------------------------------------------------

### Problem of induction

See the [Outline of the scientific method](scientific-method.html#induction)


### Probability and uncertainty

-   Kolmogorov
-   Bayes' theorem

$$ P(A|B) = P(B|A) \: P(A) \: / \: P(B) \label{eq:bayes_theorem} $$

-   Frequentist vs Bayesian probability
    -   [Bayes, Thomas (1701-1761)](https://en.wikipedia.org/wiki/Thomas_Bayes)
-   Cranmer

>   Bayes's theorem is a theorem, so there's no debating it. It is not the case that
>   Frequentists dispute whether Bayes's theorem is true. The debate is whether the
>   necessary probabilities exist in the first place. If one can define the joint
>   probability $P (A, B)$ in a frequentist way, then a Frequentist is perfectly
>   happy using Bayes theorem. Thus, the debate starts at the very definition of
>   probability. [^Cranmer2015p6]

-   Carnap
    -   "The two concepts of probability" [^Carnap1945b]
    -   "Probability as a guide in life" [^Carnap1947]
-   Royall
    -   "What do these data say?" [^Royall1997]
-   Accuracy vs precision [^Cowan1998pX]

[^Carnap1945b]: @Carnap_1945_The_two_concepts_of_probability\.
[^Carnap1947]: @Carnap_1947_Probability_as_a_guide_in_life\.
[^Cowan1998pX]: @Cowan_1998_Statistical_Data_Analysis and @Cowan_2016_Statistics\, p. X. 
[^Cranmer2015p6]: @Cranmer_2015_Practical_statistics_for_the_LHC\, p. 6.
[^Royall1997]: @Royall_1997_Statistical_Evidence_A_likelihood_paradigm\, p. 171--2.


### Early investigators

-   [Graunt, John (1620-1674)](https://en.wikipedia.org/wiki/John_Graunt)
-   [Bernoulli, Jacob (1655-1705)](https://en.wikipedia.org/wiki/Jacob_Bernoulli)
    -   *Ars Conjectandi* (1713, posthumous)
    -   First modern phrasing of the problem of parameter estimation [^Edwards1974p9]
    -   See Hacking [^Hacking1971]
    -   Early vision of decision theory:

        >   The art of measuring, as precisely as possible, probabilities of things,
        >   with the goal that we would be able always to choose or follow in our
        >   judgments and actions that course, which will have been determined to be
        >   better, more satisfactory, safer or more advantageous.

        --
        *Ars Conjectandi* (1713) Chapter II, Part IV, defining the art of conjecture [[wikiquote](https://en.wikiquote.org/wiki/Jacob_Bernoulli)].
-   [Bayes, Thomas (1701-1761)](https://en.wikipedia.org/wiki/Thomas_Bayes)
-   [Gauss, Carl Friedrich (1777-1855)](http://en.wikipedia.org/wiki/Gauss)
-   [Mill, John Stuart (1806-1873)](https://en.wikipedia.org/wiki/John_Stuart_Mill)
-   [Venn, John (1834-1923)](https://en.wikipedia.org/wiki/John_Venn)
    -   *The Logic of Chance* (1866) [^Venn1888]

[^Edwards1974p9]: @Edwards_1974_The_history_of_likelihood\, p. 9.
[^Hacking1971]: @Hacking_1971_Jacques_Bernoullis_Art_of_conjecturing\.
[^Venn1888]: @Venn_1888_The_Logic_of_Chance\.


### Foundations of statistics

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
-   [Neyman, Jerzy (1894-1981)](https://en.wikipedia.org/wiki/Jerzy_Neyman)
-   [Pearson, Egon (1895-1980)](https://en.wikipedia.org/wiki/Egon_Pearson)
    -   Neyman-Pearson confidence intervals with fixed error probabilities (also $p$-values but considering two hypotheses involves two types of errors)
-   [Jeffreys, Harold (1891-1989)](https://en.wikipedia.org/wiki/Harold_Jeffreys)
    -   objective (non-informative) Jeffreys priors
-   Pedagogy
    -   Kendall [^Kendall1946]
    -   James [^James2006]
    -   Cousins [^Cousins2018]
    -   Cowan [^Cowan1998]
    -   Cranmer [^Cranmer2015]
    -   Weisberg [^Weisberg2019]

[^Fisher1912]: @Fisher_1912_On_an_absolute_criterion_for_fitting_frequency\.
[^Fisher1915]: @Fisher_1915_Frequency_distribution_of_the_values\.
[^Fisher1921]: @Fisher_1921_On_the_probable_error_of_a_coefficient\.
[^Peirce1883]: @Peirce_1883_Studies_in_Logic\, p. 126--181.

[^Cousins2018]: @Cousins_2018_Lectures_on_statistics_in_theory_Prelude\.
[^Cowan1998]: @Cowan_1998_Statistical_Data_Analysis and @Cowan_2016_Statistics\. 
[^Cranmer2015]: @Cranmer_2015_Practical_statistics_for_the_LHC\.
[^James2006]: @James_2006_Statistical_Methods_in_Experimental_Particle\.
[^Kendall1946]: @Kendall_1946_The_Advanced_Theory_of_Statistics_VolII\.
[^Weisberg2019]: @Weisberg_2019_Odds__Ends_Introducing_Probability__Decision\.


### Point estimation and confidence intervals

-   [Inverse problem](https://en.wikipedia.org/wiki/Inverse_problem)
-   regression
-   MLE: Maximum likelihood estimators, Fisher [^Aldrich1997]
-   Cram&eacute;r-Rao bound [^Cramer-Rao]
    -   proof in Rice [^Rice2007p300]
-   Pearson $\chi^2$
-   Neyman construction
-   Bayesian credability intervals
-   Invariance of the likelihood

[^Aldrich1997]: @Aldrich_1997_RAFisher_and_the_making_of_maximum_likelihood\.
[^Cramer-Rao]: @Frechet_1943_Sur_lextension_de_certaines_evaluations\,
    @Cramer_1946_A_contribution_to_the_theory_of_statistical\,
    @Rao_1945_Information_and_the_accuracy_attainable\, and
    @Rao_1947_Minimum_variance_and_the_estimation_of_several\.
[^Rice2007p300]: @Rice_2007_Mathematical_Statistics_and_Data_Analysis\, p. 300--2.


### Statistical hypothesis testing

-   Null hypothesis significance testing (NHST)
-   Type-1 and type-2 errors in Neyman-Pearson theory
-   Power and confidence
-   Neyman-Pearson lemma [^Neyman1933]
-   Student's $t$-test
-   ANOVA
-   Wilks [^Wilks1938] and Wald [^Wald1943]
-   $p$-values and significance [^Cowan2012]
-   Flip-flopping and Feldman-Cousins confidence intervals [^Feldman1998]
-   Asymptotics [^Cowan2011]
-   Frequentist vs bayesian decision theory [^Murphy2012p197]

[^Cowan2011]: @Cowan_2011_Asymptotic_formulae_for_likelihood_based_tests\.
[^Cowan2012]: @Sinervo_2002_Signal_significance_in_particle_physics and @Cowan_2012_Discovery_sensitivity_for_a_counting_experiment\.
[^Feldman1998]: @Feldman_1998_A_unified_approach_to_the_classical_statistical\.
[^Murphy2012p197]: @Murphy_2012_Machine_Learning_A_probabilistic_perspective\, p. 197.
[^Neyman1933]: @Neyman_1933_On_the_problem_of_the_most_efficient_tests\.
[^Wald1943]: @Wald_1943_Tests_of_statistical_hypotheses_concerning_several\.
[^Wilks1938]: @Wilks_1938_The_large_sample_distribution_of_the_likelihood\.


### Systematic uncertainties

-   Class-1, class-2, and class-3 systematic uncertanties (good, bad, ugly), Classification by Pekka Sinervo (PhyStat2003) [^Sinervo2013]
-   Not to be confused with type-1 and type-2 errors in Neyman-Pearson theory
-   Profiling and the profile likelihood

[^Sinervo2013]: @Sinervo_2003_Definition_and_treatment_of_systematic\.

![Classification of measurement uncertainties ([philosophy-in-figures.tumblr.com](http://philosophy-in-figures.tumblr.com/post/150371555016/classification-of-measurement-uncertainties)).](img/systematic-uncertainties-sinervo.png){#fig:systematic-uncertainties-sinervo}


### Exploratory data analysis

-   [Tukey, John (1915-2000)](https://en.wikipedia.org/wiki/John_Tukey)
    -   [Exploratory data analysis](https://en.wikipedia.org/wiki/Exploratory_data_analysis)
    -   *Exploratory Data Analysis* (1977) [^Tukey1977]
-   Stopping rules
    -   validation dataset
    -   statistical issues
-   "Data science"
    -   Data collection, quality, analysis, archival, and reinterpretation

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
-   Jim Berger [^Berger2003]
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
-   Kevin P. Murphy
    -    Pathologies of frequentist statistics [^Murphy2012ch6]
-   Greg Gandenberger
    -   [An introduction to likelihoodist, bayesian, and frequentist methods (1/3)](http://gandenberger.org/2014/07/21/intro-to-statistical-methods/)
    -   As Neyman and Pearson put it in their original presentation of the frequentist approach,
        "without hoping to know whether each separate hypothesis is true or false,
        we may search for rules to govern our behavior with regard to them, in the
        following which we insure that, in the long run of experience, we shall not
        too often be wrong" (1933, 291). 
    -   [An introduction to likelihoodist, bayesian, and frequentist methods (2/3)](http://gandenberger.org/2014/07/28/intro-to-statistical-methods-2/)
    -   [An introduction to likelihoodist, bayesian, and frequentist methods (2/3)](http://gandenberger.org/2014/08/26/intro-to-statistical-methods-3/)
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
[^Sznajder2018]: @Sznajder_2018_Inductive_logic_as_explication_The_evolution\.


### P-value controversy

-   File-drawer effect = look-elsewhere effect
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

-   classification vs regression
-   supervised and unsupervised learning
    -   classification = supervised; clustering = unsupervised
-   Hastie, Tibshirani, & Friedman [^Hastie2009]
-   *Deep Learning*
-   Natural language processing (NLP)
    -   Perone, C.S. (2018). [NLP word representations and the Wittgenstein philosophy of language](http://blog.christianperone.com/2018/05/nlp-word-representations-and-the-wittgenstein-philosophy-of-language/).
    -   Rationalism and empiricism in artificial intellegence:
        [Church, K.W. & Hestness, J. (2019). A survey of 25 years of evaluation.](https://www.cambridge.org/core/journals/natural-language-engineering/article/survey-of-25-years-of-evaluation/E4330FAEB9202EC490218E3220DDA291)
-   Reinforcement learning (RL)

[^Hastie2009]: @Hastie_2009_The_Elements_of_Statistical_Learning_Data_Mining\.


### Auto-science

-   AutoML and AutoScience
-   "The frontier of simulation-based inference" [^Cranmer2019]
-   "Learning new physics from a machine" [^DAgnolo2019]
-   "Big data and extreme-scale computing: Pathways to Convergence-Toward a shaping strategy for a future software and data ecosystem for scientific inquiry." [^Asch2018]
    -   Note that this description of abduction is missing that it is normative (i.e. "best-fit").

![The inference cycle for the process of scientific inquiry. The three distinct forms of inference (abduction, deduction, and induction) facilitate an all-encompassing vision, enabling HPC and HDA to converge in a rational and structured manner. HPC: high- performance computing; HDA: high-end data analysis [@Asch_2018_Big_data_and_extreme_scale_computing_Pathways]. ](img/BDEC-scientific-method.png){#fig:BDEC-scientific-method}

-   "The End of Theory: The data deluge makes the scientific method obsolete." [^Anderson2008]

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

-   Univariate Distribution Relationships [^Leemis2008]
-   *All of Statistics* [^Wasserman2003]
-   *The Foundations of Statistics* [^Savage1954]

[^Leemis2008]: @Leemis_2008_Univariate_distribution_relationships\.
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
-   [Inverse problem](https://en.wikipedia.org/wiki/Inverse_problem)
-   [Ivakhnenko, Alexey (1913-2007)](https://en.wikipedia.org/wiki/Alexey_Ivakhnenko)
-   [Jeffrey, Richard (1926-2002)](https://en.wikipedia.org/wiki/Richard_Jeffrey)
-   [Jeffreys, Harold (1891-1989)](https://en.wikipedia.org/wiki/Harold_Jeffreys)
-   [Jeffreys prior](https://en.wikipedia.org/wiki/Jeffreys_prior)
-   [Kolmogorov, Andrey (1903-1987)](https://en.wikipedia.org/wiki/Andrey_Kolmogorov)
-   [Kolmogorov complexity](https://en.wikipedia.org/wiki/Kolmogorov_complexity)
-   [Laplace, Pierre-Simon (1749-1827)](https://en.wikipedia.org/wiki/Pierre-Simon_Laplace)
-   [Likelihood principle](http://en.wikipedia.org/wiki/Likelihood_principle)
-   [Likelihoodist statistics](https://en.wikipedia.org/wiki/Likelihoodist_statistics)
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

### Others

-   [errorstatistics.com](http://errorstatistics.com/) - Deborah Mayo's blog
-   [Graunt, John (1620-1674)](http://statprob.com/encyclopedia/JohnGRAUNT.html) - statprob.com
-   [Peng, R. (2016). A Simple Explanation for the Replication Crisis in Science.](http://simplystatistics.org/2016/08/24/replication-crisis/) - simplystatistics.org
-   [Why is binary classification not a hypothesis test?](https://stats.stackexchange.com/questions/240138/why-is-binary-classification-not-a-hypothesis-test) - stackexchange.com
-   [If the likelihood principle clashes with frequentist probability then do we discard one of them?](https://stats.stackexchange.com/questions/40856/if-the-likelihood-principle-clashes-with-frequentist-probability-then-do-we-disc) - stackexchange.com

</div>

<!-- REFERENCES -->



Philosophy of physics
================================================================================

Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore
eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident,
sunt in culpa qui officia deserunt mollit anim id est laborum.


<!-- PAGETOC -->


Issues and positions
--------------------------------------------------------------------------------

### Classical physics

-   History:
    -   [Newton, Isaac (1642-1727)](http://en.wikipedia.org/wiki/Isaac_Newton)
    -   [Halley, Edmond (1656-1742)](http://en.wikipedia.org/wiki/Edmond_Halley)
    -   [Leibniz, Gottfried Wilhelm (1646-1716)](http://en.wikipedia.org/wiki/Gottfried_Leibniz)
    -   [Euler, Leonhard (1707-1783)](http://en.wikipedia.org/wiki/Euler)
    -   [Lagrange, Joseph-Louis (1736-1813)](http://en.wikipedia.org/wiki/Joseph-Louis_Lagrange)
    -   [Gauss, Carl Friedrich (1777-1855)](http://en.wikipedia.org/wiki/Gauss)
    -   [Fraunhofer, Joseph von (1787-1826)](http://en.wikipedia.org/wiki/Joseph_von_Fraunhofer)
    -   [Cauchy, Augustin-Louis (1789-1857)](http://en.wikipedia.org/wiki/Augustin-Louis_Cauchy)
    -   [Faraday, Michael (1791-1867)](http://en.wikipedia.org/wiki/Michael_Faraday)
    -   [Hamilton, William Rowan (1805-1865)](http://en.wikipedia.org/wiki/William_Rowan_Hamilton)
    -   [Maxwell, James Clerk (1831-1879)](http://en.wikipedia.org/wiki/James_Clerk_Maxwell)
    -   [Noether, Emmy (1882-1935)](https://en.wikipedia.org/wiki/Emmy_Noether)

-   Principle of least action
-   Canonical dynamics
-   Noether's theorem


### Statistical physics

-   Entropy
-   Statistical mechanics and thermodynamics
-   [Boltzmann, Ludwig (1844-1906)](http://en.wikipedia.org/wiki/Ludwig_Boltzmann)
-   The 2nd Law of Thermodynamics said simply: Things tend to happen in ways for which there are many ways to happen like that.


### Emergence

Thermodynamics, statistical mechanics, renormalization.

-   More is different[^Anderson-1972]
-   Emergence[^Lisi-2017]
-   Bain

[^Anderson-1972]: @Anderson_1972_More_is_different\.
[^Lisi-2017]: @Lisi_2017_Emergence\.


### Quantum mechanics

-   Hilbert spaces.  Wigner's theorem.  The Born rule.
-   Wave-particle duality misconceptions.  Fields are more fundamental than particles.
-   The measurement problem.  Decoherence.  The Born rule again.
-   Decoherence brings quantum logic to classical logic.
-   Bell's inequality
-   PBR theorem. Wikipedia: Either the quantum state corresponds to a physically
    real object and is not merely a statistical tool, or else all quantum states,
    including non-entangled ones, can communicate by action at a distance. 
-   Gisin's Theorem

#### Foundations of QM:

-   Hilbert spaces:

$$ \hat{H} \: |n\rangle = E_{n} \: |n\rangle $$

-   Superposition principle:

$$ |\psi\rangle = \sum_{n} a_{n} \: |n\rangle $$

-   Born rule

$$ P(n) = | \langle n | \psi \rangle |^{2} = |a_{n}|^{2} $$

-   Wigner's theorem

The generators of the representation of a transformation in a Hilbert space
are the operators representing the classical Noether charges that are
conserved under that transformation.

$$ \hat{U}(x^{\mu}) = e^{ -i \: \hat{P}_\mu \: x^\mu } $$

#### Secondary properties of QM:

-   Wave function:

$$ \langle x | n \rangle = \psi_{n}(x) $$

-   Schr&ouml;dinger Equation

$$ i \hbar \: \partial_{t} \: |\psi\rangle = \hat{H} \: |\psi\rangle $$

$$ i \hbar \: \partial_{t} \: \hat{U}(t) \: |\psi\rangle = \hat{H} \: \hat{U}(t) \: |\psi\rangle $$

-   Decoherence

$$ \mathcal{H} = \mathcal{H}_\mathrm{S} \otimes \mathcal{H}_\mathrm{E} $$

$$ |\alpha\rangle \otimes |\psi\rangle \rightarrow |\alpha\rangle \otimes |\psi; \alpha\rangle $$

#### Decoherence

-   *Decoherence and the Appearance of a Classical World in Quantum Theory* [^Giulini1996]
-   My quora answer: [What is currently the best explanation for how and why the quantum wave function collapses?](https://www.quora.com/What-is-currently-the-best-explanation-for-how-and-why-the-quantum-wave-function-collapses/answer/Ryan-Reece)

[^Giulini1996]: @Giulini_1996_Decoherence_and_the_Appearance_of_a_Classical\.


#### "Atom" (2009) BBC documentary

Jim Al-Khalili tells the story of the greatest scientific discovery ever - that everything is made of atoms.

-   [watch the 3 episodes](http://topdocumentaryfilms.com/atom-tim/)

### Quantum field theory

#### Fields

-   Field definition
-   Coleman-Mandula theorem [^Coleman1967]
-   [Fiber bundles in physics](https://ncatlab.org/nlab/show/fiber+bundles+in+physics)
    -   Fiber bundles embody two central principles of modern physics:
        1.  the principle of locality
        2.  the gauge principle.
-   Maudlin on fiber bundles

[^Coleman1967]: @Coleman_1967_All_possible_symmetries_of_the_S_matrix\.

#### Foundations

-   Peskin and Schroeder
-   David Tong
-   Weinberg
-   No "2nd quantization"
-   AQFT vs LQFT
-   Redhead [^Redhead1982]
-   Redhead [^Redhead1988]

[^Redhead1982]: @Redhead_1982_Quantum_field_theory_for_philosophers\.
[^Redhead1988]: @Redhead_1988_A_philosopher_looks_at_quantum_field_theory\.

#### Spin-statistics theorem

-   Spin-statistics theorem - Pauli

#### Scattering

-   Interaction picture
-   Correlation AKA Green's functions
-   Wick's theorem
-   Vaccuum bubble cancelation
-   Dyson series
-   LSZ reduction formula [^Lehmann1955]
-   Feynman diagrams and Feynman rules

[^Lehmann1955]: @Lehmann_1955_Zur_formulierung_quantisierter_feldtheorien\.

#### Renormalization

-   Wilson
-   Huggett and Weingard [^Huggett1995]
-   Butterfield [^Butterfield2014]
-   Butterfield [^Butterfield2015]

[^Huggett1995]: @Huggett_1995_The_renormalisation_group_and_effective_field\.
[^Butterfield2014]: @Butterfield_2014_Reduction_emergence_and_renormalization\.
[^Butterfield2015]: @Butterfield_2015_Renormalization_for_philosophers\.

#### Effective field theory

-   Huggett and Weingard, again [^Huggett1995]
-   Weinberg [^Weinberg1997]
-   Bain [^Bain2013]

[^Bain2013]: @Bain_2013_Effective_field_theories and
    @Bain_2013_Emergence_in_effective_field_theories\.
[^Weinberg1997]: @Weinberg_1996_What_is_quantum_field_theory_and_what_did_we\.

#### Haag's theorem

-   Haag's theorem [^Haag1955]
-   Malament [^Malament1996]
-   Bain [^Bain2000]
-   Earman and Fraser's analysis [^Earman2006]
-   Klaczynski's analysis [^Klaczynski2016]

[^Bain2000]: @Bain_2000_Against_particlefield_duality_Asymptotic\.
[^Earman2006]: @Earman_2006_Haags_theorem_and_its_implications_for\.
[^Haag1955]: @Haag_1955_On_quantum_field_theories\.
[^Klaczynski2016]: @Klaczynski_2016_Haags_theorem_in_renormalised_quantum_field\.
[^Malament1996]: @Malament_1996_In_defence_of_dogma_Why_there_cannot_be\.

#### Supersymmetry

-   Haag-&#321;opusza&#324;ski-Sohnius theorem [^Haag1975]

[^Haag1975]: @Haag_1975_All_possible_generators_of_supersymmetries_of\.


### Interpretations of quantum mechanics

-   Copenhagen
-   de Broglie-Bohm
-   Everett
-   others

![Interpretations of quantum mechanics ([philosophy-in-figures.tumblr.com](http://philosophy-in-figures.tumblr.com/post/145247040756/interpretations-of-quantum-mechanics-v2)).](img/interpretations-of-quantum-mechanics-v2.png){#fig:interpretations-of-quantum-mechanics-v2}


### The standard model of particle physics

-   GWS electroweak theory: SU(2) $\times$ U(1)
-   QCD: SU(3)
-   Nima Arkani-Hamed doing particle physics *a priori*: ["Why is there a Macroscopic Universe?"](https://www.youtube.com/watch?v=F2Fxt_yCrcc)


### Beyond the standard model

-   Neutrino masses and mixings
-   Running of the couplings
-   Grand unification
-   Supersymmetry
-   Strong $CP$ problem
-   Quantum gravity


### Cosmology

-   Big bang
-   Dark matter
-   [Bullet Cluster](https://en.wikipedia.org/wiki/Bullet_Cluster)
-   "A direct empirical proof of the existence of dark matter" [astro-ph/0608407](http://arxiv.org/abs/astro-ph/0608407)
-   Inflation
-   $\Lambda$+CMD Cosmological Standard Model


### Bracketing human experience

-   Reductionism
-   [Sean Carroll's acceptance speech](https://www.youtube.com/watch?v=40eiycH077A#t=402)
    for the FFRF's the emperor has no clothes award.
-   ["Quantum Field Theory and the Limits of Knowledge"](http://www.preposterousuniverse.com/blog/2015/04/21/quantum-field-theory-and-the-limits-of-knowledge/) - Sean Carroll
-   ["Poetic Naturalism"](https://www.youtube.com/watch?v=xv0mKsO2goA) - Sean Carroll


### Fine-tuning

-   Fine-tuning
-   Anthropic principle
-   Relationship to evolution
-   [Richard Dawkins and Steven Weinberg Discuss Science and Religion](https://www.youtube.com/watch?v=EGL8SesIo6Y)


My thoughts
--------------------------------------------------------------------------------

Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore
eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident,
sunt in culpa qui officia deserunt mollit anim id est laborum.

-   gravity: from aether to not to fabric
-   Sean Carroll QM: what there is, is more than we can see.


Annotated bibliography
--------------------------------------------------------------------------------

### Einstein, A., Podolsky, B. & Rosen, N. (1935). Can quantum-mechanical description of physical reality be considered complete?

-   @Einstein_1935_Can_quantum_mechanical_description_of_physical

#### My thoughts

-   TODO.


--------------------------------------------------------------------------------

### Anderson, P. (1972). More is different.

-   @Anderson_1972_More_is_different

#### My thoughts

-   TODO.


--------------------------------------------------------------------------------

### Redhead, M. (1988). A philosopher looks at quantum field theory.


-   @Redhead_1988_A_philosopher_looks_at_quantum_field_theory

#### My thoughts

-   TODO.


--------------------------------------------------------------------------------

### Giulini, D., E. Joos, C. Kiefer, J. Kupsch, I.O. Stamatescu, & H. Zeh (1996). *Decoherence and the Appearance of a Classical World in Quantum Theory*.

-   @Giulini_1996_Decoherence_and_the_Appearance_of_a_Classical

#### My thoughts

-   TODO.


--------------------------------------------------------------------------------

### Pusey, M.F., Barrett, J., & Rudolph, T. (2012). On the reality of the quantum state.

-   @Pusey_2012_On_the_reality_of_the_quantum_state
-   [arxiv:1111.3328](http://arxiv.org/abs/1111.3328)

#### My thoughts

-   TODO.


--------------------------------------------------------------------------------

### More articles to do

-   [Aaronson, S. (2015). "Bell inequality violation finally done right."](http://www.scottaaronson.com/blog/?p=2464)
-   [Hensen, B. et al. (2015). "Experimental loophole-free violation of a Bell inequality using entangled electron spins separated by 1.3 km."](http://arxiv.org/abs/1508.05949)
-   @Schwichtenberg_2015_Physics_from_Symmetry


Links and encyclopedia articles
--------------------------------------------------------------------------------

### SEP

-   [Being and Becoming in Modern Physics](http://plato.stanford.edu/entries/spacetime-bebecome/)
-   [Bell's Theorem](http://plato.stanford.edu/entries/bell-theorem/)
-   [Bohmian Mechanics](http://plato.stanford.edu/entries/qm-bohm/)
-   [Chaos](http://plato.stanford.edu/entries/chaos/)
-   [Collapse Theories](http://plato.stanford.edu/entries/qm-collapse/)
-   [Computer Simulations in Science](http://plato.stanford.edu/entries/simulations-science/)
-   [Copenhagen Interpretation of Quantum Mechanics](http://plato.stanford.edu/entries/qm-copenhagen/)
-   [Decoherence](http://plato.stanford.edu/entries/qm-decoherence/)
-   [Emergent Properties](http://plato.stanford.edu/entries/properties-emergent/)
-   [Everett's Relative-State Formulation of Quantum Mechanics](http://plato.stanford.edu/entries/qm-everett/)
-   [General relativity, Early philosophical interpretations of](http://plato.stanford.edu/entries/genrel-early/)
-   [Holism and Nonseparability in Physics](http://plato.stanford.edu/entries/physics-holism/)
-   [Identity and Individuality in Quantum Theory](http://plato.stanford.edu/entries/qt-idind/)
-   [Identity of Indiscernibles](http://plato.stanford.edu/entries/identity-indiscernible/)
-   [Kochen-Specker Theorem](http://plato.stanford.edu/entries/kochen-specker/)
-   [Many-Worlds Interpretation of Quantum Mechanics](http://plato.stanford.edu/entries/qm-manyworlds/)
-   [Modal Interpretations of Quantum Mechanics](http://plato.stanford.edu/entries/qm-modal/)
-   [Measurement in Quantum Theory](http://plato.stanford.edu/entries/qt-measurement/)
-   [Philosophical Issues in Quantum Theory](http://plato.stanford.edu/entries/qt-issues/)
-   [Poincar&eacute;, Henri (1854-1912)](https://plato.stanford.edu/entries/poincare/)
-   [Quantum Entanglement and Information](http://plato.stanford.edu/entries/qt-entangle/)
-   [Quantum Field Theory](http://plato.stanford.edu/entries/quantum-field-theory/)
-   [Quantum Field Theory, History of](http://plato.stanford.edu/entries/quantum-field-theory/qft-history.html)
-   [Quantum Gravity](https://plato.stanford.edu/entries/quantum-gravity/)
-   [Quantum Logic and Probability Theory](http://plato.stanford.edu/entries/qt-quantlog/)
-   [Quantum Mechanics](http://plato.stanford.edu/entries/qm/)
-   [Quantum Theory: von Neumann vs Dirac](https://plato.stanford.edu/entries/qt-nvd/)
-   [Relational Quantum Mechanics](http://plato.stanford.edu/entries/qm-relational/)
-   [Statistical mechanics, Philosophy of](http://plato.stanford.edu/entries/statphys-statmech/)
-   [Supertasks](http://plato.stanford.edu/entries/spacetime-supertasks/)
-   [Symmetry and Symmetry Breaking](http://plato.stanford.edu/entries/symmetry-breaking/)
-   [Time](http://plato.stanford.edu/entries/time/)
-   [Weyl, Hermann (1885-1955)](https://plato.stanford.edu/entries/weyl/)

### IEP

-   [Einstein-Podolsky-Rosen Argument and the Bell Inequalities](http://www.iep.utm.edu/epr/)
-   [Emergence](http://www.iep.utm.edu/emergenc/)
-   [Interpretations of Quantum Mechanics](http://www.iep.utm.edu/int-qm/)
-   [Laws of nature](http://www.iep.utm.edu/lawofnat/)
-   [What Else Science Requires of Time](http://www.iep.utm.edu/requires/)

### Scholarpedia

-   [Algebraic renormalization](http://www.scholarpedia.org/article/Algebraic_renormalization)
-   [ATLAS experiment](http://www.scholarpedia.org/article/The_ATLAS_experiment)
-   [Bjorken scaling](http://www.scholarpedia.org/article/Bjorken_scaling)
-   [Coleman-Mandula theorem](http://www.scholarpedia.org/article/Coleman-Mandula_theorem)
-   [Coleman-Weinberg mechanism](http://www.scholarpedia.org/article/Coleman-Weinberg_mechanism)
-   [CP violation in electroweak interactions](http://www.scholarpedia.org/article/CP_violation_in_electroweak_interactions)
-   [Critical Phenomena: field theoretical approach](http://www.scholarpedia.org/article/Critical_Phenomena:_field_theoretical_approach)
-   [Daya Bay Experiment](http://www.scholarpedia.org/article/The_Daya_Bay_Experiment)
-   [Englert-Brout-Higgs-Guralnik-Hagen-Kibble mechanism](http://www.scholarpedia.org/article/Englert-Brout-Higgs-Guralnik-Hagen-Kibble_mechanism)
-   [Englert-Brout-Higgs-Guralnik-Hagen-Kibble mechanism (history)](http://www.scholarpedia.org/article/Englert-Brout-Higgs-Guralnik-Hagen-Kibble_mechanism_(history))
-   [Faddeev-Popov ghosts](http://www.scholarpedia.org/article/Faddeev-Popov_ghosts)
-   [Gauge invariance](http://www.scholarpedia.org/article/Gauge_invariance)
-   [Gauge theories](http://www.scholarpedia.org/article/Gauge_theories)
-   [Glashow-Iliopoulos-Maiani mechanism](http://www.scholarpedia.org/article/Glashow-Iliopoulos-Maiani_mechanism)
-   [Grand unification](http://www.scholarpedia.org/article/Grand_unification)
-   [Lagrangian formalism for fields](http://www.scholarpedia.org/article/Lagrangian_formalism_for_fields)
-   [Lattice gauge theories](http://www.scholarpedia.org/article/Lattice_gauge_theories)
-   [Lattice quantum field theory](http://www.scholarpedia.org/article/Lattice_quantum_field_theory)
-   [Leptogenesis](http://www.scholarpedia.org/article/Leptogenesis)
-   [Local operator](http://www.scholarpedia.org/article/Local_operator)
-   [MS-bar definition of parton distribution functions](http://www.scholarpedia.org/article/MS-bar_definition_of_parton_distribution_functions)
-   [Multiloop Feynman integrals](http://www.scholarpedia.org/article/Multiloop_Feynman_integrals)
-   [Operator product expansion](http://www.scholarpedia.org/article/Operator_product_expansion)
-   [Parton shower Monte Carlo event generators](http://www.scholarpedia.org/article/Parton_shower_Monte_Carlo_event_generators)
-   [Path integral](http://www.scholarpedia.org/article/Path_integral)
-   [Path integral: mathematical aspects](http://www.scholarpedia.org/article/Path_integral:_mathematical_aspects)
-   [Principle of least action](http://www.scholarpedia.org/article/Principle_of_least_action)
-   [QCD evolution equations for parton densities](http://www.scholarpedia.org/article/QCD_evolution_equations_for_parton_densities)
-   [Second quantization](http://www.scholarpedia.org/article/Second_quantization)
-   [Symmetry breaking in classical systems](http://www.scholarpedia.org/article/Symmetry_breaking_in_classical_systems)
-   [Wightman quantum field_theory](http://www.scholarpedia.org/article/Wightman_quantum_field_theory)

### Wikipedia

-   [AdS/CFT correspondence](http://en.wikipedia.org/wiki/AdS/CFT_correspondence)
-   [Aharonov-Bohm effect](https://en.wikipedia.org/wiki/Aharonov%E2%80%93Bohm_effect)
-   [Amp&egrave;re, Andr&eacute;-Marie (1775-1836)](https://en.wikipedia.org/wiki/Andr%C3%A9-Marie_Amp%C3%A8re)
-   [Background independence](http://en.wikipedia.org/wiki/Background_independence)
-   [Bargmann, Valentine (1908-1989)](https://en.wikipedia.org/wiki/Valentine_Bargmann)
-   [Bargmann-Wigner equations](https://en.wikipedia.org/wiki/Bargmann%E2%80%93Wigner_equations)
-   [Bell's theorem](http://en.wikipedia.org/wiki/Bell%27s_theorem)
-   [Bekenstein bound](https://en.wikipedia.org/wiki/Bekenstein_bound)
-   [Black hole information paradox](http://en.wikipedia.org/wiki/Black_hole_information_paradox)
-   [Bohm, David (1917-1992)](https://en.wikipedia.org/wiki/David_Bohm)
-   [Bohr, Niels (1885-1962)](https://en.wikipedia.org/wiki/Niels_Bohr)
-   [Bohr-Einstein debates](http://en.wikipedia.org/wiki/Bohr%E2%80%93Einstein_debates)
-   [Born rule](http://en.wikipedia.org/wiki/Born_rule)
-   [Bullet Cluster](https://en.wikipedia.org/wiki/Bullet_Cluster)
-   [C*-algebra](https://en.wikipedia.org/wiki/C*-algebra)
-   [Casimir effect](https://en.wikipedia.org/wiki/Casimir_effect)
-   [Cauchy, Augustin-Louis (1789-1857)](http://en.wikipedia.org/wiki/Augustin-Louis_Cauchy)
-   [Causal Processes](http://plato.stanford.edu/entries/causation-process/)
-   [Causal perturbation theory](https://en.wikipedia.org/wiki/Causal_perturbation_theory)
-   [Central limit theorem](http://en.wikipedia.org/wiki/Central_limit_theorem)
-   [Causality](http://en.wikipedia.org/wiki/Causality_(physics))
-   [CHSH inequality](http://en.wikipedia.org/wiki/CHSH_inequality)
-   [Chronology of the universe](http://en.wikipedia.org/wiki/Chronology_of_the_universe)
-   [Church-Turing-Deutsch principle](https://en.wikipedia.org/wiki/Church%E2%80%93Turing%E2%80%93Deutsch_principle)
-   [Church-Turing thesis](https://en.wikipedia.org/wiki/Church%E2%80%93Turing_thesis)
-   [Complexity](http://en.wikipedia.org/wiki/Complexity)
-   [Constructor theory](http://en.wikipedia.org/wiki/Constructor_theory)
-   [CP violation](https://en.wikipedia.org/wiki/CP_violation)
-   [de Broglie, Louis (1892-1987)](https://en.wikipedia.org/wiki/Louis_de_Broglie)
-   [De Broglie-Bohm theory](http://en.wikipedia.org/wiki/De_Broglie%E2%80%93Bohm_theory)
-   [Determinism](http://en.wikipedia.org/wiki/Determinism)
-   [Digital philosophy](http://en.wikipedia.org/wiki/Digital_philosophy)
-   [Digital physics](http://en.wikipedia.org/wiki/Digital_physics)
-   [Effective field theory](http://en.wikipedia.org/wiki/Effective_field_theory)
-   [Einselection](https://en.wikipedia.org/wiki/Einselection)
-   [Equivalence principle](http://en.wikipedia.org/wiki/Equivalence_principle)
-   [Emergence](http://en.wikipedia.org/wiki/Emergence)
-   [Entropic gravity](http://en.wikipedia.org/wiki/Entropic_gravity)
-   [Entropy](http://en.wikipedia.org/wiki/Entropy)
-   [Entropy, Introduction to](http://en.wikipedia.org/wiki/Introduction_to_entropy)
-   [Equipartition theorem](https://en.wikipedia.org/wiki/Equipartition_theorem)
-   [Erlangen program](https://en.wikipedia.org/wiki/Erlangen_program)
-   [Eternalism (philosophy of time)](https://en.wikipedia.org/wiki/Eternalism_(philosophy_of_time))
-   [Franklin, Benjamin (1706-1790)](https://en.wikipedia.org/wiki/Benjamin_Franklin)
-   [Fraunhofer, Joseph von (1787-1826)](http://en.wikipedia.org/wiki/Joseph_von_Fraunhofer)
-   [Four-dimensionalism](https://en.wikipedia.org/wiki/Four-dimensionalism)
-   [Field](http://en.wikipedia.org/wiki/Field_(physics))
-   [Firewall](http://en.wikipedia.org/wiki/Firewall_%28physics%29)
-   [Gauss, Carl Friedrich (1777-1855)](http://en.wikipedia.org/wiki/Gauss)
-   [Gelfand-Naimark theorem](https://en.wikipedia.org/wiki/Gelfand%E2%80%93Naimark_theorem)
-   [Gelfand-Naimark-Segal construction](https://en.wikipedia.org/wiki/Gelfand%E2%80%93Naimark%E2%80%93Segal_construction)
-   [Ghirardi-Rimini-Weber theory](https://en.wikipedia.org/wiki/Ghirardi%E2%80%93Rimini%E2%80%93Weber_theory)
-   [Gibbs, Josiah Willard (1839-1903)](https://en.wikipedia.org/wiki/Josiah_Willard_Gibbs)
-   [Grand Unified Theory](http://en.wikipedia.org/wiki/Grand_Unified_Theory)
-   [Haag, Rudolf (1922-2016)](https://en.wikipedia.org/wiki/Rudolf_Haag)
-   [Haag-&#321;opusza&#324;ski-Sohnius theorem](https://en.wikipedia.org/wiki/Haag%E2%80%93%C5%81opusza%C5%84ski%E2%80%93Sohnius_theorem)
-   [Haag's theorem](https://en.wikipedia.org/wiki/Haag%27s_theorem)
-   [Hidden variable theory](https://en.wikipedia.org/wiki/Hidden_variable_theory)
-   [Hierarchy problem](https://en.wikipedia.org/wiki/Hierarchy_problem)
-   [Hilbert, David (1862-1943)](https://en.wikipedia.org/wiki/David_Hilbert)
-   [Hilbert space](http://en.wikipedia.org/wiki/Hilbert_space)
-   [Holographic principle](http://en.wikipedia.org/wiki/Holographic_principle)
-   [Holomovement](https://en.wikipedia.org/wiki/Holomovement)
-   [Kaluza-Klein theory](https://en.wikipedia.org/wiki/Kaluza%E2%80%93Klein_theory)
-   [Kochen-Specker Theorem](https://en.wikipedia.org/wiki/Kochen%E2%80%93Specker_theorem)
-   [Lambda-CDM model](https://en.wikipedia.org/wiki/Lambda-CDM_model)
-   [Landau pole](https://en.wikipedia.org/wiki/Landau_pole)
-   [Little hierarchy problem](https://en.wikipedia.org/wiki/Little_hierarchy_problem)
-   [Locality, Principle of](https://en.wikipedia.org/wiki/Principle_of_locality)
-   [Local hidden variable theory](https://en.wikipedia.org/wiki/Local_hidden_variable_theory)
-   [Local quantum field theory](https://en.wikipedia.org/wiki/Local_quantum_field_theory)
-   [Loopholes in Bell test experiments](https://en.wikipedia.org/wiki/Loopholes_in_Bell_test_experiments)
-   [Measurement in quantum mechanics](https://en.wikipedia.org/wiki/Measurement_in_quantum_mechanics)
-   [Measurement problem](http://en.wikipedia.org/wiki/Measurement_problem)
-   [M-theory](http://en.wikipedia.org/wiki/M-theory)
-   [M-theory, Introduction to](http://en.wikipedia.org/wiki/Introduction_to_M-theory)
-   [Mu problem](https://en.wikipedia.org/wiki/Mu_problem)
-   [No-cloning theorem](http://en.wikipedia.org/wiki/No-cloning_theorem)
-   [Noether, Emmy (1882-1935)](https://en.wikipedia.org/wiki/Emmy_Noether)
-   [Noether's theorem](http://en.wikipedia.org/wiki/Noether%27s_theorem)
-   [Objective collapse theory](https://en.wikipedia.org/wiki/Objective_collapse_theory)
-   [Particle physics](http://en.wikipedia.org/wiki/Particle_physics)
-   [Particle physics and representation theory](http://en.wikipedia.org/wiki/Particle_physics_and_representation_theory)
-   [PBR theorem](http://en.wikipedia.org/wiki/PBR_theorem)
-   [Physical cosmology](http://en.wikipedia.org/wiki/Physical_cosmology)
-   [Physicalism](http://en.wikipedia.org/wiki/Physicalism)
-   [Physics, Philosophy of](http://en.wikipedia.org/wiki/Philosophy_of_physics)
-   [Poincar&eacute;, Henri (1854-1912)](https://en.wikipedia.org/wiki/Henri_Poincar%C3%A9)
-   [Poincar&eacute; group](https://en.wikipedia.org/wiki/Poincar%C3%A9_group)
-   [Quantization](https://en.wikipedia.org/wiki/Quantization_(physics))
-   [Quantization, Canonical](https://en.wikipedia.org/wiki/Canonical_quantization)
-   [Quantization, Geometric](https://en.wikipedia.org/wiki/Geometric_quantization)
-   [Quantum decoherence](http://en.wikipedia.org/wiki/Quantum_decoherence)
-   [Quantum entanglement](http://en.wikipedia.org/wiki/Quantum_entanglement)
-   [Quantum field theory](http://en.wikipedia.org/wiki/Quantum_field_theory)
-   [Quantum gravity](http://en.wikipedia.org/wiki/Quantum_gravity)
-   [Quantum mechanics](http://en.wikipedia.org/wiki/Quantum_mechanics)
-   [Quantum mechanics, Mathematical formulation of](http://en.wikipedia.org/wiki/Mathematical_formulation_of_quantum_mechanics)
-   [Quantum triviality](https://en.wikipedia.org/wiki/Quantum_triviality)
-   [Reeh-Schlieder theorem](https://en.wikipedia.org/wiki/Reeh%E2%80%93Schlieder_theorem)
-   [Regularization](https://en.wikipedia.org/wiki/Regularization_(physics))
-   [Relational quantum mechanics](https://en.wikipedia.org/wiki/Relational_quantum_mechanics)
-   [Relativity](http://en.wikipedia.org/wiki/Theory_of_relativity)
-   [Relativity, General](http://en.wikipedia.org/wiki/General_relativity)
-   [Relativity, Introduction to General](http://en.wikipedia.org/wiki/Introduction_to_general_relativity)
-   [Renormalization](http://en.wikipedia.org/wiki/Renormalization)
-   [Renormalization group](http://en.wikipedia.org/wiki/Renormalization_group)
-   [Representation theory](http://en.wikipedia.org/wiki/Representation_theory)
-   [Rietdijk-Putnam argument](https://en.wikipedia.org/wiki/Rietdijk%E2%80%93Putnam_argument)
-   [Standard Model](http://en.wikipedia.org/wiki/Standard_Model)
-   [Standard Model (mathematical formulation)](http://en.wikipedia.org/wiki/Standard_Model_(mathematical_formulation))
-   [Statistical mechanics](http://en.wikipedia.org/wiki/Statistical_mechanics)
-   [Stone-von Neumann theorem](https://en.wikipedia.org/wiki/Stone%E2%80%93von_Neumann_theorem)
-   [String theory](http://en.wikipedia.org/wiki/String_theory)
-   [Strong CP problem](https://en.wikipedia.org/wiki/Strong_CP_problem)
-   [Supertask](https://en.wikipedia.org/wiki/Supertask)
-   [Supergravity](https://en.wikipedia.org/wiki/Supergravity)
-   [Supersymmetry](http://en.wikipedia.org/wiki/Supersymmetry)
-   [Thermal and statistical physics, Philosophy of](http://en.wikipedia.org/wiki/Philosophy_of_thermal_and_statistical_physics)
-   [Timeline of cosmological theories](http://en.wikipedia.org/wiki/Timeline_of_cosmological_theories)
-   [Timeline of particle physics](http://en.wikipedia.org/wiki/Timeline_of_particle_physics)
-   [Timeline of particle physics technology](http://en.wikipedia.org/wiki/Timeline_of_particle_physics_technology)
-   [Timeline of quantum mechanics](http://en.wikipedia.org/wiki/Timeline_of_quantum_mechanics)
-   [Ultraviolet catastrophe](https://en.wikipedia.org/wiki/Ultraviolet_catastrophe)
-   [Universality](https://en.wikipedia.org/wiki/Universality_(dynamical_systems))
-   [Unruh effect](https://en.wikipedia.org/wiki/Unruh_effect)
-   [Unsolved problems in physics, List of](http://en.wikipedia.org/wiki/List_of_unsolved_problems_in_physics)
-   [Volta, Alessandro (1745-1827)](https://en.wikipedia.org/wiki/Alessandro_Volta)
-   [von Neumann, John (1903-1957)](https://en.wikipedia.org/wiki/John_von_Neumann)
-   [Wave function](http://en.wikipedia.org/wiki/Wave_function)
-   [Wave function collapse](http://en.wikipedia.org/wiki/Wave_function_collapse)
-   [Wave-particle duality](http://en.wikipedia.org/wiki/Wave%E2%80%93particle_duality)
-   [Weinberg-Witten theorem](https://en.wikipedia.org/wiki/Weinberg%E2%80%93Witten_theorem)
-   [Weyl, Hermann (1885-1955)](https://en.wikipedia.org/wiki/Hermann_Weyl)
-   [Wigner, Eugene (1902-1995)](https://en.wikipedia.org/wiki/Eugene_Wigner)
-   [Wigner's theorem](http://en.wikipedia.org/wiki/Wigner%27s_theorem)
-   [Wigner-Eckart theorem](http://en.wikipedia.org/wiki/Wigner%E2%80%93Eckart_theorem)

### Others

-   [bohmianmechanics.org](http://www.bohmianmechanics.org/)
-   [Can the quantum state be interpreted statistically?](http://mattleifer.info/2011/11/20/can-the-quantum-state-be-interpreted-statistically/) - Matt Leifer
-   [Can we trivialize the equivalence between canonical quantization of fields and second quantization of particles?](http://physics.stackexchange.com/questions/86920/can-we-trivialize-the-equivalence-between-canonical-quantization-of-fields-and/87194) - physics.stackexchange
-   [Could one argue that $h$ (Planck constant) and $\hbar/2$ (Dirac constant) are in fact independant constants?](http://physics.stackexchange.com/questions/51631/could-one-argue-that-h-planck-constant-and-hbar-2-dirac-constant-are-in-f/51636) - physics.stackexchange
-   [Effective field theory](http://ncatlab.org/nlab/show/effective+quantum+field+theory) - nlab
-   [Emergence](http://rationalwiki.org/wiki/Emergence) - RationalWiki.org
-   [Fiber bundles in physics](https://ncatlab.org/nlab/show/fiber+bundles+in+physics) - nlab
-   [Intuitively, why are bundles so important in Physics?](https://physics.stackexchange.com/questions/77368/intuitively-why-are-bundles-so-important-in-physics/77416#77416) - nlab
-   [Is a third quantization possible?](http://physics.stackexchange.com/questions/625/is-a-third-quantization-possible/823) - physics.stackexchange
-   [Kochen-Specker theorem](https://ncatlab.org/nlab/show/Kochen-Specker+theorem)
-   [lqp2.org](http://www.lqp2.org/) - serving several papers on AQFT
-   [Philosophy of general relativity](http://faculty.poly.edu/~jbain/philrel/) - Jonathan Bain
-   [Philosophy of quantum mechanics](http://ls.poly.edu/~jbain/philqm/) - Jonathan Bain
-   [Quantization](https://ncatlab.org/nlab/show/quantization) - nlab
-   [What is a gauge?](https://terrytao.wordpress.com/2008/09/27/what-is-a-gauge/) - Terence Tao
-   [Struggles With the Continuum](https://www.physicsforums.com/insights/struggles-continuum-part-1/) - John Baez

### Videos

-   [Carroll, S. (2013). Particles, Fields and The Future of Physics.](https://www.youtube.com/watch?v=gEKSpZPByD0)
-   [Tong, D. (2017). Quantum Fields: The Real Building Blocks of the Universe.](https://www.youtube.com/watch?v=zNVQfWC_evg)


<!-- REFERENCES -->



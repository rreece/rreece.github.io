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
    -   [Laplace, Pierre-Simon (1749-1827)](https://en.wikipedia.org/wiki/Pierre-Simon_Laplace)
    -   [Gauss, Carl Friedrich (1777-1855)](http://en.wikipedia.org/wiki/Gauss)
    -   [Fraunhofer, Joseph von (1787-1826)](http://en.wikipedia.org/wiki/Joseph_von_Fraunhofer)
    -   [Cauchy, Augustin-Louis (1789-1857)](http://en.wikipedia.org/wiki/Augustin-Louis_Cauchy)
    -   [Faraday, Michael (1791-1867)](http://en.wikipedia.org/wiki/Michael_Faraday)
        -   Invented the concept of a *field*
    -   [Hamilton, William Rowan (1805-1865)](http://en.wikipedia.org/wiki/William_Rowan_Hamilton)
    -   [Maxwell, James Clerk (1831-1879)](http://en.wikipedia.org/wiki/James_Clerk_Maxwell)
    -   [Noether, Emmy (1882-1935)](https://en.wikipedia.org/wiki/Emmy_Noether)
-   Classical mechanics
-   Electrodynamics
-   *The Feynman Lectures on Physics* [^Feynman1963]

[^Feynman1963]: @Feynman_1963_The_Feynman_Lectures_on_Physics_Volume_I\.


### Statistical physics

-   Entropy
-   Statistical mechanics and thermodynamics
-   [Boltzmann, Ludwig (1844-1906)](http://en.wikipedia.org/wiki/Ludwig_Boltzmann)
-   The 2nd Law of Thermodynamics said simply: Things tend to happen in ways for which there are many ways to happen like that.
-   See [Emergence](#emergence)


### Symmetry-first physics

-   Principle of least action
-   Canonical dynamics
-   Curie's principle
-   Noether's theorem
-   group theory [^tHooft2007]
-   *Physics from Symmetry* [^Schwichtenberg2015]
-   Wigner-stone theorems as cornerstone's of QM (Ovrut)

[^Schwichtenberg2015]: @Schwichtenberg_2015_Physics_from_Symmetry\.
[^tHooft2007]: @tHooft_2007_Lie_Groups_in_Physics\.


### Quantum mechanics

#### Introduction

-   Traditionally focus on NRQM [^Ney2013]
-   Hilbert spaces.  Wigner's theorem.  The Born rule.
-   Wave-particle duality misconceptions.  Fields are more fundamental than particles.
-   The measurement problem.  Decoherence.  The Born rule again.
-   Decoherence brings quantum logic to classical logic.

[^Ney2013]: @Ney_2013_The_Wave_Function_Essays_on_the_metaphysics\.


#### History

-   Planck
-   Einstein
-   Bohr
-   Heisenberg
-   Schr&ouml;dinger
-   Born


#### Foundations of QM

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

#### Secondary properties of QM

-   Wave function:

$$ \langle x | n \rangle = \psi_{n}(x) $$

-   Schr&ouml;dinger equation:

$$ \partial_{t} \: |\psi\rangle = -i \hbar \: \hat{H} \: |\psi\rangle $$

-   Heisenberg picture:

$$ i \hbar \: \partial_{t} \: \hat{U}(t) \: |\psi\rangle = \hat{H} \: \hat{U}(t) \: |\psi\rangle $$

-   Decoherence

$$ \mathcal{H} = \mathcal{H}_\mathrm{S} \otimes \mathcal{H}_\mathrm{E} $$

$$ |\alpha\rangle \otimes |\psi\rangle \rightarrow |\alpha\rangle \otimes |\psi; \alpha\rangle $$

#### Decoherence

-   *Decoherence and the Appearance of a Classical World in Quantum Theory* [^Giulini1996]
-   Drossel [^Drossel2015]
-   My quora answer: [What is currently the best explanation for how and why the quantum wave function collapses?](https://www.quora.com/What-is-currently-the-best-explanation-for-how-and-why-the-quantum-wave-function-collapses/answer/Ryan-Reece)

[^Drossel2015]: @Drossel_2015_On_the_relation_between_the_second_law\, p. 51--2.
[^Giulini1996]: @Giulini_1996_Decoherence_and_the_Appearance_of_a_Classical\.


### Quantum field theory

#### Fields

-   Field definition
-   Coleman-Mandula theorem [^Coleman1967]
-   [Wigner's classification](https://en.wikipedia.org/wiki/Wigner%27s_classification)
-   CPT theorem
-   Feynman's Nobel Lecture on QED [^Feynman1965]

[^Coleman1967]: @Coleman_1967_All_possible_symmetries_of_the_S_matrix\.
[^Feynman1965]: @Feynman_1965_The_Development_of_the_Space_Time_View_of_Quantum\.


#### Foundations

-   Peskin and Schroeder
-   David Tong
-   Weinberg
-   No "2nd quantization"
-   Redhead [^Redhead1982]
-   Redhead [^Redhead1988]
-   AQFT vs LQFT
-   *Local Quantum Physics* [^Haag1992]

>   Rudolf [Haag] is not satisfied by a notion of local observables relying
>   plainly on space and time. Instead he wishes to base the theory on concepts
>   related to individual processes. This attitude seems to me to move towards a
>   basic "algebra of procedures", pointing towards a theory of (non-commutative)
>   space-time. I know that, coming from a very different angle, Alain Connes
>   also believes the ultimate algebra of basic physics to be a discrete algebra
>   of elements standing for experimental procedures---following the idea 
>   that the spatial notions man acquires in his cradle are less basic than
>   his procedures at [particle] accelerators. [^Kastler2003p6]

[^Haag1992]: @Haag_1992_Local_Quantum_Physics_Fields_Particles_Algebras\.
[^Kastler2003p6]: @Kastler_2003_Rudolf_Haag_Eighty_Years\, p. 6.
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
-   Haag-Ruelle scattering theory
-   Feynman diagrams and Feynman rules
-   Martin [^Martin2018]

[^Lehmann1955]: @Lehmann_1955_Zur_formulierung_quantisierter_feldtheorien\.
[^Martin2018]: @Martin_2018_Phenomenology_of_particle_physics\.


#### Renormalization

-   Dyson [^Dyson1949]
-   Wilson
-   Huggett and Weingard [^Huggett1995]
-   Goldenfeld [^Goldenfeld1992]
-   Butterfield [^Butterfield2014]
-   Butterfield [^Butterfield2015]
 
[^Dyson1949]: @Dyson_1949_The_S_matrix_in_quantum_electrodynamics\.
[^Goldenfeld1992]: @Goldenfeld_1992_Lectures_on_Phase_Transitions\.
[^Huggett1995]: @Huggett_1995_The_renormalisation_group_and_effective_field\.
[^Butterfield2014]: @Butterfield_2014_Reduction_emergence_and_renormalization\.
[^Butterfield2015]: @Butterfield_2015_Renormalization_for_philosophers\.


#### Effective field theory

-   Huggett and Weingard, again [^Huggett1995]
-   Weinberg [^Weinberg1997]
-   Bain [^Bain2013]
-   Preskill, J. (2013). [We are all Wilsonians now](https://quantumfrontiers.com/2013/06/18/we-are-all-wilsonians-now/).

[^Bain2013]: @Bain_2013_Effective_field_theories and
    @Bain_2013_Emergence_in_effective_field_theories\.
[^Weinberg1997]: @Weinberg_1996_What_is_quantum_field_theory_and_what_did_we\.


#### Haag's theorem

-   Haag's theorem [^Haag1955]
    -   The interaction picture does not exist in interacting relativistic QFT.
    -   States in the free theory are unitarily inequivalent to those in interacting relativistic QFT.
-   Discussion:
    -   Malament [^Malament1996]
    -   Teller [^Teller1997p115]
    -   Earman and Fraser's analysis [^Earman2006]
    -   Klaczynski's analysis [^Klaczynski2016]
-   Resolution:
    -   Bain [^Bain2000]
    -   Duncan [^Duncan2012]
    -   Wallace
    -   QFT requires an ultraviolet regulator (a cutoff, a lattice),
        and Haag's theorem does not apply when the regulator is in place.

<center>
<blockquote class="twitter-tweet">
<p lang="en" dir="ltr">I have really fallen into a rabbit hole over Haag&#39;s theorem. 
<a href="https://twitter.com/hashtag/HaagsTheorem?src=hash&amp;ref_src=twsrc%5Etfw">#HaagsTheorem</a> 
<a href="https://twitter.com/hashtag/philsci?src=hash&amp;ref_src=twsrc%5Etfw">#philsci</a> 
<a href="https://twitter.com/hashtag/philqft?src=hash&amp;ref_src=twsrc%5Etfw">#philqft</a> 
<a href="https://t.co/6DhBpnWPKQ">pic.twitter.com/6DhBpnWPKQ</a></p>&mdash; Ryan Reece (&commm;RyanDavidReece) 
<a href="https://twitter.com/RyanDavidReece/status/908051901219971072?ref_src=twsrc%5Etfw">September 13, 2017</a>
</blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</center>

<center>
<blockquote class="twitter-tweet">
<p lang="en" dir="ltr">You all weren&#39;t much help on Haag&#39;s theorem.<br>Duncan, A. (2012). Conceptual Framework of QFT. Oxford. p. 359. 
<a href="https://t.co/NIHgfNh7s6">pic.twitter.com/NIHgfNh7s6</a></p>&mdash; Ryan Reece (&commm;RyanDavidReece)
<a href="https://twitter.com/RyanDavidReece/status/910703819515871233?ref_src=twsrc%5Etfw">September 21, 2017</a>
</blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</center>

[^Bain2000]: @Bain_2000_Against_particlefield_duality_Asymptotic\.
[^Duncan2012]: @Duncan_2012_Conceptual_Framework_of_Quantum_Field_Theory\.
[^Earman2006]: @Earman_2006_Haags_theorem_and_its_implications\.
[^Haag1955]: @Haag_1955_On_quantum_field_theories\.
[^Klaczynski2016]: @Klaczynski_2016_Haags_theorem_in_renormalised_quantum_field\.
[^Malament1996]: @Malament_1996_In_defence_of_dogma_Why_there_cannot_be\.
[^Teller1997p115]: @Teller_1997_An_Interpretive_Introduction_to_Quantum_Field\, p. 115.


### Exotics in quantum field theory

#### Higher gauge theory

-   [Fiber bundles in physics](https://ncatlab.org/nlab/show/fiber+bundles+in+physics)
    -   Fiber bundles embody two central principles of modern physics:
        1.  the principle of locality
        2.  the gauge principle.
-   Healey on the Aharonov-Bohm effect [^Healey2007ch2]
-   Holonomy
-   Maudlin on fiber bundles
-   [Higher gauge field](https://ncatlab.org/nlab/show/higher+gauge+field) - nLab

>   If we adopt the metaphysics of the fiber bundle to represent chromodynamics,
>   then we must reject the notion that quark color is a universal, or that there are
>   color tropes which can be duplicates, or that quarks are parts of 'natural sets'
>   which include all and only the quarks of the same color, for there is no fact
>   about whether any two quarks are the same color or different. Further, we must
>   reject the notion that there is any metaphysically pure relation of comparison
>   between quarks at different points, since the only comparisons available are
>   necessarily dependent on the existence of a continuous path in space-time
>   connecting the points. So it seems that there are no color properties and no
>   metaphysically pure internal relations between quarks. [^Maudlin2007p96]

>   But if one asks whether, in this picture, the electromagnetic field is a
>   substance or an instance of a universal or a trope, or some combination of
>   these, none of the options seems very useful. If the electromagnetic field
>   is a connection on a fiber bundle, then one understands what it is by studying
>   fiber bundles directly, not by trying to translate modern mathematics into
>   archaic philosophical terminology. [^Maudlin2007p101]

[^Healey2007ch2]: @Healey_2007_Gauging_Whats_Real\, ch. 2-4.
[^Maudlin2007p96]: @Maudlin_2007_The_Metaphysics_Within_Physics\, p. 96.
[^Maudlin2007p101]: @Maudlin_2007_The_Metaphysics_Within_Physics\, p. 101.


#### Non-perturbative features

-   Sphalerons
-   Instanton
-   Shifman [^Shifman2012]

[^Shifman2012]: @Shifman_2012_Advanced_Topics_in_Quantum_Field_Theory_A_lecture\.


#### Supersymmetry

-   Haag-&#321;opusza&#324;ski-Sohnius theorem [^Haag1975]
-   Deligne's theorem on tensor categories
    -   [Deligne's theorem](https://www.physicsforums.com/insights/supersymmetry-delignes-theorem/) - physicsforums.com
    -   [Deligne's theorem on tensor categories](https://ncatlab.org/nlab/show/Deligne%27s+theorem+on+tensor+categories) - ncatlab.org
    -   [supersymmetry](https://ncatlab.org/nlab/show/supersymmetry) - ncatlab.org
-   Martin [^Martin2016]
-   Ellis, J. (2020). [The Higgs, supersymmetry and all that](https://cerncourier.com/a/the-higgs-supersymmetry-and-all-that/). *CERN Courier*. January 10, 2020.

[^Haag1975]: @Haag_1975_All_possible_generators_of_supersymmetries\.
[^Martin2016]: @Martin_2016_A_supersymmetry_primer\.


### Interpretations of quantum mechanics

>   The withdrawal of philosophy into a "professional" shell of its own has had 
>   disastrous consequences. The younger generation of physicists, the Feynmans,
>   the Schwingers, etc., may be very bright; they may be more intelligent than
>   their predecessors, than Bohr, Einstein, Schr&ouml;dinger, Boltzmann, 
>   Mach and so on. But they are uncivilized savages, they lack in philosophical 
>   depth---and this is the fault of the very same idea of professionalism which
>   you are now defending.

-- from a letter in Appendix B of Feyerabend's *Against Method*


#### EPR paradox

TODO


#### Bell's theorem

TODO


#### Copenhagen "interpretation"

TODO

![Interpretations of quantum mechanics ([philosophy-in-figures.tumblr.com](http://philosophy-in-figures.tumblr.com/post/145247040756/interpretations-of-quantum-mechanics-v2)).](img/interpretations-of-quantum-mechanics-v2.png){#fig:interpretations-of-quantum-mechanics-v2}


#### Bohmian mechanics

-   de Broglie-Bohm


#### Everettian interpretation

-   Everett
-   DeWitt
-   note relationship with decoherence
-   *Something Deeply Hidden* [^Carroll2019]

[^Carroll2019]: @Carroll_2019_Something_Deeply_Hidden\.


#### Collapse interpretations

-   GRW
-   TODO: find ref that GRW is empirical


#### Epistemic interpretations

-   $\psi$-epistemic interpretations
-   quantum Bayesianism (QBism)


#### PBR theorem

-   PBR [^Pusey2012]
-   Wikipedia: Either the quantum state corresponds to a physically
    real object and is not merely a statistical tool, or else all quantum states,
    including non-entangled ones, can communicate by action at a distance. 
-   Gisin's Theorem

[^Pusey2012]: @Pusey_2012_On_the_reality_of_the_quantum_state\.


#### Other interpretations

-   relational quantum mechanics
-   transactional quantum mechanics
-   ...


### The standard model of particle physics

![The total action of the physics of the standard model 
    together with general relativity as presented by [Sean Carroll on his blog](http://www.preposterousuniverse.com/blog/2013/01/04/the-world-of-everyday-experience-in-one-equation/).
    In this all encompassing equation, fermions are the quanta of the $\psi$ fields and
    bosons are the quanta of the $g$, $A$, and $\Phi$ fields.
    ](img/carroll-standard-model-action.jpg){#fig:carroll-standard-model-action}

-   GWS electroweak theory: SU(2) $\times$ U(1)
-   QCD: SU(3)
-   Nima Arkani-Hamed doing particle physics *a priori*: ["Why is there a Macroscopic Universe?"](https://www.youtube.com/watch?v=F2Fxt_yCrcc)
-   Nima Arkani-Hamed on [Collider Physics from the Bottom Up](https://www.youtube.com/watch?v=uG8VJb3jRzU)


### Beyond the standard model

-   Neutrino masses and mixings
-   Running of the couplings
-   Grand unification
-   Supersymmetry
-   Minimal Supersymmetric Standard Model (MSSM)
-   Strong $CP$ problem
-   Quantum gravity

![Two-loop renormalization group evolution of the inverse gauge couplings, $\alpha^{-1}$,
    in the Standard Model (dashed lines) and the MSSM (solid lines).
    In the MSSM case, the sparticle masses are treated as a common
    threshold varied between 750 GeV (blue) and 2.5 TeV (red). [^Martin2016p66]
    ](img/martin-running-of-the-couplings.png){#fig:martin-running-of-the-couplings}

[^Martin2016p66]: @Martin_2016_A_supersymmetry_primer\, p. 66.


#### Criticisms

-   *Farewell to Reality* [^Baggott2013]

[^Baggott2013]: @Baggott_2013_Farewell_to_Reality_How_modern_physics_has\.


### Gravity and cosmology

#### General relativity

-   *Spacetime and Geometry* [^Carroll2004]

[^Carroll2004]: @Carroll_2004_Spacetime_and_Geometry\.


#### Cosmology

-   Big bang
-   Dark matter
-   [Bullet Cluster](https://en.wikipedia.org/wiki/Bullet_Cluster)
-   "A direct empirical proof of the existence of dark matter" [astro-ph/0608407](http://arxiv.org/abs/astro-ph/0608407)
-   Inflation
-   $\Lambda$+CMD Cosmological Standard Model


### Fine-tuning

-   Fine-tuning
-   Anthropic principle
-   Relationship to evolution
-   [Richard Dawkins and Steven Weinberg discuss science and religion](https://www.youtube.com/watch?v=EGL8SesIo6Y)


### Complexity

-   nonlinear systems
-   chaos


### Emergence

Thermodynamics, statistical mechanics, renormalization.

-   More is different[^Anderson-1972]
-   Emergence[^Lisi-2017]
-   Bain
-   Views on reductionism
    -   [Mariam Thalos - 3:AM Magazine interview](https://www.3ammagazine.com/3am/multi-scale-existentialist-freedoms/)
-   [Closer To Truth: What's Strong Emergence?](https://www.youtube.com/watch?v=zkffv2nVF64)
    -   George F. R. Ellis vs Barry Loewer
-   See also the [Outline on naturalism](naturalism.html#reductionism)

[^Anderson-1972]: @Anderson_1972_More_is_different\.
[^Lisi-2017]: @Lisi_2017_Emergence\.


### Bracketing human experience

-   Entailment, Reductionism
-   [Sean Carroll's acceptance speech](https://www.youtube.com/watch?v=40eiycH077A#t=402)
    for the FFRF's the emperor has no clothes award.
-   ["Quantum Field Theory and the Limits of Knowledge"](http://www.preposterousuniverse.com/blog/2015/04/21/quantum-field-theory-and-the-limits-of-knowledge/) - Sean Carroll
-   ["Poetic Naturalism"](https://www.youtube.com/watch?v=xv0mKsO2goA) - Sean Carroll

![Sean on the entailment of everyday life by physics.](img/sean-entailment.jpg)


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
-   Reece, R. (2017). [Quora: What is currently the best explanation for how and why the quantum wave function collapses?](https://www.quora.com/What-is-currently-the-best-explanation-for-how-and-why-the-quantum-wave-function-collapses/answer/Ryan-Reece)


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


Links and encyclopedia articles
--------------------------------------------------------------------------------

<div class="clickmore"><a id="link:encyclopedia_articles" class="closed" onclick="toggle_more('encyclopedia_articles')">
Click to show links
</a></div>
<div id="encyclopedia_articles" class="more">

### SEP

-   [Being and Becoming in Modern Physics](http://plato.stanford.edu/entries/spacetime-bebecome/)
-   [Bell's Theorem](http://plato.stanford.edu/entries/bell-theorem/)
-   [Bohmian Mechanics](http://plato.stanford.edu/entries/qm-bohm/)
-   [Boltzmann's Work in Statistical Physics](https://plato.stanford.edu/entries/statphys-Boltzmann/)
-   [Chaos](http://plato.stanford.edu/entries/chaos/)
-   [Collapse Theories](http://plato.stanford.edu/entries/qm-collapse/)
-   [Computer Simulations in Science](http://plato.stanford.edu/entries/simulations-science/)
-   [Copenhagen Interpretation of Quantum Mechanics](http://plato.stanford.edu/entries/qm-copenhagen/)
-   [Decoherence](http://plato.stanford.edu/entries/qm-decoherence/)
-   [Emergent Properties](http://plato.stanford.edu/entries/properties-emergent/)
-   [Everett's Relative-State Formulation of Quantum Mechanics](http://plato.stanford.edu/entries/qm-everett/)
-   [Fine-tuning](https://seop.illc.uva.nl/entries/fine-tuning/)
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
-   [Clinamen](https://en.wikipedia.org/wiki/Clinamen)
-   [Complexity](http://en.wikipedia.org/wiki/Complexity)
-   [Constructor theory](http://en.wikipedia.org/wiki/Constructor_theory)
-   [CP violation](https://en.wikipedia.org/wiki/CP_violation)
-   [Curie's Principle](https://en.wikipedia.org/wiki/Curie%E2%80%99s_Principle)
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
-   [General relativity](https://en.wikipedia.org/wiki/General_relativity)
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
-   [Holonomy](https://en.wikipedia.org/wiki/Holonomy)
-   [Kaluza-Klein theory](https://en.wikipedia.org/wiki/Kaluza%E2%80%93Klein_theory)
-   [Kochen-Specker Theorem](https://en.wikipedia.org/wiki/Kochen%E2%80%93Specker_theorem)
-   [Lambda-CDM model](https://en.wikipedia.org/wiki/Lambda-CDM_model)
-   [Landau pole](https://en.wikipedia.org/wiki/Landau_pole)
-   [Little hierarchy problem](https://en.wikipedia.org/wiki/Little_hierarchy_problem)
-   [Locality, Principle of](https://en.wikipedia.org/wiki/Principle_of_locality)
-   [Local hidden variable theory](https://en.wikipedia.org/wiki/Local_hidden_variable_theory)
-   [Local (algebraic) quantum field theory](https://en.wikipedia.org/wiki/Local_quantum_field_theory)
-   [Loopholes in Bell test experiments](https://en.wikipedia.org/wiki/Loopholes_in_Bell_test_experiments)
-   [Mach's principle](https://en.wikipedia.org/wiki/Mach%27s_principle)
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
-   [Shape dynamics](https://en.wikipedia.org/wiki/Shape_dynamics)
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
-   [Topological order](https://en.wikipedia.org/wiki/Topological_order)
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
-   [Wightman axioms](https://en.wikipedia.org/wiki/Wightman_axioms)
-   [Wigner, Eugene (1902-1995)](https://en.wikipedia.org/wiki/Eugene_Wigner)
-   [Wigner's classification](https://en.wikipedia.org/wiki/Wigner%27s_classification)
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

-   Al-Khalili, J. (2009). ["Atom" BBC documentary](http://topdocumentaryfilms.com/atom-tim/) (3 episodes)
-   Carroll, S. (2013). [Particles, Fields and The Future of Physics.](https://www.youtube.com/watch?v=gEKSpZPByD0)
-   Carroll, S. (2019). [Something Deeply Hidden - talk at Google.](https://www.youtube.com/watch?v=F6FR08VylO4)
-   Kuhn, R.L. (2020). [Closer To Truth: What's Strong Emergence?](https://www.youtube.com/watch?v=zkffv2nVF64)
-   Maudlin, T. (2018). [Ontological clarity, electromagnetism, Aharanov-Bohm effect.](https://www.fetzer-franklin-fund.org/media/ontological-clarity-electromagnetism-aharanov-bohm-effect-maudlin-video/)
-   Tong, D. (2017). [Quantum Fields: The Real Building Blocks of the Universe.](https://www.youtube.com/watch?v=zNVQfWC_evg)

</div>

<!-- REFERENCES -->

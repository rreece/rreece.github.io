Philosophy of mathematics
================================================================================

These next several outlines deal with philosophy of certain
specialized topics, starting with this one on the philosophy of mathematics.
Here we dig into issues of what is _**abstraction**_.

First we survey the following branches of mathematics:
algebra, analysis, numbers theory, logic, model theory, and category theory.
Then we discuss unification programs across branches,
followed by sections on positions in philosophy of mathematics,
in particular dealing with the realism/antirealism or platonism/nominalism
debate.


<!-- PAGETOC -->


Algebra
--------------------------------------------------------------------------------

### Introduction

TODO

>   Prove all things; hold fast that which is good.

-- *1 Thessalonians*, 5:21--28, KJV


### History

-   roots from Babylonians
-   [Al-Karaji](https://en.wikipedia.org/wiki/Al-Karaji) (c. 953-1029)
-   [Gerolamo Cardano](https://en.wikipedia.org/wiki/Gerolamo_Cardano) (1501-1576)
-   Carl Friedrich Gauss (1777-1855)
    -   published a proof of the fundamental theorem of algebra (1797)
    -   The theorem states that the field of complex numbers is algebraically closed.
-   [&Eacute;variste Galois](https://en.wikipedia.org/wiki/%C3%89variste_Galois) (1811-1832)
-   [Arthur Cayley](https://en.wikipedia.org/wiki/Arthur_Cayley) (1821-1895)
-   [Leopold Kronecker](https://en.wikipedia.org/wiki/Leopold_Kronecker) (1823-1891)
-   arithmetic vs abstract algebra


### Linear algebra

-   Linear equations and transformation
-   Vector spaces and dual spaces
    -   For an infinite dimensional vector space, V, while elements of V must have
        "finite support" (only finitely many nonzero coordinates in any basis representation),
        elements of V* can have "infinite support."
-   Axler, S. (2024). [*Linear Algebra Done Right*](https://link.springer.com/content/pdf/10.1007/978-3-031-41026-0.pdf).
-   [Spectral theorem](https://en.wikipedia.org/wiki/Spectral_theorem):
    $A$ is normal, $A A^\dagger = A^\dagger A \iff A = U D U^\dagger$
    is an eigendecomposition of $A$, where the column vectors of $U$
    are the eigenvectors of $A$ with corresponding eigenvalues on the
    diagonal of $D$.
-   [Principal Component Analysis (PCA)](https://en.wikipedia.org/wiki/Principal_component_analysis)
-   [Rayleigh quotient](https://en.wikipedia.org/wiki/Rayleigh_quotient)

![Matrix World: Classifying all matrices (source: [The Art of Linear Algebra](https://github.com/kenjihiranabe/The-Art-of-Linear-Algebra/tree/main)).](img/matrix-world.png){#fig:matrix-world}

See also:

-   [Estimation of covariance matrices](ethics.html#estimation-of-covariance-matrices)
-   [Convex optimization](ethics.html#convex-optimization)


### Finite groups

-   [Group](https://en.wikipedia.org/wiki/Group_(mathematics))
-   [Sporadic group](https://en.wikipedia.org/wiki/Sporadic_group)
-   [Classification of finite simple groups](https://en.wikipedia.org/wiki/Classification_of_finite_simple_groups)
-   Elwes, R. (2006). [An enormous theorem: The classification of finite simple groups](https://plus.maths.org/content/enormous-theorem-classification-finite-simple-groups).
-   There are 26 sporadic simple groups (27 if you count the Tits group).
-   YouTube 3Blue1Brown: [Group theory and why I love       
    808,017,424,794,512,875,886,459,904,961,710,757,005,754,368,000,000,000](https://www.youtube.com/watch?v=mH0oCDa74tE).
-   [Monstrous moonshine](https://en.wikipedia.org/wiki/Monstrous_moonshine)
-   [Richard Borcherds](https://en.wikipedia.org/wiki/Richard_Borcherds) (b. 1959)
-   Carter, N. (2009). *Visual Group Theory*. [^Carter2009]

[^Carter2009]: @Carter_2009_Visual_Group_Theory\.


### Lie groups

-   [Lie group](https://en.wikipedia.org/wiki/Lie_group)
    -   [Sophus Lie](https://en.wikipedia.org/wiki/Sophus_Lie) (1842-1899)
    -   [&Eacute;lie Cartan](https://en.wikipedia.org/wiki/%C3%89lie_Cartan) (1869-1951)
    -   Schwichtenberg, J. (2016). [Classification of simple Lie groups](http://jakobschwichtenberg.com/classification-of-simple-lie-groups/).
    -   Hall, B.C. (2000). [*An Elementary Introduction to Groups and Representations*](https://arxiv.org/abs/math-ph/0005032). [^Hall2000]
    -   Zee, A. (2016). *Group Theory in a Nutshell for Physicists*. [^Zee2016]
-   Dynkin diagrams
    -   [ADE classification](https://en.wikipedia.org/wiki/ADE_classification)
    -   Siegel, K. (2014). The ubiquity of ADE classifications in nature.

[^Hall2000]: @Hall_2000_An_Elementary_Introduction_to_Groups\.
[^Zee2016]: @Zee_2016_Group_Theory_in_a_Nutshell_for_Physicists\.


### Abstract algebra

-   A field is a commutative division ring.
-   Vector space
-   Modules are to rings as vector spaces are to fields.


### More

-   Jordan algebras
    -   McCrimmon, K. (2000). *A Taste of Jordan Algebras*. [^McCrimmon2000]
-   [Algebraic number theory](https://en.wikipedia.org/wiki/Algebraic_number_theory)
-   [Representation theory](https://en.wikipedia.org/wiki/Representation_theory)
-   [Langlands program](https://en.wikipedia.org/wiki/Langlands_program)
-   [Universal algebra](https://en.wikipedia.org/wiki/Universal_algebra)
-   [Hurwitz's theorem](https://en.wikipedia.org/wiki/Hurwitz%27s_theorem_(composition_algebras))
    -   The real numbers, the complex numbers, the quaternions, and the octonions
        exhaust all the possible normed division algebras.
    -   Baez, J.C. (2002). [The octonions](https://arxiv.org/abs/math/0105155). [^Baez2002]
    -   Westbury, B.W. (2010). [Hurwitz' theorem on composition algebras](https://arxiv.org/abs/1011.6197). [^Westbury2010]

See also:

-   [Foundations of QM](physics.html#foundations-of-qm)
-   [Supersymmetry](physics.html#supersymmetry) in the Outline of [physics](physics.html)

[^Baez2002]: @Baez_2002_The_octonions\.
[^McCrimmon2000]: @McCrimmon_2000_A_Taste_of_Jordan_Algebras\.
[^Westbury2010]: @Westbury_2010_Hurwitz_theorem_on_composition_algebras\.


Analysis
--------------------------------------------------------------------------------

### Introduction

TODO


### History

-   Ren&eacute; Descartes (1596-1650)
    -   Geometry and coordinates, modern notation, geometric problems forumalted with algebra
    -   *La G&eacute;om&eacute;trie* (1637)
-   Isaac Newton (1642-1726/7)
-   Gottfried Wilhelm Leibniz (1646-1716)
-   Jacob Bernoulli (1655-1705)
-   Leonhard Euler (1707-1783)
    -   *Mechanica* (1736)
-   [Pierre-Simon Laplace](https://en.wikipedia.org/wiki/Pierre-Simon_Laplace) (1749-1827)
-   Carl Friedrich Gauss (1777-1855)
-   Augustin-Louis Cauchy (1789-1857)
-   Karl Weierstrass (1815-1897)
-   George Stokes (1819-1903)
-   Differential forms
-   Geometry and the [Erlangen program](https://en.wikipedia.org/wiki/Erlangen_program)


### Development of calculus

![Leibniz's notation of integration: $\int$ (*summa*) and
    differentiation: $d$ (*differentia*) summarized in the margin of his notes in 1675.
    Note that $\Pi$ was Leibniz's notation for equality.
    Photo by [S. Wolfram](https://writings.stephenwolfram.com/2013/05/dropping-in-on-gottfried-leibniz/) (2013)
    of notes in the Leibniz-Archiv in Hanover, Germany.
    ](img/leibniz-1675-summa-and-diff.jpg){#fig:leibniz-1675-summa-and-diff}

-   James Gregory (1638-1675) 
-   Isaac Barrow (1630-1677)
    -   Fundamental theorem of calculus in
        Proposition 11, Lecture 10, of his *Lectiones Geometricae*, published in 1670.
-   Isaac Newton (1642-1727)
    -   Newton claimed to have the ideas of calculus in the mid 1660s.
    -   In 1669, Newton wrote an article on infinite series with ideas leading to calculus: "De analysi per aequationes numero terminorum infinitas", which wasn't published until 1711, 42 years later.
    -   *Philosophi&aelig; Naturalis Principia Mathematica* (1687)
-   Gottfried Wilhelm Leibniz (1646-1716)
    -   Leibniz first used $dx$ in publication in        
        Leibniz, G.W. (1684). Nova methodus pro maximis et minimis. *Acta Eruditorum*.
    -   Leibniz first used his intergral sign, $\int$, in publication in         
        Leibniz, G.W. (1686). De geometria recondita et analysi indivisibilium atque infinitorum. *Acta Eruditorum*.
    -   Wolfram, S. (2013). [Dropping in on Gottfried Leibniz](https://writings.stephenwolfram.com/2013/05/dropping-in-on-gottfried-leibniz/).
-   Aldrich, John. (?). [Earliest uses of symbols of calculus](http://jeff560.tripod.com/calculus.html).
-   [Leibniz-Newton calculus controversy](https://en.wikipedia.org/wiki/Leibniz%E2%80%93Newton_calculus_controversy)
    -   In 1849, C. I. Gerhardt, while going through Leibniz's manuscripts, found extracts from Newton's "De analysi per aequationes numero terminorum infinitas".
    -   Starbird, M. (2016). [Who invented calculus?](https://www.thegreatcoursesdaily.com/invented-calculus-newton-leibniz/)


#### Matrix calculus

-   [Matrix calculus](https://explained.ai/matrix-calculus/)
-   Dwyer, P.S. (1967). [Some applications of matrix derivatives in multivariate analysis](https://www.tandfonline.com/doi/abs/10.1080/01621459.1967.10482934). [^Dwyer1967]

[^Dwyer1967]: @Dwyer_1967_Some_applications_of_matrix_derivatives\.


### Differential geometry

-   History
    -   Leonhard Euler (1707-1783)
    -   William Rowan Hamilton (1805-1865)
    -   George Stokes (1819-1903)
    -   Josiah Willard Gibbs (1839-1903)
    -   &Eacute;lie Cartan (1869-1951)
    -   W.V.D. Hodge (1903-1975)
-   Vector calculus
    -   Stokes' theorem
    -   Tong, D. (2022). [Lectures on Vector Calculus](https://www.damtp.cam.ac.uk/user/tong/vc.html).
-   Differential forms
    -   Manifold, tangent and cotangent spaces, vector bundle, fiber bundle
    -   Burke, W.L. (1985). *Applied Differential Geometry*. [^Burke1985]
    -   Frankel, T. (1997). *The Geometry of Physics: An Introduction*. [^Frankel1997]
    -   Review by Fr&egrave; [^Fre2013v1ch2]
    -   Varadarajan, V. S. (2003). Vector bundles and connections in physics and mathematics: some historical remarks. [^Varadarajan2003]
    -   Tao, T. (2007). [Differential forms and integration](https://www.math.ucla.edu/~tao/preprints/forms.pdf). [^Tao2007]
    -   Sussman, G.J. & Wisdom, J. (2013). [*Functional Differential Geometry*](https://mitpress.mit.edu/books/functional-differential-geometry). [^Sussman2013]
    -   Tu, L.W. (2017). *Differential Geometry: Connections, Curvature, and Characteristic Classes*. [^Tu2017]
    -   Bronstein, M.M. et al. (2021). [Geometric deep learning: Grids, groups, graphs, geodesics, and gauges](https://arxiv.org/abs/2104.13478). [^Bronstein2021p56]
-   [De Rham cohomology](https://en.wikipedia.org/wiki/De_Rham_cohomology)
-   [Chern-Simons theory](https://en.wikipedia.org/wiki/Chern%E2%80%93Simons_theory)
-   Non-commutative
    -   Connes, A. (1985). [Non-commutative differential geometry](https://link.springer.com/article/10.1007/BF02698807). [^Connes1985a]

$$ a \times b = \star(a \wedge b) $$

See also:

-   [Fiber bundles](physics.html#fiber-bundles)

[^Bronstein2021p56]: @Bronstein_2021_Geometric_deep_learning_Grids_groups_graphs\, p. 56--60.
[^Burke1985]: @Burke_1985_Applied_Differential_Geometry\.
[^Connes1985a]: @Connes_1985_Non_commutative_differential_geometry\.
[^Frankel1997]: @Frankel_1997_The_Geometry_of_Physics_An_Introduction\.
[^Fre2013v1ch2]: @Fre_2013_Gravity_a_Geometrical_Course_Volume_1\, ch. 2.
[^Sussman2013]: @Sussman_2013_Functional_Differential_Geometry\.
[^Tao2007]: @Tao_2007_Differential_forms_and_integration\.
[^Tu2017]: @Tu_2017_Differential_Geometry_Connections_Curvature\.
[^Varadarajan2003]: @Varadarajan_2003_Vector_bundles_and_connections_in_physics\.


Number theory
--------------------------------------------------------------------------------

### Introduction

-   [Peano axioms](https://en.wikipedia.org/wiki/Peano_axioms)
-   [Robinson arithmetic](https://en.wikipedia.org/wiki/Robinson_arithmetic)
-   Newstead, C. (2022). [*An Infinite Descent into Pure Mathematics*](https://infinitedescent.xyz/dl/infdesc.pdf).


### Set theory

-   Membership: Axiom of extensionality
-   von Neumann's set theoretical definition of numbers


#### Naive Set Theory

-   [Axiom of unrestricted comprehension](https://en.wikipedia.org/wiki/Axiom_schema_of_specification#Unrestricted_comprehension)
    -   There exists the set $\{ x : \phi(x) \}$, the set whose members are those that satisfy $\phi$.
-   [Russell's paradox](https://en.wikipedia.org/wiki/Russell%27s_paradox)
    -   Let $y = \{ x : x \notin x \}$ then $y \in y \Leftrightarrow y \notin y$
-   [Curry's paradox](https://en.wikipedia.org/wiki/Curry%27s_paradox)


#### Zermelo-Fraenkel set theory

-   [Zermelo-Fraenkel set theory](https://en.wikipedia.org/wiki/Zermelo%E2%80%93Fraenkel_set_theory)
-   [Axiom schema of specification](https://en.wikipedia.org/wiki/Axiom_schema_of_specification) AKA Axiom of restricted comprehension
    -   Define a set by defining a subset of a known set $A$, $\{ x \in A : \phi(x) \}$, instead of the more general $\{ x : \phi(x) \}$
    -   Given any set A, there exists a subset of $A$, whose memebers are those that satisfy $\phi$ (and are also members of $A$).
-   [Zermelo-Fraenkel set theory](https://en.wikipedia.org/wiki/Zermelo%E2%80%93Fraenkel_set_theory) + [Axiom of choice](https://en.wikipedia.org/wiki/Axiom_of_choice) = ZFC


#### Other approaches

-   [Von Neumann-Bernays-G&ouml;del set theory](https://en.wikipedia.org/wiki/Von_Neumann%E2%80%93Bernays%E2%80%93G%C3%B6del_set_theory)
-   [Quine's New Foundations](https://en.wikipedia.org/wiki/New_Foundations)


### Transfinite numbers

-   Ordinal (index) vs cardinal (size) numbers
-   [Cantor-Bernstein-Schr&ouml;eder theorem](https://en.wikipedia.org/wiki/Schr%C3%B6der%E2%80%93Bernstein_theorem)
-   [Transfinite numbers](https://en.wikipedia.org/wiki/Transfinite_number):
    -   $\omega$: the smallest transfinite ordinal number; the order type of the natural numbers.
    -   $\aleph_0$: the first transfinite cardinal number; the cardinality of the natural numbers, $\aleph_0 \equiv |\mathbb{N}|$
    -   There is a one-to-one correspondence between ordinal and cardinal numbers. [^Trioni2020Omega]
        $\omega = \aleph_0$       
    -   The $\aleph_n$ hierarchy of cardinals is defined by transfinite recursion:
        -   $\aleph_0$ is the smallest infinite cardinal.
        -   $\aleph_{n+1}$ is the successor cardinal to $\aleph_{n}$
        -   $\aleph_{\lambda} = \mathrm{sup}_{n<\lambda} \aleph_n$ for limit ordinals $\lambda$
    -   $\aleph_0$ is the smallest infinite cardinal; it is countable.
    -   $\aleph_1$ is the first uncountable cardinal.
    -   $\aleph_2$ is the second uncountable cardinal.
-   Transfinite numbers were anticipated by [Robert Grosseteste](https://plato.stanford.edu/entries/grosseteste/) (ca. 1168-1253).
-   Developed by [Georg Cantor](https://en.wikipedia.org/wiki/Georg_Cantor) (1845-1918) in 1895
    -   [Cantor's first set theory article](https://en.wikipedia.org/wiki/Cantor%27s_first_set_theory_article)
    -   Proved that the real numbers are uncountably infinite.
    -   The cardinalities of $\mathbb{R}$ and $\mathbb{R}^n$ are both $C$.
-   [Schr&ouml;der–Bernstein theorem](https://en.wikipedia.org/wiki/Schr%C3%B6der%E2%80%93Bernstein_theorem)
    -   Not accepted in intuitionism
-   [Cantor's theorem](https://en.wikipedia.org/wiki/Cantor%27s_theorem)
    -   Let $|A| \equiv \mathrm{card}(A)$ denote the cardinality (i.e size) of a set, $A$.
    -   A power set, $P(A)$, of a set, $A$, is the set of all subsets of $A$.
    -   The cardinality of a power set is $|P(A)| = 2^{|A|}$
    -   The cardinality of a power set is strictly larger than the set: $|A| < |P(A)|$
-   [Cardinality of the continuum](https://en.wikipedia.org/wiki/Cardinality_of_the_continuum)
    -   The cardinality of the reals: $C \equiv |\mathbb{R}|$
    -   Examples of sets with cardinality = $C$
        -   real numbers, $\mathbb{R}$
        -   closed or open intervals on $\mathbb{R}$
        -   Euclidean space, $\mathbb{R}^n$
        -   complex numbers, $\mathbb{C}$
        -   set of all continuous functions from $\mathbb{R}$ to $\mathbb{R}$
        -   power set of of natural numbers, $P(\mathbb{N})$
    -   The cardinality of the reals is the power set of the natural numbers:
        $C \equiv |\mathbb{R}| = |P(\mathbb{N})| = 2^{|\mathbb{N}|} = 2^{\aleph_0} > \aleph_0$
-   [Continuum Hypothesis](https://en.wikipedia.org/wiki/Continuum_hypothesis) (CH)
    -   CH: There is no set $S$ such that $\aleph_0 < |S| < 2^{\aleph_0}$
    -   $C = 2^{\aleph_0}$, and under CH, $C = 2^{\aleph_0} = \aleph_1$.
    -   Relationship with the [axiom of choice](https://en.wikipedia.org/wiki/Axiom_of_choice)
    -   Paul Cohen showed the CH is undecidable in ZFC (1963).
-   Generalized Continuum Hypothesis (GCH)
    -   $\aleph_{n+1} = 2^{\aleph_n}$
 
Hilbert:

>   There is, however, a completely satisfactory way of avoiding the paradoxes
>   without betraying our science. The desires and attitudes which help us
>   find this way and show us what direction to take are these:
>   
>   1.  Wherever there is any hope of salvage, we will carefully investigate
>       fruitful definitions and deductive methods. We will nurse them,
>       strengthen them, and make them useful. No one shall drive us out
>       of the paradise which Cantor has created for us.
>   2.  We must establish throughout mathematics the same certitude for
>       our deductions as exists in ordinary elementary number theory,
>       which no one doubts and where contradictions and paradoxes
>       arise only through our own carelessness. [^Hilbert1926p191]

[^Hilbert1926p191]: @Hilbert_1926_Uber_das_Unendliche\, p. 191.
[^Trioni2020Omega]: Trioni, S. (2020). [Cantor's attic](https://neugierde.github.io/cantors-attic/Omega) - Omega.


Logic
--------------------------------------------------------------------------------

### Introduction

Pedagogy:

-   Hunter, G. (1971). *Metalogic: An Introduction to the Metatheory of Standard First-Order Logic*. [^Hunter1971]
-   Monk, J.D. (1976). *Mathematical Logic*. [^Monk1976]
-   Sullivan, B.W. (2013). [*Everything You Always Wanted To Know About Mathematics*](https://www.math.cmu.edu/~jmackey/151_128/bws_book.pdf). [^Sullivan2013]
-   Smith, P. (2020). *An Introduction to Formal Logic*. [^Smith2020]
-   Smith, P. (2022). *Beginning Mathematical Logic A Study Guide*. [^Smith2022]

More:

-   Carnap, R. (1958). *Introduction to Symbolic Logic and its Applications*. [^Carnap1958]
-   Teller, P. (1989). *A Modern Formal Logic Primer*. [^Teller1989]
-   Bonevac, D. (2003). *Deduction: Introductory to Symbolic Logic*. [^Bonevac2003]
-   MacFarlane, J. (2021). *Philosophical Logic: A Contemporary Introduction.* [^MacFarlane2021]
-   [*The Open Logic Text*](https://openlogicproject.org/) [^OpenLogicText]
-   [logicinaction.org](http://www.logicinaction.org/)
-   [logicmatters.net](https://www.logicmatters.net/)

[^Bonevac2003]: @Bonevac_2003_Deduction_Introductory_to_Symbolic_Logic\.
[^Carnap1958]: @Carnap_1958_Introduction_to_Symbolic_Logic_and_its\.
[^Hunter1971]: @Hunter_1971_Metalogic_An_Introduction_to_the_Metatheory\.
[^MacFarlane2021]: @MacFarlane_2021_Philosophical_Logic_A_contemporary_introduction\.
[^Monk1976]: @Monk_1976_Mathematical_Logic\.
[^OpenLogicText]: @Open_2020_The_Open_Logic_Text\.
[^Smith2020]: @Smith_2020_An_Introduction_to_Formal_Logic\.
[^Smith2022]: @Smith_2022_Beginning_Mathematical_Logic_A_Study_Guide\.
[^Sullivan2013]: @Sullivan_2013_Everything_You_Always_Wanted_To_Know_About\.
[^Teller1989]: @Teller_1989_A_Modern_Formal_Logic_Primer\.


### History

-   [Aristotle](http://en.wikipedia.org/wiki/Aristotle) (384-322 BCE)
    -   founded logic
    -   [Square of opposition](https://en.wikipedia.org/wiki/Square_of_opposition)
    -   *Modus ponens*, *modus tollens*, Affirming the consequent, Proof by contrapositive
-   [Euclid](http://en.wikipedia.org/wiki/Euclid) (fl. 300 BCE)
    -   logico-deductive method founded by Euclid's *Elements*
-   [Chrysippus](https://en.wikipedia.org/wiki/Chrysippus) (c. 279-206 BCE)
-   [Vasubandhu](https://en.wikipedia.org/wiki/Vasubandhu) (fl. 4th to 5th century CE)
-   [Dign&amacr;ga](https://en.wikipedia.org/wiki/Dign%C4%81ga) (c. 480-540 CE)
-   [Charles Sanders Peirce](https://en.wikipedia.org/wiki/Charles_Sanders_Peirce) (1839-1914)
-   [Gottlob Frege](https://en.wikipedia.org/wiki/Gottlob_Frege) (1848-1925)
    -   [*Begriffsschrift*](https://en.wikipedia.org/wiki/Begriffsschrift) (1879)
-   [Alfred North Whitehead](https://en.wikipedia.org/wiki/Alfred_North_Whitehead) (1861-1947) and [Bertrand Russell](http://en.wikipedia.org/wiki/Bertrand_Russell) (1872-1970) published [*Principia Mathematica*](https://en.wikipedia.org/wiki/Principia_Mathematica) in 1910
    -   [Russell's paradox](https://en.wikipedia.org/wiki/Russell%27s_paradox)
    -   PM avoids Russell's paradox by introduction of the "ramified theory of types".
    -   Later lead to Church's (1976) formulation of the logic of PM with $r$-types.
-   [Henry M. Sheffer](https://en.wikipedia.org/wiki/Henry_M._Sheffer) (1882-1964)
    -   Sheffer, H.M. (1913). [A set of five independent postulates for Boolean algebras, with application to logical constants](https://www.ams.org/journals/tran/1913-014-04/S0002-9947-1913-1500960-1/). [^Sheffer1913]
    -    Propositional logic can be formulated using a single connective: either logical NAND or its dual, logical NOR.
-   [Emil Post](https://en.wikipedia.org/wiki/Emil_Leon_Post) (1897-1954)
-   [Alfred Tarski](https://en.wikipedia.org/wiki/Alfred_Tarski) (1901-1983)
-   [Kurt G&ouml;del](https://en.wikipedia.org/wiki/Kurt_G%C3%B6del) (1906-1978)
    -   [G&ouml;del's completeness theorem](https://en.wikipedia.org/wiki/G%C3%B6del%27s_completeness_theorem) (1929)
    -   [G&ouml;del's incompleteness theorems](http://en.wikipedia.org/wiki/G%C3%B6del%27s_incompleteness_theorems) (1931)
-   [Gerhard Gentzen](https://en.wikipedia.org/wiki/Gerhard_Gentzen) (1909-1945)
-   [Leon Henkin](https://en.wikipedia.org/wiki/Leon_Henkin) (1921-2006)


[^Sheffer1913]: @Sheffer_1913_A_set_of_five_independent_postulates_for_Boolean\.


### Propositional logic

-   [Propositional logic](https://en.wikipedia.org/wiki/Propositional_logic)
    -   AKA propositional calculus and zeroth-order logic
-   Validity and soundness:
    -   An argument is *valid* iff for any assignment of the truth values in the argument
        where all of the premises are true, the conclusion is always true.
    -   An argument is *sound* iff it is valid and all of its premises are true.
-   [Sequent calculus](https://en.wikipedia.org/wiki/Sequent_calculus)

*Syntactic consequence:*

$$ A \vdash B $$

means that $B$ is logically derivable/provable from $A$; $B$ is a theorem of the premises, $A$.

*Semantic consequence:*

$$ A \models B $$

means that in all possible valuations in which $A$ is true, $B$ is also true.
One says that $A$ "entails" $B$, or $A$ "models" $B$.

Note that $\vdash$, $\models$, and $\equiv$ are all metalogical symbols,
not part of the rules of logic; they are shorthands.

$\vdash$  means "from which, it is derivable that".          
$\models$ means "entails that, *i.e.* in every case this is true, that is true (regardless of provability)".           
$\equiv$ means "is identical to".         

Lecture notes on soundness and completeness:

-   [Cornell](https://www.cs.cornell.edu/courses/cs2800/2016sp/lectures/lec39-sound-complete.html)
-   [Waterloo](https://cs.uwaterloo.ca/~plragde/cs245old/03-propsem.pdf)

A formal system is *sound* if everything that is provable is in fact true,
i.e. if $A_1, A_2, \ldots A_n \vdash B$, then $A_1, A_2, \ldots A_n \models B$.

A formal system is *complete* if everything that is true has a proof,
i.e. if $A_1, A_2, \ldots A_n \models B$, then $A_1, A_2, \ldots A_n \vdash B$.

Propositional logic was proven to be sound ($\vdash$ implies $\models$)
and complete ($\models$ implies $\vdash$) by Emil Post in 1921. [^Post1921]

-   Emil Post and his anticipation of G&ouml;del and Turing [^Stillwell2004]

*Material implication:*

$$ P \rightarrow Q \equiv \lnot P \lor Q $$

-   [Paradoxes of material implication](https://en.wikipedia.org/wiki/Paradoxes_of_material_implication)
-   [Vacuous truth](https://en.wikipedia.org/wiki/Vacuous_truth)
-   von Fintel, K. (2011). [Conditionals](https://dspace.mit.edu/handle/1721.1/95781). [^vonFintel2011]

*Modus ponens:*

$$ P \rightarrow Q, P \vdash Q $$

*Modus tollens:*

$$ P \rightarrow Q, \lnot Q \vdash \lnot P $$

*Peirce's law:*

$$ ((P \rightarrow Q) \rightarrow P) \rightarrow P $$

-   TODO: More basic examples in propositional logic
-   TODO: Use-mention distinction: P vs 'P' vs Quine quotes
-   [Cut-elimination theorem](https://en.wikipedia.org/wiki/Cut-elimination_theorem)
-   [Gerhard Gentzen](https://en.wikipedia.org/wiki/Gerhard_Gentzen) (1909-1945)

[^Post1921]: @Post_1921_Introduction_to_the_general_theory_of_elementary\.
[^Stillwell2004]: @Stillwell_2004_Emil_Post_and_his_anticipation_of_Godel\.
[^vonFintel2011]: @vonFintel_2011_Conditionals\.


### First-order logic

-   [First-order logic](https://en.wikipedia.org/wiki/First-order_logic)
    -   AKA predicate logic
    -   Domain of discourse: $\{x\}$
    -   Adds (non-logical) predicates, $Fx$, and quantification over elements, $\exists x\ Fx$.
-   C.S Peirce was first to distinguish between propositional logic,
    first-order logic, and second-order logic in 1885. [^Ewald2018]
-   Consistency, completeness, expressivity
-   [G&ouml;del's completeness theorem](https://en.wikipedia.org/wiki/G%C3%B6del%27s_completeness_theorem)
    -   Establishes a correspondence between semantic truth and syntactic
        provability in first-order logic.
    -   G&ouml;del, K. (1929). *&Uuml;ber die Vollst&auml;ndigkeit des Logikkalk&uuml;ls*. [^Godel1929]
        -   His doctoral dissertation, University Of Vienna.
        -   The first proof of the completeness theorem.
    -   Henkin, L. (1996). The discovery of my completeness proofs. [^Henkin1996]
    -   Awodey, S. & Forssell, H. (2013). First-order logical duality. [^Awodey2013]
    -   [Lindstr&ouml;m's theorem](https://en.wikipedia.org/wiki/Lindstr%C3%B6m%27s_theorem)
-   [Presburger arithmetic](https://en.wikipedia.org/wiki/Presburger_arithmetic)
    -   First-order theory of the natural numbers with addition, but without multiplication.
    -   Presburger arithmetic is consistent, complete, and decidable.

[^Godel1929]: @Godel_1929_Uber_die_Vollstandigkeit_des\.
[^Henkin1996]: @Henkin_1996_The_discovery_of_my_completeness_proofs\.


#### Limitations

-   [L&ouml;wenheim-Skolem theorem](https://en.wikipedia.org/wiki/L%C3%B6wenheim%E2%80%93Skolem_theorem)
    -   The L&ouml;wenheim-Skolem theorem implies that infinite structures
        cannot be categorically axiomatized in first-order logic.
    -   No first-order theory has the strength to uniquely describe a
        structure with an infinite domain, such as the natural numbers
        or the real line.
-   In second-order logic, it is possible to define the addition and
    multiplication operations from the successor operation, but this
    cannot be done in the more restrictive setting of first-order logic.
    -   TODO: show this.
    -   B&egrave;s, A. (2002). [A survey of arithmetical definability](http://lacl.u-pec.fr/bes/publi/survey.pdf). [^Bes2002]
    -   B&egrave;s, A. & Choffrut, C. (2022). [Decidability of definability issues in the theory of real addition](https://fi.episciences.org/10753). [^Bes2022]
-   [Tennenbaum's theorem](https://en.wikipedia.org/wiki/Tennenbaum%27s_theorem)
-   Quantifiers other than $\forall$ and $\exists$ are only definable
    within second-order logic or higher-order logics.

See also:

-   [Number theory](#number-theory)

[^Awodey2013]: @Awodey_2013_First_order_logical_duality\.
[^Bes2002]: @Bes_2002_A_survey_of_arithmetical_definability\.
[^Bes2022]: @Bes_2022_Decidability_of_definability_issues_in_the_theory\.
[^Ewald2018]: @Ewald_2018_The_emergence_of_first_order_logic\.


### Second-order logic

-   [Second-order logic](https://en.wikipedia.org/wiki/Second-order_logic)
-   [Second-order and higher-order logic](https://plato.stanford.edu/entries/logic-higher-order/), *SEP*
-   Includes relation variables in addition to object variables and allows quantification over both.
    -   Extends first-order logic to allow predicates having predicates or functions as arguments, or in which one or both of predicate quantifiers or function quantifiers are permitted.
    -   $\exists P\ P(x)$
-   Addition and multiplication are definabile in second-order logic.
    -   [Peano arithmetic](https://en.wikipedia.org/wiki/Peano_axioms#Peano_arithmetic_as_first-order_theory), PA
    -   [Second-order arithmetic](https://en.wikipedia.org/wiki/Second-order_arithmetic), $\mathrm{Z}_{2}$
-   The power set can be written in terms of second-order logic.
    -   This second-order expressibility of the power-set operation permits the simulation of higher-order logic within second order. [^Enderton2009]
-   $\mathbb{N} \models \mathrm{PA}$
    -   The natural numbers model PA, but not uniquely in FOL.
    -   In SOL, PA is *categorical*, meaning it has only one model up to isomorphism.
-   Henkin semantics
    -   SOL with Henkin semantics is complete. [^Henkin1950]
-   Higher-order logics, type theory
    -   Russell's theory of types [^Russell1908]
    -   Alonzo Church's lambda calculus [^Church1940]
    -   All higher-order logics have the same expressive power as second-order logic.
    -   Modern type theory and its relationship with category theory

[^Church1940]: @Church_1940_A_formulation_of_the_simple_theory_of_types\.
[^Henkin1950]: @Henkin_1950_Completeness_in_the_theory_of_types\.
[^Russell1908]: @Russell_1908_Mathematical_logic_as_based_on_the_theory\.


#### Incompleteness of second-order logic

-   Second-order logic opens the door to G&ouml;del's incompleteness theorems.
-   According to G&ouml;del's incompleteness theorems, the theory of PA (if consistent) is incomplete.
-   Kleene, S.C. (1943). [Recursive predicates and quantifiers](https://www.jstor.org/stable/1990131). [^Kleene1943]
    -   The incompleteness of second-order logic is deeply related to recursion.
-   Rossberg, M. (2004). [First-order logic, second-order logic, and completeness](http://logic.amu.edu.pl/images/4/46/Completenessrossberg.pdf). [^Rossberg2004]

See also:

-   [Model theory](#model-theory)
-   [Incompleteness](#incompleteness)

[^Godel1931]: @Godel_1931_Uber_formal_unentscheidbare_Satze_der\.
[^Godel1951]: @Godel_1995_Some_basic_theorems_on_the_foundations\.
[^Kleene1943]: @Kleene_1943_Recursive_predicates_and_quantifiers\.
[^Rossberg2004]: @Rossberg_2004_First_order_logic_second_order_logic\.


#### Discussion

-   Michael Dummett
-   S.C. Kleene
    -   Kleene, S.C. (1952). *Introduction to Metamathematics*. [^Kleene1952]
        -   First formulation of the sequent calculus in the modern style
-   Setwart Shapiro
    -   *Foundations without Foundationalism: A Case for Second-Order Logic* (1991) [^Shapiro1991]
-   Gillian Russell
    -   Russell, G. (2015). The justification of the basic laws of logic. [^Russell2015]
-   Eliezer Yudkowsky
    -   [Second-Order Logic: The Controversy](https://www.lesswrong.com/posts/SWn4rqdycu83ikfBa/second-order-logic-the-controversy)
    -   "Second-order logic is sound, in the sense that anything syntactically
        provable from a set of premises, is true in any model obeying those
        premises. But second-order logic isn't complete; there are semantic
        consequences you can't derive. If you take second-order logic at face
        value, there's no effectively computable way of deriving all the
        consequences of what you say you 'believe'... which is a major reason
        some mathematicians are suspicious of second-order logic. What does it
        mean to believe something whose consequences you can't derive?"
-   George Boolos
    -   Boolos, G. (1984). [To be is to be the value of a variable (or to be some values of some variables)](https://www.jstor.org/stable/2026308). [^Boolos1984]
    -   [Plural quantification](https://en.wikipedia.org/wiki/Plural_quantification)
-   Ethan Jerzak
    -   Jerzak, E. (2009). [Second-order logic, or: How I learned to stop worrying and love the incompleteness theorems](http://www.math.uchicago.edu/~may/VIGRE/VIGRE2009/REUPapers/Jerzak.pdf). [^Jerzak2009]
-   Ot&aacute;vio Bueno
    -   Bueno, O. (2010). [A defense of second-order logic](https://web.as.miami.edu/personal/obueno/Site/Online_Papers_files/SecnOrd_FINAL.pdf). [^Bueno2010]
-   Ted Sider
    -   Sider, T. (2022). [Crash course on higher-order logic](https://tedsider.org/teaching/higher_order_20/higher_order_crash_course.pdf). [^Sider2022]

[^Boolos1984]: @Boolos_1984_To_be_is_to_be_the_value_of_a_variable_or_to_be\.
[^Bueno2010]: @Bueno_2010_A_defense_of_second_order_logic\.
[^Enderton2009]: @Enderton_2009_Second_order_and_higher_order_logic\.
[^Jerzak2009]: @Jerzak_2009_Second_order_logic_or_How_I_learned_to_stop\.
[^Kleene1952]: @Kleene_1952_Introduction_to_Metamathematics\.
[^Russell2015]: @Russell_2015_The_justification_of_the_basic_laws_of_logic\.
[^Shapiro1991]: @Shapiro_1991_Foundations_without_Foundationalism_A_Case\.
[^Sider2022]: @Sider_2022_Crash_course_on_higher_order_logic\.


### Modal logic

-   [C.I. Lewis](https://en.wikipedia.org/wiki/C._I._Lewis) (1883-1964)
    -   Founded modern modal logic.
    -   Criticism of material implication. Introduced strict implication. [^Lewis1917]
    -   Strict implication is not truth-functional. It requires asking
        about the truth-values that propositions take in worlds other than
        the actual world.
-   [Rudolf Carnap](https://en.wikipedia.org/wiki/Rudolf_Carnap) (1891-1970)
    -   Carnap, R. (1947). *Meaning and Necessity*. [^Carnap1947b]
-   [Saul Kripke](https://en.wikipedia.org/wiki/Saul_Kripke) (1940-2022)
    -   Kripke, S.A. (1959). A completeness theorem in modal logic. [^Kripke1959]
    -   Revives Leibniz's idea that necessity is truth in all possible worlds.
-   [David Lewis](https://en.wikipedia.org/wiki/David_Lewis_(philosopher)) (1941-2001)
    -   *On the Plurality of Worlds* (1986) [^Lewis1986]

$\Box$ means "necessarily". $\Diamond$ means "possibly".

If necessarily $P$, then necessarily necessarily $P$:

$$ \Box P \rightarrow \Box \Box P $$

De Morgan duality:

$$ \Diamond P = \lnot \Box \lnot P $$

$$ \Box P = \lnot \Diamond \lnot P $$

More:

-   [Security logic](https://www.johndcook.com/blog/2018/10/30/modal-logic-security/)
-   [*De dicto* and *de_re*](https://en.wikipedia.org/wiki/De_dicto_and_de_re)

[^Carnap1947b]: @Carnap_1947_Meaning_and_Necessity\.
[^Kripke1959]: @Kripke_1959_A_completeness_theorem_in_modal_logic\.
[^Lewis1917]: @Lewis_1917_The_issues_concerning_material_implication\.
[^Lewis1986]: @Lewis_1986_On_the_Plurality_of_Worlds\.


### Alternative logics

-   Liar paradox
    -   Carroll, L. (1895). [What the tortoise said to Achilles](http://www.ditext.com/carroll/tortoise.html). [^Carroll1895]
-   Intuitionistic Logic
    -   Law of excluded middle (LEM), *Tertium non datur*:        
        $\vdash A \lor \lnot A$
    -   Law of double negation (LDN):        
        $\lnot \lnot A \leftrightarrow A$
    -   Intuitionistic logic rejects LEM and LDN.
    -   Constructive mathematics
-   Paraconsistent logic
    -   [Principle of explosion](https://en.wikipedia.org/wiki/Principle_of_explosion)
    -   *Ex contradictione quodlibet* (ECQ): from a contradiction anything follows.         
        $A, \lnot A \models B$
    -   Law of No Contradiction (LNC).            
        $\models \lnot ( A \land \lnot A )$
    -   Paraconsistent logics reject ECQ, and may or may not invalidate LNC.
    -   Dialetheism rejects LNC.
    -   Priest, G. (1998). What is so bad about contradictions? [^Priest1998]
    -   Mart&iacute;nez-Ordaz, M. del R. (2021). The ignorance behind inconsistency toleration. [^MartinezOrdaz2021b]

Criticism:

-   Quine, W.V.O. (1986). *Philosophy of Logic*. [^Quine1986b]

See also:

-   [Intuitionism](#intuitionism)

[^Carroll1895]: @Carroll_1895_What_the_tortoise_said_to_Achilles\.
[^Priest1998]: @Priest_1998_What_is_so_bad_about_contradictions\.
[^Quine1986b]: @Quine_1986_Philosophy_of_Logic\.
[^MartinezOrdaz2021b]: @Martinez_Ordaz_2021_The_ignorance_behind_inconsistency_toleration\.


### Proof theory

-   [Curry-Howard correspondence](https://en.wikipedia.org/wiki/Curry%E2%80%93Howard_correspondence)
-   [Proof-theoretic semantics](https://plato.stanford.edu/entries/proof-theoretic-semantics/)
-   [Realizability](https://en.wikipedia.org/wiki/Realizability)
-   Viteri, S. & DeDeo, S. (2022). [Epistemic phase transitions in mathematical proofs](https://www.sciencedirect.com/science/article/pii/S0010027722001081). [^Viteri2022]

See also:

-   [Category theory](#category-theory)
-   [Complexity theory](#complexity-theory)
-   [Hilbert's program](#hilberts-program)
-   [Logicism](#logicism)
-   [Formalism](#formalism)

[^Viteri2022]: @Viteri_2022_Epistemic_phase_transitions_in_mathematical\.


Model theory
--------------------------------------------------------------------------------

### Introduction

-   Wikipedia: [Model theory](https://en.wikipedia.org/wiki/Model_theory)
-   Hodges: [^Hodges1997pvii]
    -   model theory = universal algebra + logic
    -   model theory = algebraic geometry - fields
-   SEP: [Model theory](https://plato.stanford.edu/entries/model-theory/)
    -   Model theory is the study of the interpretation of any language, formal or natural, by means of set-theoretic structures, with Alfred Tarski's truth definition as a paradigm.

Hunter:

>   *Model theory* is the theory of interpretations of formal languages
>   (a *model* of a formula of a language is an interpretation of the
>   language for which the formula comes out true). [^Hunter1971p6]

Weiss & D'Mello:

>   Model Theory is the part of mathematics which shows how to apply logic
>   to the study of structures in pure mathematics. [^Weiss2015p1]

Pedagogy:

-   Weiss, W. & D'Mello, C. (2015). [*Fundamentals of Model Theory*](https://www.math.toronto.edu/weiss/model_theory.pdf). [^Weiss2015]
-   Button, T. & Walsh, S. (2018). *Philosophy and Model Theory*. [^Button2018]

More:

-   [Model theory](https://ncatlab.org/nlab/show/model+theory) - nLab
-   [Formal epistemology](https://plato.stanford.edu/entries/formal-epistemology/)
-   Makowsky, J.A. (1995). [The impact of model theory on theoretical computer science](https://doi.org/10.1016/S0049-237X(06)80047-9). [^Makowsky1995]

See also:

-   [Formal epistemology](scientific-method.html#formal-epistemology)

[^Button2018]: @Button_2018_Philosophy_and_Model_Theory\.
[^Hodges1997pvii]: @Hodges_1997_A_Shorter_Model_Theory\, p. vii.
[^Hunter1971p6]: @Hunter_1971_Metalogic_An_Introduction_to_the_Metatheory\, p. 6.
[^Makowsky1995]: @Makowsky_1995_The_impact_of_model_theory_on_theoretical_computer\.
[^Weiss2015]: @Weiss_2015_Fundamentals_of_Model_Theory\.
[^Weiss2015p1]: @Weiss_2015_Fundamentals_of_Model_Theory\, p. 1.


### History

-   William Rowan Hamilton (1805-1865)
-   Alfred North Whitehead (1861-1947)
    -   Whitehead, A.N. (1898). *A Treatise on Universal Algebra*.
-   L&ouml;wenheim-Skolem theorem (1915, 1920)
-   Rudolf Carnap (1891-1970)
-   Alfred Tarski (1901-1983)
-   Kurt G&ouml;del (1906-1978)
-   Leon Henkin (1921-2006)
-   Jaakko Hintikka (1929-2015)
-   Wilfrid Hodges (b. 1941)
    -   Hodges, W. (1985). [Truth in a structure](https://www.jstor.org/stable/4545041). [^Hodges1985]

[^Hodges1985]: @Hodges_1985_Truth_in_a_structure\.


### Incompleteness

-   [Kurt G&ouml;del](https://en.wikipedia.org/wiki/Kurt_G%C3%B6del) (1906-1978)
    -   Carnap inspired G&ouml;del to study logic. [^Goldfarb2005]
-   G&ouml;del, K. (1931). &Uuml;ber formal unentscheidbare S&auml;tze der Principia Mathematica und verwandter Systeme, I. [^Godel1931]
-   G&ouml;del, K. (1951). Some basic theorems on the foundations of mathematics and their implications. [^Godel1951]
-   G&ouml;del presented his incompleteness theorems at the
    Second Conference on the Epistemology of the Exact Sciences
    in K&ouml;nigsberg September 5-7, 1930.
    -   von Neumann recognized the importance first.
    -   Carnap had warning of G&ouml;del's results the month before. [^Edmonds2020p96]
-   Goldstein [^Goldstein2005]

Fom the SEP:

>   The first incompleteness theorem states that in any consistent formal
>   system $F$ within which a certain amount of arithmetic can be carried out,
>   there are statements of the language of $F$ which can neither be proved
>   nor disproved in $F$. According to the second incompleteness theorem,
>   such a formal system cannot prove that the system itself is consistent
>   (assuming it is indeed consistent). [^Raatikainen2020]

Related:

-   Tarski's undefinability theorem on the formal undefinability of truth
    -   Tarski, A. (1936). The concept of truth in formalized languages. [^Tarski1936]
    -   Tarski, A. (1969). [Truth and proof](https://web.archive.org/web/20141229081319/http://people.scs.carleton.ca/~bertossi/logic/material/tarski.pdf) [^Tarski1969]
-   Church's proof that Hilbert's Entscheidungsproblem is unsolvable
    -   Church, A. (1936). A note on the Entscheidungsproblem. [^Church1936]
-   Turing's theorem that there is no algorithm to solve the halting problem
    -   Turing, A.M. (1937). On computable numbers, with an application to the Entscheidungsproblem. [^Turing1937]
-   Rice's theorem that all non-trivial semantic properties of programs are undecidable
    -   [Rice's theorem](https://en.wikipedia.org/wiki/Rice%27s_theorem) (1951)

Chaitin:

>   [M]y information-theoretic approach to incompleteness makes incompleteness
>   appear pervasive and natural. This is because algorithmic information theory
>   sometimes enables one to measure the information content of a set of axioms
>   and of a theorem and to deduce that the theorem cannot be obtained from the
>   axioms because it contains too much information.
>   
>   This suggests to me that sometimes to prove more one must assume more, in
>   other words, that sometimes one must put more in to get more out. [^Atiyah1994p182]

More:

-   G&ouml;del was a platonist, a (religious) realist.
-   Armstrong, S. (2012). [Completeness, incompleteness, and what it all means: first versus second order logic](https://www.lesswrong.com/posts/MLqhJ8eDy5smbtGrf/completeness-incompleteness-and-what-it-all-means-first).
-   [Hilbert's program](#hilberts-program) is challenged by incompleteness.
-   Discuss how incompleteness is overblown in overly epistemically defeatist ways.
    -   Seems to indicate that no formal system lacks the full context for _everything_.
        Additional axioms will be appropriate for introducing further contexts.
    -   Franz&eacute;n, T. (2005). *G&ouml;del's Theorem: An incomplete guide to its use and abuse*. [^Franzen2005]
-   Seely, R.A. [G&ouml;del on the net.](http://www.math.mcgill.ca/rags/JAC/124/godel.html)
-   Video: [Veritasium - Math Has a Fatal Flaw](https://www.youtube.com/watch?v=HeQX2HjkcNo)
-   Lloyd, S. (1993). Quantum-mechanical computers and uncomputability. [^Lloyd1993]
-   Cubitt, T., Perez-Garcia, D., & Wolf, M. (2015). Undecidability of the spectral gap. [^Cubitt2015]

Relationship to mind:

-   [Lucas-Penrose Argument about G&ouml;del's Theorem](https://www.iep.utm.edu/lp-argue/) - IEP

See also:

-   [Artificial intelligence](mind.html#artificial-intelligence)
-   [Formalism](#formalism)
-   [Hilbert's program](#hilberts-program)
-   [Incompleteness of second-order logic](#incompleteness-of-second-order-logic)

[^Atiyah1994p182]: @Atiyah_1994_Responses_to_Theoretical_Mathematics_Toward\, p. 182.
[^Church1936]: @Church_1936_A_note_on_the_Entscheidungsproblem\.
[^Cubitt2015]: @Cubitt_2015_Undecidability_of_the_spectral_gap\.
[^Edmonds2020p96]: @Edmonds_2020_The_Murder_of_Professor_Schlick_The_Rise_and_Fall\, p. 96
    and TODO: Carnap's diary.
[^Franzen2005]: @Franzen_2005_Godels_Theorem_An_incomplete_guide_to_its\.
[^Goldfarb2005]: @Goldfarb_2005_On_Godels_way_in_The_influence_of_Rudolf\.
[^Goldstein2005]: @Goldstein_2005_Incompleteness_The_Proof_and_Paradox_of_Kurt\.
[^Lloyd1993]: @Lloyd_1993_Quantum_mechanical_computers_and_uncomputability\.
[^Raatikainen2020]: @Raatikainen_2020_Godels_incompleteness_theorems\.
[^Tarski1936]: @Tarski_1983_The_concept_of_truth_in_formalized_languages\.
[^Tarski1969]: @Tarski_1969_Truth_and_proof\.
[^Turing1937]: @Turing_1937_On_computable_numbers_with_an_application\.


### Complexity theory

-   [Church-Turing thesis](https://en.wikipedia.org/wiki/Church%E2%80%93Turing_thesis)
    -   G&ouml;del-Church-Turing
    -   Ord, T. (2024). [Bounds on the rates of growth and convergence of all physical processes](https://arxiv.org/abs/2410.10928). [^Ord2024]
-   Scott Aaronson's [Complexity Zoo](https://complexityzoo.net/Complexity_Zoo)
-   Aaronson, S. (2011). [Why philosophers should care about computational complexity](https://arxiv.org/abs/1108.1791). [^Aaronson2011]
-   Savage, J.E. (2008). [*Models of Computation: Exploring the Power of Computing*](https://cs.brown.edu/people/jsavage/book/pdfs/ModelsOfComputation.pdf).
-   [Fagin's theorem](https://en.wikipedia.org/wiki/Fagin%27s_theorem)

See also:

-   [Proof theory](#proof-theory)

[^Aaronson2011]: @Aaronson_2011_Why_philosophers_should_care_about_computational\.
[^Ord2024]: @Ord_2024_Bounds_on_the_rates_of_growth_and_convergence\.


Category theory
--------------------------------------------------------------------------------

### Introduction

-   [Category theory](https://ncatlab.org/nlab/show/category+theory) - nLab
-   Eilenberg, S. & MacLane, S. (1945). [General theory of natural equivalences](https://www.ams.org/journals/tran/1945-058-00/S0002-9947-1945-0013131-6/S0002-9947-1945-0013131-6.pdf). [^Eilenberg1945]
-   Rodin, A. (2012). [Axiomatic method and category theory](https://arxiv.org/abs/1210.1478). [^Rodin2012]
-   Spivak, D.I. (2013). [Category theory for scientists](https://arxiv.org/abs/1302.6946). [^Spivak2013b]
-   Fong, B. & Spivak, D.I. (2018). [Seven sketches in compositionality: An invitation to applied category theory](https://arxiv.org/abs/1803.05316). [^Fong2018]
-   Bradley, T.D. (2018). [What is applied category theory?](https://arxiv.org/abs/1809.05923) [^Bradley2018]
-   [Categorical product](https://en.wikipedia.org/wiki/Product_(category_theory))
    -   Cook, J.D. (2016). [Categorical products](https://www.johndcook.com/blog/2016/03/22/categorical-products/).
    -   Zucker, P. (2020). [Computational category theory in python I: Dictionaries for FinSet](https://www.philipzucker.com/computational-category-theory-in-python-i-dictionaries-for-finset/).
    -   Zucker, P. (2020). [Computational category theory in python II: numpy for FinVect](https://www.philipzucker.com/computational-category-theory-in-python-ii-numpy-for-finvect/).
    -   Zucker, P. (2020). [Computational category theory in python III: Monoids, groups, and preorders](https://www.philipzucker.com/computational-category-theory-in-python-3-monoids-groups-and-preorders/).
    -   For the category of abelian groups, the coproduct is the direct sum.
-   Functors
-   [Yoneda lemma](https://en.wikipedia.org/wiki/Yoneda_lemma)
    -   Related to: [Pragmatic maxim](https://en.wikipedia.org/wiki/Pragmatic_maxim), [Identity of indiscernibles](https://en.wikipedia.org/wiki/Identity_of_indiscernibles)
-   Relation to set theory
-   Relation to Russell type theory
-   Univalent foundations
    -   Lawvere, F.W. (1963). [*Functorial Semantics of Algebraic Theories and Some Algebraic Problems in the context of Functorial Semantics of Algebraic Theories*](http://www.tac.mta.ca/tac/reprints/articles/5/tr5abs.html). [^Lawvere1963]
-   Categories are semigroupoids.
-   [Curry-Howard-Lambek correspondence](https://en.wikipedia.org/wiki/Curry%E2%80%93Howard_correspondence#Curry%E2%80%93Howard%E2%80%93Lambek_correspondence)
    -   Three-way isomorphism between intuitionistic logic, typed lambda calculus, and cartesian closed categories

See also:

-   [Univalent foundations](math.html#univalent-foundations)

[^Bradley2018]: @Bradley_2018_What_is_applied_category_theory\.
[^Eilenberg1945]: @Eilenberg_1945_General_theory_of_natural_equivalences\.
[^Fong2018]: @Fong_2018_Seven_sketches_in_compositionality_An_invitation\.
[^Lawvere1963]: @Lawvere_1963_Functorial_Semantics_of_Algebraic_Theories\.
[^Rodin2012]: @Rodin_2012_Axiomatic_method_and_category_theory\.
[^Spivak2013b]: @Spivak_2013_Category_theory_for_scientists\.


### History

-   Samuel Eilenberg (1913-1998) and Saunders Mac Lane (1909-2005)
-   [Alexander Grothendieck](https://en.wikipedia.org/wiki/Alexander_Grothendieck) (1928-2014)
-   [Bill Lawvere](https://en.wikipedia.org/wiki/William_Lawvere) (b. 1937)

Grothendieck:

>   If there is one thing in mathematics that fascinates me more than anything
>   else (and doubtless always has), it is neither "number" nor "size", but
>   always form. And among the thousand-and-one faces whereby form
>   chooses to reveal itself to us, the one that fascinates me more than any
>   other and continues to fascinate me, is the structure hidden in mathematical
>   things. [^Grothendieck]

[^Grothendieck]: TODO


### Homotopy type theory

-   Homotopy type theory (HoTT)
-   [Intuitionistic type theory](https://en.wikipedia.org/wiki/Intuitionistic_type_theory)
    -   Per Martin-L&ouml;f (b. 1942)
-   [Homotopy type theory](https://ncatlab.org/nlab/show/homotopy+type+theory) - nLab
-   [*Homotopy Type Theory: Univalent Foundations of Mathematics*](https://homotopytypetheory.org/book/) (2013)

See also:

-   [Univalent foundations](math.html#univalent-foundations)


### Cobordism hypothesis

-   [Cobordism hypothesis](https://ncatlab.org/nlab/show/cobordism+hypothesis) - nLab
-   Baez, J.C. & Dolan, J. (1995). [Higher‐dimensional algebra and topological quantum field theory](https://arxiv.org/abs/q-alg/9503002). [^Baez1995]
-   Baez, J.C. & Stay, M. (2009). [Physics, topology, logic, and computation: A Rosetta Stone](https://arxiv.org/abs/0903.0340). [^Baez2009a]
-   Lurie, J. (2009). [On the classification of topological field theories](https://arxiv.org/abs/0905.0465).
-   [Jacob Lurie's Home Page](https://www.math.ias.edu/~lurie/)
-   Morton, J. (2013). [Blog on the cobordism hypothesis](https://theoreticalatlas.wordpress.com/2013/04/22/seminar-on-cob-hyp/).

See also:

-   [Topological QFT](physics.html#topological-qft)

[^Baez1995]: @Baez_1995_Higher_dimensional_algebra_and_topological_quantum\.
[^Baez2009a]: @Baez_2009_Physics_topology_logic_and_computation\.


### Topos theory

-   Baez, J. (2021). [Topos theory in a nutshell](https://math.ucr.edu/home/baez/topos.html).


### Applications

-   Univalent foundations
-   Functional programming
-   Language models
    -   Bradley, T.D., Terilla, J., & Vlassopoulos, Y. (2021). [An enriched category theory of language: from syntax to semantics](https://arxiv.org/abs/2106.07890). [^Bradley2021] 

[^Bradley2021]: @Bradley_2021_An_enriched_category_theory_of_language_from\.

See also:

-   [Univalent foundations](math.html#univalent-foundations)


Unification programs
--------------------------------------------------------------------------------

### Introduction

Yanofsky, N.S. (2016). Why mathematics works so well:

>   When you have two distinct fields of mathematics and they are shown to be
>   intimately related in a way that results of one field can be used to get
>   results of another field, you have a type of unification. An example of
>   such unification is monstrous moonshine. This subject describes the
>   shocking connection between the monster group and modular functions.
>   Another example is the Langlands program which connects Galois groups
>   in algebraic number theory to automorphic forms and representation theory
>   of algebraic groups. The Erlangen program can also be seen as a way of
>   unifying different types of geometries using group theory. In all these
>   examples of unifications, there is a function (or an isomorphism) from
>   the domain of discourse of one field to the domain of discourse of another
>   field. The symmetries of one field (the true mathematical statements) will
>   than map to symmetries of the other field. Category theory is an entire
>   branch of mathematics that was created to describe such unifications. The
>   founders of category theory invented a language that was based on algebraic
>   topology, which is a branch of mathematics that unifies algebra and
>   topology. Category theory is now used in many areas to show that seemingly
>   different parts of mathematics (and physics and theoretical computer science)
>   are closely related. [^Aguirre2016p153]

[^Aguirre2016p153]: Yanofsky (2016) In @Aguirre_2016_Trick_Or_Truth_The_mysterious_connection_between\, p. 153.


### Erlangen program

-   [Erlangen program](https://en.wikipedia.org/wiki/Erlangen_program)
-   A program proposed by Felix Klein in 1872 to classify geometries based on their symmetry groups.


### Langlands program

-   [Langlands program](https://en.wikipedia.org/wiki/Langlands_program)
    -   Proposed by Robert Langlands (1967, 1970)
-   [Geometric Langlands correspondence](https://en.wikipedia.org/wiki/Geometric_Langlands_correspondence)
    -   It translates number-theoretic problems into geometric ones.
-   [Fundamental lemma](https://en.wikipedia.org/wiki/Fundamental_lemma_(Langlands_program))
    -   Proved by G&eacute;rard Laumon and Ng&ocirc; B&#7843;o Ch&acirc;u (2010)
-   Endoscopic groups
-   Local Langlands correspondence vs global
-   Frenkel, E. (2005). [Lectures on the Langlands program and conformal field theory](https://arxiv.org/abs/hep-th/0512172). [^Frenkel2005]
-   Gaitsgory, D., Raskin, S., et al. (2024). [Proof of the geometric Langlands conjecture](https://people.mpim-bonn.mpg.de/gaitsgde/GLC/). (May 2024).

[^Frenkel2005]: @Frenkel_2005_Lectures_on_the_Langlands_program_and_conformal\.


### Univalent foundations

-   [Univalent foundations](https://en.wikipedia.org/wiki/Univalent_foundations)
-   Proposed by Vladimir Voevodsky, 2006-2009.
-   Category theory
-   [Introduction to Univalent Foundations of Mathematics with Agda](https://www.cs.bham.ac.uk/~mhe/HoTT-UF-in-Agda-Lecture-Notes/index.html)

See also:

-   [Category theory](#category-theory)
-   [Hilbert's program](#hilberts-program)


Platonism
--------------------------------------------------------------------------------

### Introduction

>   What has been is what will be,              
>   and what has been done is what will be done;              
>   there is nothing new under the sun.              
>   Is there a thing of which it is said,              
>   "See, this is new"?              
>   It has already been,              
>   in the ages before us. [^Ecclesiastes_1_9]

-   Podnieks, K. (1992). [Platonism, intuition, and the nature of mathematics](http://web.archive.org/web/20070819181740/http://www.ltn.lv/~podnieks/gt1.html#twin).

[^Ecclesiastes_1_9]: *Ecclesiastes* 1:9--10 (NRSV).


### Pythagoreanism

-   Radical realism
-   Monism: everything is math.
-   Tegmark, M. (2014). *Our Mathematical Universe*. [^Tegmark2014]

![Bronnikov, F. (1869). Pythagoreans celebrate sunrise. ([Wikimedia](https://commons.wikimedia.org/wiki/File:Bronnikov_gimnpifagoreizev.jpg), 2007).](img/Bronnikov-Pythagoreans-celebrate-sunrise.jpg){#fig:Bronnikov-Pythagoreans-celebrate-sunrise}

[^Tegmark2014]: @Tegmark_2014_Our_Mathematical_Universe\.


### Plato

-   Realist
-   Theory of the forms
-   Dualism: the world and forms?
-   The Academy (387 BCE - 529 CE): "Let no one ignorant of geometry enter"
-   Mathematics is descriptive of a real but trans-empirical realm.
-   Plato perhaps doubts Platonism in *Parmenides*
-   Aristotle on universals

![Detail of *School of Athens* by Raphael (1511), showing Plato and Aristotle
    ([Wikimedia](https://commons.wikimedia.org/wiki/File:%22The_School_of_Athens%22_by_Raffaello_Sanzio_da_Urbino.jpg), 2013).
    ](img/Raphael-School-of-Athens-1511-detail-Plato-Aristotle-mod.jpg){#fig:Raphael-School-of-Athens-1511-detail-Plato-Aristotle}

>   I think you know that the students of geometry, calculation, and the like
>   hypothesize the odd and the even, the various figures, the three kinds of
>   angles, and other things akin to these in each of their investigations,
>   as if they knew them. They make their hypotheses and don't think it
>   necessary to give any account of them, either to themselves or to others,
>   as if they were clear to everyone. And going from these first principles
>   through the remaining steps, they arrive in full agreement.
>
>   I certainly know as much.
>
>   Then you also know that, although they use visible figures and make claims
>   about them, their thought isn't directed to them but to those other
>   things that they are like. They make claims for the sake of the square
>   itself and the diagonal itself, not the diagonal they draw, and similarly
>   with the others. These figures that they make and draw, of which shadows
>   and reflections in water are images, they now in turn use as images,
>   in seeking to see those others themselves that one cannot see except
>   by means of thought. [^RepublicVI510c]

[^RepublicVI510c]: Plato, *Republic VI* 510c, @Cooper_1997_Plato_Complete_works\, p. 1131.

-   [A very platonist math documentary](https://www.youtube.com/watch?v=8gd-gUlBv_s)


### Contemporary platonism

-   Quine's "reluctant platonism"
    -   Indispensability argument
    -   Quine, W.V.O. (1948). On what there is. [^Quine1948b]
    -   distinction between *meaning* and *naming*

>   Whatever we say with the help of names can be said in a language which shuns names
>   altogether. To be assumed as an entity is, purely and simply, to be reckoned as the value of a
>   variable. In terms of the categories of traditional grammar, this amounts roughly to saying that
>   to be is to be in the range of reference of a pronoun. Pronouns are the basic media of
>   reference; nouns might better have been named propronouns. The variables of quantification,
>   'something', 'nothing', 'everything', range over our whole ontology, whatever it may be; and
>   we are convicted of a particular ontological presupposition if, and only if, the alleged
>   presuppositum has to be reckoned among the entities over which our variables range in order
>   to render one of our affirmations true. [^Quine1948p7]

>   a theory is committed to those and only those entities to which the bound variables of the
>   theory must be capable of referring in order that the affirmations made in the theory be
>   true. [^Quine1948p9]

-   Neopythagoreanism: Tegmark. (2008). "The mathmatical universe". [^Tegmark2008]
    -   Mathematical Universe Hypothesis (MUH)
-   Seth Lloyd - the universe is a computer - pythagorean?
-   Clearly Ed Witten is a platonist. Video: [How is mathematics truth and beauty?](https://www.youtube.com/watch?v=O3isFuQ2q2A) *Closer To Truth*.
-   De Cruz, H. (2016). [Numerical cognition and mathematical realism](http://hdl.handle.net/2027/spo.3521354.0016.016). [^DeCruz2016]
-   Carroll, S. (2021). [Mindscape 127: Justin Clarke-Doane on Mathematics, Morality, Objectivity, and Reality](https://www.youtube.com/watch?v=3tvfq8ehHOk).
-   [Abstract object theory](https://en.wikipedia.org/wiki/Abstract_object_theory)
    -   Alexius Meinong (1853-1920)
    -   Ernst Mally (1879-1944)
    -   Edward N. Zalta (b. 1952)
    -   [The Metaphysics Research Lab](https://mally.stanford.edu/index.html) - Stanford, CA
    -   Zalta, E.N. (1983). [*Abstract Objects: An Introduction to Axiomatic Metaphysics*](https://mally.stanford.edu/abstract-objects.pdf). [^Zalta1983]
    -   Zalta, E.N. (2024). [*Principia Logico-Metaphysica*](https://mally.stanford.edu/principia.pdf) (Draft). [^Zalta2024]
-   [Basic formal ontology](https://en.wikipedia.org/wiki/Basic_Formal_Ontology)
    -   Barry Smith (b. 1952)
-   John Conway (1937-2020)
    -   Surreal numbers

[^DeCruz2016]: @DeCruz_2016_Numerical_cognition_and_mathematical_realism\.
[^Quine1948b]: @Quine_1948_On_what_there_is\.
[^Quine1948p7]: @Quine_1948_On_what_there_is\, p. 7.
[^Quine1948p9]: @Quine_1948_On_what_there_is\, p. 9.
[^Tegmark2008]: @Tegmark_2008_The_mathematical_universe\.
[^Zalta1983]: @Zalta_1983_Abstract_Objects_An_Introduction_to_Axiomatic\.
[^Zalta2024]: @Zalta_2024_Principia_Logico_Metaphysica\.


### Visual proofs

![Composite numbers can be arranged into rectangles but prime numbers cannot (source: [Wikimedia](https://en.wikipedia.org/wiki/File:Primes-vs-composites.svg)).](img/primes-vs-composites.png)

![A visual proof that $\sum_{k=1}^{n} k = (n^2+n)/2$.](img/visual-proof-sum-n.jpg)

![A visual proof that $\sum_{k=1}^{\infty} \frac{1}{4^k} = \frac{1}{3}$.](img/visual-proof-geometric-series-sum-to-third.jpg)

![Visualization of the binomial theorem (source: [Wikimedia](https://en.wikipedia.org/wiki/File:Binomial_theorem_visualisation.svg)).](img/Binomial_theorem_visualisation.png)

-   [Proofs without words](https://artofproblemsolving.com/wiki/index.php/Proofs_without_words)

Criticism:

-   3Blue1Brown. (2022). Video: [How to lie using visual proofs](https://www.youtube.com/watch?v=VYQVlVoWoPY).


Nominalism
--------------------------------------------------------------------------------

### Introduction

-   Antirealist


### History

Antisthenes:

>   A horse I can see, but horsehood I cannot see.

-   Plato: "Third Man Argument" in *Parmenides*
-   Medieval nominalism
    -   [Medieval Problem of Universals](https://plato.stanford.edu/entries/universals-medieval/)
    -   [Roscellinus (c. 1050 - c. 1125)](https://en.wikipedia.org/wiki/Roscellinus)
    -   [Ockham, William of (1287-1347)](http://en.wikipedia.org/wiki/William_of_Ockham)
-   Modern nominalism

Bayes:

>   It is not the business of a mathematician to show that a straight line or
>   circle can be drawn, but he tells you what he means by these;
>   and if you understand him, you may proceed further with him; and it would not
>   be to the purpose to object that there is no such thing in nature
>   as a true straight line or perfect circle, for this is none of his
>   concern: he is not inquiring how things are in matter of fact,
>   but supposing things to be in a certain way, what are the consequences
>   to be deduced from them. [^Bayes1736p9]

Johwn Stuart Mill:

>   Nominalists, who, repudiating Universal Substances, held that
>   there is nothing general except names. [^Mill1877]

-   Positivism, Carnap, ESO
-   Goodman & Quine [^Goodman1947]
-   Henkin, L. (1953). [Some notes on nominalism](https://doi.org/10.2307/2266323). [^Henkin1953]
-   Azzouni, J. (2015). Nominalism, the nonexistence of mathematical objects. [^Azzouni2015]

See also:

-   [Natural kinds](naturalism.html#natural-kinds)

[^Azzouni2015]: @Azzouni_2015_Nominalism_the_nonexistence_of_mathematical\.
[^Bayes1736p9]: @Bayes_1736_An_Introduction_to_the_Doctrine_of_Fluxions\, p. 9--10.
[^Goodman1947]: @Goodman_1947_Steps_toward_a_constructive_nominalism\.
[^Goodman1947p105]: @Goodman_1947_Steps_toward_a_constructive_nominalism\, p. 105.
[^Henkin1953]: @Henkin_1953_Some_notes_on_nominalism\.
[^Mill1877]: @Mill_1877_An_Examination_of_Sir_William_Hamiltons\.


### *Science Without Numbers*

Field: Abstract platonic entities, were they to exist, could not
interact causally with the world. [^Field1989p68]

-   Field: *Science Without Numbers* [^Field2016]
-   John Burgess [^Burgess1983]
-   Bueno [^Bueno2013]
-   Chen, E.K. (2018). [The intrinsic structure of quantum mechanics](http://philsci-archive.pitt.edu/15140/). [^Chen2018b]

>   significant in context but naming nothing. [^Goodman1947p105]

[^Bueno2013]: @Bueno_2013_Nominalism_in_the_philosophy_of_mathematics\.
[^Chen2018b]: @Chen_2018_The_intrinsic_structure_of_quantum_mechanics\.
[^Field1989p68]: @Field_1989_Realism_Mathematics_and_Modality\, p. 68. TODO: Get exact quote.
[^Burgess1983]: @Burgess_1983_Why_I_am_not_a_nominalist\.
[^Field2016]: @Field_2016_Science_Without_Numbers\.


Logicism
--------------------------------------------------------------------------------

### Introduction

-   A program to derive all or part of mathematics from logic.
-   Richard Dedekind (1831-1916)
-   Gottlob Frege (1848-1925)
    -   All mathematical structures can be constructed from sets and natural numbers.
    -   Natural numbers can be constructed from sets.
    -   The properties of sets can be reduced to logic. Sets are the extensions of arbitrary conditions.
-   Giuseppe Peano (1858-1932)
-   Bertrand Russell (1872-1970)
-   Alfred North Whitehead (1861-1947)
-   [Ernst Zermelo](https://en.wikipedia.org/wiki/Ernst_Zermelo) (1871-1953)
    -   Sets are _not_ simply the extensions of arbitrary conditions. Some conditions have no corresponding set.
-   Realist
-   Relationship with positivism?
-   Russell, B. (1905). [On denoting](https://www.finophd.eu/wp-content/uploads/2018/11/russell_on_denoting.pdf). [^Russell1905]
-   Russell expresses support for the platonic "universals" [^Russell1912p91]
-   Carnap's logicism
    -   Rudolf Carnap (1931) presents the logicist thesis in two parts: [^Carnap1931]
        1.  The concepts of mathematics can be derived from logical concepts through explicit definitions.
        2.  The theorems of mathematics can be derived from logical axioms through purely logical deduction.
    -   Marschall, B. (2021). [Carnap and Beth on the limits of tolerance](https://doi.org/10.1017/can.2021.16). [^Marschall2021]
    -   Marschall, B. (2022). [Carnap's philosophy of mathematics](https://doi.org/10.1111/phc3.12884). [^Marschall2022]
-   Snapper, E. (1979). [The three crises in mathematics: Logicism, intuitionism and formalism](https://www.maa.org/sites/default/files/pdf/upload_library/22/Allendoerfer/1980/0025570x.di021111.02p0048m.pdf). [^Snapper1979]
-   Shapiro, S. (2000). *Thinking about Mathematics: The Philosophy of Mathematics*. [^Shapiro2000]
-   [Hume's principle](https://en.wikipedia.org/wiki/Hume%27s_principle)
-   [Frege's theorem](https://en.wikipedia.org/wiki/Frege%27s_theorem)

[^Carnap1931]: @Carnap_1983_The_Logicist_foundations_of_mathematics\.
[^Marschall2021]: @Marschall_2021_Carnap_and_Beth_on_the_limits_of_tolerance\.
[^Marschall2022]: @Marschall_2022_Carnaps_philosophy_of_mathematics\.
[^Russell1905]: @Russell_1905_On_denoting\.
[^Russell1912p91]: @Russell_1912_The_Problems_of_Philosophy\, p. 91--118.
[^Shapiro2000]: @Shapiro_2000_Thinking_about_Mathematics_The_Philosophy\.
[^Snapper1979]: @Snapper_1979_The_three_crises_in_mathematics_Logicism\.


### *Principia Mathematica*

-   *Principia Mathematica* (1910)
-   [Alfred North Whitehead](https://en.wikipedia.org/wiki/Alfred_North_Whitehead) (1861-1947)
-   [Bertrand Russell](https://en.wikipedia.org/wiki/Bertrand_Russell) (1872-1970)
-   Russell's Paradox
-   "Failure of PM"


### ZFC

-   ZFC
-   ZFC actually does circumvent Russell's paradox by restricting the
    comprehension axiom to already existing sets by the use of subset axioms.


### Neologicism

-   [Crispin Wright](https://en.wikipedia.org/wiki/Crispin_Wright) (b. 1942)
-   [Bob Hale](https://en.wikipedia.org/wiki/Bob_Hale_(philosopher)) (1945-2017)
-   Linsky, B. & Zalta, E.N. (2006). [What is Neologicism?](http://mally.stanford.edu/Papers/neologicism2.pdf) [^Linsky2006]
-   Linsky, B. & Zalta, E.N. (1995). [Naturalized platonism versus platonized naturalism](https://www.jstor.org/stable/2940786) [^Linsky1995]
-   Leitgeb, H., Nodelman, U., & Zalta, E.N. (2024). [A defense of logicism](https://mally.stanford.edu/Papers/logicism.pdf). [^Leitgeb2024]

Linsky & Zalta:

>   Our knowledge of mathematics is to be explained in terms of the faculty
>   we use to understand language, since that is the only faculty we need to
>   understand object abstraction. [^Linsky2006p43]

[^Leitgeb2024]: @Leitgeb_2024_A_defense_of_logicism\.
[^Linsky1995]: @Linsky_1995_Naturalized_platonism_versus_platonized\.
[^Linsky2006]: @Linsky_2006_What_is_Neologicism\.
[^Linsky2006p43]: @Linsky_2006_What_is_Neologicism\, p. 43.


Formalism
--------------------------------------------------------------------------------

### Introduction

-   Hilbert
-   Antirealist?
-   Michael Hallett

Hilbert:

>   We must know. We shall know.

Hilbert:

>   Mathematics is a presuppositionless science. To found it I do not need God, 
>   as does Kronecker, or the assumption of a special faculty of our understanding 
>   attuned to the principle of mathematical induction, as does Poincar&eacute;, 
>   or the primal intuition of Brouwer, or, finally, as do Russell and Whitehead, 
>   axioms of infinity, reducibility, or completeness, which in fact are actual, 
>   contentual assumptions that cannot be compensated for by consistency
>   proofs. [^Hilbert1967p479]

-   Video: Veritasium - [You can't prove everything that's true](https://www.youtube.com/watch?v=HeQX2HjkcNo)

[^Hilbert1967p479]: @Hilbert_1967_The_foundations_of_mathematics\, p. 479.
    Discussion by [Michael J. O'Donnell](http://people.cs.uchicago.edu/~odonnell/OData/Courses/22C:096/Lecture_notes/Hilbert_program.html):

    >   Well, the tone sounds like hubris again, but this is actually a relatively modest claim, 
    >   and largely substantiated by events. Mathematics may arguably be understood as the 
    >   science of forms, which have an objective quality independent of individual beliefs.
    >   What is missing here is the claim that a single formal system may embrace all of mathematics
    >   at once, and that we may prove that it contains no error. Notice that Hilbert objects to the 
    >   "actual, contentual assumptions" of Russell and Whitehead. 
    >   But, recall that Hilbert claims to treat numerical equations contentually, and even seems 
    >   to regard that as a virtue. It is not the mere contentual quality of Russell's and 
    >   Whitehead's assumptions that Hilbert objects to, but the fact that each particular 
    >   assumptions is not verifiable by a single computation or finite observation, and 
    >   furthermore that there is not even a proof that they are consistent with basic
    >   numerical equations. Of course, Hilbert's proposed system never gets its consistency proof either. 
    >   Oh well.


### Hilbert's program

-   [Hilbert's program](http://en.wikipedia.org/wiki/Hilbert%27s_program)
-   Influenced by *Principia Mathematica*
-   Hilbert, D. (1926). On the infinite. [^Hilbert1926]
-   G&ouml;del derailed the program
-   TODO: What do we expect from proof theory now?

Hilbert wanted math to be

-   Consistent?
-   ~~Decidable~~
-   ~~Complete~~

See also:

-   [Incompleteness](#incompleteness)
-   [Proof theory](#proof-theory)

[^Hilbert1926]: @Hilbert_1926_Uber_das_Unendliche\.


Intuitionism
--------------------------------------------------------------------------------

### Introduction

-   Antirealist
-   Leopold Kronecker's finitism was a forerunner of intuitionism in foundations of mathematics.
-   Kronecker: "God made the integers, all else is the work of man".
-   L.E.J. Brouwer (1881-1966)
    -   Brouwer, L.E.J. (1908). [Unreliability of the logical principles](https://arxiv.org/abs/1511.01113). [^Brouwer1908]
-   Constructive mathematics
-   Gisin, N. (2020). [Indeterminism in physics and intuitionistic mathematics](https://arxiv.org/abs/2011.02348). [^Gisin2020]

See also:

-   [Alternative logics](#alternative-logics)

[^Brouwer1908]: @Brouwer_1908_Unreliability_of_the_logical_principles\.
[^Gisin2020]: @Gisin_2020_Indeterminism_in_physics_and_intuitionistic\.


### Linear logic

-   Girard, J.Y. (1987). [Linear logic](http://girard.perso.math.cnrs.fr/linear.pdf). [^Girard1987]

[^Girard1987]: @Girard_1987_Linear_logic\.


### Criticism

Hilbert: 

>   Taking the Principle of the Excluded Middle from the mathematician ...
>   is the same as ... prohibiting the boxer the use of his fists. [^Reid1996p149]

-   Tait, W.W. (1983). Against intuitionism: Constructive mathematics is part of classical mathematics. [^Tait1983]

[^Reid1996p149]: @Reid_1996_Hilbert\, p. 149.
[^Tait1983]: @Tait_1983_Against_intuitionism_Constructive_mathematics_is\.


Fictionalism
--------------------------------------------------------------------------------

-   Antirealist
-   Stephen Yablo
-   [Chris Bateman interviews Stephen Yablo](https://onlyagame.typepad.com/only_a_game/2011/05/yablo-on-fictionalism.html)


Structuralism
--------------------------------------------------------------------------------

-   Realist
-   Awodey, S. (2014). Structuralism, invariance, and univalence. [^Awodey2014]

[^Awodey2014]: @Awodey_2014_Structuralism_invariance_and_univalence\.


Naturalism
--------------------------------------------------------------------------------

### Unreasonable effectiveness

>   Philosophy is written in that great book which
>   ever lies before our eyes---I mean the
>   Universe---but we cannot understand it if we do
>   not learn the language and grasp the symbols in
>   which it is written. This book is written in the
>   mathematical language, and the symbols are
>   triangles, circles, and other geometrical figures
>   without whose help it is impossible to comprehend
>   a single word of it, without which one wanders in
>   vain through a dark labyrinth.

-- Galileo Galilei. (1623). *Il Saggiatore (The Assayer)*. [^Drake1957p237]

-   Wigner [^Wigner1960]
-   Putnam [^Putnam1975]
-   Hamming [^Hamming1980]
-   Tegmark: MUH
-   Zee: Physics uses simple Lie groups, "Nature is kind" [^Zee2016p564]
-   Dan A. Roberts. (2021). [Why is AI hard and Physics simple?](https://arxiv.org/abs/2104.00008) [^Roberts2021b]
    -   See also: [No free lunch theorems](statistics.html#no-free-lunch-theorems)

[^Drake1957p237]: @Drake_1957_Discoveries_and_Opinions_of_Galileo\, p.237-8.
[^Hamming1980]: @Hamming_1980_The_unreasonable_effectiveness_of_mathematics\.
[^Putnam1975]: @Putnam_1975_What_is_mathematical_truth\.
[^Roberts2021b]: @Roberts_2021_Why_is_AI_hard_and_physics_simple\.
[^Wigner1960]: @Wigner_1960_The_unreasonable_effectiveness_of_mathematics\.
[^Zee2016p564]: @Zee_2016_Group_Theory_in_a_Nutshell_for_Physicists\, p. 564.


### Quine-Putnam indispensability thesis

-   Quine
-   Putnam [^Putnam1975MMM]

Putnam:

>   [Q]uantification over mathematical entities is indispensable for science...;
>   therefore we should accept such quantification; but this commits us to
>   accepting the existence of the mathematical entities in question. [^Putnam1971p57]

[^Putnam1971p57]: @Putnam_1971_Philosophy_of_Logic\, p. 57.
[^Putnam1975MMM]: @Putnam_1975_Mathematics_Matter_and_Method\, p. TODO\.


### Mathematical naturalism
-   Maddy
-   Realist?
-   See the outline on [Naturalism](naturalism.html).


My thoughts
--------------------------------------------------------------------------------

-   What would happen if you asked an alien to solve a Rubik's cube?


Annotated bibliography
--------------------------------------------------------------------------------

<div class="clickmore"><a id="link:annotated_bibliography" class="closed" onclick="toggle_more('annotated_bibliography')">
Click to show annotated bibliography
</a></div>
<div id="annotated_bibliography" class="more">

### Wigner, E.P. (1960). The Unreasonable Effectiveness of Mathematics in the Natural Sciences.

-   @Wigner_1960_The_unreasonable_effectiveness_of_mathematics

#### My thoughts

-   TODO.

--------------------------------------------------------------------------------

### Field, H. (1980). *Science Without Numbers*.

-   @Field_2016_Science_Without_Numbers

#### My thoughts

-   TODO.

--------------------------------------------------------------------------------

### Snapper, E. (1979). The Three Crises in Mathematics: Logicism, Intuitionism, Formalism.

-   @Snapper_1979_The_three_crises_in_mathematics_Logicism

#### My thoughts

-   TODO.

--------------------------------------------------------------------------------

### More articles to do

-   TODO.

</div>


Links and encyclopedia articles
--------------------------------------------------------------------------------

<div class="clickmore"><a id="link:encyclopedia_articles" class="closed" onclick="toggle_more('encyclopedia_articles')">
Click to show links
</a></div>
<div id="encyclopedia_articles" class="more">

### SEP

-   [Algebra](https://plato.stanford.edu/entries/algebra/)
-   [Algebra of logic](https://plato.stanford.edu/entries/algebra-logic-tradition/)
-   [Alternative axiomatic set theories](https://plato.stanford.edu/entries/settheory-alternative/)
-   [Analysis](http://plato.stanford.edu/entries/analysis/)
-   [Analytic/synthetic distinction](http://plato.stanford.edu/entries/analytic-synthetic/)
-   [Ancient logic](https://plato.stanford.edu/entries/logic-ancient/)
-   [Aristotle and mathematics](http://plato.stanford.edu/entries/aristotle-mathematics/)
-   [Automated reasoning](https://plato.stanford.edu/entries/reasoning-automated/)
-   [Boolean algebra, The mathematics of](http://plato.stanford.edu/entries/boolalg-math/)
-   [Bradley's Regress](https://plato.stanford.edu/entries/bradley-regress/)
-   [Brouwer, Luitzen Egbertus Jan (1881-1966)](http://plato.stanford.edu/entries/brouwer/)
-   [Category theory](https://plato.stanford.edu/entries/category-theory/)
-   [Computer science, Philosophy of](https://plato.stanford.edu/entries/computer-science/)
-   [Computer simulations in science](http://plato.stanford.edu/entries/simulations-science/)
-   [Contradiction](https://plato.stanford.edu/entries/contradiction/)
-   [Constructive mathematics](http://plato.stanford.edu/entries/mathematics-constructive/)
-   [Dedekind's contributions to the foundations of mathematics](http://plato.stanford.edu/entries/dedekind-foundations/)
-   [Descartes' mathematics](http://plato.stanford.edu/entries/descartes-mathematics/)
-   [Diagrams](https://plato.stanford.edu/entries/diagrams/)
-   [Dialetheism](https://plato.stanford.edu/entries/dialetheism/)
-   [Emergence of first-order logic](https://plato.stanford.edu/entries/logic-firstorder-emergence/)
-   [Epistemology of visual thinking in mathematics](http://plato.stanford.edu/entries/epistemology-visual-thinking/)
-   [Explanation in mathematics](http://plato.stanford.edu/entries/mathematics-explanation/)
-   [Fictionalism](http://plato.stanford.edu/entries/fictionalism/)
-   [Fictionalism in the philosophy of mathematics](http://plato.stanford.edu/entries/fictionalism-mathematics/)
-   [First-order model theory](https://plato.stanford.edu/entries/modeltheory-fo/)
-   [Formal epistemology](https://plato.stanford.edu/entries/formal-epistemology/)
-   [Frege, Gottlob (1848-1925)](http://plato.stanford.edu/entries/frege/)
-   [Frege-Hilbert controversy](http://plato.stanford.edu/entries/frege-hilbert/)
-   [Frege's theorem and foundations for arithmetic](http://plato.stanford.edu/entries/frege-theorem/)
-   [Formalism in the philosophy of mathematics](http://plato.stanford.edu/entries/formalism-mathematics/)
-   [Game Theory](http://plato.stanford.edu/entries/game-theory/)
-   [G&ouml;del, Kurt (1906-1978)](http://plato.stanford.edu/entries/goedel/)
-   [G&ouml;del's incompleteness theorems](http://plato.stanford.edu/entries/goedel-incompleteness/)
-   [Grosseteste, Robert (ca. 1168-1253)](https://plato.stanford.edu/entries/grosseteste/)
-   [Hilbert's Program](http://plato.stanford.edu/entries/hilbert-program/)
-   [Identity theory of truth](http://plato.stanford.edu/entries/truth-identity/)
-   [Inconsistent tathematics](http://plato.stanford.edu/entries/mathematics-inconsistent/)
-   [Indispensability arguments in the philosophy of mathematics](http://plato.stanford.edu/entries/mathphil-indis/)
-   [Infinity](https://plato.stanford.edu/entries/infinity/)
-   [Intuitionism in the philosophy of mathematics](http://plato.stanford.edu/entries/intuitionism/)
-   [Intuitionistic Logic, Development of](https://plato.stanford.edu/entries/intuitionistic-logic-development/)
-   [Intuitionistic type theory](https://plato.stanford.edu/entries/type-theory-intuitionistic/)
-   [Kant's Philosophy of Mathematics](http://plato.stanford.edu/entries/kant-mathematics/)
-   [Leibniz, Gottfried Wilhelm (1646-1716)](http://plato.stanford.edu/entries/leibniz/)
-   [Liar Paradox](https://plato.stanford.edu/entries/liar-paradox/)
-   [Logicism and Neologicism](http://plato.stanford.edu/entries/logicism/)
-   [Mathematics, Philosophy of](http://plato.stanford.edu/entries/philosophy-mathematics/)
-   [Model theory](http://plato.stanford.edu/entries/model-theory/)
-   [Naturalism in the philosophy of mathematics](http://plato.stanford.edu/entries/naturalism-mathematics/)
-   [Negation](http://plato.stanford.edu/entries/negation/)
-   [Nominalism in metaphysics](http://plato.stanford.edu/entries/nominalism-metaphysics/)
-   [Nominalism in the philosophy of mathematics](http://plato.stanford.edu/entries/nominalism-mathematics/)
-   [Non-deductive methods in mathematics](http://plato.stanford.edu/entries/mathematics-nondeductive/)
-   [Ockham, William of (1287-1347)](https://plato.stanford.edu/entries/ockham/)
-   [Paraconsistent logic](https://plato.stanford.edu/entries/logic-paraconsistent/)
-   [Plato's *Parmenides*](https://plato.stanford.edu/entries/plato-parmenides/)
-   [Platonism in the philosophy of mathematics](http://plato.stanford.edu/entries/platonism-mathematics/)
-   [Platonism in metaphysics](http://plato.stanford.edu/entries/platonism/)
-   [*Principia Mathematica* (1910)](http://plato.stanford.edu/entries/principia-mathematica/)
-   [Proof-theoretic semantics](https://plato.stanford.edu/entries/proof-theoretic-semantics/)
-   [Proof theory](http://plato.stanford.edu/entries/proof-theory-development/)
-   [Pythagoras (570-495 BCE)](https://plato.stanford.edu/entries/pythagoras/)
-   [Pythagoreanism](https://plato.stanford.edu/entries/pythagoreanism/)
-   [Quantifiers and quantification](https://plato.stanford.edu/entries/quantification/)
-   [Quine's New Foundations (NF)](https://plato.stanford.edu/entries/quine-nf/)
-   [Russell, Bertrand (1872-1970)](http://plato.stanford.edu/entries/russell/)
-   [Russell's logical atomism](http://plato.stanford.edu/entries/logical-atomism/)
-   [Russell's Paradox](http://plato.stanford.edu/entries/russell-paradox/)
-   [Second-order and higher-order logic](https://plato.stanford.edu/entries/logic-higher-order/)
-   [Self-reference](https://plato.stanford.edu/entries/self-reference/)
-   [Set theory](https://plato.stanford.edu/entries/set-theory/)
-   [Skolem's Paradox](https://plato.stanford.edu/entries/paradox-skolem/)
-   [Tarski, Alfred (1901-1983)](http://plato.stanford.edu/entries/tarski/)
-   [Tarski's truth definitions](http://plato.stanford.edu/entries/tarski-truth/)
-   [Truth](http://plato.stanford.edu/entries/truth/)
-   [Truth, Axiomatic theories of](http://plato.stanford.edu/entries/truth-axiomatic/)
-   [Truth, Coherence theory of](http://plato.stanford.edu/entries/truth-coherence/)
-   [Truth, Correspondence theory of](http://plato.stanford.edu/entries/truth-correspondence/)
-   [Truth, Deflationary theory of](http://plato.stanford.edu/entries/truth-deflationary/)
-   [Truth, Logical](http://plato.stanford.edu/entries/logical-truth/)
-   [Truth, Pluralist theories of](http://plato.stanford.edu/entries/truth-pluralist/)
-   [Truth, Revision theory of](http://plato.stanford.edu/entries/truth-revision/)
-   [Truth values](http://plato.stanford.edu/entries/truth-values/)
-   [Type theory](http://plato.stanford.edu/entries/type-theory/)
-   [Types and tokens](http://plato.stanford.edu/entries/types-tokens/)
-   [Whitehead, Alfred North (1861-1947)](http://plato.stanford.edu/entries/whitehead/)
-   [Wittgenstein's philosophy of mathematics](http://plato.stanford.edu/entries/wittgenstein-mathematics/)

### IEP

-   [Analytic philosophy](http://www.iep.utm.edu/analytic/)
-   [Applicability of mathematics](http://www.iep.utm.edu/math-app/)
-   [Constructive mathematics](https://iep.utm.edu/con-math/)
-   [Dummett, Michael (1925-2011)](https://iep.utm.edu/dummett/)
-   [Fictionalism in the philosophy of mathematics](http://www.iep.utm.edu/mathfict/)
-   [Frege, Gottlob (1848-1925)](http://www.iep.utm.edu/frege/)
-   [Game theory](http://www.iep.utm.edu/game-th/)
-   [Indispensability argument in the philosophy of mathematics](http://www.iep.utm.edu/indimath/)
-   [Infinite](http://www.iep.utm.edu/infinite/)
-   [Lucas-Penrose argument about G&ouml;del's theorem](https://www.iep.utm.edu/lp-argue/)
-   [Mathematical platonism](http://www.iep.utm.edu/mathplat/)
-   [Mathematical structuralism](http://www.iep.utm.edu/m-struct/)
-   [Modal metaphysics](http://www.iep.utm.edu/mod-meta/)
-   [Models](http://www.iep.utm.edu/models/)
-   [Model-theoretic conceptions of logical consequence](http://www.iep.utm.edu/logcon-m/)
-   [Neo-platonism](http://www.iep.utm.edu/neoplato/)
-   [Plato (428/7 or 424/3 - 348/7 BCE)](http://www.iep.utm.edu/plato/)
-   [Platonism, mathematical](http://www.iep.utm.edu/mathplat/)
-   [Platonism, middle](http://www.iep.utm.edu/midplato/)
-   [Plato's Academy (387 BCE - 529 CE)](http://www.iep.utm.edu/academy/)
-   [Poincar&eacute;, Jules Henri (1854-1912)](http://www.iep.utm.edu/poincare/)
-   [Poincar&eacute;'s philosophy of mathematics](http://www.iep.utm.edu/poi-math/)
-   [Process philosophy](http://www.iep.utm.edu/processp/)
-   [Pythagoras (570-495 BCE)](http://www.iep.utm.edu/pythagor/)
-   [Relational models theory](http://www.iep.utm.edu/r-models/)
-   [Russell's Paradox](http://www.iep.utm.edu/par-russ/)
-   [Universals](http://www.iep.utm.edu/universa/)
-   [Wittgenstein's later philosophy of mathematics](http://www.iep.utm.edu/wittmath/)

### Wikipedia

-   [Affirming the consequent](https://en.wikipedia.org/wiki/Affirming_the_consequent)
-   [Aristotle (384-322 BCE)](http://en.wikipedia.org/wiki/Aristotle)
-   [Begriffsschrift](https://en.wikipedia.org/wiki/Begriffsschrift)
-   [Brouwer, L.E.J. (1881-1966)](https://en.wikipedia.org/wiki/L._E._J._Brouwer)
-   [Cantor, Georg (1845-1918)](https://en.wikipedia.org/wiki/Georg_Cantor)
-   [Category theory](https://en.wikipedia.org/wiki/Category_theory)
-   [Cauchy, Augustin-Louis (1789-1857)](http://en.wikipedia.org/wiki/Augustin-Louis_Cauchy)
-   [Central limit theorem](http://en.wikipedia.org/wiki/Central_limit_theorem)
-   [Classification of finite simple groups](https://en.wikipedia.org/wiki/Classification_of_finite_simple_groups)
-   [Contraposition](https://en.wikipedia.org/wiki/Contraposition)
-   [Continuum hypothesis](http://en.wikipedia.org/wiki/Continuum_hypothesis)
-   [Deduction theorem](https://en.wikipedia.org/wiki/Deduction_theorem)
-   [Deductive reasoning](https://en.wikipedia.org/wiki/Deductive_reasoning)
-   [Diagonal lemma](http://en.wikipedia.org/wiki/Diagonal_lemma)
-   [Erlangen program](https://en.wikipedia.org/wiki/Erlangen_program)
-   [Ethnomathematics](http://en.wikipedia.org/wiki/Ethnomathematics)
-   [Euclid (fl. 300 BCE)](http://en.wikipedia.org/wiki/Euclid)
-   [Euler, Leonhard (1707-1783)](https://en.wikipedia.org/wiki/Leonhard_Euler)
-   [First-order logic](https://en.wikipedia.org/wiki/First-order_logic)
-   [Frege, Gottlob (1848-1925)](http://en.wikipedia.org/wiki/Gottlob_Frege)
-   [Frege's theorem](https://en.wikipedia.org/wiki/Frege%27s_theorem)
-   [Galois, &Eacute;variste (1811-1832))](https://en.wikipedia.org/wiki/%C3%89variste_Galois)
-   [Lie, Sophus (1842-1899)](https://en.wikipedia.org/wiki/Sophus_Lie)
-   [Logicism](https://en.wikipedia.org/wiki/Logicism)
-   [Gauss, Carl Friedrich (1777-1855)](https://en.wikipedia.org/wiki/Carl_Friedrich_Gauss)
-   [Gentzen's consistency proof](http://en.wikipedia.org/wiki/Gentzen%27s_consistency_proof)
-   [G&ouml;del, Kurt (1906-1978)](https://en.wikipedia.org/wiki/Kurt_G%C3%B6del)
-   [G&ouml;del's completeness theorem](https://en.wikipedia.org/wiki/G%C3%B6del%27s_completeness_theorem)
-   [G&ouml;del's incompleteness theorems](http://en.wikipedia.org/wiki/G%C3%B6del%27s_incompleteness_theorems)
-   [Hilbert, David (1862-1943)](https://en.wikipedia.org/wiki/David_Hilbert)
-   [Hilbert's Program](http://en.wikipedia.org/wiki/Hilbert%27s_program)
-   [History of algebra](https://en.wikipedia.org/wiki/History_of_algebra)
-   [Hume's principle](https://en.wikipedia.org/wiki/Hume%27s_principle)
-   [Jacobi, Carl Gustav Jacob (1804-1851)](https://en.wikipedia.org/wiki/Carl_Gustav_Jacob_Jacobi)
-   [Kronecker, Leopold (1823-1891)](https://en.wikipedia.org/wiki/Leopold_Kronecker)
-   [Kripke, Saul (1940-2022)](https://en.wikipedia.org/wiki/Saul_Kripke)
-   [Langlands program](https://en.wikipedia.org/wiki/Langlands_program)
-   [Laplace, Pierre-Simon (1749-1827)](https://en.wikipedia.org/wiki/Pierre-Simon_Laplace)
-   [Law of excluded middle](https://en.wikipedia.org/wiki/Law_of_excluded_middle)
-   [Logic](https://en.wikipedia.org/wiki/Logic)
-   [Logicism](http://en.wikipedia.org/wiki/Logicism)
-   [L&ouml;wenheim-Skolem theorem](https://en.wikipedia.org/wiki/L%C3%B6wenheim%E2%80%93Skolem_theorem)
-   [Mathematical induction](https://en.wikipedia.org/wiki/Mathematical_induction)
-   [Mathematical Universe Hypothesis](http://en.wikipedia.org/wiki/Mathematical_universe_hypothesis)
-   [Metamathematics](https://en.wikipedia.org/wiki/Metamathematics)
-   [Modus ponens](https://en.wikipedia.org/wiki/Modus_ponens)
-   [Modus tollens](https://en.wikipedia.org/wiki/Modus_tollens)
-   [Monster group](https://en.wikipedia.org/wiki/Monster_group)
-   [Monstrous moonshine](https://en.wikipedia.org/wiki/Monstrous_moonshine)
-   [Natural number](http://en.wikipedia.org/wiki/Natural_number)
-   [Newton, Isaac (1642-1726/7)](https://en.wikipedia.org/wiki/Isaac_Newton)
-   [Noether, Emmy (1882-1935)](https://en.wikipedia.org/wiki/Emmy_Noether)
-   [Ockham, William of (1287-1347)](http://en.wikipedia.org/wiki/William_of_Ockham)
-   [Peirce's law](https://en.wikipedia.org/wiki/Peirce%27s_law)
-   [Plato (428/7 or 424/3 - 348/7 BCE)](https://en.wikipedia.org/wiki/Plato)
-   [Platonic Academy (387 BCE - 529 CE)](https://en.wikipedia.org/wiki/Platonic_Academy)
-   [Platonic realism](https://en.wikipedia.org/wiki/Platonic_realism)
-   [Platonism](https://en.wikipedia.org/wiki/Platonism)
-   [Philosophy of mathematics](http://en.wikipedia.org/wiki/Philosophy_of_mathematics)
-   [Problem of universals](https://en.wikipedia.org/wiki/Problem_of_universals)
-   [Proof by contrapositive](https://en.wikipedia.org/wiki/Proof_by_contrapositive)
-   [Proof theory](https://en.wikipedia.org/wiki/Proof_theory)
-   [Propositional calculus](https://en.wikipedia.org/wiki/Propositional_calculus)
-   [*Principia Mathematica* (1910)](https://en.wikipedia.org/wiki/Principia_Mathematica)
-   [Pythagoras (570-495 BCE)](https://en.wikipedia.org/wiki/Pythagoras)
-   [Pythagoreanism](https://en.wikipedia.org/wiki/Pythagoreanism)
-   [Riemann hypothesis](https://en.wikipedia.org/wiki/Riemann_hypothesis)
-   [Rule of inference](https://en.wikipedia.org/wiki/Rule_of_inference)
-   [Russell, Bertrand (1872-1970)](http://en.wikipedia.org/wiki/Bertrand_Russell)
-   [Russell's paradox](https://en.wikipedia.org/wiki/Russell%27s_paradox)
-   [Second-order logic](https://en.wikipedia.org/wiki/Second-order_logic)
-   [Square of opposition](https://en.wikipedia.org/wiki/Square_of_opposition)
-   [Sporadic group](https://en.wikipedia.org/wiki/Sporadic_group)
-   [Stokes, George (1819-1903)](https://en.wikipedia.org/wiki/Sir_George_Stokes,_1st_Baronet)
-   [Tarski, Alfred (1901-1983)](https://en.wikipedia.org/wiki/Alfred_Tarski)
-   [Tarski's undefinability theorem](https://en.wikipedia.org/wiki/Tarski%27s_undefinability_theorem)
-   [Third man argument](https://en.wikipedia.org/wiki/Third_man_argument)
-   [Transfinite induction](https://en.wikipedia.org/wiki/Transfinite_induction)
-   [Type theory](https://en.wikipedia.org/wiki/Type_theory)
-   [Unsolved problems in information theory, List of](http://en.wikipedia.org/wiki/List_of_unsolved_problems_in_information_theory)
-   [Unsolved problems in linquistics, List of](http://en.wikipedia.org/wiki/List_of_unsolved_problems_in_linguistics)
-   [Unsolved problems in mathematics, List of](http://en.wikipedia.org/wiki/List_of_unsolved_problems_in_mathematics)
-   [von Neumann, John (1903-1957)](https://en.wikipedia.org/wiki/John_von_Neumann)
-   [Weierstrass, Karl (1815-1897)](https://en.wikipedia.org/wiki/Karl_Weierstrass)
-   [When a white horse is not a horse](https://en.wikipedia.org/wiki/When_a_white_horse_is_not_a_horse)
-   [Whitehead, Alfred North (1861-1947)](https://en.wikipedia.org/wiki/Alfred_North_Whitehead)
-   [Wittgenstein's philosophy of mathematics](https://en.wikipedia.org/wiki/Ludwig_Wittgenstein%27s_philosophy_of_mathematics)
-   [Zeroth-order logic](https://en.wikipedia.org/wiki/Zeroth-order_logic)
-   [Zermelo, Ernst (1871-1953)](https://en.wikipedia.org/wiki/Ernst_Zermelo)
-   [Zermelo-Fraenkel set theory (ZFC)](https://en.wikipedia.org/wiki/Zermelo%E2%80%93Fraenkel_set_theory)
-   [ZFC, List of statements independent of](https://en.wikipedia.org/wiki/List_of_statements_independent_of_ZFC)

### Others

-   [Math Pages](https://www.mathpages.com/)
-   [Model theory](https://ncatlab.org/nlab/show/model+theory) - nLab
-   [ZFC](https://ncatlab.org/nlab/show/ZFC) - nLab
-   Smith, Peter. (2006-2016). [Logic Matters](http://www.logicmatters.net/).
-   Pigliucci, Massimo. (2015). [Smolin on mathematics](https://scientiasalon.wordpress.com/2015/04/21/smolin-on-mathematics/).
-   Zach, Richard. (2015). [Quine's Paradox and G&ouml;del's Theorem](http://richardzach.org/2015/03/30/quines-paradox-and-godels-theorem/).
-   Baez, J.C. (2018). [Nonstandard Integers as Complex Numbers](https://johncarlosbaez.wordpress.com/2018/03/03/nonstandard-integers-as-complex-numbers/).
-   Baez, J.C. (2018). [Insanely Long Proofs](https://johncarlosbaez.wordpress.com/2012/10/19/insanely-long-proofs/).
-   Schwichtenberg, J. (XXXX). [Classification of Simple Lie Groups](http://jakobschwichtenberg.com/classification-of-simple-lie-groups/).
-   Tao, T. (2019). [Career advice](https://terrytao.wordpress.com/career-advice/).
-   Trioni, S. (2020). [Cantor's attic](https://neugierde.github.io/cantors-attic/).

### Videos

-   [The Limits of Understanding](https://www.youtube.com/watch?v=DfY-DRsE86s)
    -   Gregory Chaitin, Mario Livio, Marvin Minsky, Rebecca Newberger Goldstein
    -   June 4, 2010
-   [A very platonist math documentary](https://www.youtube.com/watch?v=8gd-gUlBv_s)

</div>

<!-- REFERENCES -->

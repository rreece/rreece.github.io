Language models and Wittgenstein
===============================================================================

*September 1, 2022*


<!-- PAGETOC -->


Introduction
-------------------------------------------------------------------------------

-   OpenAI. (2022). [ChatGPT: Optimizing Language Models for Dialogue](https://openai.com/blog/chatgpt).
-   OpenAI. (2023). [GPT-4](https://openai.com/research/gpt-4).


Questions of meaning
-------------------------------------------------------------------------------

-   Intension vs extension
-   Syntax vs semantics
-   Putnam, H. (1973). Meaning and reference. [^Putnam1973]
-   Putnam, H. (1975). The meaning of "meaning". [^Putnam1975]

[^Putnam1973]: @Putnam_1973_Meaning_and_reference\.
[^Putnam1975]: @Putnam_1975_The_meaning_of_meaning\.


Wittgenstein's evolution
-------------------------------------------------------------------------------

### Background

-   The Vienna Circle
-   Edmonds [^Edmonds2020]
-   *Tractatus Logico-Philosophicus* (1922) [^Tractatus]
-   *Philosophical Investigations* (1953) [^PhilosophicalInvestigations]

[^Edmonds2020]: @Edmonds_2020_The_Murder_of_Professor_Schlick_The_Rise_and_Fall\.
[^PhilosophicalInvestigations]: @Wittgenstein_2009_Philosophical_Investigations\.
[^Tractatus]: @Wittgenstein_1961_Tractatus_Logico_Philosophicus\.


### The picture theory of meaning

-   *Tractatus Logico-Philosophicus* (1922) [^Wittgenstein1961pTODO]
-   The picture theory of meaning is a correspondence theory of truth.
-   [philosophy-in-figures/picture-theory-of-meaning-wittgenstein](https://philosophy-in-figures.tumblr.com/post/179388014391/picture-theory-of-meaning-wittgenstein)
-   Daitz, E. (1953). [The picture theory of meaning](https://www.jstor.org/stable/2251383). [^Daitz1953]
-   Keyt, D. (1964). [Wittgenstein's picture theory of language](https://www.jstor.org/stable/2183303). [^Keyt1964]
-   Gaskin, R. (2009). [Realism and the picture theory of meaning](https://www.jstor.org/stable/43154543). [^Gaskin2009]

[^Wittgenstein1961pTODO]: @Wittgenstein_1961_Tractatus_Logico_Philosophicus\, p. TODO
[^Daitz1953]: @Daitz_1953_The_picture_theory_of_meaning\.
[^Keyt1964]: @Keyt_1964_Wittgensteins_picture_theory_of_language\.
[^Gaskin2009]: @Gaskin_2009_Realism_and_the_picture_theory_of_meaning\.


### Meaning as use

-   *Philosophical Investigations* (1953)
-   The theory of meaning as use is a coherence theory of truth.
-   Carnap
    -   Principle of tolerance
-   Firth
    -   Firth, J.R. (1957): "You shall know a word by the company it keeps." [^Firth1957]

Wittgenstein in *PI*:

>   The meaning of a word is its use in the language. [^Wittgenstein2009Sec43]

and

>   One cannot guess how a word functions.
>   One has to look at its use, and learn from that. [^Wittgenstein2009Sec340]

[^Firth1957]: @Firth_1957_A_synopsis_of_linguistic_theory_1930_1955\.
[^Wittgenstein2009Sec43]: @Wittgenstein_2009_Philosophical_Investigations\, &sect;43.
[^Wittgenstein2009Sec340]: @Wittgenstein_2009_Philosophical_Investigations\, &sect;340.


Word meanings in deep learning
-------------------------------------------------------------------------------

### Word embeddings

![Left panel shows vector offsets for three word
    pairs illustrating the gender relation. Right panel shows
    a different projection, and the singular/plural relation for
    two words. In high-dimensional space, multiple relations
    can be embedded for a single word
    [@Mikolov_2013_Linguistic_regularities_in_continuous_space_word].
    ](img/word2vec-king-queen.png){#fig:word2vec-king-queen}

-   Mikolov: word2vec [^Mikolov2013]
    -   Word (token) embeddings
-   Olah, C. (2014). [Deep learning, NLP, and representations](https://colah.github.io/posts/2014-07-NLP-RNNs-Representations/).
-   Alammar, J. (2019). [The illustrated word2vec](https://jalammar.github.io/illustrated-word2vec/).
-   Migdal, P. (2017). [king - man + woman is queen; but why?](https://p.migdal.pl/2017/01/06/king-man-woman-queen-why.html)
-   Discussion of relations captured by word2vec by [The Gradient](https://thegradient.pub/nlp-imagenet/)
-   Perone, C.S. (2018). [NLP word representations and the Wittgenstein philosophy of language](http://blog.christianperone.com/2018/05/nlp-word-representations-and-the-wittgenstein-philosophy-of-language/). [^Perone2018]


[^Mikolov2013]: @Mikolov_2013_Efficient_estimation_of_word_representations\,
    @Mikolov_2013_Linguistic_regularities_in_continuous_space_word\, and
    @Mikolov_2013_Distributed_representations_of_words_and_phrases\.
[^Perone2018]: @Perone_2018_NLP_word_representations_and_the_Wittgenstein\.


### Transformers

![Meme about the fame of the transformer network architecture (source: [&commat;mishig25](https://twitter.com/mishig25/status/1549859201207484417)).](img/transformer-as-a-famous-painting.jpg){#fig:transformer-as-a-famous-painting}

-   Transformer [^Vaswani2017]
-   Positional encodings
-   Self-attention

[^Vaswani2017]: @Vaswani_2017_Attention_is_all_you_need\.


### Generative language modeling

-   Generative execution of next-token prediction with language models
-   GPT
-   Wolfram, S. (2023). [What is ChatGPT doing---and why does it work?](https://writings.stephenwolfram.com/2023/02/what-is-chatgpt-doing-and-why-does-it-work/) [^Wolfram2023]

[^Wolfram2023]: @Wolfram_2023_What_is_ChatGPT_doing_and_why_does_it_work\.


### Discussion

-   Belloni, M. (2019). [Neural networks and philosophy of language: Why Wittgenstein’s theories are the basis of all modern NLP](https://towardsdatascience.com/neural-networks-and-philosophy-of-language-31c34c0796da).
-   Goldhill, O. (2019). [Google Translate is a manifestation of Wittgenstein’s theory of language](https://qz.com/1549212/google-translate-is-a-manifestation-of-wittgensteins-theory-of-language).
-   Skelac, I. & Jandric, A. (2020). Meaning as use: From Wittgenstein to Google’s Word2vec. [^Skelac2020]
-   Boccelli, D. (2022). [Word embeddings align with Kandinsky’s theory of color](https://towardsdatascience.com/word-embeddings-align-with-kandinskys-theory-of-color-26288b864834).
-   [Tweet by Joscha Bach, Mar 25, 2023](https://twitter.com/Plinz/status/1639629419881873410)

Piantadosi:

>   Modern large language models integrate syntax and semantics in the underlying
>   representations: encoding words as vectors in a high-dimensional space,
>   without an effort to separate out e.g. part of speech categories from semantic
>   representations, or even predict at any level of analysis other than the literal
>   word. Part of making these models work well was in determining how to encode
>   semantic properties into vectors, and in fact initializing word vectors via
>   encodings of distribution semantics from e.g. Mikolov et al. 2013 (Radford et al. 2019).
>   Thus, an assumption of the autonomy of syntax is not required to make models
>   that predict syntactic material and may well hinder it. [^Piantadosi2023p15]

[^Piantadosi2023p15]: @Piantadosi_2023_Modern_language_models_refute_Chomskys_approach\, p. 15.
[^Skelac2020]: @Skelac_2020_Meaning_as_use_From_Wittgenstein_to_Googles\.


Conclusion
-------------------------------------------------------------------------------

Bender & Lascarides:

>   While machine learning has made impressive progress
>   on many separate tasks (given appropriately curated data sets), the keys to generalizing beyond
>   any specific set of end-to-end systems lie in modeling the linguistic system itself such that that
>   model can be reused across tasks. And this can only be done based on an understanding of how
>   language works, including how sentences come to mean what they mean (semantics) and how
>   speakers can use sentence meaning to convey communicative intent (pragmatics). [^Bender2020]

TODO: Not acknowledging the evidence.

TODO: Fallacy of moving the goalposts.

-   A surprising amount about the world can be learned from simply predicting what will come next in written language.
-   What do words mean?
-   LLMs can be seen as a vindication of the later Wittgenstein theory of meaning as use.
-   On the other hand, the division between syntax and semantics is porous.
-   That true structural relations can be found in language alone supports a view of accurate correspondence,
    something like the picture theory of meaning.
-   Structural realism
-   Both of Wittgenstein's views remain relevant.

[^Bender2020]: @Bender_2020_Linguistic_Fundamentals_for_Natural_Language\.


<!-- REFERENCES -->

# Language_Predictor_ML_NLP
Click below to checkout the website of this ml model

 
#To run code: streamlit run app.py

Check out the hosted website [here👉](https://www.example.com).


## Introduction

This project uses Natural Language Processing (NLP) techniques to analyze text data. In NLP, we often need to convert text data into numerical form so that it can be processed by machine learning algorithms. 

## TfidfVectorizer

The `TfidfVectorizer` method helps us to achieve this by generating a numerical representation of each text document based on the frequency of each term and how often it appears in each document compared to its frequency in the entire corpus.

The `ngram_range` parameter in `TfidfVectorizer` specifies the range of n-grams to be considered. An n-gram is a contiguous sequence of n items from a given sample of text or speech. By default, `TfidfVectorizer` uses a unigram approach, but specifying `ngram_range=(1,2)` means that both unigrams and bigrams will be considered.

The `analyzer` parameter in `TfidfVectorizer` specifies the type of analysis to be performed. By setting `analyzer='char'`, the vectorizer will generate character-level n-grams instead of word-level n-grams.

Using `TfidfVectorizer` from the `feature_extraction.text` module in the `scikit-learn` library, we can generate numerical representations of text data based on term frequency and inverse document frequency. By specifying `ngram_range=(1,2)` and `analyzer='char'`, we can consider both unigrams and bigrams at the character level.

## Examples

Here are some examples of how to use the `TfidfVectorizer` method in Python:


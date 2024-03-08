# Language_Predictor_ML_NLP



 ## huggingface
Check out the hosted website [here👉](https://vishal815-language-predictor-ml-nlp-app-dqjsvm.streamlit.app/).

## rander server
Check out the hosted website [here👉](https://huggingface.co/spaces/Visal9252/Languagepredictormlnlp)


![Screenshot 2023-04-21 022042](https://github.com/vishal815/Language_Predictor_ML_NLP/assets/83393190/1a9180f0-92fb-4b18-80fc-9664bd3a406d)

#To run code: streamlit run app.py



## TfidfVectorizer

The `TfidfVectorizer` method helps us to achieve this by generating a numerical representation of each text document based on the frequency of each term and how often it appears in each document compared to its frequency in the entire corpus.

The `ngram_range` parameter in `TfidfVectorizer` specifies the range of n-grams to be considered. An n-gram is a contiguous sequence of n items from a given sample of text or speech. By default, `TfidfVectorizer` uses a unigram approach, but specifying `ngram_range=(1,2)` means that both unigrams and bigrams will be considered.

The `analyzer` parameter in `TfidfVectorizer` specifies the type of analysis to be performed. By setting `analyzer='char'`, the vectorizer will generate character-level n-grams instead of word-level n-grams.

Using `TfidfVectorizer` from the `feature_extraction.text` module in the `scikit-learn` library, we can generate numerical representations of text data based on term frequency and inverse document frequency. By specifying `ngram_range=(1,2)` and `analyzer='char'`, we can consider both unigrams and bigrams at the character level.




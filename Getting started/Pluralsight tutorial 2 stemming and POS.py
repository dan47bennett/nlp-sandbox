from nltk.tokenize import word_tokenize, sent_tokenize as sentence_tokenize
from nltk.corpus import stopwords as stopWords
from string import punctuation

#stemming
text = "Mary closed on closing night when she in the mood to close"
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
stemmedWords = [stemmer.stem(word) for word in word_tokenize(text)]
print(stemmedWords)

#part of speech tagging
print(nltk.pos_tag(word_tokenize(text)))
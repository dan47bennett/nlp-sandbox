# tokenising the text
from nltk.tokenize import word_tokenize, sent_tokenize as sentence_tokenize
text = "Mary had a little lamb. Her fleece was white as snow"
sentences = sentence_tokenize(text)
words = [word_tokenize(sentence) for sentence in sentences] # seemingly this is not used below


# remove stopwords
from nltk.corpus import stopwords as stopWords
from string import punctuation
customStopWords = customStopWords = set(stopWords.words('english') + list(punctuation))

# remove stopwords from the text
wordsNoStopWords = [word for word in word_tokenize(text) if word not in customStopWords]

# find bigrams
from nltk.collocations import *
bigrams_measures = nltk.collocations.BigramAssocMeasures()
BCfinder = BigramCollocationFinder.from_words(wordsNoStopWords)

print(sorted(BCfinder.ngram_fd.items())) #all the bigrams and their frequencies
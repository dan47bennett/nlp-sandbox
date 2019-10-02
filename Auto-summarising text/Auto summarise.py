import urllib2
from bs4 import BeautifulSoup
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()


# retrieve text
def getTextWaPo(url):
    page=urllib2.urlopen(url).read().decode('utf8','ignore')
    soup = BeautifulSoup(page,"lxml")
    text = ' '.join(map(lambda p: p.text, soup.find_all('article')))  #cut each article part out of html and add to a single string
    return text.encode('ascii',errors='replace').replace("?"," ")

articleURL = "https://www.washingtonpost.com/news/the-switch/wp/2016/10/18/the-pentagons-massive-new-telescope-is-designed-to-track-space-junk-and-watch-out-for-killer-asteroids/"

text = getTextWaPo(articleURL)


# preprocess the text
from nltk.tokenize import sent_tokenize as sentence_tokenize, word_tokenize
from nltk.corpus import stopwords as stopWords
from string import punctuation

sentences = sentence_tokenize(text) #list of the sentences

words = word_tokenize(text.lower()) #list of all the words in the article

customStopWords = customStopWords = set(stopWords.words('english') + list(punctuation))
wordsNoStopWords = [word for word in words if word not in customStopWords]              #all non filler words



stemmedWords = [stemmer.stem(word) for word in wordsNoStopWords]


# process words
from nltk.probability import FreqDist
frequency = FreqDist(stemmedWords)


from heapq import nlargest

from collections import defaultdict

ranking = defaultdict(int)


#count score for each sentence
for i,sentence in enumerate(sentences):
    for j in word_tokenize(sentence.lower()):
        stemmedWord=stemmer.stem(j)
        if stemmedWord in frequency:
            ranking[i] += frequency[stemmedWord]


sentenceIndices = nlargest(4, ranking, key=ranking.get)

print([sentences[k] for k in sorted(sentenceIndices)])
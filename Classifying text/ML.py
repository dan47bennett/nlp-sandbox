with open('posts.txt', 'r') as postsFile:
    posts = postsFile.readlines()

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(max_df = 0.5, min_df = 2, stop_words='english')
postsVectors = vectorizer.fit_transform(posts)

from sklearn.cluster import KMeans
km = KMeans(n_clusters = 3, init = 'k-means++', max_iter = 100, n_init = 1, verbose = True)


km.fit(postsVectors)


import numpy
print(numpy.unique(km.labels_, return_counts = True))

text = {}
for i,cluster in enumerate(km.labels_):
    oneDocument = posts[i]
    if cluster not in text.keys():
        text[cluster] = oneDocument
    else:
        text[cluster] += oneDocument


from nltk.tokenize import sent_tokenize as sentence_tokenize, word_tokenize
from nltk.corpus import stopwords as stopWords
from string import punctuation
from nltk.probability import FreqDist
from heapq import nlargest
from collections import defaultdict
import nltk

completeStopWords = set(stopWords.words('english') + list(punctuation) + ["million","billion","year","millions","billions","y/y","'s","''"])


keyWords = {}
counts = {}
for cluster in range(3):
    allWords = word_tokenize(text[cluster].lower())
    allWords = [word for word in allWords if word not in completeStopWords]
    freq = FreqDist(allWords)
    keyWords[cluster] = nlargest(100, freq, key = freq.get)
    counts[cluster] = freq

uniqueKeys = {}
for cluster in range(3):
    otherClustersWords = list(set(range(3)) - set([cluster]))
    otherClustersKeyWords = set(keyWords[otherClustersWords[0]]).union(set(keyWords[otherClustersWords[1]]))    #only works with 3 clusters
    uniqueWords = set(keyWords[cluster]) - otherClustersKeyWords
    uniqueKeys[cluster] = nlargest(10, uniqueWords,key = counts[cluster].get)

print(uniqueKeys)

article="Newly-minted unicorn Quora has even bigger ambitions than text questions-and-answers. And it’s not going to let video giants or startups disrupt its future. This week Quora began testing video answers, because sometimes it’s a lot easier to show someone how something works, the best way to complete a task, or why one thing is better than another than try to write it out for them. Users in the beta group will be able to record videos on iOS or Android as supplements or complete answers that everyone on Quora can watch. It’s considering allowing video uploads, which might offer more polished content but increase spam concerns. Previously, Quora only let users answer with text, natively hosted photos, links, and embedded videos from platforms like YouTube. Now it’s actively hosting and soliciting video uploads. Quora’s entry into the space could box out younger competitors like Justin Kan’s mobile video Q&A app Whale, and video Ask Me Anything app Yam. These apps are focused entirely on simplifying the process of recording video answers to questions with features like filters to make you look better, and both give creators ways to earn money. But Quora’s 190 million users, $226 million in funding, and 8-year head start give it a big edge. It’s been cautiously curating a network of experts and content, while building a brand name known for quality in contrast to its predecessor Yahoo Answers. Its network effect may be tough to break."

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=20)
classifier.fit(postsVectors,km.labels_)

test = vectorizer.transform([article.decode('utf8').encode('ascii',errors='ignore')])

print(classifier.predict(test))
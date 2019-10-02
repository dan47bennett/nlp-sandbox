from nltk.tokenize import word_tokenize, sent_tokenize as sentence_tokenize

#word definitions
from nltk.corpus import wordnet
for synset in wordnet.synsets('bass'):
    synset,synset.definition()


#understand word meaning in the context of the sentence
from nltk.wsd import lesk

#context 1
text1 = 'Sing in a lower tone, along with the bass'
interpretation1 = lesk(word_tokenize(text1), 'bass')
print('Interpretation of "bass" in the following sentence. "' + text1 + '"')
print(interpretation1, interpretation1.definition())

#context 2
text2 = 'This sea bass was really hard to catch'
interpretation2 = lesk(word_tokenize(text2), 'bass')
print('Interpretation of "bass" in the following sentence. "' + text2 + '"')
print(interpretation2, interpretation2.definition())

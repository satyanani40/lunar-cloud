import nltk
from nltk.corpus import wordnet
import hashlib
from nltk.stem.wordnet import WordNetLemmatizer

def extract_keywords(sentence):
    tokens = nltk.tokenize.word_tokenize(sentence)
    word_tags = nltk.pos_tag(tokens)
    keywords=filter(lambda x:'NN' in x[1] or 'VB' in x[1],word_tags)
    return keywords

def similar_words(word):
    l=wordnet.synsets(word)
    wordlist=set()
    for i in l:
        for j in i.lemma_names:
            wordlist.add(j)
    return wordlist

def parse_sentence(sentence):
    keywords = extract_keywords(sentence)
    related_words = set()
    for keyword in keywords:
        sim_words = similar_words(keyword[0])
        for i in sim_words:
            related_words.add(i)
    return related_words

def get_singular_sentence(sentence):
    lmtzr = WordNetLemmatizer()
    keywords = extract_keywords(sentence.lower())
    singular_words = []
    for keyword in keywords:
        if (lmtzr.lemmatize(keyword[0])):
            singular_words.append(lmtzr.lemmatize(keyword[0]))
        else:
            singular_words.append(keyword[0])

    return ' '.join(singular_words)


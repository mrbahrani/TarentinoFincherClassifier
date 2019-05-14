import nltk
from nltk.corpus import stopwords
nltk.download("stopwords")


def stop_word_remove(dictionary):
    for s in set(stopwords.words("english")):
        if s in dictionary.keys():
            dictionary.pop(s)
    return dictionary
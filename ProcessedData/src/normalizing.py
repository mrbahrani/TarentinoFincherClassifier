from nltk.tokenize.punkt import PunktSentenceTokenizer
from stemming.porter2 import stem
import string

def tokenize(text):
    text = text.lower()
    #remove punctuation
    for p in string.punctuation.replace("'", "♪").replace("`", ""):
        text = text.replace(p,"")
    text = text.replace("n't", " not").replace("'m", " am").replace("'ve", " have").replace("'re", " are")
    return text.split()


def normalize(text_list, bag_of_words:dict):
    for word in text_list:
        if word in bag_of_words.keys():
            bag_of_words[word] += 1
        else:
            bag_of_words[word] = 1
    return bag_of_words


if __name__ == "__main__":
    bg = dict()
    print(normalize(tokenize("dont ali don't."), bg))
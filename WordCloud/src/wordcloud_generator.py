import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
from ProcessedData.src.normalizing import normalize,tokenize
from Data.src import datacleaning
from os import walk,curdir, path

def create_wordcloud(dictionary, image=None, name="0.jpg",):
    wordcloud = WordCloud().generate_from_frequencies(dictionary)
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.savefig(name)
    plt.show()


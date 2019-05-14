from ProcessedData.src.normalizing import tokenize, normalize
from ProcessedData.src.dictionary_subtraction import subtract_dictionary_frequency
import ProcessedData.src.stom_word_removing as stop
import pickle
from os import walk

if __name__ == "__main__":
    full_tarentino = dict()
    full_fincher = dict()
    subtracted_tarentino = dict()
    subtracted_fincher = dict()
    full_tarentino_s = dict()
    full_fincher_s = dict()
    subtracted_tarentino_s = dict()
    subtracted_fincher_s = dict()

    tar_list = list()
    for r, d, f in walk("../../Data/label1/"):
        for file in f:
            if ".txt" in file:
                tar_list.append(file)

    for tar_film in tar_list:
        bag_list = tokenize(open("../../Data/label1/"+tar_film,"r", encoding=None).read())
        full_tarentino = normalize(bag_list, full_tarentino)

    finch_list = list()
    for r, d, f in walk("../../Data/label2/"):
        for file in f:
            if ".txt" in file:
                finch_list.append(file)

    for finch_film in finch_list:
        bag_list = tokenize(open("../../Data/label2/" + finch_film, "r", encoding=None).read())
        full_fincher = normalize(bag_list, full_fincher)

    subtracted_tarentino = subtract_dictionary_frequency(full_tarentino, full_fincher)
    subtracted_fincher = subtract_dictionary_frequency(full_fincher, full_tarentino)

    full_tarentino_s = stop.stop_word_remove(full_tarentino.copy())
    full_fincher_s = stop.stop_word_remove(full_fincher.copy())
    subtracted_tarentino_s = stop.stop_word_remove(subtracted_tarentino.copy())
    subtracted_fincher_s = stop.stop_word_remove(subtracted_fincher.copy())

    pickle.dump(full_tarentino, open("../../WordCloud/src/pickles/1.p", "wb"))
    pickle.dump(full_fincher, open("../../WordCloud/src/pickles/2.p", "wb"))
    pickle.dump(subtracted_tarentino, open("../../WordCloud/src/pickles/3.p", "wb"))
    pickle.dump(subtracted_fincher, open("../../WordCloud/src/pickles/4.p", "wb"))
    pickle.dump(full_tarentino_s, open("../../WordCloud/src/pickles/5.p", "wb"))
    pickle.dump(full_fincher_s, open("../../WordCloud/src/pickles/6.p", "wb"))
    print("sob", subtracted_tarentino_s)
    pickle.dump(subtracted_tarentino_s, open("../../WordCloud/src/pickles/7.p", "wb"))
    pickle.dump(subtracted_fincher_s, open("../../WordCloud/src/pickles/8.p", "wb"))
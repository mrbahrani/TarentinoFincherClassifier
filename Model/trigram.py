from Model.unigram import UnigramModel
from Model.bigram import BigramModel
import math
import numpy as np


class TrigramModel:
    def __init__(self, train_file, test_file):
        self.trained = False
        self.train_file = train_file
        self.test_file = test_file
        self.model_dict = dict()
        self.unigram = UnigramModel(train_file, test_file)
        self.bigram = BigramModel(train_file, test_file)
        self.unk_support = True
        self.start_support = True

    def train(self):
        t = open(self.train_file, "r")
        self.unigram.train()
        self.bigram.train()
        not_normalized = dict()
        if self.start_support:
            start = "<s> "
            end = " </s>"
        else:
            start = end = ""
        for line in t:
            line = start + line + end

            bag = line.split()
            word0 = bag[0]
            word1 = bag[1]
            for index in range(2, len(bag)):
                word2 = bag[index]
                if (word0, word1, word2) not in not_normalized.keys():
                    not_normalized[(word0, word1, word2)] = 1
                else:
                    not_normalized[(word0, word1, word2)] += 1
                word0 = word1
                word1 = word2
        size_of_vocab = len(self.unigram.model_dict.keys())-1

        if self.unk_support:
            added_vocab = size_of_vocab
            added_unk = 1
        else:
            added_unk = 0
            added_vocab = 0

        for (word0, word1, word2) in not_normalized.keys():
            self.model_dict[(word0, word1, word2)] = \
                ((not_normalized[word0, word1, word2] + added_unk) /
                 (self.bigram.count_dict[(word0, word1)]+added_vocab))
        if self.unk_support:
            for (word0, word1) in self.bigram.model_dict.keys():
                self.model_dict[(word0, word1, "<unk>")] = (1 / size_of_vocab)
        self.trained = True

    def is_trained(self):
        return self.trained

    def export(self, model_file):
        f = open(model_file, "w")
        for (word0, word1, word2) in self.model_dict:
            f.write("%s|%s|%s|%f\n" % (word0, word1, word2, self.model_dict[(word0, word1, word2)]))
        f.close()

    def get_possibility(self, word):
        if word in self.model_dict:
            return self.model_dict[word]
        else:
            return self.model_dict["<unk>"]

    def get_perplexity(self, sentence):
        sentence_word = sentence.split()
        word1 = sentence_word[0]
        word2 = sentence_word[1]
        sum_of_logs = 0
        for word3 in sentence_word[2:]:
            sum_of_logs += -math.log(self.model_dict[(word1, word2, word3)])
            word1 = word2
            word2 = word3
        return sum_of_logs**(1/len(sentence_word))

    def genrate_sentence(self):
        unkless_model = dict()
        for item in self.model_dict.keys():
            if "<unk>" not in item:
                unkless_model[item] = self.model_dict[item]

        last_words = ["<s>", ""]
        max_length = 10
        sentence_length = 0
        sentence = "<s> "
        w = list()
        p = list()
        for item in unkless_model.keys():
            if item[0] == "<s>":
                w.append((item[1] + "|" + item[2]))
                p.append(unkless_model[item])
        chs = np.random.choice(w, 1, p)
        last_words = chs[0].split("|")
        sentence += last_words[0] + " " + last_words[1] + " "
        print("sentence before while...", sentence)
        while (last_words[1] != "</s>") and (sentence_length < max_length):
            print("last words", last_words)
            w = list()
            p = list()
            for item in unkless_model.keys():
                if [item[0], item[1]] == last_words:
                    w.append(item[2])
                    print("item", item)
                    p.append(unkless_model[item])
            ch = np.random.choice(w, 1, p)
            sentence += ch[0] + " "
            print(sentence)
            last_words.pop(0)
            last_words.append(ch[0])

        return sentence


if __name__ == "__main__":
    tr = TrigramModel("example.txt", None)
    tr.train()
    tr.genrate_sentence()

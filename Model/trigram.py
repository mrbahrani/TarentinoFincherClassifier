from Model.unigram import UnigramModel
from Model.bigram import BigramModel
import math


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


if __name__ == "__main__":
    tr = TrigramModel("example.txt", None)
    tr.train()
    print(tr.get_perplexity("You sound like a"))

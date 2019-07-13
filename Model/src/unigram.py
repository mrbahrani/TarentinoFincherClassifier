import math


class UnigramModel:
    def __init__(self, train_file="", test_file=None):
        self.trained = False
        self.train_file = train_file
        self.test_file = test_file
        self.model_dict = dict()
        self.count_dict = dict()
        self.unk_support = True
        self.start_support = True
        self.vocabulary_count = 0
        self.bag = None

    def __init2__(self, bag):
        print(bag)
        self.bag = bag

    def train(self):
        not_normalized = dict()
        # Train by file
        if self.train_file != "":
            t = open(self.train_file, "r")
            if self.start_support:
                start = "<s> "
                end = " </s>"
            else:
                start = end = ""
            for line in t:
                line = start + line + end

                bag = line.split()
                for word in bag:
                    if word not in not_normalized.keys():

                        not_normalized[word] = 1
                    else:
                        not_normalized[word] += 1

        # Train by bag of words
        if not(self.bag is None):
            not_normalized = self.bag

        size_of_vocab = len(not_normalized.keys())
        all_count = sum(not_normalized.values())

        if self.unk_support:
            added_vocab = size_of_vocab
            added_unk = 1
            self.model_dict["<unk>"] = 1 / (all_count + size_of_vocab)
        else:
            added_unk = 0
            added_vocab = 0

        for word in not_normalized.keys():
            self.model_dict[word] = (not_normalized[word]+ added_unk) / (all_count+added_vocab)
        self.count_dict = not_normalized
        self.trained = True

        print("Model", self.model_dict)
        print("Vocab size", size_of_vocab)
        print("count", not_normalized)
        print("all count", all_count)

    def is_trained(self):
        return self.trained

    def export(self, model_file):
        f = open(model_file, "w")
        for word in self.model_dict:
            f.write("%s|%f\n" % (word, self.model_dict[word]))

    def get_possibility(self, word):
        if word in self.model_dict:
            return self.model_dict[word]
        else:
            return self.model_dict["<unk>"]

    def get_perplexity(self, sentence: str):
        sentence_words = sentence.split()
        sum_of_logs = 0
        for word in sentence_words:
            sum_of_logs += -math.log(self.get_possibility(word), 2)
        return sum_of_logs**(1/len(sentence_words))


    def generate_sentence(self):
        pass


if __name__ == "__main__":
    u = UnigramModel("in.1gram", "te_test")
    u.unk_support = False
    u.start_support = True
    u.train()
    u.export("1gr")

from Model.src.unigram import UnigramModel
import math

class NBClass:
    def __init__(self, label:str):
        self.label = label
        self.prior = 0
        self.language_model = None


class NaiveBayesClassifier:
    def __init__(self, train_filename):
        self.train_filename = train_filename
        self.count_dict = dict()
        self.class_list = []
        self.class_prior = dict()

    def train(self):
        trainer = open(self.train_filename, "r")
        class_count = dict()
        classes_dict = dict()
        total_docs = 0
        for line in trainer:
            total_docs += 1
            line_list = line.split()
            class_type = line_list[0]
            words = line_list[1:]
            if not(class_type in classes_dict):
                self.class_list.append(NBClass(class_type))
                classes_dict[class_type] = dict()
                class_count[class_type] = 0
            class_count[class_type] += 1

            for word in words:
                if word in classes_dict[class_type]:
                    classes_dict[class_type][word] += 1
                else:
                    classes_dict[class_type][word] = 1
        print(class_count)
        for cl in self.class_list:
            cl.prior = class_count[cl.label]/total_docs
            cl.language_model = UnigramModel()
            cl.language_model.__init2__(classes_dict[cl.label])
            cl.language_model.train()

    def get_log_possibility(self, sentence: str):
        poss_list = []
        tokens = sentence.split()
        for cl in self.class_list:
            likelihood = 1
            for token in tokens:
                likelihood *= cl.language_model.get_possibility(token)
            try:
                poss_list.append(math.log(cl.prior*likelihood, 2))
            except:
                poss_list.append(math.inf)
        return poss_list


if __name__ == "__main__":
    nb = NaiveBayesClassifier("train_set.txt")
    nb.train()
    t = open("sentence_label1.txt_test", "r")
    cnt = 0
    a = 0
    for line in t:
        x = nb.get_log_possibility(line)
        if x[0]>x[1]:
            #print("Tarentino")
            cnt += 1
        else:
            pass
        #print("Fincher")
        a += 1
    print(cnt/a)

    t = open("sentence_label2.txt_test", "r")
    cnt = 0
    a = 0
    for line in t:
        x = nb.get_log_possibility(line)
        if x[0]<x[1]:
            #print("Tarentino")
            cnt += 1
        else: #print("Fincher")
            pass
        a += 1
    print(cnt/a)
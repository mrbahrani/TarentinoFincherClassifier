from random import randint


data_file_name = "sentence_label1.txt"
all_data = open(data_file_name,"r")
train_data = open(data_file_name+"_train","w")
test_data = open(data_file_name+"_test","w")

counter = 0
sample = []
for sentence in all_data:
    sample.append(sentence)
    counter += 1
    if counter == 5:
        counter = 0
        r = randint(0,4)
        test_data.write(sample.pop(r))
        for s in sample:
            train_data.write(s)
        sample = []

all_data.close()
train_data.close()
test_data.close()

data_file_name = "sentence_label2.txt"
all_data = open(data_file_name, "r")
train_data = open(data_file_name+"_train","w", encoding="utf-8")
test_data = open(data_file_name+"_test","w", encoding="utf-8")

counter = 0
sample = []
print()
for sentence in all_data:
    sample.append(sentence)
    counter += 1
    if counter == 5:
        counter = 0
        r = randint(0, 4)
        test_data.write(sample.pop(r))
        for s in sample:
            train_data.write(s)
        sample = []

all_data.close()
train_data.close()
test_data.close()
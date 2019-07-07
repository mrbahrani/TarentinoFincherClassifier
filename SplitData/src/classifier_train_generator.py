if __name__ == "__main__":
    tr = open("train_set.txt", "w")
    l1 = open("sentence_label1.txt_train")
    for line in l1:
        tr.write("label1 "+line)
    l1.close()
    l2 = open("sentence_label2.txt_train")
    for line in l2:
        tr.write("label2 " + line)
    l2.close()

    tr.close()

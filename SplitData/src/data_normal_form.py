from nltk import sent_tokenize

if __name__ == "__main__":

    l1 = open("label1.txt")
    ss = l1.read().replace("\n"," ")
    q = sent_tokenize(ss)
    l1o = open("sentence_label1.txt", "w")
    for s in q:
        l1o.write(s[:-1:1]+"\n")
    l1o.close()

    l2 = open("label2.txt")
    ss = l2.read().replace("\n", " ")
    q = sent_tokenize(ss)
    print(ss)
    print(q)
    l2o = open("sentence_label2.txt", "w")
    for s in q:
        print(s)
        l2o.write(s[:-1:1]+"\n")
    l2o.close()

from WordCloud.src.wordcloud_generator import create_wordcloud
import pickle

for cloud in range(1,9):
    d = pickle.load(open("./pickles/%d.p" %cloud,"rb"))
    print(d)
    create_wordcloud(d,None,"../out/"+ str(cloud)+"jpg")
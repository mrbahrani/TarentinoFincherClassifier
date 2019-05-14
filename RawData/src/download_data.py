from RawData.src import getsubtitle
from RawData.src import movielist

if __name__=="__main__":

    tar = "0000233"
    tar_list = movielist.get_movie_list_by_director_id(tar)
    for tari in tar_list:
        sub = open("../tarentino/%s.zip" % tari[1], "wb")
        sub.write(getsubtitle.get_subtitle_zip(tari[0]))
        sub.close()
        getsubtitle.unzip_subtitle("../tarentino/%s.zip" % tari[1])

    finch = "0000399"
    finch_list = movielist.get_movie_list_by_director_id(finch)
    for finch in finch_list:
        sub = open("../fincher/%s.zip" % finch[1], "wb")
        sub.write(getsubtitle.get_subtitle_zip(finch[0]))
        sub.close()
        getsubtitle.unzip_subtitle("../fincher/%s.zip" % finch[1])
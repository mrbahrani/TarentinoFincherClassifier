import requests
from bs4 import BeautifulSoup
import zipfile
import time
import os
def get_subtitle_zip(movie_id):
    page = requests.get("https://www.yifysubtitles.com/movie-imdb/tt%s" % movie_id)
    bs = BeautifulSoup(page.text, "html.parser")
    existence = bs.findAll("h2", {"class":"movie-main-title"})
    print(len(existence))
    if not len(existence):
        return bytes(1)
    print("Oh my")
    links = bs.findAll("a", attrs={"class":"subtitle-download"})
    for link in links:
        if "english" in link["href"]:
            subtitle_name = link["href"].split("/")[2]
            print("https://www.yifysubtitles.com/subtitle/%s.zip"% subtitle_name)
            subtitle = requests.get("https://www.yifysubtitles.com/subtitle/%s.zip" %subtitle_name)
            return subtitle.content


def unzip_subtitle(zip_name):
    try:
        zip_ref = zipfile.ZipFile(zip_name, 'r')
        zip_ref.extractall("")
        for srt_file in zip_ref.filelist:
            if ".srt" in srt_file.filename:
                os.rename(srt_file.filename, zip_name.replace("zip", "srt"))
        zip_ref.close()
        time.sleep(3)
    except:
        pass
    try:
        os.remove(zip_name)
    except:
        print("Literally why?")
if __name__ == "__main__":
    sub = open("test.zip","wb")
    sub.write(get_subtitle_zip("0110912"))
    sub.close()
    unzip_subtitle("test.zip")
from Data.src import datacleaning
from os import walk, curdir, path
s_list = list()
for r, d, f in walk("../../RawData/tarentino"):
    for file in f:
        if ".srt" in file:
            s_list.append(file)

for s in s_list:
    datacleaning.remove_subtitle_time(s, None,src="../../RawData/tarentino/", dst="../label1/")

s_list = list()
for r, d, f in walk("../../RawData/fincher"):
    for file in f:
        if ".srt" in file:
            s_list.append(file)

for s in s_list:
    datacleaning.remove_subtitle_time(s, None,src="../../RawData/fincher/", dst="../label2/")
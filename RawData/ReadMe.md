In this project, we try to distinguish between "Quentin Tarentino"'s dialogues and "David Fincher"'s.
1. As a movie fan, I was just interested to know whether I can develop a system that can do so.
2. I have to main sources i.e. 1) IMDB, which give me a filmography of each director, and 2) YIFY subtitles as a source
for scenarios
3. There was already a library for scrapping IMDb, imdbpy. For the subtitles, I personally scrapped YIFY. I may wrap my
code in a library for python later. (depends on various factors:))
4. Well, the short answer is "Run download_data.py". This file iterates on each movie list of directors and downloads
available subtitles. I shall honestly say that the exception handling is quite adolescent but the error won't stop 
running.
To be honest, there are two files which where encoded "uniform", I just changed them to UTF-8 manually. If you want to
recreate the data, do so for "Pulp Fiction" and "Fight club" 
* Using venv do not forget - $pip install -r requirements.txt
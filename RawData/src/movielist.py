from imdb import IMDb, Movie
from string import punctuation
def get_movie_list_by_director_id(director_id):
    im = IMDb()
    all_roles = im.get_person_filmography(director_id)['data']["filmography"]
    m_list = []
    for role in all_roles:
        if "director" in role.keys():
            for movie in role["director"]:
                mname = str(movie)
                for p in punctuation:
                    mname = mname.replace(p,"")
                m_list.append((movie.getID(), str(mname)))
            break
    return m_list


if __name__ == "__main__":
    print(get_movie_list_by_director_id("0000233"))
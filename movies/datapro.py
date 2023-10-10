from json import load

path="C:\\Users\\thanveer\\OneDrive\\Desktop\\luminar\\movies\\mdb.json"

with open(path,encoding="utf-8")as f:
    films=load(f)

# print(len(films))

# movie_name=[f.get("title") for f in films if f.get("year")=="2015"]
# print(movie_name)

# cmdy_movies=[f.get("title") for f in films if "Comedy" in f.get("genres")]
# print(cmdy_movies)

# runtime=[f.get("title") for f in films if f.get("id") in range(20,31) and f.get("runtime")>="110"]
# print(runtime)

# single_title=[f.get("title") for f in films if len(f.get("title").split(" "))==1]
# print(single_title)

# genre_runtime=[f for f in films if "Drama" in f.get("genres")]
# lenghty_movie=max(genre_runtime,key=lambda f:int(f.get("runtime")))
# print(lenghty_movie)

# # print all genres
# # most number of movies released year

# all_genre=[f.get("genres") for f in films if f.get("genres")]
# print(all_genre)


wc={}

for m in films:
     year=m.get("year")

     if year in wc:
         wc[year]+=1
     else:
         wc[year]=1

# out=max(wc,key=lambda k:wc.get(k))
# print(out)

print(max((v,k) for k,v in wc.items()))
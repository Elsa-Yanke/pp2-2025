def above(movie):
    return movie["imdb"] > 5.5
def above_multiple(movies):
    filtered = []
    for movie in movies:
        if movie["imdb"] > 5.5:
            filtered.append(movie)
    return filtered
def category(movies):
    cate = []
    for movie in movies:
        if movie["category"] == "Comedy":
            cate.append(movie)
    return cate
def average(movies):
    total = 0
    count = 0
    for movie in movies:
        total +=movie["imdb"]
        count +=1
    return total/count

def average_category(movies):
    total = 0
    count = 0
    for movie in movies:
        if movie["category"] == "Action":
            total +=movie["imdb"]
            count +=1
    return total/count

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

print(above(movies[7]))
filtered = above_multiple(movies)
print(filtered)
cate = category(movies)
print(cate)
print(average(movies))
print(average_category(movies))
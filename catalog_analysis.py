import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

def average_rating(movies):
    """Возвращает среднюю оценку по каталогу, округленную до 1 знака"""

    average_rate = 0

    for movie in  movies:
        average_rate += movie["rating"]

    return round(average_rate/len(movies), 1)

def catalog_age_stats(movies, current_year=2026):
    """Возвращает кортеж (самый старый фильм в годах, самый новый фильм в годах, среднее) """

    oldest = ''
    the_most_new = ''
    oldest_year = 2999
    the_most_new_year = 0

    for movie in  movies:
        if movie["year"] < oldest_year:
            oldest = movie["title"] 
            oldest_year = movie["year"]
        if  movie["year"] > the_most_new_year:
            the_most_new = movie["title"]
            the_most_new_year = movie["year"]
    
    sum_year = sum((current_year - movie["year"])for movie in movies) 

    return (oldest, the_most_new, math.ceil(sum_year/len(movies)))

def duration_in_hours(minutes):
    """Переводит минуты в формат "2ч 35м"""
    houres = minutes // 60
    mins = minutes % 60 
    return f"{houres}ч {mins}м"

def rating_tier(rating):

    '''По оценке возвращает категорию'''

    if rating >= 9:
        mark = "шедевр"
    elif 7 <= rating <= 8.9:
        mark = "хорошо"
    else:
        mark = "средне" if 5 <= rating <= 6.9 else "слабо"

    return mark

def decade_label(year):
    '''Классифицирцет фильмы по времени'''
    match year:
        case _ if year >= 2020:
            return "новые"
        case _ if year >= 2015 &  year < 2020:
            return "недавние"
        case _ if year < 2015:
            return "старые"


for movie in movies:
    if "comedy" in movie['genres']:
        continue
    else:
        print(movie['title'])

i = 0
while  i < len(movies):
    if movies[i]['rating'] > 9.0:
        print(movies[i]['title'])
        break
    i+= 1
else:
    print("Шедевров не найдено")
    
    
def count_long_movies(movies, threshold=120):

    '''Cчитает количество фильмов длиннее threshold минут'''
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1

    return count

def normalize_title(title):
    '''Приводит строку к формату Title Case'''

    words = title.split(' ')
    title_words = []
    for word in words:
        title_word = "".join(word[0].upper() + word[1:])
        title_words.append(title_word)
    return " ".join(title_words)

def make_slug(title):
    '''Превращает нормализованное название в «слаг» вида the-quiet-algorithm'''
    return title.lower().replace(" ", "-")

def format_report_line(movie):
    '''Возвращает единую строку с описанием фильма'''
    title = normalize_title(movie["title"])
    minutes = duration_in_hours(movie["duration_min"])
    genres = ", ".join(sorted(movie["genres"]))

    return f"{"'"}{'"'}{title}{'"'} {"("}{movie["year"]}{")"} {"-"} {movie["rating"]}{"/10, "} {minutes}, {"жанры: "} {genres}{"'"}"


def titles_sorted_by_rating(movies):
    '''Возвращает список названий фильмов, отсортированных по убыванию рейтинга'''
    sorted_movies =sorted(movies , key= lambda movie: movie["rating"], reverse=True)
    return [movie["title"] for movie in sorted_movies]


def top_n_by_rating(movies, n=3):
    '''Список из n кортежей (title, rating) — топ по рейтингу'''
    sorted_movies =sorted(movies , key= lambda movie: movie["rating"], reverse=True)
    top_list = [(movie["title"], movie["rating"]) for movie in sorted_movies[:n]]

    return top_list


def count_by_genre(movies):
    '''Возвращает словарь {жанр: количество фильмов}'''

    dict_genres = {}
    for movie in movies:
        for genre in movie["genres"]:
            dict_genres[genre] = dict_genres.get(genre, 0) + 1
    return dict_genres

    
def actor_filmography(movies):
    '''Возвращает словарь {актер: [список названий фильмов]}'''

    dict_actors = {}
    for movie in movies:
        for actor in movie["actors"]:
            dict_actors[actor] = dict_actors.get(actor, []) + [movie["title"]]
    return dict_actors


title_rating = [{m["title"]: m["rating"]} for m in movies if m["rating"] > average_rating(movies)]


def all_genres(movies):
    '''Возвращает множество всех уникальных жанров'''

    set_genres = set()
    for movie in movies:
        set_genres = set_genres | movie["genres"]
    return set_genres


def common_actors(movie1, movie2):
    '''Возвращает множество актеров, снимавшихся в обоих фильмах'''

    return set(movie1["actors"] ) & set(movie2["actors"] )


def genres_only_in_one(movies_a, movies_b):
    '''Возвращает жанры, встречающиеся в movies_a, но не встречающиеся в movies_b'''

    return set(movies_a["actors"] ) - set(movies_b["actors"] )


def iter_high_rated(movies, min_rating=8.0):
    '''Возвращает фильмы с рейтингом не ниже min_rating'''

    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie

for movie in iter_high_rated(movies):
    print(format_report_line(movie))

print(sum(m["duration_min"] for m in movies if m["rating"] > 7))


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

print(format_report_line(movies[7]))
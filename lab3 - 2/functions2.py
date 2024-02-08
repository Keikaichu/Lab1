# Dictionary of movies
Dictionary_of_movies_movies = [ 
    { "name": "Usual Suspects", "imdb": 7.0, "category": "Thriller" }, 
    { "name": "Hitman", "imdb": 6.3, "category": "Action" }, 
    { "name": "Dark Knight", "imdb": 9.0, "category": "Adventure" }, 
    { "name": "The Help", "imdb": 8.0, "category": "Drama" }, 
    { "name": "The Choice", "imdb": 6.2, "category": "Romance" }, 
    { "name": "Colonia", "imdb": 7.4, "category": "Romance" }, 
    { "name": "Love", "imdb": 6.0, "category": "Romance" }, 
    { "name": "Bride Wars", "imdb": 5.4, "category": "Romance" }, 
    { "name": "AlphaJet", "imdb": 3.2, "category": "War" }, 
    { "name": "Ringing Crime", "imdb": 4.0, "category": "Crime" }, 
    { "name": "Joking muck", "imdb": 7.2, "category": "Comedy" }, 
    { "name": "What is the name", "imdb": 9.2, "category": "Suspense" }, 
    { "name": "Detective", "imdb": 7.0, "category": "Suspense" }, 
    { "name": "Exam", "imdb": 4.2, "category": "Thriller" }, 
    { "name": "We Two", "imdb": 7.2, "category": "Romance" } ]

#ex1
#Write a function that takes a single movie and returns True if its IMDB score is above 5.5
def isabove5_5(movie):
    return movie.get("imdb", 0) > 5.5
movie = {"name": "Hitman", "imdb": 6.3, "category": "Action"}
print(isabove5_5(movie),end="\n")

#ex2
#Write a function that returns a sublist of movies with an IMDB score above 5.5.
def is_above5_5(Dictionary_of_movies_movies):
    return [movie for movie in Dictionary_of_movies_movies if movie.get("imdb", 0)> 5.5]
print(is_above5_5(Dictionary_of_movies_movies),end="\n")

#ex3
#Write a function that takes a category name and returns just those movies under that category.
def isthatcategory(Dictionary_of_movies_movies):
    return [movie for movie in Dictionary_of_movies_movies if movie.get("category") == category]
category=input()
print(isthatcategory(Dictionary_of_movies_movies),end="\n")

#ex4
#Write a function that takes a list of movies and computes the average IMDB score.
def theaverage(Dictionary_of_movies_movies):
    total_imdb=sum(movie.get("imdb", 0) for movie in Dictionary_of_movies_movies)
    return total_imdb/len(Dictionary_of_movies_movies)
print(theaverage(Dictionary_of_movies_movies),end="\n")

#ex5
#Write a function that takes a category and computes the average IMDB score.
def the_average_category(Dictionary_of_movies_movies):
    category_movies = [movie for movie in Dictionary_of_movies_movies if movie.get("category") == categoryy]
    total_category_imdb=sum(movie.get("imdb", 0) for movie in category_movies)
    return total_category_imdb/len(category_movies)
categoryy=input()
print(the_average_category(Dictionary_of_movies_movies))
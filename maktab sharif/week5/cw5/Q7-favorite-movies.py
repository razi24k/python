# favorite_movies = [
#     ("Inception", 2010),
#     ("The Shawshank redemption", 1994),
#     ("Pulp fiction", 1994)
# ]
favorite_movies = []
adding_movies = True
while adding_movies:
    movie = input("What is the name of the movie?(press enter to quit) ")
    if not movie:
        adding_movies = False
        break
    try:
        movie_year = int(input("What is the year of the movie? (press enter to quit) "))
        if not movie_year:
            adding_movies = False
            break
    except ValueError:
        print("Please enter a valid year")
        continue
    favorite_movies.append((movie, movie_year))

new_list = sorted(favorite_movies, key=lambda movie: movie[1], reverse=True)
print(new_list)

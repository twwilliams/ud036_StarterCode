"""
The entry point to the movie display Web page project. Instantiates the
list of media.Movie() objects and passes them to the function that
renders a Web page from the Movie() data and opens it in the system
default Web browser.
"""

import media
import fresh_tomatoes
import json

# Load movie data from data file
with open('movies.json') as movie_data:
    movie_list = json.load(movie_data)

# Create the list of movies from the movie data
movies = []

for movie in movie_list:
    movies.append(media.Movie(
        title=movie['title'],
        poster_image_url=movie['poster_image_url'],
        trailer_youtube_url=movie['trailer_youtube_url']
    ))

# Render the page and open the Web browser
fresh_tomatoes.open_movies_page(movies)

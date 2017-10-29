"""
The entry point to the movie display Web page project. Instantiates the
list of media.Movie() objects and passes them to the function that
renders a Web page from the Movie() data and opens it in the system
default Web browser.
"""

import json

import media
import fresh_tomatoes

JSON_DATA_FILE = 'movies.json'


# Load movie data from data file
def load_movie_data(data_file):
    """
    Loads movie data from a JSON file
    :return: List of dicts with movie data
    """
    with open(data_file) as movie_data:
        movie_data_list = json.load(movie_data)

    return movie_data_list


def create_movies_from_data(movie_list):
    """
    Construct a list of media.Movie() objects from the supplied list of dicts
    :param movie_list: List of dicts with movie data
    :return: List of media.Movie() objects
    """
    movie_objects = []
    for movie in movie_list:
        movie_objects.append(media.Movie(
            title=movie['title'],
            poster_image_url=movie['poster_image_url'],
            trailer_youtube_url=movie['trailer_youtube_url']
        ))
    return movie_objects


if __name__ == '__main__':

    movie_list = load_movie_data(JSON_DATA_FILE)

    movies = create_movies_from_data(movie_list)

    # Render the page and open the Web browser
    fresh_tomatoes.open_movies_page(movies)

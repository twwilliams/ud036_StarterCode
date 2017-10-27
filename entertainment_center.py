"""
The entry point to the movie display Web page project. Instantiates the
list of media.Movie() objects and passes them to the function that
renders a Web page from the Movie() data and opens it in the system
default Web browser.

A future enhancement might include loading the movie data from a database
or a configuration file so that the list could be updated without
editing the code itself.


A note about the formatting of the poster image URLs:

I found inconsistent advice about handling long URLs in PEP8. It seems like
URLs should not be split when they are part of comments or docstrings to make
it easier to copy and paste or to click on them in editors/viewers.

In the case of passing URLs to the media.Movie() constructor, I found it far
more readable and elegant to split them and include whitespace within the call
to media.Movie() rather than keeping the URLs on one line and then adding a
# NOQA comment.
"""

import media
import fresh_tomatoes

# Create the list of movies
movies = [
    media.Movie(
        title='The Ninth Configuration',

        poster_image_url='https://images-na.ssl-images-amazon.com/images/M/'
        'MV5BZjI3NzUyMWEtNmNlZC00OWIwLTlkOTEtNGI0ZjMwNDJiMTQzXkEyXkFqcGdeQX'
        'VyMjI4MjA5MzA@._V1_.jpg',

        trailer_youtube_url='https://www.youtube.com/watch?v=S9i-fzlJSs4'
    ),

    media.Movie(
        title='Thoroughly Modern Millie',

        poster_image_url='https://images-na.ssl-images-amazon.com/images/M/'
        'MV5BZTlhYTc4MzEtZDNlYi00NjM2LTk2ZjQtZTUyZmRlMmYzODAyXkEyXkFqcGdeQX'
        'VyMjI4MjA5MzA@._V1_.jpg',

        trailer_youtube_url='https://www.youtube.com/watch?v=jCug0golA6c'
    ),

    media.Movie(
        title='The Last Dragon',

        poster_image_url='https://images-na.ssl-images-amazon.com/images/M/'
        'MV5BMjlkNDA2NTQtYzNlOS00YmY1LTk5YzEtMWVhYTY0ZDI0ZDIxXkEyXkFqcGdeQXV'
        'yNjEwMTA0NTc@._V1_.jpg',

        trailer_youtube_url='https://www.youtube.com/watch?v=Z7Crt4S1IZM'
    ),

    media.Movie(
        title='Grosse Pointe Blank',

        poster_image_url='https://images-na.ssl-images-amazon.com/images/M/'
        'MV5BMmRhYTg0N2QtMWZhMS00OWQwLTk1ZmEtMmUyMTY0NTE4YWUwXkEyXkFqcGdeQXV'
        'yNzQ1ODk3MTQ@._V1_.jpg',

        trailer_youtube_url='https://www.youtube.com/watch?v=iF7t91gbSf8'
    ),

    media.Movie(
        title='La La Land',

        poster_image_url='https://images-na.ssl-images-amazon.com/images/M/'
        'MV5BMzUzNDM2NzM2MV5BMl5BanBnXkFtZTgwNTM3NTg4OTE@._V1_SY1000_SX675_'
        'AL_.jpg',

        trailer_youtube_url='https://www.youtube.com/watch?v=0pdqf4P9MB8'
    ),

    media.Movie(
        title='Logan',

        poster_image_url='https://images-na.ssl-images-amazon.com/images/M/'
        'MV5BMjQwODQwNTg4OV5BMl5BanBnXkFtZTgwMTk4MTAzMjI@._V1_.jpg',

        trailer_youtube_url='https://www.youtube.com/watch?v=Div0iP65aZo'
    )
]

# Render the page and open the Web browser
fresh_tomatoes.open_movies_page(movies)

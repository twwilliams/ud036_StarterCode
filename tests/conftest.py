"""Common configurations and fixtures for the test suite"""

import pytest

import media


@pytest.fixture(scope='session')
def movie_instance():
    """media.Movie() instance to use with tests"""
    return media.Movie(
            title="Star Wars: The Last Jedi",

            poster_image_url='https://images-na.ssl-images-amazon.com/images/'
            'M/MV5BMjQ1MzcxNjg4N15BMl5BanBnXkFtZTgwNzgwMjY4MzI@._V1_SY1000_CR'
            '0,0,675,1000_AL_.jpg',

            trailer_youtube_url="https://www.youtube.com/watch?v=Q0CbN8sfihY"
        )

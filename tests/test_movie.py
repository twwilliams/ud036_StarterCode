"""Tests for the media.Movie class"""

import pytest

import media


def test_constructor():
    movie = media.Movie(
        title="Star Wars: The Last Jedi",

        poster_image_url="https://images-na.ssl-images-amazon.com/images/M/"
                         "MV5BMjQ1MzcxNjg4N15BMl5BanBnXkFtZTgwNzgwMjY4MzI@._"
                         "V1_SY1000_CR0,0,675,1000_AL_.jpg",

        trailer_youtube_url="https://www.youtube.com/watch?v=Q0CbN8sfihY"
    )

    assert (
        movie.title == "Star Wars: The Last Jedi" and
        movie.poster_image_url.endswith('1000_AL_.jpg') and
        movie.trailer_youtube_url.endswith('Q0CbN8sfihY')
    )


def test_insufficient_args():
    with pytest.raises(TypeError):
        movie = media.Movie(
            title="Something"
        )

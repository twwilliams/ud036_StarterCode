"""
Tests for the fresh_tomatoes.py module

While this file was supplied as part of the course, I have made some changes
and need to verify they work.
"""

import os
import io

import fresh_tomatoes


def test_file_path_from_template_name():
    """
    An integration test rather than a unit test.
    """
    name = 'main_page_content'
    template_name = fresh_tomatoes._file_path_from_template_name(name)

    assert template_name.endswith(
        os.path.join(os.sep, 'templates', name + '.html')
    )


def test_read_template_file():
    """
    Another integration test since it will read actual data from the
    filesystem.
    """
    name = 'movie_tile_content'

    contents = fresh_tomatoes._read_template_file(name)

    first_line = '<div class="col-md-6 col-lg-4 movie-tile text-center"'
    assert (contents.startswith(first_line) and
            len(contents.split('\n')) == 7)


def test_create_movie_tiles_content(movie_instance):
    movies = [movie_instance]

    movie_tiles = fresh_tomatoes._create_movie_tiles_content(movies)

    assert 'data-trailer-youtube-id="Q0CbN8sfihY"' in movie_tiles


def test_create_movies_page(movie_instance):
    movies = [movie_instance]

    output_file = fresh_tomatoes._create_movies_page(movies)

    assert isinstance(output_file, io.TextIOBase)

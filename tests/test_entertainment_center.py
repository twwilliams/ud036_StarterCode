"""Test entertainment_center.py"""
import json

import media
import entertainment_center


def _movie_data_for_data_file():
    return [
        {
            'title': 'Star Wars: The Last Jedi',
            'poster_image_url': 'https://images-na.ssl-images-amazon.com/images'
                                '/M/MV5BMjQ1MzcxNjg4N15BMl5BanBnXkFtZTgwNzgwMjY'
                                '4MzI@._V1_SY1000_CR0,0,675,1000_AL_.jpg',
            'trailer_youtube_url': 'https://www.youtube.com/watch?v=Q0CbN8sfihY'
        },
        {
            'title': 'Wonder Woman',
            'poster_image_url': 'https://images-na.ssl-images-amazon.com/images'
                                '/M/MV5BNDFmZjgyMTEtYTk5MC00NmY0LWJhZjktOWY2MzI'
                                '5YjkzODNlXkEyXkFqcGdeQXVyMDA4NzMyOA@@._V1_SY10'
                                '00_SX675_AL_.jpg',
            'trailer_youtube_url': 'https://www.youtube.com/watch?v=VSB4wGIdDwo'
        }
    ]


def _create_json_data_file(tmpdir):
    json_file = tmpdir.join('movies_test.json')
    json_file_name = str(json_file)

    with open(json_file_name, 'w') as wf:
        json.dump(_movie_data_for_data_file(), wf)

    return json_file_name


def test_load_movie_data(tmpdir):
    json_data_file = _create_json_data_file(tmpdir)
    movie_data_list = entertainment_center.load_movie_data(json_data_file)

    assert len(movie_data_list) == 2
    assert movie_data_list[1]['title'] == 'Wonder Woman'


def test_create_movies_from_data():
    movies = entertainment_center.create_movies_from_data(
        _movie_data_for_data_file())

    assert len(movies) == 2
    assert isinstance(movies[1], media.Movie)

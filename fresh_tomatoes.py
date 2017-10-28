"""Creates the Web page, parses the media.Movie() entries, and opens
the page in a browser."""

import webbrowser
import os
import re


# Configuration options
TEMPLATES_DIRECTORY = 'templates'


# Supporting functions for loading HTML template data from files
def _file_path_from_template_name(template_name):
    """
    Converts a template name into a file path
    :param template_name: string that matches file in templates directory
    :return: full file path to template file
    """

    file_name = template_name + '.html'
    return os.path.abspath(os.path.join(TEMPLATES_DIRECTORY, file_name))


def _read_template_file(template_name):
    """
    Read in the HTML template from a file. Makes it easier to update the look
    and feel of the page by using an HTML editor rather than just handling
    inside Python strings.
    :param string template_name: HTML template name for file stored in templates/
    :return: Contents from the HTML template file
    """

    contents = ""
    template_file_path = _file_path_from_template_name(template_name)

    with open(template_file_path, 'r') as template:
        contents = template.read()

    return contents


# Styles and scripting for the page
# The title and <head> of the page
MAIN_PAGE_HEAD = _read_template_file('main_page_head')

# The main page layout and title bar
MAIN_PAGE_CONTENT = _read_template_file('main_page_content')

# A single movie entry html template
MOVIE_TILE_CONTENT = _read_template_file('movie_tile_content')


def _create_movie_tiles_content(movies):
    """
    Parses movie content to format rendering on the page.

    :param list movies: List of media.Movie() objects
    :return: Formatted HTML snippet
    """
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the YouTube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += MOVIE_TILE_CONTENT.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content


def open_movies_page(movies):
    """
    Creates the HTML page from template pieces and opens it in the browser.
    :param list movies: List of media.Movie() objects
    :return: No return value. Creates HTML page and opens Web browser.
    """
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = MAIN_PAGE_CONTENT.format(
        movie_tiles=_create_movie_tiles_content(movies))

    # Output the file
    output_file.write(MAIN_PAGE_HEAD + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)

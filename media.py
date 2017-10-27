"""A module for different classes of media, like Movie or TVShow"""


class Movie:
    """
    Holds data about movies that can be displayed on a Web page. Only three
    attributes for now, as described in the constructor documentation.
    """

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """
        Movie constructor. All attributes are required at initialization.

        No special checks on the content performed here since that seems
        to violate Python's ethos that we are all adults here and will
        do the right thing.

        Debating whether it would be better to accept just the YouTube
        video ID rather than taking the whole URL for the trailer. That
        would simplify some of the code in fresh_tomatoes.py.

        :param title: The name of the movie
        :param poster_image_url: URL pointing to the movie's poster image
        :param trailer_youtube_url: The movie's trailer on YouTube
        """
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

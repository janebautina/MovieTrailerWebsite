import webbrowser


class Movie():
    """This class provides a way to store movie related information.

    Attributes:
        VALID_RATINGS: A string array of movies' ratings
    """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, image, trailer, star):
        """Inits Movie class with a movie title, a box art image,
           a trailer video and a Hollywood star
        """
        self.title = movie_title
        self.poster_image_url = image
        self.trailer_youtube_url = trailer
        self.star = star

    def show_trailer(self):
        """Shows a movie trailer from youtube.com"""
        webbrowser.open(self.trailer_youtube_url)

import media
import fresh_tomatoes


# create and initialize 7 Movie class objects
erin = media.Movie("Erin Brockovich",
                   "http://bit.ly/1OHw4CE",
                   "https://www.youtube.com/watch?v=_2GvrAQMNoU",
                   "Julia Roberts")
bride = media.Movie("Runaway Bride",
                    "http://bit.ly/1Mjzr0b",
                    "https://www.youtube.com/watch?v=Ay8QC6tL7k0",
                    "Julia Roberts")
angelica = media.Movie("Angelica",
                       "http://bit.ly/1V2pGWu",
                       "https://www.youtube.com/watch?v=NjFwmMlIu_E",
                       "Michèle Mercier")
prada = media.Movie("The Devil Wears Prada",
                    "http://bit.ly/1MjzsBq",
                    "https://www.youtube.com/watch?v=2PjZAeiU7uM",
                    "Anne Jacqueline Hathaway")
angels = media.Movie("City Of Angels",
                     "http://bit.ly/1FndcXo",
                     "https://www.youtube.com/watch?v=6zSG_oVliis",
                     "Nicolas Cage")
eat_pray_love = media.Movie("Eat Pray Love",
                            "http://bit.ly/1FndayX",
                            "https://www.youtube.com/watch?v=mjay5vgIwt4",
                            "Julia Roberts")
woman = media.Movie("Pretty Woman",
                    "http://bit.ly/1KYPP96",
                    "https://www.youtube.com/watch?v=MAiQvt1_TsM",
                    "Julia Roberts")
# this is the list of movies to display on the site
movies = [erin, bride, angelica, prada, angels, eat_pray_love, woman]
fresh_tomatoes.open_movies_page(movies)

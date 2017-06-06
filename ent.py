import fresh_tomatoes
import media

# Movies List created by using instances.

Arrival = media.Movie("Arrival",
                      "About Alien Language as a weapon",
                      "https://www.youtube.com/watch?v=tFMo3UJ4B4g",
                      "https://upload.wikimedia.org/wikipedia/en/d/df/Arrival%2C_Movie_Poster.jpg")  # NOQA

Wonder_Woman = media.Movie("Wonder Woman",
                           """In the early 20th century, the Amazon princess
                              Diana, who is living on the island of Themyscira,
                              meets American military pilot Steve Trevor when
                              he is washed ashore. After learning from him
                              about the ongoing events of World War I, she
                              leaves her home to bring an early end
                              to the war.[3]""",
                           "https://www.youtube.com/watch?v=1Q8fG0TtVAY",
                           "https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg")  # NOQA

Dark_Knigth = media.Movie("The Dark Knight",
                          "I'm Batman",
                          "https://www.youtube.com/watch?v=EXeTwQWrcwY",
                          "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg")  # NOQA
Logan = media.Movie("Logan",
                    """Logan attempts to hide from the world and his legacy.
                       However, when a mysterious woman (Elizabeth Rodriguez)
                       asks for Logan's help with Laura (Dafne Keen), a young
                       mutant being pursued by dark forces, he is drawn back
                       into action despite his hopelessness.""",
                    "https://www.youtube.com/watch?v=RH3OxVFvTeg",
                    "https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg")  # NOQA
Inception = media.Movie("Inception",
                        """A thief, who steals corporate secrets through use
                           of dream-sharing technology, is given the inverse
                           task of planting an idea into the mind of a CEO.""",
                        "https://www.youtube.com/watch?v=YoHD9XEInc0",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg")  # NOQA
Interstellar = media.Movie("Interstellar",
                           """A team of explorers travel through a wormhole in
                              space in an attempt to ensure
                              humanity's survival.""",
                           "https://www.youtube.com/watch?v=2LqzF5WauAw",
                           "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg")  # NOQA
Sherlock = media.Movie("Sherlock Holmes",
                       """Detective Sherlock Holmes and his stalwart partner
                          Watson engage in a battle of wits and brawn with a
                          nemesis whose plot is a threat to all of England.""",
                       "https://www.youtube.com/watch?v=Egcx63-FfTE",
                       "https://upload.wikimedia.org/wikipedia/en/e/e0/Sherlock_holmes_ver5.jpg")  # NOQA
WWS = media.Movie("The Wolf of Wall Street",
                  """Based on the true story of Jordan Belfort, from his rise
                     to a wealthy stock-broker living the high life to his fall
                     involving crime, corruption and federal government.""",
                  "https://www.youtube.com/watch?v=pabEtIERlic",
                  "https://upload.wikimedia.org/wikipedia/en/1/1f/WallStreet2013poster.jpg")  # NOQA
Dunkirk = media.Movie("Dunkirk",
                      """Allied soldiers from Belgium, the British Empire,
                         Canada, and France are surrounded by the German army
                         and evacuated during a fierce battle
                         in World War II""",
                      "https://www.youtube.com/watch?v=F-eMt3SrfFU",
                      "https://upload.wikimedia.org/wikipedia/en/1/15/Dunkirk_Film_poster.jpg")  # NOQA


# A list of movies created.
movie_list = [Arrival, Wonder_Woman, Dark_Knigth, Logan, Inception,
              Interstellar, Sherlock, WWS, Dunkirk]
# Calling the open_movies_page function from the fresh_tomatoes module.
fresh_tomatoes.open_movies_page(movie_list)
# print(media.Movie.__module__)

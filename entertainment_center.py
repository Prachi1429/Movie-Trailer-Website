import media
import fresh_tomatoes

# First instance of class Movie - Toy Story with arguments
toy_story = media.Movie("Toy Story",
                      "A Story of a boy and his toys that come to life",
                      "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                      "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# Instance of class Movie - Avatar
avatar = media.Movie("Avatar",
                   "A Marine on an alien Planet",
                   "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                   "https://www.youtube.com/watch?v=5PSNL1qE6VY")

# Instance of class Movie - The Pursuit of Happyness
the_pursuit_of_happyness = media.Movie("The Pursuit of Happyness",
                                    "If YOU want something Go Get It, PERIOD!",
                                    "https://upload.wikimedia.org/wikipedia/en/8/81/Poster-pursuithappyness.jpg",
                                    "https://www.youtube.com/watch?v=89Kq8SDyvfg")

# Instance of class Movie - La La Land
la_la_land = media.Movie("La La Land",
                         "The story of an aspiring actress and a dedicated jazz musician, who are struggling to make ends meet in a city known for crushing hopes and breaking hearts.",
                         "https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_%28film%29.png",
                         "https://www.youtube.com/watch?v=0pdqf4P9MB8")

# Instance of class Movie - My Name is Khan
my_name_is_khan = media.Movie("My Name Is Khan",
                              "An Indian Muslim man with Asperger's syndrome takes a challenge to speak to the President seriously, and embarks on a cross-country journey.",
                              "https://upload.wikimedia.org/wikipedia/en/5/5d/My_Name_Is_Khan_film_poster.jpg",
                              "https://www.youtube.com/watch?v=nqxgYT3TYzY")

# Instance of class Movie - Eternal Sunshine Of The Spotless Mind
eternal_sunshine_of_the_spotless_mind = media.Movie("Eternal Sunshine Of The Spotless Mind",
                                                    "When their relationship turns sour, a young couple undergoes a medical procedure to have each other erased from their memories.",
                                                    "https://images-na.ssl-images-amazon.com/images/I/51%2Bwf-vBCUL.jpg",
                                                    "https://www.youtube.com/watch?v=0zFywiAh7N0")

# Instance of class Movie - Lion
lion = media.Movie("Lion",
                   "A five-year-old Indian boy gets lost on the streets of Calcutta, thousands of kilometers from home. He survives many challenges before being adopted by a couple in Australia. 25 years later, he sets out to find his lost family.",
                   "https://upload.wikimedia.org/wikipedia/en/f/f0/Lion_%282016_film%29.png",
                   "https://www.youtube.com/watch?v=9DbLKvpjFQk")

# Instance of class Movie - Me Before You
me_before_you = media.Movie("Me Before You",
                            "A girl in a small town forms an unlikely bond with a recently-paralyzed man she's taking care of.",
                            "https://upload.wikimedia.org/wikipedia/en/f/fd/Me_Before_You_%28film%29.jpg",
                            "https://www.youtube.com/watch?v=YU9uIx2qhUs")

# Instance of class Movie - Love, Rosie
love_rosie = media.Movie("Love, Rosie",
                         "Rosie and Alex are best friends until Alex's family moves to America. They gamble everything to keep their love and friendship alive over the years and miles",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BMTk0Mzg1MTU1MF5BMl5BanBnXkFtZTgwMjU3ODI2MzE@._V1_UX182_CR0,0,182,268_AL_.jpg",
                         "https://www.youtube.com/watch?v=dOMTh9Jd81w")

# Instance of class Movie - The Perks of Being a Wallflower
perks_of_being_a_wallflower = media.Movie("The Perks of Being a Wallflower",
                                          "Charlie, a 15-year-old introverted bright Pittsburgh boy, enters high school and is nervous about his new life. He is befriended by his seniors who show him the way to the real world.",
                                          "https://upload.wikimedia.org/wikipedia/en/0/0b/The_Perks_of_Being_a_Wallflower_Poster.jpg",
                                          "https://www.youtube.com/watch?v=got-J4mBg4Y")

# Instance of class Movie - Paper Towns
paper_towns = media.Movie("Paper Towns",
                          "Quentin's girl crush Margo disappears one night mysteriously after leaving behind clues for him to look for her. Along with a bunch of friends, he sets out on a search mission trailing the clues.",
                          "https://upload.wikimedia.org/wikipedia/en/0/00/Paper_Towns_%28film%29.jpg",
                          "https://www.youtube.com/watch?v=rFGiHm5WMLk")

# Instance of class Movie - The Space Between Us
the_space_between_us = media.Movie("The Space Between Us",
                                   "The first human born on Mars travels to Earth for the first time, experiencing the wonders of the planet through fresh eyes. He embarks on an adventure with a street smart girl to discover how he came to be.",
                                   "https://upload.wikimedia.org/wikipedia/en/7/78/The_Space_Between_Us_poster.jpg",
                                   "https://www.youtube.com/watch?v=x73-573aWfs")

# An array is made of all the instances of Movie to pass as argument to open_movies_page function
movies=[toy_story,avatar,the_pursuit_of_happyness,la_la_land,my_name_is_khan,eternal_sunshine_of_the_spotless_mind,lion,me_before_you,love_rosie,perks_of_being_a_wallflower,paper_towns,the_space_between_us]
# To build the HTML file to display the website
fresh_tomatoes.open_movies_page(movies)

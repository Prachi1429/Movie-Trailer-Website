import webbrowser

# A Movie class is specified with properties of a movie
class Movie():
    # A constructor to create objects of movie
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
        # Arguments are assigned to the instance variables
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    
    def show_trailer(self):
        # Open the webbrowser with the link of the youtube url
        webbrowser.open(self.trailer_youtube_url)

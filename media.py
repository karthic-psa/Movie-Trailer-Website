import webbrowser


class Movie():
    "Instance Method to create space in memory for the new instance"
    def __init__(self, name, story, trailer, image):
        self.title = name
        self.storyline = story
        self.poster_image_url = image
        self.trailer_youtube_url = trailer

    # Instance Method to open the webrowser and play the youtube trailer.
    def showt(self):
        webbrowser.open(self.trailer_youtube_url)

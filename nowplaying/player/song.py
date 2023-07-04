class Song:
    def __init__(self, artists, album, title):
        self.album = album
        self.artists = artists
        self.title = title

    def __str__(self):
        return  u'' + ', '.join(self.artists) + ' - ' +\
            self.title + ' (' + self.album + ')'

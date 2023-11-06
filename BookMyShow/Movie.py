class Movie:
    def __init__(self) -> None:
        self.movieId : int = None
        self.movieName : str = None
        self.movieDurationInMinutes : int = None

    def getMovieId(self):
        return self.movieId
    
    def setMovieId(self, movieId : int):
        self.movieId = movieId

    def getMovieName(self):
        return self.movieName
    
    def setMovieName(self, movieName : str):
        self.movieName = movieName

    def getMovieDurationInMinutes(self):
        return self.movieDurationInMinutes
    
    def setMovieDurationInMinutes(self, movieDurationInMinutes : int):
        self.movieDurationInMinutes = movieDurationInMinutes

    
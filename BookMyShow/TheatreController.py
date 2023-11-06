from Enums.City import City
from Theatre import Theatre

class TheatreController:
    def __init__(self) -> None:
        self.cityVsTheatre: dict(City, Theatre) = {}
        self.allTheatre: list[Theatre] = []

    def addTheatre(self, theatre, city):
        self.allTheatre.append(theatre)
        theatres = self.cityVsTheatre.get(city, [])
        theatres.append(theatre)
        self.cityVsTheatre[city]=theatres

    def getAllShows(self, movie, city):
        theatreVsShows = {}
        theatres = self.cityVsTheatre.get(city)
        for theatre in theatres:
            givenMovieShows = []
            shows = theatre.getShows()
            for show in shows:
                if show.movie.getMovieId() == movie.getMovieId():
                    givenMovieShows.append(show)
            if givenMovieShows:
                theatreVsShows[theatre] = givenMovieShows
        return theatreVsShows

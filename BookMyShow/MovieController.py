from Movie import Movie
from Enums.City import City

class MovieController:
    def __init__(self) -> None:
        self.cityVsMovies = {}
        self.allMovies = []

    def addMovie(self, movie : Movie, city : City):
        self.allMovies.append(movie)
        movies = self.cityVsMovies.get(city, [])
        movies.append(movie)
        self.cityVsMovies[city] = movies

    def getMovieByName(self, movieName : str):
        for movie in self.allMovies:
            if movie.getMovieName() == movieName:
                return movie
        return None
    
    def getMoviesByCity(self, city: City):
        return self.cityVsMovies.get(city)
    
    #remove movie from a particular city, make use of cityVsMovies map

    #update movie from a particular city, make use of cityVsMovies map

    #crud operation based on movie id, make use of allMovies list
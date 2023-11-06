from MovieController import MovieController
from TheatreController import TheatreController

from Enums.City import City
from Enums.SeatCategory import SeatCategory

from Movie import Movie
from Theatre import Theatre
from Screen import Screen
from Show import Show
from Seat import Seat
from Booking import Booking

class BookMyShow:
    def __init__(self) -> None:
        self.movieController = MovieController()
        self.theatreController = TheatreController()

    def initialize(self):
        self.createMovies()
        self.createTheatres()
    
    def createMovies(self):
        # Create Movies
        avengers = Movie()
        avengers.setMovieId(1)
        avengers.setMovieName("AVENGERS")
        avengers.setMovieDurationInMinutes(128)

        baahubali = Movie()
        baahubali.setMovieId(2)
        baahubali.setMovieName("BAAHUBALI")
        baahubali.setMovieDurationInMinutes(180)

        # Add movies to cities
        self.movieController.addMovie(avengers, City.Bangalore)
        self.movieController.addMovie(avengers, City.Delhi)
        self.movieController.addMovie(baahubali, City.Bangalore)
        self.movieController.addMovie(baahubali, City.Delhi)

    def createTheatres(self):
        #creating 2 theatre
        avengerMovie = self.movieController.getMovieByName("AVENGERS")
        baahubali = self.movieController.getMovieByName("BAAHUBALI")

        inoxTheatre = Theatre()
        inoxTheatre.setTheatreId(1)
        inoxTheatre.setScreen(self.createScreen())
        inoxTheatre.setCity(City.Bangalore)
        inoxShows = []
        inoxMorningShow = self.createShows(1, inoxTheatre.getScreen()[0], avengerMovie, 8)
        inoxEveningShow = self.createShows(2, inoxTheatre.getScreen()[0], baahubali, 16)
        inoxShows.append(inoxMorningShow)
        inoxShows.append(inoxEveningShow)
        inoxTheatre.setShows(inoxShows)

        pvrTheatre = Theatre()
        pvrTheatre.setTheatreId(2)
        pvrTheatre.setScreen(self.createScreen())
        pvrTheatre.setCity(City.Delhi)
        pvrShows = []
        pvrMorningShow = self.createShows(3, pvrTheatre.getScreen()[0], avengerMovie, 13)
        pvrEveningShow = self.createShows(4, pvrTheatre.getScreen()[0], baahubali, 20)
        pvrShows.append(pvrMorningShow)
        pvrShows.append(pvrEveningShow)
        pvrTheatre.setShows(pvrShows)

        self.theatreController.addTheatre(inoxTheatre, City.Bangalore)
        self.theatreController.addTheatre(pvrTheatre, City.Delhi)

    def createScreen(self):
        screens = []
        screen1 = Screen()
        screen1.setScreenId(1)
        screen1.setSeats(self.createSeats())
        screens.append(screen1)
        return screens

    def createShows(self, showId, screen, movie, showStartTime):
        show = Show()
        show.setShowId(showId)
        show.setScreen(screen)
        show.setMovie(movie)
        show.setShowStartTime(showStartTime)  # 24 hrs time ex: 14 means 2pm and 8 means 8AM
        return show
    
    def createSeats(self):
        # Creating 100 seats for testing purposes, this can be generalized
        seats = []

        # 1 to 40: SILVER
        for i in range(40):
            seat = Seat()
            seat.setSeatId(i)
            seat.setSeatCategory(SeatCategory.SILVER)
            seats.append(seat)

        # 41 to 70: GOLD
        for i in range(40, 70):
            seat = Seat()
            seat.setSeatId(i)
            seat.setSeatCategory(SeatCategory.GOLD)
            seats.append(seat)

        # 71 to 100: PLATINUM
        for i in range(70, 100):
            seat = Seat()
            seat.setSeatId(i)
            seat.setSeatCategory(SeatCategory.PLATINUM)
            seats.append(seat)

        return seats

    def createBooking(self, userCity, movieName):
        # 1. Search for movies in the user's city
        movies = self.movieController.getMoviesByCity(userCity)

        # 2. Select the movie the user wants to see
        interestedMovie = None
        for movie in movies:
            if movie.getMovieName() == movieName:
                interestedMovie = movie

        # 3. Get all shows of the interested movie in the user's city
        showsTheatreWise = self.theatreController.getAllShows(interestedMovie, userCity)

        # 4. Select the particular show the user is interested in
        entry = next(iter(showsTheatreWise.items()))
        runningShows = entry[1]
        interestedShow = runningShows[0]

        # 5. Select the seat
        seatNumber = 30
        bookedSeats = interestedShow.getBookedSeatIds()
        if seatNumber not in bookedSeats:
            bookedSeats.append(seatNumber)
            # Start payment
            booking = Booking()
            myBookedSeats = []
            for screenSeat in interestedShow.getScreen().getSeats():
                if screenSeat.getSeatId() == seatNumber:
                    myBookedSeats.append(screenSeat)
            booking.setBookedSeats(myBookedSeats)
            booking.setShow(interestedShow)
        else:
            # Throw an exception
            print("Seat already booked, please try again")
            return

        print("BOOKING SUCCESSFUL")
    
if __name__ == "__main__":
    book_my_show = BookMyShow()
    book_my_show.initialize()
    # User 1
    book_my_show.createBooking(City.Bangalore, "BAAHUBALI")
    # User 2
    book_my_show.createBooking(City.Bangalore, "BAAHUBALI")
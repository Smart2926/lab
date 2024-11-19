from enum import Enum

class Genre(Enum):
    ACTION = "Action"
    COMEDY = "Comedy"
    DRAMA = "Drama"
    FANTASY = "Fantasy"
    POLUNYCHKA = "Polunychka"

class Movie:
    def __init__(self, id, title, genre, ranking, release_date, character_number, ticket_price, comment=""):
        self.id = id
        self.title = title
        self.genre = genre
        self.ranking = ranking
        self.release_date = release_date
        self.character_number = character_number
        self.ticket_price = ticket_price
        self.comment = comment

    def __del__(self):
        print(f"Deleting movie: {self.title}")

    def display_info(self):
        print(f"ID: {self.id}, Title: {self.title}, Genre: {self.genre.value}, Ranking: {self.ranking}, "
              f"Release Date: {self.release_date}, Characters: {self.character_number}, "
              f"Ticket Price: {self.ticket_price}, Comment: {self.comment}")

class Cinema:
    def __init__(self, name, location, krysha):
        self.name = name
        self.location = location
        self.krysha = krysha
        self.movies = []

    def __del__(self):
        print(f"Deleting cinema: {self.name}")

    def add_movie(self, movie):
        self.movies.append(movie)
        print(f"Added movie: {movie.title}")

    def calculate_profit(self, movie, tickets_sold):
        profit = movie.ticket_price * tickets_sold
        print(f"Profit for {movie.title} on specific day: {profit}")
        return profit

    def select_movie(self, genre=None, min_ranking=None):
        selected_movies = []
        for movie in self.movies:
            if (genre is None or movie.genre == genre) and (min_ranking is None or movie.ranking >= min_ranking):
                selected_movies.append(movie)
        return selected_movies

    
    def _is_earlier_date(self, date1, date2):
        year1, month1, day1 = map(int, date1.split("-"))
        year2, month2, day2 = map(int, date2.split("-"))
        if year1 != year2:
            return year1 < year2
        elif month1 != month2:
            return month1 < month2
        else:
            return day1 < day2
    def sort_movies_by_release_date(self):
        n = 0
        for _ in self.movies:
            n += 1
        for i in range(n):
            for j in range(0, n - i - 1):
                if not self._is_earlier_date(self.movies[j].release_date, self.movies[j + 1].release_date):
                    self.movies[j], self.movies[j + 1] = self.movies[j + 1], self.movies[j]
        print("Movies sorted by release date:")
        for movie in self.movies:
            movie.display_info()

    def display_movies(self):
        print(f"Movies in {self.name}:")
        for movie in self.movies:
            movie.display_info()

    def evaluate_profitability(self, attendance_per_genre):
        profitable_genres = {}
        for genre in Genre:
            genre_movies = [m for m in self.movies if m.genre == genre]
            if not genre_movies:
                continue
            
            attendance = attendance_per_genre.get(genre, 0)
            
            total_income = 0
            for m in genre_movies:
                total_income += m.ticket_price * attendance
            
            net_income = total_income - self.krysha
            profitability = (net_income / self.krysha) * 100  

            if profitability >= 20:  
                profitable_genres[genre] = profitability
                print(f"{genre.value} is profitable with {profitability:.2f}% profitability.")

            else:
                print(f"{genre.value} is not profitable, only {profitability:.2f}% profitability.")

        return profitable_genres
    
def main():
    movie1 = Movie(1, "Inception", Genre.ACTION, 8.8, "2010-07-16", 10, 12.5, "A mind-bending thriller")
    movie2 = Movie(2, "The Godfather", Genre.DRAMA, 9.2, "1972-03-24", 12, 10.0, "Classic mafia story")
    movie3 = Movie(3, "Toy Story", Genre.POLUNYCHKA, 8.3, "1995-11-22", 5, 15.0, "Fun for all ages")

    cinema = Cinema("Multiplex", "Victoria Gardens", krysha=500)

    cinema.add_movie(movie1)
    cinema.add_movie(movie2)
    cinema.add_movie(movie3)

    cinema.display_movies()

    cinema.sort_movies_by_release_date()

    attendance_per_genre = {
        Genre.ACTION: 50,
        Genre.DRAMA: 30,
        Genre.COMEDY: 40,
        Genre.FANTASY: 20,
        Genre.POLUNYCHKA: 100,
    }
    cinema.evaluate_profitability(attendance_per_genre)

main()


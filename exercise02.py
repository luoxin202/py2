import sqlite3


# Function to create the SQLite database and table
def create_database_and_table():
    conn = sqlite3.connect('stephen_king_adaptations.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS stephen_king_adaptations_table (
                        movieID INTEGER PRIMARY KEY AUTOINCREMENT,
                        movieName TEXT,
                        movieYear INTEGER,
                        imdbRating REAL
                    )''')

    conn.commit()
    conn.close()


# Function to read the file and insert data into the database
def insert_data_from_file_to_db(filename):
    conn = sqlite3.connect('stephen_king_adaptations.db')
    cursor = conn.cursor()

    with open(filename, 'r') as file:
        for line in file:
            movie_data = line.strip().split(',')
            cursor.execute(
                "INSERT INTO stephen_king_adaptations_table (movieName, movieYear, imdbRating) VALUES (?, ?, ?)",
                (movie_data[0], int(movie_data[1]), float(movie_data[2])))

    conn.commit()
    conn.close()


# Function to search for movies in the database
def search_movies():
    conn = sqlite3.connect('stephen_king_adaptations.db')
    cursor = conn.cursor()

    while True:
        print("Options:")
        print("1. Search by movie name")
        print("2. Search by movie year")
        print("3. Search by movie rating")
        print("4. STOP")

        choice = input("Enter your choice: ")

        if choice == '1':
            movie_name = input("Enter movie name: ")
            cursor.execute("SELECT * FROM stephen_king_adaptations_table WHERE movieName=?", (movie_name,))
            result = cursor.fetchone()
            if result:
                print("Movie found:")
                print(f"Movie Name: {result[1]}")
                print(f"Movie Year: {result[2]}")
                print(f"IMDB Rating: {result[3]}")
            else:
                print("No such movie exists in our database")

        elif choice == '2':
            movie_year = int(input("Enter movie year: "))
            cursor.execute("SELECT * FROM stephen_king_adaptations_table WHERE movieYear=?", (movie_year,))
            results = cursor.fetchall()
            if results:
                print("Movies found:")
                for result in results:
                    print(f"Movie Name: {result[1]}")
                    print(f"Movie Year: {result[2]}")
                    print(f"IMDB Rating: {result[3]}")
            else:
                print("No movies were found for that year in our database.")

        elif choice == '3':
            rating = float(input("Enter minimum rating: "))
            cursor.execute("SELECT * FROM stephen_king_adaptations_table WHERE imdbRating >= ?", (rating,))
            results = cursor.fetchall()
            if results:
                print("Movies found:")
                for result in results:
                    print(f"Movie Name: {result[1]}")
                    print(f"Movie Year: {result[2]}")
                    print(f"IMDB Rating: {result[3]}")
            else:
                print("No movies at or above that rating were found in the database.")

        elif choice == '4':
            break

        else:
            print("Invalid choice. Please select a valid option.")

    conn.close()


# Main program
if __name__ == '__main__':
    create_database_and_table()
    insert_data_from_file_to_db('stephen_king_adaptations.txt')
    search_movies()
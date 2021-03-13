MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []


# You may want to create a function for this code
def add_movie():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })

#  listing movies
def list_movies():
    for movie in movies:
        print(movie['title'])

#  finding movies
def find_movies(list_movies):
    search_title = input('Enter movie title you are looking for: ')

    for movie in movies:
        if search_title.lower() == movie['title'].lower():
            print(movie['title'])

# And another function here for the user menu
def user_menu(): 
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == "a":
            add_movie()
        elif selection == "l":
            list_movies()
        elif selection == "f":
            find_movies()
        else:
            print('Unknown command. Please try again.')

        selection = input(MENU_PROMPT)


# Remember to run the user menu function at the end!
user_menu()
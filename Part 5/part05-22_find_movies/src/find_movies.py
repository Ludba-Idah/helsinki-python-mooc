def find_movies(database: list, search_term: str):

    matching_movies = []

    for movie in database:

        if search_term.lower() in movie["name"].lower():
            
            matching_movies.append(movie)
            
    return matching_movies

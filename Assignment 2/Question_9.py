'''
Program to store details of 3 movies in a dictionary.
'''

movies = {}
for i in range(3):
    print(f"Movie {i+1}")
    title = input("Title: ")
    director = input("Director: ")
    year = int(input("Release Year: "))
    rating = float(input("Rating: "))
    movies[f"Movie{i+1}"] = {"Title": title, "Director": director, "Year": year, "Rating": rating}

print("\nMovie Details:")
for k, v in movies.items():
    print(k, ":", v)

animal_movies = ('The Lion King', 'Jurassic Park', 'Finding Nemo')

# Write your code here
temp_movies = list(animal_movies)

movies_to_add = ("Dumbo", "Zootopia")

temp_movies += movies_to_add

animal_movies = tuple(temp_movies)

del temp_movies

print("Updated animal movies:", animal_movies)
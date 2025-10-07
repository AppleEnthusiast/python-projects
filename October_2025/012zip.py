movies = ["Inception","Interstellar","Matrix","The Dark Knight"]
ratings = [9.0,8.6,8.7,9.1]

print("Iterable:")
print(zip(movies,ratings))
print()

print("for-loop:")
for movie,rating in zip(movies,ratings):
	print(movie,":",rating)
print()

print("Tuple:")
print(tuple(zip(movies,ratings)))
print()

print("List:")
print(list(zip(movies,ratings)))
print()

print("Dictionary:")
print(dict(zip(movies,ratings)))
print()


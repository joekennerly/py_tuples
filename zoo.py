# Original tuple
zoo = ("monkey", "chicken", "gator", "zebra", "snake")

# Index of chicken
i = zoo.index("chicken")
print(i)

# Create variables for each element
(monkey, chicken, gator, zebra, snake) = zoo
print(monkey)

# Convert tuple to a list
zoo_list = list(zoo)
print(zoo_list)

# Add a new list of animals
more_animals = ["lion", "peacock", "baboon"]
zoo_list.extend(more_animals)
print(zoo_list)

# Back to tuple
tuple_list = tuple(zoo_list)
print(tuple_list)
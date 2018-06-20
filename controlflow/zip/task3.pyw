# Use zip to create a dictionary cast that uses names as keys and heights as values.
cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = dict(zip(cast_names,cast_heights))# replace with your code
print(cast)


# Unzip the cast tuple into two names and heights tuples.


cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

# define names and heights here
names,heights=zip(*cast)

print(names)
print(heights)

# Use zip to transpose data from a 4-by-3 matrix to a 3-by-4 matrix.
#  There's actually a cool trick for this! Feel free to look at the solutions if you can't figure it out.


data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

data_transpose = tuple(zip(*data))# replace with your code
print(data_transpose)




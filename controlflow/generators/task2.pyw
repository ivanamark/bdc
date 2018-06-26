# Here's a cool concept that combines generators and list comprehensions!
#  You can actually create a generator in the same way you'd normally write a list comprehension,
#   except with parentheses instead of square brackets. For example:

sq_list = [x**2 for x in range(10)]  # this produces a list of squares
print(sq_list)
sq_iterator = (x**2 for x in range(10))  # this produces an iterator of squares

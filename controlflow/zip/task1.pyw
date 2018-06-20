letters = ['a', 'b', 'c']
nums = [1, 2, 3]

for letter, num in zip(letters, nums):
    print("{}: {}".format(letter, num))
    # create a list
print(list(zip(letters,nums)))
# create a dictionary
print(dict(zip(letters,nums)))

# you can also unzip a list using an asterisk.
some_list = [('a', 1), ('b', 2), ('c', 3)]
letters, nums = zip(*some_list)    
print(letters)
print(nums)

# enumerate is a built in function that returns an iterator of tuples containing indices and values of a list. You'll often use this when you want the index along with each element of an iterable in a loop.

letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i, letter)

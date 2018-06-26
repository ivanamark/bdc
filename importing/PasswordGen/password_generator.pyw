# Write a function called generate_password that selects three random words from the
#  list of words word_list and concatenates them into a single string. Your function should 
#  not accept any arguments and should reference the global 
# variable word_list to build the password.


# Use an import statement at the top

import random
import os
PasswordGen = os.path.dirname(os.path.abspath(__file__))
word_file = os.path.join(PasswordGen, "words.txt")
# import os
# THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
# my_file = os.path.join(THIS_FOLDER, 'myfile.txt')
# word_file = "words.txt"
word_list = []

#fill up the word_list
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)

# Add your function generate_password here
# It should return a string consisting of three random words 
# concatenated together without spaces
def generate_password():
    return "".join(random.sample(word_list,3))


# test your function
print(generate_password())
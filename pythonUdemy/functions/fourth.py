# Create a function that takes two strings as arguments and concatenates them.
#  Example: Given the strings John and Smith, the function should output John Smith.
def concatenate(s1, s2):
    s = s1 + " " + s2
    return s
 
print(concatenate("John", "Smith"))
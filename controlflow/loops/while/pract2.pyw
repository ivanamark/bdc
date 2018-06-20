# Practice: Factorials with While Loops
# Start with a sample number for first test - change this when testing your code more!
number = 6    
# We'll always start with our product equal to the number
product = number
while number>1:
    product=product*(number-1)
    number-=1
print(product)

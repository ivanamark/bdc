keys = ('name', 'age', 'food')
values = ('Monty', 42, 'spam')    
dict = {keys[i]: values[i] for i in range(len(keys))}
print(dict)
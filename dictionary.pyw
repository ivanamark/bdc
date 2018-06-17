population = {'Shanghai':17.8,'Istanbul':13.3,'Karachi':13.0,'Mumbai':12.5}
print(population)
print(population['Istanbul'])

animals = {'dogs': [20, 10, 15, 8, 32, 15], 'cats': [3,4,2,8,2,4], 'rabbits': [2, 3, 3], 'fish': [0.3, 0.5, 0.8, 0.3, 1]}

print(animals['dogs'][3])
print(animals['dogs'])

elements = {"hydrogen": {"number": 1,
                         "weight": 1.00794,
                         "symbol": "H"},
              "helium": {"number": 2,
                         "weight": 4.002602,
                         "symbol": "He"}}


helium = elements["helium"]  # get the helium dictionary
hydrogen_weight = elements["hydrogen"]["weight"]  # get hydrogen's weight
print(hydrogen_weight)    

elements_sec = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H','is_noble_gas':False},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He','is_noble_gas':True}}
            
print(elements_sec['hydrogen']['is_noble_gas'])
print(elements_sec['helium']['is_noble_gas'])
                     
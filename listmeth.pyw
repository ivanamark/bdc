new_str = "\n".join(["fore", "aft", "starboard", "port"])
print(new_str)

letters = ['a', 'b', 'c', 'd']
letters.append('z')
print(letters)

a = [1, 5, 8]
b = [2, 6, 9, 10]
c = [100, 200]

print(max([len(a), len(b), len(c)]))
print(min([len(a), len(b), len(c)]))

names = ["Carol", "Albert", "Ben", "Donna"]
print(" & ".join(sorted(names)))
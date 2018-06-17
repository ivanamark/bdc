x = [1,2,3,4]
out = []
for item in x:
    out.append(item**2)
print(out)
[1, 4, 9, 16]
# vs.
x = [1,2,3,4]
out = [item**2 for item in x]
print(out)
[1, 4, 9, 16]
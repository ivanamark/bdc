fruit=["orange","strawberry","apple"]
foods=["apple","apple","humus","toast"]
fruit_count=0
for food in foods:
    if food not in fruit:
        print("Not a fruit")
        continue  #here we terminate iteration if the food is not found in fruit
    fruit_count += 1
    print("Found a fruit")
print("Total fruit: ",fruit_count)        
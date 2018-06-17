points = 174  # use this input to make your submission
wooden_rabbit="wooden rabbit"
no_prize="Oh dear, no prize this time."
wafer_thin_mint="wafer-thin mint"
penguin="penguin"
if 1<=points<=50:
    prize=wooden_rabbit
elif 51<=points<=150:
    print(no_prize)
elif 151<=points<=180:
    prize=wafer_thin_mint
elif 181<=points<=200:
    prize=penguin
else:
    print('You can\'t have more than 200 points' )
# write your if statement here

result="Congratulations! You won a {}!".format(prize)
print(result)

points_1 = 174  # use this input when submitting your answer

# set prize to default value of None
prize_1 = None

# use the value of points to assign prize to the correct prize name
if points_1 <= 50:
    prize_1 = "wooden rabbit"
elif 151 <= points_1 <= 180:
    prize_1 = "wafer-thin mint"
elif points_1 >= 181:
    prize_1 = "penguin"

# use the truth value of prize to assign result to the correct message
if prize_1:
    result_1 = "Congratulations! You won a {}!".format(prize)
else:
    result_1 = "Oh dear, no prize this time."

print(result)
# Write a function named readable_timedelta. The function should take one argument, 
# an integer days, and return a string that says how many weeks and days that is. 
def readable_timedelta(days):
    week=days // 7
    day=days % 7
    return "{} week(s) and {} day(s).".format(week,day)
# test your function
print(readable_timedelta(10))

egg_count = 0

def buy_eggs(count):
    return count + 12  # purchase a dozen eggs
egg_count = buy_eggs(egg_count)
print(egg_count)
    
# Suppose you want to count from some number start_num by another number count_by until you hit a final number end_num. Use break_num as the variable that you'll change each time through the loop.

# Before the loop, what do you want to set break_num equal to? How do you want to change break_num each time through the loop? What condition will you use to see when it's time to stop looping?

# After the loop is done, print out break_num, showing the value that indicated it was time to stop looping.


start_num = 6#provide some start number
end_num = 10#provide some end number that you stop when you hit
count_by =2 #provide some number to count by 
break_num=0
# write a while loop that uses break_num as the ongoing number to 
#   check against end_num
while start_num<=end_num-count_by:
    start_num+=1
    break_num=start_num+count_by
    
print(break_num)

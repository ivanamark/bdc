# Write a for loop that iterates over a list of strings, tokens, and counts how many of them are XML tags. 

tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0
for token in tokens:
    if token[0]=="<"and token[len(token)-1]==">":
       count+=1
# write your for loop here


print(count)

# Write some code, including a for loop, that iterates over a list of strings and creates a single string, html_str, which is an HTML list. For example, if the list is items = ['first string', 'second string'], printing html_str should output:

# <ul>
# <li>first string</li>
# <li>second string</li>
# </ul>
items = ['first string', 'second string']
html_str = "<ul>\n" 
for item in items:
    html_str+="<li>{}</li>\n".format(item)
html_str+="</ul>"
print(html_str)
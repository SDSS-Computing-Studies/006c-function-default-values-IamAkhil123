#!python3

x = " "
def title(x):
 if x == " ":
  x = "="
 return(x+x+x+x+x+x+x+x+x+"\n"+x+" Title "+x+"\n"+x+x+x+x+x+x+x+x+x)

y = title(x)
print(y)

"""
Create a function called title that creates a single line of output to display the word
"Title" with a box around it.  
The function will have 1 optional input:
symbol : string.  The symbolt to use as the border. Default symbol is "="

The return value is the output string with escaped line breaks.

example assertion:
assert title("*") == "*********\n* Title *\n*********"
assert title() == "=========\n= Title =\n========="
(2 points)
"""




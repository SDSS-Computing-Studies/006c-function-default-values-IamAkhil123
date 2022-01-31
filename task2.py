#!python3

x = 2
y = " "

def multiply(x,y):
 if y == " ":
  y = 12
 list = []
 p = 0
 x1 = x
 while True:
   list.append(x)
   x = x + x1
   p = p + 1 
   if p == y:
    return(list)
 
 
t = multiply(x,y)
print(t)
"""
Create a function called multiplication that takes 2 input paremeters:
number: integer.  
end: integer. It should have a default value of 12.

The function will create a list that stores the multiplication tables for the number, and ends at end.

return value:
list.  The multiplication tables starting at a multiple of 1 and ending at whatever the default value is.

example assertion:
assert multiplication(5) == [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
assert multiplication(2,5) == [2, 4, 6, 8, 10]
"""
total = 10
greet = 'Hello'
both = total + greet
print(both)

# answer
#Traceback (most recent call last):
#  File "d:\IIT NOTES\Degree\Year 1\Semester 1\Software Development 1\week 02\tut 1&2 3.b.2.py", line 3, in <module>
#    both = total + greet
#           ~~~~~~^~~~~~~
#TypeError: unsupported operand type(s) for +: 'int' and 'str'

total = str(10)
greet = 'Hello'
both = total + greet
print(both)

#answer
#10Hello

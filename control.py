'''
Control statements:
In Python, Loops are used to iterate repeatedly over a block of code. In order to change the way a loop is executed
from its usual behavior, control statements are used. Control statements are used to control the flow of the
execution of the loop based on a condition.
There are three types of control statements

* Pass statement:
Pass Statement: We use pass statement to write empty loops. Pass is also used for empty
control statements, functions and classes.
'''
# example
for letter in 'asifshahrukh':
    pass
print('Last Letter :', letter)

'''
* Continue statement: It returns the control to the beginning of the loop.
'''
# example
for letter in 'vn2solutions':
    if letter == 'o' or letter == 's':
         continue
    print('Current Letter :', letter)
    var = 10

'''
* Break statement:It brings control out of the loop.
'''
# example
for letter in 'asifshahrukh':
    if letter == 's' or letter == 'h':
        break

print('Current Letter :', letter)
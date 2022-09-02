'''
Decision Making:
Decision-making is anticipation of conditions occurring while execution of the program and specifying actions taken
according to the conditions. Decision structures evaluate multiple expressions which produce TRUE or FALSE as outcome.
Decisions in a program are used when the program has conditional choices to execute a code block.
For example when we see the traffic signal we see green, yellow and red signal. We pass through the red when the signal
is green, else we will stop when the signal is red.
Python has four conditional statement, they are if, else, elif and nested.
* If statement consists of a Boolean expression which results are either TRUE or FALSE, followed by one or more
  statements.'''
# example
a = 15

if a > 10:
   print("a is greater")

'''
* Else also contains a Boolean expression. The if statement is followed by an optional else statement & if the 
  expression results in FALSE, then else statement gets executed
'''
# example
a = 15
b = 20

if a > b:
   print("a is greater")
else:
   print("b is greater")

'''
* elif - is a keyword used in Python replacement of else if to place another condition in the program. 
  This is called chained conditional statement.
'''
# example
a = 15
b = 15

if a > b:
   print("a is greater")
elif a == b:
   print("both are equal")
else:
   print("b is greater")

'''
* Nested if is a statement where there is an if condition inside another if condition. Python allows us to stack any 
  number of if statements inside the block of another if statements. they are useful to make a series of decision.
'''
# example
num1 = int(input())
num2 = int(input())

if num1 >= num2:
    if num1 == num2:
        print(f'{num1} and {num2} are equal')
    else:
        print(f'{num1} is greater than {num2}')
else:
    print(f'{num1} is smaller than {num2}')

'''
Loops:
  Loops are similar to conditional statements because they run on true/false value set. The loop iterates while the 
  condition is true and terminates when it is false. Its a great technique to reuse the code and therefore limit 
  the amount of statements a program needs.
  
* counter: Its a variable that is incremented or decremented each time a loop repeat.
It can be used to control the execution of the loop and it should be initialized before entering the loop.

There are three types of loops
* While loop:
It is known as indefinite or conditional loops. They will keep on iterating until the condition is true.
It will only come out of the loop once the condition is met false.
 '''
# example

count = 0
while count < 9:
    print('the count is: ', count)
    count = count + 1

# example of else in while loop

count = 0
while (count < 3):
    count = count + 1
    print("Hello world")
else:
    print("my world")
'''
* For Loop:
For loops are used for sequential traversal. For example: traversing a list or string or array etc.
'''

# example

n = 4
for i in range(0, n):
    print(i)

list = ["my", "name", "asif"]
for index in range(len(list)):
    print(list[index])
else:
    print("Asif shahrukh")

'''
* Nested loop:
A nested loop is a loop inside the body of the outer loop. The inner or outer loop can be any type, such as a while 
loop or for loop. For example, the outer for loop can contain a while loop and vice versa.
'''
# example

names = ['asif', 'chetan', 'manoj']
for name in names:
    count = 0
    while count < 5:
        print(name, end=' ')
        count = count + 1
    print()

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
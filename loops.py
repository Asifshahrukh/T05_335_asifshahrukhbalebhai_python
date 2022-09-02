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

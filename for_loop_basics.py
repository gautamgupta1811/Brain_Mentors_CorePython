# loops --> for, while

a = ["mango", "orange", "banana", "apple", "papaya"]

for item in a:
    print(item)


# for (int i=0;i<n;i++)
# start, stop, step
for i in range(0,34,1):
    print(i)

# for variable in list:
#   statement

for i in range(2,6):
    print(i)

# for i in range(stop)
# for i in range(start, stop)
# for i in range(start, stop, step)
# for i in some_list

'''
*
* *
* * *
* * * *
'''

for i in range(1,5):
    for j in range(i):
        print("* ", end="")
    print()

for i in range(1,5):
    print("* "*i)

'''
* * * *
* * *
* *
*
'''
'''
1
2 2
3 3 3
4 4 4 4
'''

for i in range(5):
    print(str(i)*i)

'''
AAAA
BBBB
CCCC
DDDD
'''

for i in range(4):
    print(chr(65+i)*4)
'''
A
B B
C C C
D D D D
'''
'''
  *
 ***
*****
 ***
  *
'''

for i in range(3):
    print(" "*(3-(i+1))+"*"*(2*i+1))
for i in range(1, -1, -1):
    print(" "*(3-(i+1))+"*"*(2*i+1))
'''
*****
   *
  *
 *
*****
'''
for i in range(4):
    for j in range(4):
        if i==0 or i == 3 or j ==0 or j == 3:
            print("*", end="")
        else:
            print(" ", end="")
    print()


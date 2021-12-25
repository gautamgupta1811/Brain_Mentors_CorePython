Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> random.random()
0.25993250532560963
>>> random.random()
0.6168611316326506
>>> random.random()
0.7956607872668687
>>> random.random()
0.6302145724932776
>>> random.random()
0.954102257281797
>>> random.randint(2, 60)
56
>>> random.randint(2, 60)
18
>>> random.randint(2, 60)
51
>>> random.randint(2, 60)
47
>>> random.randint(2, 60)
27
>>> random.randint(2, 60)
44
>>> random.randint(2, 60)
14
>>> random.randint(2, 60)
44
>>> a = ["apple", "banana" ,"orange", "strawberry"]
>>> random.choice(a)
'apple'
>>> random.choice(a)
'strawberry'
>>> random.choice(a)
'apple'
>>> random.choice(a)
'orange'
>>> random.choice(a)
'strawberry'
>>> random.choice(a)
'strawberry'
>>> random.choice(a)
'apple'
>>> random.randrange(1,8)
1
>>> random.randrange(1,8)
5
>>> random.randrange(1,8)
7
>>> random.randrange(1,8)
2
>>> random.randrange(1,8)
4
>>> random.randrange(1,8)
7
>>> random.randrange(1,8)
6
>>> random.randrange(1,8)
7
>>> random.randrange(1,8)
6
>>> random.randrange(1,8)
6
>>> random.randrange(1,8)
5
>>> import math
>>> math.factorial()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    math.factorial()
TypeError: factorial() takes exactly one argument (0 given)
>>> math.factorial(5)
120
>>> math.gcd(2, 7)
1
>>> math.pi
3.141592653589793
>>> math.prod()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    math.prod()
AttributeError: module 'math' has no attribute 'prod'
>>> 
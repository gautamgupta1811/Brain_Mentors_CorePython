Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = "hello"
>>> a = 'hello'
>>> a
'hello'
>>> a = "hello"
>>> a
'hello'
>>> a = "hello'
SyntaxError: EOL while scanning string literal
>>> string = "HELLO THIS IS PYTHON PROGRAMMING"
>>> string.lower()
'hello this is python programming'
>>> string_1 = "Hello this IS python Programming"
>>> string_1.lower()
'hello this is python programming'
>>> string = "this is python programming"
>>> string.upper()
'THIS IS PYTHON PROGRAMMING'
>>> string_1.upper()
'HELLO THIS IS PYTHON PROGRAMMING'
>>> string_1.title()
'Hello This Is Python Programming'
>>> string_1.captalize()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    string_1.captalize()
AttributeError: 'str' object has no attribute 'captalize'
>>> string_1.capitalize()
'Hello this is python programming'
>>> age = "23"
>>> age.isnum()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    age.isnum()
AttributeError: 'str' object has no attribute 'isnum'
>>> age.isndigit()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    age.isndigit()
AttributeError: 'str' object has no attribute 'isndigit'
>>> age.isdigit()
True
>>> string_1.isdigit()
False
>>> a = "ghgkjhk"
>>> a.isalpha()
True
>>> age.isalpha()
False
>>> string_
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    string_
NameError: name 'string_' is not defined
>>> string_1
'Hello this IS python Programming'
>>> string_1.isalpha()
False
>>> "Python".isalpha()
True
>>> "Python!".isalpha()
False
>>> "dfgh1234".isalnum()
True
>>> "gbhn 34 gbh".isalnum()
False
>>> "Python".isalnum()
True
>>> "Python".count("P")
1
>>> "Python is programming language".count("P")
1
>>> "Python is programming language".count("p")
1
>>> "Python is programming language".count("language")
1
>>> "Python is programming language".count(" ")
3
>>> "Python is programming language".count("on")
1
>>> "Python is programming language".lower().count("p")
2
>>> "Python is programming language".lower()
'python is programming language'
>>> "Python is a high level language".endswith("age")
True
>>> "Python is a high level language".endswith("ag")
False
>>> "Python is a high level language".endswith("language")
True
>>> "Python is a high level language".endswith("lanuage")
False
>>> "Python is a high level language".startswith("Python")
True
>>> "Python is a high level language".startswith("python")
False
>>> "          Python is                 ".strip()
'Python is'
>>> "###########Python is #########".strip("#")
'Python is '
>>> "###########Python is #########".strip(1)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    "###########Python is #########".strip(1)
TypeError: strip arg must be None or str
>>> "###########Python is #########".strip("1")
'###########Python is #########'
>>> "###########Python is #########".lstrip("#")
'Python is #########'
>>> "###########Python is #########".rstrip("#")
'###########Python is '
>>> "###########Python is #########".strip("is")
'###########Python is #########'
>>> "###########Python isisisisis".strip("is")
'###########Python '
>>> "###########Python is".strip("is")
'###########Python '
>>> 
===================== RESTART: D:/Deceber/Core_Python/ques_2.py =====================
Enter any string:      12345    reefrt 
12345    reefrt
12345    reefrt
>>> 
===================== RESTART: D:/Deceber/Core_Python/ques_2.py =====================
Enter any string:  b r a i n  
b r a i n
b r a i n
>>> "w###########Python is".strip("#")
'w###########Python is'
>>> "P####ython i###s'
SyntaxError: EOL while scanning string literal
>>> "P####ython i###s"
'P####ython i###s'
>>> "P####ython i###s".strip("#")
'P####ython i###s'
>>> 
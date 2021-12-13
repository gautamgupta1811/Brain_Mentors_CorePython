Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = []
>>> type(a)
<class 'list'>
>>> a = list()
>>> type(a)
<class 'list'>
>>> a = [1,2,3,3.0,5.6,"hello", "world", True, False]
>>> #indexing
>>> a[0]
1
>>> a[2]
3
>>> a[-1]
False
>>> a[-2]
True
>>> #slicing
>>> a[0:4]
[1, 2, 3, 3.0]
>>> a[1:8]
[2, 3, 3.0, 5.6, 'hello', 'world', True]
>>> a[1:8:2]
[2, 3.0, 'hello', True]
>>> a[::-1]
[False, True, 'world', 'hello', 5.6, 3.0, 3, 2, 1]
>>> # list pre-defined functions
>>> a
[1, 2, 3, 3.0, 5.6, 'hello', 'world', True, False]
>>> a.append(2)
>>> a
[1, 2, 3, 3.0, 5.6, 'hello', 'world', True, False, 2]
>>> a.extend([1,2,3,4])
>>> a
[1, 2, 3, 3.0, 5.6, 'hello', 'world', True, False, 2, 1, 2, 3, 4]
>>> a.insert(3, "new element")
>>> a
[1, 2, 3, 'new element', 3.0, 5.6, 'hello', 'world', True, False, 2, 1, 2, 3, 4]
>>> a.insert(0, "first element")
>>> a
['first element', 1, 2, 3, 'new element', 3.0, 5.6, 'hello', 'world', True, False, 2, 1, 2, 3, 4]
>>> a[1] = "new assigned element"
>>> a
['first element', 'new assigned element', 2, 3, 'new element', 3.0, 5.6, 'hello', 'world', True, False, 2, 1, 2, 3, 4]
>>> a[-1] = "last element changed"
>>> a
['first element', 'new assigned element', 2, 3, 'new element', 3.0, 5.6, 'hello', 'world', True, False, 2, 1, 2, 3, 'last element changed']
>>> a[2:4] = ["ele 1", "ele 2"]
>>> a
['first element', 'new assigned element', 'ele 1', 'ele 2', 'new element', 3.0, 5.6, 'hello', 'world', True, False, 2, 1, 2, 3, 'last element changed']
>>> a[2:4] = ["ele 1"]
>>> a
['first element', 'new assigned element', 'ele 1', 'new element', 3.0, 5.6, 'hello', 'world', True, False, 2, 1, 2, 3, 'last element changed']
>>> a[2:4] = ["ele A", "ele B", "ele C"]
>>> a
['first element', 'new assigned element', 'ele A', 'ele B', 'ele C', 3.0, 5.6, 'hello', 'world', True, False, 2, 1, 2, 3, 'last element changed']
>>> a.pop()
'last element changed'
>>> a.remove(True)
>>> a
['first element', 'new assigned element', 'ele A', 'ele B', 'ele C', 3.0, 5.6, 'hello', 'world', False, 2, 1, 2, 3]
>>> a.pop(3)
'ele B'
>>> a.index(False)
8
>>> a.count(2)
2
>>> a.count(1)
1
>>> a.reverse()
>>> a
[3, 2, 1, 2, False, 'world', 'hello', 5.6, 3.0, 'ele C', 'ele A', 'new assigned element', 'first element']
>>> b = "ger"
>>> b = [5,6,3,4,2,5,7,3,26,1,24]
>>> b.sort()
>>> b
[1, 2, 3, 3, 4, 5, 5, 6, 7, 24, 26]
>>> b.sort(reverse=True)
>>> b
[26, 24, 7, 6, 5, 5, 4, 3, 3, 2, 1]
>>> b  = ["a", "c", "e", "f", "a", "u", "f" ,"p"]
>>> b.sort()
>>> b
['a', 'a', 'c', 'e', 'f', 'f', 'p', 'u']
>>> c = [1,"a", "v", 2, 3.0]
>>> c.sort()
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    c.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
>>> sorted(c)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    sorted(c)
TypeError: '<' not supported between instances of 'str' and 'int'
>>> sorted(b)
['a', 'a', 'c', 'e', 'f', 'f', 'p', 'u']
>>> a.clear()
>>> a
[]
>>> print("first name", first_name, last_name,sep="+")
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    print("first name", first_name, last_name,sep="+")
NameError: name 'first_name' is not defined
>>> print("first name", "Brain", "Mentors",sep="+")
first name+Brain+Mentors
>>> print("first name"+ "Brain", "Mentors",sep="+")
first nameBrain+Mentors
>>> a = "this is some random string"
>>> a.split()
['this', 'is', 'some', 'random', 'string']
>>> a = "this#is#some#random#string"
>>> a.split("#")
['this', 'is', 'some', 'random', 'string']
>>> a = "this is some random string"
>>> a.split("#")
['this is some random string']
>>> b = "this", "again", "is", "some", "list"]
SyntaxError: invalid syntax
>>> b = ["this", "again", "is", "some", "list"]
>>> "+".join(b)
'this+again+is+some+list'
>>> " ".join(b)
'this again is some list'
>>> 
===================== RESTART: D:/Deceber/Core_Python/ques_4.py =====================
this
is
some
programming
class
>>> #nested list
>>> a = [1,2,3,[4,5,6]]
>>> a
[1, 2, 3, [4, 5, 6]]
>>> type(a)
<class 'list'>
>>> a[1]
2
>>> type(a[1])
<class 'int'>
>>> type(a[-1])
<class 'list'>
>>> c = a[-1]
>>> c.append("new ele")
>>> a[-1].append("oh yeah!")
>>> a
[1, 2, 3, [4, 5, 6, 'new ele', 'oh yeah!']]
>>> a[-1][0]
4
>>> a[-1][-1]
'oh yeah!'
>>> 
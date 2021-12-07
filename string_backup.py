Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # strings --> collections of alphabets, numbers, special char
>>> a = "this is python class"
>>> b = 'this is python class'
>>> a
'this is python class'
>>> b
'this is python class'
>>> a = "thid is python class'
SyntaxError: EOL while scanning string literal
>>> a = "ofvnjmc'hbbrhnfcd"
>>> a
"ofvnjmc'hbbrhnfcd"
>>> # indexing, slicing
>>> a= "python"
>>> a[0]
'p'
>>> a[1]
'y'
>>> a[2]
't'
>>> a[-1]
'n'
>>> a[-2]
'o'
>>> a[-3]
'h'
>>> len(a)
6
>>> b = " this is python programming. Welcome to Brain Mentors"
>>> len(b)
53
>>> a[len(a) -1]
'n'
>>> b[0:5]
' this'
>>> b[0:7]
' this i'
>>> b[3:8]
'is is'
>>> b[2:16:2]
'hsi yhn'
>>> b[2:16:3]
'h  tn'
>>> #string[start:stop:step]
>>> b[:5]
' this'
>>> b[:]
' this is python programming. Welcome to Brain Mentors'
>>> b[::2]
' hsi yhnpormig ecm oBanMnos'
>>> b[5:1]
''
>>> b[-5:-1]
'ntor'
>>> b[-5:]
'ntors'
>>> b[-5:10000000000000000000]
'ntors'
>>> b[5:1:-1]
' sih'
>>> b[::-1]
'srotneM niarB ot emocleW .gnimmargorp nohtyp si siht '
>>> b[::-2]
'sonMnaBo mce gimropnhy ish '
>>> 
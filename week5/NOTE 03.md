# NOTE 03

````python
>>> from datetime import date
>>> date
<class 'datetime.date'>
>>> today = date(2015, 2, 20)
>>> today
datetime.date(2015, 2, 20)
>>> freedom = date(2015, 5, 12)
>>> str(freedom - today)
'81 days, 0:00:00'
>>> today.year
2015
>>> today.month
2
>>> today.strftime("%A %B %d")
'Friday February 20'
>>> a = 'A'
>>> ord(a)
65
>>> hex(ord(a))
'0x41'
#dictionary and list are mutable

>>> four = [1, 2, 3, 4]
>>> len(four)
4
>>> def mystery(s):
...     s.pop()
...     s.pop()
... 
>>> mystery(four)
>>> four
[1, 2]

>>> def another_mystery():
...     four.pop()
...     four.pop()
... 
>>> four = [1, 2, 3, 4]
>>> another_mystery()
>>> four
[1, 2]

#tuple
>>> (3, 4, 5, 6, 7)
(3, 4, 5, 6, 7)
>>> 3, 4, 5, 6, 7
(3, 4, 5, 6, 7)
>>> tuple([3, 4, 5])
(3, 4, 5)
>>> (2,)
(2,)
>>> 2
2
>>> (3, 4) + (5, 6)
(3, 4, 5, 6)
>>> 5 in (3, 4, 5)
True

>>> s = ([3, 4], 2)
>>> s[0] = 4
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> s[0][0] = 1
>>> s
([1, 4], 2)

>>> [10] == [10]
True
>>> a = [10]
>>> b = [10]
>>> a is b
False
>>> a.extend([20,30])
>>> a
[10, 20, 30]
>>> b
[10]
>>> c = b
>>> c is b
True

>>> def f(s=[]):
...     s.append(3)
...     return len(s)
... 
>>> f()
1
>>> f()
2
>>> f()
3
>>> def f(s=[]):
...     s.append(3)
...     return len(s)
... 
>>> f()
1
>>> f()
2
>>> f()
3


````


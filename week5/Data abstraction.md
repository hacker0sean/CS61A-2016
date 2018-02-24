# Data abstraction

## LIST

```python
for _ in range(n):
	pass
#if you don't care the iterator, you can ignore it by set it to be _

>>>letters = ['a', 'b', 'c', 'd', 'e', 'f', 'm', 'n', 'o', 'p']
>>>[letters[i] for i in [3, 4, 5, 6]]
['d', 'e', 'm', 'o'`]
# list comprehensions

odds = [1, 3, 5, 7, 9]
[x for x in odds if 25 % x == 0]
[1, 5]

>>>'here' in 'hewxcrlle'
True
>>> 234 in [2, 3, 4, 5]
False

>>> numerals = {'I':1, 'V':5, 'X':10}
>>> numerals
{'X': 10, 'V': 5, 'I': 1}
>>> numerals['X']
10
>>> numerals.items()
dict_items([('X', 10), ('V', 5), ('I', 1)])
>>>items = [('X', 10), ('V', 5), ('I', 1)]
[('X', 10), ('V', 5), ('I', 1)]
>>> dict(items)
{'I':1, 'V':5, 'X':10}
>>> 'X' in numerals
True
>>> numerals.get('X-ray', 0)
0
>>> {x:x*x for x in range(10)}
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
>>> {[1]: 2}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'

```






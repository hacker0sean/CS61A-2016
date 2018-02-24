## NOTE 02

````python
>>> odds = [3, 5, 7, 9, 11]
>>> list(range(1,3))
[1, 2]
>>> [odds[i] for i in range(1, 3)]
[5, 7]
>>> odds[:3]
[3, 5, 7]
>>> odds[:]
[3, 5, 7, 9, 11]
````



## sum(iterable[, start]) -> value

```python
#case 1
>>> sum([2, 3, 4])
9
#case 2
>>> sum(['2', '3', '4'])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
#case 3
>>> sum([[2, 3],[4]], [])
[2, 3, 4]
#case 4
>>> sum([[2, 3],[4]])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'list'
# You must provide which to add in the case 2 and 4 ,default they are added to 0 first, howervr. Like case 3, you can choose a specified value to add firstly
```

## max

````python
#max(iterable[, key=func]) -> value
#max(a, b, c, ...[, key = func]) -> value
>>>max(range(10), key=lambda x:7-(x-4)*(x-2))
3
# max of which x takes that returns the maximum value of calling of the function
````



## BOOL

````python
>>> bool('hello')
True
>>> [x < 5 for x in range(5)]
[True, True, True, True, True]
>>> all([x < 5 for x in range(5)])
True
# return true if all true value
````


```python
>>> from fractions import Fraction
>>> half = Fraction(1, 2)
>>> repr(half)
'Fraction(1, 2)'
>>> str(half)
'1/2'
>>> print(half)
1/2
>>> eval(str(half))
0.5
>>> s = "Hello, World!"
>>> s
'Hello, World!'
>>> repr(s)
"'Hello, World!'"
>>> print(repr(s))
'Hello, World!'
>>> print(s)
Hello, World!
>>> str(s)
'Hello, World!'
>>> half.__repr__()
'Fraction(1, 2)'
```

```python
class Bear:
	"""A Bear."""
    
    #def __init__(self):
		#self.__repr__ = lambda: 'oski'
        #self.__str__ = lambda: 'this bear'
    
    def __repr__(self):
      	return 'Bear()'
      
    #def __str__(self):
		#return 'a bear'

oski = Bear()
print(oski)
print(str(oski))
print(repr(oski))
print(oski.__str__())
print(oski.__repr__())

Bear()
Bear()
Bear()
Bear()
Bear()


class Bear:
	"""A Bear."""
    
    #def __init__(self):
		#self.__repr__ = lambda: 'oski'
        #self.__str__ = lambda: 'this bear'
    
    def __repr__(self):
      	return 'Bear()'
      
    def __str__(self):
		return 'a bear'

oski = Bear()
print(oski)
print(str(oski))
print(repr(oski))
print(oski.__str__())
print(oski.__repr__())

a bear
a bear
Bear()
a bear
Bear()


class Bear:
	"""A Bear."""
    
    def __init__(self):
		self.__repr__ = lambda: 'oski'
        self.__str__ = lambda: 'this bear'
    
    def __repr__(self):
      	return 'Bear()'
      
    def __str__(self):
		return 'a bear'

oski = Bear()
print(oski)
print(str(oski))
print(repr(oski))
print(oski.__str__())
print(oski.__repr__())

a bear
a bear
Bear()
this bear
oski
```


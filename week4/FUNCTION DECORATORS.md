# FUNCTION DECORATORS

````
def trace1(fn):
	def traced(x):
		print('Callint', fn, 'on argument', x)
		return fn(x)
	return traced
	
@trace1
def square(x):
	return x * x

#it's identical to the following
def square(x):
	return x * x
square = trace1(square)
````



````
def pirate(arggg):
	print('matey')
	def plunder(arggg):
		return arggg
	return plunder
````

add(pirate(3)(square)(4), 1)    evaluates to 17  interactive output is Matey(print)  17(the value of the function)

tips: the value of the function occurs only once in the interactive output **if it fails it returns error**

````
def el(i, za):
     def angelica():
             return i + 1
     if i > 10:
             return za()
     elif i > 4:
             print(angelica())
             return el( i * i , za)
     else:
             return el( i * i, angelica)

el(3, el)

evaluates : 10 , 4 （the last za call is really tricky)
````


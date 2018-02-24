class Fib():
    """A Fibonacci number.

    >>> start = Fib()
    >>> start
    0
    >>> start.next()
    1
    >>> start.next().next()
    1
    >>> start.next().next().next()
    2
    >>> start.next().next().next().next()
    3
    >>> start.next().next().next().next().next()
    5
    >>> start.next().next().next().next().next().next()
    8
    """

    def __init__(self):
        self.value = 0

    def next(self):
        if self.value == 0:
            self.value, self.prev = 1, 0
        else:
            self.value, self.prev = self.value + self.prev, self.value
        return self

    def __repr__(self):
        return str(self.value)


class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.store = 0
        self.deposit_money = 0

    def restock(self, amount):
        self.store += amount
        print(repr("Current " + self.name +  " stock: " + str(self.store)))

    def vend(self):
        if self.store == 0:
            print(repr("Machine is out of stock."))
        elif self.deposit_money < self.price:
            print(repr("You must deposit $" + str(self.price - self.deposit_money) + " more."))
        else:
            if self.deposit_money - self.price > 0:
                print(repr("Here is your " + self.name + " and $" + str(self.deposit_money - self.price) +" change."))
            else:
                print(repr("Here is your " + self.name + "."))
            self.deposit_money = 0
            self.store -= 1

    def deposit(self, amount):
            if self.store > 0:
                self.deposit_money += amount
                print(repr("Current balance: $" + str(self.deposit_money)))
            else:
                print(repr("Machine is out of stock. Here is your $" + str(amount) + "."))


class MissManners:
    """A container class that only forward messages that say please.

    >>> v = VendingMachine('teaspoon', 10)
    >>> v.restock(2)
    'Current teaspoon stock: 2'

    >>> m = MissManners(v)
    >>> m.ask('vend')
    'You must learn to say please first.'
    >>> m.ask('please vend')
    'You must deposit $10 more.'
    >>> m.ask('please deposit', 20)
    'Current balance: $20'
    >>> m.ask('now will you vend?')
    'You must learn to say please first.'
    >>> m.ask('please hand over a teaspoon')
    'Thanks for asking, but I know not how to hand over a teaspoon.'
    >>> m.ask('please vend')
    'Here is your teaspoon and $10 change.'

    >>> double_fussy = MissManners(m) # Composed MissManners objects
    >>> double_fussy.ask('deposit', 10)
    'You must learn to say please first.'
    >>> double_fussy.ask('please deposit', 10)
    'Thanks for asking, but I know not how to deposit.'
    >>> double_fussy.ask('please please deposit', 10)
    'Thanks for asking, but I know not how to please deposit.'
    >>> double_fussy.ask('please ask', 'please deposit', 10)
    'Current balance: $10'
    """
    def __init__(self, obj):
        self.obj = obj

    def ask(self, message, *args):
        magic_word = 'please '
        if not message.startswith(magic_word):
            return 'You must learn to say please first.'
        else:
            message_list = message.split(' ')
            message = ' '.join(message_list[1: ])
            if hasattr(self.obj, message):
                return getattr(self.obj, message)(*args)
            else:
                return 'Thanks for asking, but I know not how to {0}.'.format(message)

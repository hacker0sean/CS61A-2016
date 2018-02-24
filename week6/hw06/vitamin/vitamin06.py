def make_counter():
    """Return a counter function.

    >>> c = make_counter()
    >>> c('a')
    1
    >>> c('a')
    2
    >>> c('b')
    1
    >>> c('a')
    3
    >>> c2 = make_counter()
    >>> c2('b')
    1
    >>> c2('b')
    2
    >>> c('b') + c2('b')
    5
    """
    count_dic = {}
    def count(a):
        nonlocal count_dic
        if a in count_dic.keys():
            count_dic[a] += 1
        else:
            count_dic[a] = 1
        return count_dic[a]
    return count

def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called.

    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    """
    fib_pre = 1
    fib_cur = 0
    first = 0
    def fib():
        nonlocal fib_pre, fib_cur, first
        if first == 0:
            first = 1
            return 0
        else:
            fib_pre, fib_cur = fib_cur, fib_pre + fib_cur
            return fib_cur
    return fib

class Account:
    """An account has a balance and a holder.

    >>> a = Account('John')
    >>> a.deposit(10)
    10
    >>> a.balance
    10
    >>> a.interest
    0.02

    >>> a.time_to_retire(10.25) # 10 -> 10.2 -> 10.404
    2
    >>> a.balance               # balance should not change
    10
    >>> a.time_to_retire(11)    # 10 -> 10.2 -> ... -> 11.040808032
    5
    >>> a.time_to_retire(100)
    117
    """

    interest = 0.02  # A class attribute

    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        """Add amount to balance."""
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        """Subtract amount from balance if funds are available."""
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance

    def time_to_retire(self, amount):
        """Return the number of years until balance would grow to amount."""
        assert self.balance > 0 and amount > 0 and self.interest > 0
        year = 0
        temp = self.balance
        while amount > temp:
            inter = self.interest * temp
            temp = inter + temp
            year += 1
        return year

class FreeChecking(Account):
    """A bank account that charges for withdrawals, but the first two are free!

    >>> ch = FreeChecking('Jack')
    >>> ch.balance = 20
    >>> ch.withdraw(3)    # First one's free
    17
    >>> ch.withdraw(100)  # And the second
    'Insufficient funds'
    >>> ch.balance
    17
    >>> ch.withdraw(3)    # Ok, two free withdrawals is enough
    13
    >>> ch.withdraw(3)
    9
    >>> ch2 = FreeChecking('John')
    >>> ch2.balance = 10
    >>> ch2.withdraw(3) # No fee
    7
    >>> ch.withdraw(3)  # ch still charges a fee
    5
    """
    withdraw_fee = 1
    free_withdrawals = 2
    free_time = 0
    def __init__(self, name):
        self.balance = 0
        self.holder = name

    def withdraw(self, amount):
        if self.free_time < self.free_withdrawals:
            self.free_time += 1
            if self.balance < amount:
                return 'Insufficient funds'
            self.balance = self.balance - amount
            return self.balance
        else:
            if self.balance < amount + self.withdraw_fee:
                return 'Insufficient funds'
            self.balance = self.balance - amount - self.withdraw_fee
            return self.balance

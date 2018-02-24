def bathtub(n):
    """
    >>> annihilator = bathtub(500) # the force awakens...
    >>> kylo_ren = annihilator(10)
    >>> kylo_ren()
    490 rubber duckies left
    >>> finn = annihilator(-20)
    >>> finn()
    510 rubber duckies left
    >>> kylo_ren()
    500 rubber duckies left
    """
    def ducky_annihilator(rate):
        def ducky():
            nonlocal n
            n -= rate
            print(str(n) + " rubber duckies left")
        return ducky
    return ducky_annihilator
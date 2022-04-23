def is_fibonacci(num):
    """check if a number is in the Fibonacci sequence

        print(is_fibonacci(21))
        >>> True

    """ 
    a = 0
    b = 1
    c = a + b

    if num == a or num == b:
        return True
    while b < num:
        c = a + b
        a,b = b,c
        if num == a or num == b:
            return True
        elif c > num:
            return False




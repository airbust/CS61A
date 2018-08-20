def repeated(f, n, x):
    if n == 0:
        return x
    return f(repeated(f, n-1, x))

def sum_digits(n):
    if n == 0:
        return 0
    return sum_digits(n // 10) + n % 10

def double_eights(n):
    if n % 100 == 88:
        return True
    elif n < 100:
        return False
    else:
        return double_eights(n // 10) 

# # Să se scrie o funcție care primește un număr nedefinit de parametrii și să se calculeze suma parametrilor care reprezintă
# # numere întregi sau reale.
# #   your_function(1, 5, -3, ‘abc’, [12, 56, ‘cad’]) va returna 3 (1 + 5 - 3).
# #   your_function() va returna 0.
# #   your_function(2, 4, ‘abc’, param_1=2) va returna 6 (2 + 4).

def your_function(*args, **kwargs):
    sum = 0
    for i in args:
        if type(i) is int:
            sum += i
    return sum

print(your_function(1, 5, -3, 'abc', [12, 56, 'cad']))
print(your_function())
print(your_function(2, 4, 'abc',param_1 = 2))


# # Să se scrie o funcție recursivă care primește ca parametru un număr întreg și returnează:
# #       suma tuturor numerelor de la [0, n]

def f_recursive_sum(n: int):
    if n > 0:
        return n + f_recursive_sum(n-1)
    else:
        return 0
print(f_recursive_sum(10))

# #       suma numerelor pare de la [0, n]
def f_recursive_even(n: int):
    if n > 0:
        if n % 2 == 0:
            return n + f_recursive_even(n-1)
        else:
            return f_recursive_even(n-1)
    else:
        return 0
print(f_recursive_even(4))

#       suma numerelor impare de la [0. n]
def f_recursive_odd(n: int):
    if n > 0:
        if n % 2 == 1:
            return n + f_recursive_odd(n-1)
        else:
            return f_recursive_odd(n - 1)
    else:
        return 0
print(f_recursive_odd(4))

# Să se scrie o funcție care citește de la tastatură și returnează valoarea dacă aceasta este un număr întreg, altfel returnează
# valoarea 0.
def func():
    try:
        x = int(input("Input your number: "))
        if int(x) > 0 and (type(x) is int):
            return x
    except ValueError:
        return 0
print(func())
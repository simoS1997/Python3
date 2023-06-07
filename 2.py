def lltonum(ll):
    i = 10 ** (len(ll) - 1)
    n = 0
    for e in ll:
        n = n + i * int(e)
        i = i // 10  # Corrección: Utilizar el operador de división entera //
    return int(n)

print(lltonum(['4', '3', '2', '5']))

from functools import reduce
def passar_a_numero(digits):
    return reduce(lambda x, y: x * 10 + y, digits)

print(passar_a_numero([4, 3, 9, 2]))

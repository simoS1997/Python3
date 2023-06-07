def llbc(ll, c):
    n = []
    for x in ll:
        if x[:1] == c:
            n.append(x)
    return n

print(llbc(['sabó', 'taula', 'teclat', 'ratolí', 'tren', 'rem', 'roda', 'seba', 'samarreta'], 'r'))

def a(llista, lletra):
    return list(filter(lambda a: a[0] == lletra, llista))

print(a(['maria', 'manta', 'peu', 'mà'], 'p'))

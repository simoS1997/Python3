def idempos(l):
    num = 0
    for i, e in enumerate(l):
        if i == e:
            num = num + 1
    return num

a = [0, 1, 2, 3, 4, 5]
print("Hi ha {} números on coincideixen la posició i el número".format(idempos(a)))

def numi(l):
    return len([e for i, e in enumerate(l) if e == i])

print(numi([0, 2, 2, 1, 5, 5, 6, 10]))

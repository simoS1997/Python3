def cll(l1, l2, c):
    a = len(l1)
    b = len(l2)
    lr = []
    if a == b or b > a:
        for i in range(a):
            lr.append(l1[i] + c + l2[i])
    else:
        for i in range(b):
            lr.append(l1[i] + c + l2[i])
    return lr

print(cll(['sub', 'supra'], ['campió', 'campiona'], '-'))

def c(l, p, con):
    return [a + con + b for (a, b) in zip(l, p)]

print(c(['sub', 'supra'], ['campió', 'campiona'], '-'))

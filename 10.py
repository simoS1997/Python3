def div(a, b):
    try:
        r = a / b
    except ZeroDivisionError:
        print("Error, el segon paràmetre és zero!")
    else:
        print("El resultat de dividir {} i {} és {}".format(a, b, r))

div(3, 0)

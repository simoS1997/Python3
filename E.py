class Vehicle:
    def __init__(self, marca, model, any):
        self.marca = marca
        self.model = model
        self.any = any

    def mostrar_info(self):
        print("Marca:", self.marca)
        print("Model:", self.model)
        print("Any:", self.any)


class Cotxe(Vehicle):
    def __init__(self, marca, model, any, color):
        super().__init__(marca, model, any)
        self.color = color

    def mostrar_info(self):
        super().mostrar_info()
        print("Color:", self.color)

    def accelerar(self):
        print("El cotxe està accelerant.")


class Moto(Vehicle):
    def __init__(self, marca, model, any, cilindrada):
        super().__init__(marca, model, any)
        self.cilindrada = cilindrada

    def mostrar_info(self):
        super().mostrar_info()
        print("Cilindrada:", self.cilindrada)

    def accelerar(self):
        print("La moto està accelerant.")


def aplicacio_4():
    print("Aplicació 4 seleccionada.")

    # Exemple d'ús
    cotxe = Cotxe("Seat", "Ibiza", 2022, "Blau")
    cotxe.mostrar_info()
    cotxe.accelerar()

    print()

    moto = Moto("Honda", "CBR", 2021, "1000cc")
    moto.mostrar_info()
    moto.accelerar()


# Programa principal
aplicacio_4()

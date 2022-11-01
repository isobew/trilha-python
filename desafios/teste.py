print([n**2 if n > 6 else n for n in range(10) if n % 2 == 0])

frutas = ["maçã", "laranja", "uva", "pera"]
print(frutas[-1])

carros = ("gol")
# print(isinstance(carros, tuple))

carros = ("gol", "celta", "palio",)
# carros[0] = "fusca"

# print(carros[0])

carro = {"marca": "Fiat", "modelo": "palio", "placa": "ABD-9826"}
carro.get("motor")

def funcao(*args, **kw):
    print(args, kw)

funcao("python", 2022, curso="dio")


class Foo:
    def hello(self):
        print(self.__class__.__name__.lower())


class Bar(Foo):
    def hello(self):
        return super().hello()


bar = Bar()
bar.hello()
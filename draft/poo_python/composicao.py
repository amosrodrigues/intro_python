class Ventilador:
    def __init__(self, cor, potencia=220, tensao=110, preco=50):
        self.preco = preco
        self.__cor = cor
        self.__potencia = potencia
        self.__tensao = tensao
        self.__ligado = False

    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self, nova_cor):
        if isinstance(nova_cor, str) and nova_cor.lower() == "roxo":
            raise ValueError("Não existe ventilador roxo :(")

        self.__cor = nova_cor

    def __str__(self):
        return self.cor


class Pessoa:
    def __init__(self, nome, saldo_na_conta):
        self.nome = nome
        self.saldo_na_conta = saldo_na_conta
        self.ventilador = None

    def comprar_ventilador(self, ventilador):
        if ventilador.preco <= self.saldo_na_conta:
            self.saldo_na_conta -= ventilador.preco
            self.ventilador = ventilador

    def __str__(self):
        if self.ventilador:
            return f"{self.nome} - possui um ventilador."
        return f"{self.nome} - não possui um ventilador."


ventilador_branco = Ventilador("branco", potencia=250, tensao=220, preco=100)
pessoa = Pessoa("Maria", saldo_na_conta=2000)
pessoa.comprar_ventilador(ventilador_branco)

print(pessoa)

ventilador_teste = Ventilador("preto", potencia=250, tensao=220, preco=100)
print(ventilador_teste)

try:
    ventilador_teste.cor = "roxo"
except ValueError as err:
    print(f"Ocorreu um ValueError: {err}")
else:
    print(ventilador_teste)

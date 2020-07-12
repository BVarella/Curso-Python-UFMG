class Conta:
    def __init__(self, numero: int):
        self.__numero = numero
        self.__saldo = 0.0

    @property
    def saldo(self) -> float:
        return self.__saldo

    def depositar(self, valor: float) -> None:
        self.__saldo += valor

    def sacar(self, valor: float) -> None:
        self.__saldo -= valor


class ContaCorrente(Conta):
    def __init__(self, numero: int, taxa: float):
        super().__init__(numero)
        self.__taxa = taxa

    def cobrar_taxa(self) -> None:
        self.sacar(self.__taxa)


class ContaPoupanca(Conta):
    def __init__(self, numero: int, juros: float):
        super().__init__(numero)
        self.__juros = juros

    def aplicar_juros(self) -> None:
        add = self.saldo * self.__juros
        self.depositar(add)


def main():
    conta_poupanca = ContaPoupanca(1, 0.15)
    conta_poupanca.depositar(10)
    conta_poupanca.aplicar_juros()
    print("%.2f" % conta_poupanca.saldo)


if __name__ == "__main__":
    main()

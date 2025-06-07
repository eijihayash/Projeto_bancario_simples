from contas import Conta, ContaCorrente, ContaPoupanca

class Pessoa:

    def __init__(self, nome: str, idade: int) -> None:
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, idade):
        self._idade = idade



class Cliente(Pessoa):

    def __init__(self,nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self._contas: list[Conta] = []
        self._contacorrente: bool = False
        self._contapoupanca: bool = False

    @property
    def contas(self):
        return self._contas
    
    @property
    def contacorrente(self):
        return self._contacorrente
    
    @property
    def contapoupanca(self):
        return self._contapoupanca

    def inserir_conta(self, conta: Conta) -> None:
        if isinstance(conta, ContaCorrente) and not self._contacorrente:
            self._contas.append(conta)
            self._contacorrente = True
            print(f'{repr(conta)} inserido com sucesso')
        elif isinstance(conta, ContaPoupanca) and not self._contapoupanca:
            self._contas.append(conta)
            self._contapoupanca = True
            print(f'{repr(conta)} inserido com sucesso')
        else:
            print(f"O cliente já possuí {type(conta).__name__}")

    def possui_conta(self) -> None:
        if not self._contas:
            print('Não possui conta')
            return
        
        self._tipo_conta('O cliente tem')

    def _tipo_conta(self, msg ='') -> None:
        if self._contas:
            for conta in self._contas:
                if isinstance(conta, ContaCorrente):
                    print(f'{msg} Conta corrente')
                else:
                    print(f'{msg} Conta poupança')
                return
        print('Não possui conta')

if __name__ == '__main__':
    c1 = Cliente('Eiji', 25)
    c1.possui_conta()
    cp1 = ContaPoupanca(111, 12345, 0)
    cp2 = ContaPoupanca(115, 12345, 0)
    cc1 = ContaCorrente(112, 12345, 0, 300)
    c1.inserir_conta(cp1)
    c1.inserir_conta(cp2)
    c1.possui_conta()
    c1.inserir_conta(cc1)
    print(c1.contas)
    print(c1.contas[0].agencia)


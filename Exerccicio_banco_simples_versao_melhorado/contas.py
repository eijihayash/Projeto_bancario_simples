from abc import ABC, abstractmethod

class Conta(ABC):

    def __init__(self, agencia: int, numeroconta: int, saldo:float = 0) -> None:
        super().__init__()
        self.agencia: int = agencia
        self.numeroconta: int = numeroconta
        self.saldo: float = saldo


    def depositar(self, valor: float) -> float:
        try:
            valor = float(valor)

            if valor <= 0:
                print('Valor inválido, tente novamente.')
                return self.saldo
            
            self.saldo += valor
            self.detalhes(f'(DEPÓSITO R${valor:.2f})')
            return self.saldo
            
        except ValueError:
            print('Valor inválido, tente novamente.')
            return self.saldo

    @abstractmethod
    def sacar(self, valor: float) -> float:
        ...

    def detalhes(self, msg: str = '') -> None:
        print(f'O seu saldo é R${self.saldo:.2f} {msg}')



class ContaCorrente(Conta):
    
    def __init__(self,agencia: int, numeroconta: int, saldo: float = 0, limite: float = 0) -> None:
        super().__init__(agencia, numeroconta, saldo)
        self.limite: float = limite

    def sacar(self, valor: float) -> float:
        try:
            valor = float(valor)

            if valor <= 0:
                print('Valor inválido, tente novamente.')
                return self.saldo
            
            valor_pos_saque = self.saldo - valor
            limite_maximo = -self.limite

            if valor_pos_saque >= 0:
                self.saldo -= valor
                self.detalhes(f'(SAQUE R${valor:.2f})')
                return self.saldo
            
            elif valor_pos_saque >= limite_maximo:
                self.saldo -= valor
                self.detalhes(f'(SAQUE LIMITE R${valor:.2f})')
                return self.saldo
        
            print('Não foi possível sacar o valor desejado.')
            print(f'Seu limite é R${self.limite:.2f}')
            self.detalhes(f'(SAQUE NEGADO R$ {valor:.2f})')
            return self.saldo

        except ValueError:
            print('Valor inválido')
            return self.saldo

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.numeroconta!r}, {self.saldo!r}, {self.limite!r})'
        return f'{class_name}{attrs}'


class ContaPoupanca(Conta):

    
    def __init__(self, agencia: int, numeroconta: int, saldo: float = 0) -> None:
        super().__init__(agencia, numeroconta, saldo)
        
    
    def sacar(self, valor: float) -> float:
        try:
            valor = float(valor)

            if valor <= 0:
                print('Valor inválido, tente novamente.')
                return self.saldo
            
            valor_pos_saque = self.saldo - valor
            
            if valor_pos_saque >= 0:
                self.saldo -= valor
                self.detalhes(f'(SAQUE R${valor:.2f})')
                return self.saldo
            
            print('Não foi possível sacar o valor desejado')
            self.detalhes(f'(SAQUE NEGADO R${valor:.2f})')
            return self.saldo  

        except ValueError:
            print('Valor inválido')
            return self.saldo
        
    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.numeroconta!r}, {self.saldo!r})'
        return f'{class_name}{attrs}'
    

if __name__ == '__main__':
    cp1 = ContaPoupanca(111, 12345, 0)
    print(cp1.agencia, cp1.numeroconta, cp1.saldo)
    cp1.depositar(100)
    cp1.sacar(50)
    cp1.sacar(200)
    cp1.depositar(-1)

    cc1 = ContaCorrente(112, 12345, 0, 300)
    print(cc1.agencia, cc1.numeroconta, cc1.saldo, cc1.limite)
    cc1.depositar(100)
    cc1.sacar(50)
    cc1.sacar(300)
    cc1.sacar(1000)

    
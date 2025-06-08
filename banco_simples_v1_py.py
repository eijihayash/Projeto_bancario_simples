from abc import ABC, abstractmethod

class Conta(ABC):

    def __init__(self, agencia, numeroconta):
        super().__init__()
        self._agencia = agencia
        self._numeroconta = numeroconta
        self._saldo = 0

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def agencia(self):
        return self._agencia
    
    @agencia.setter
    def agencia(self,agencia):
        self._agencia = agencia

    @property
    def numeroconta(self):
        return self._numeroconta
    
    @numeroconta.setter
    def numeroconta(self,numero):
        self._numeroconta = numero


    @abstractmethod
    def deposito(self):
        ...

    @abstractmethod
    def saque(self):
        ...

    def mostrar_saldo(self):
        print(f'Saldo disponível R${self._saldo:.2f}')



class ContaCorrente(Conta):
    
    def __init__(self,agencia, numeroconta):
        super().__init__(agencia, numeroconta)
        self._limite = 500
        self._limite_utilizado = False

    @property
    def limite(self):
        return self._limite


    def deposito(self, valor):
        try:
            valor = float(valor)

            if valor <= 0:
                print('Valor inválido, tente novamente.')
                return False
            
            print(f'Valor R$ {valor:.2f} depositado com sucesso!')

            if self._limite < 500:
                valor_faltante_limite = 500 - self._limite
                if valor < valor_faltante_limite:
                    self._limite += valor
                    valor = 0
                
                else:
                    self._limite += valor_faltante_limite
                    valor = valor - valor_faltante_limite
                    self._limite_utilizado = False

                    
          
            self._saldo += valor
            return True

        except ValueError:
            print('Valor inválido, tente novamente.')
            return False

    def saque(self, valor):
        try:
            saldo_total = self._saldo + self._limite
            valor = float(valor)
            saque_realizado = False

            if valor <= 0:
                print('Valor inválido, tente novamente.')
                return False
            
            if valor <= self._saldo:
                self._saldo -= valor
                saque_realizado = True
                
            if valor > self._saldo and valor <= saldo_total:
                saque_realizado = True
                self._limite_utilizado = True
                valor_limite_utilizado = valor - self._saldo
                self._limite -= valor_limite_utilizado
                self._saldo = 0

            if saque_realizado:
                print(f'Saque no valor R$ {valor:.2f} realizado com sucesso!')
                if self._limite_utilizado:
                    print(f'Limite extra de R$ {valor_limite_utilizado} utilizado')
                    print(f'Limite disponível R$ {self._limite:.2f}')
                
                print(f'Saldo atual {self._saldo:.2f}')
                return True

            else:
                print('Saque negado! Valor do saldo insuficientes para saque.')
                return False
                

        except ValueError:
            print('Valor inválido')
            return False

    def __repr__(self):
        class_name = type(self).__name__
        return class_name


class ContaPoupanca(Conta):

    
    def __init__(self, agencia, numeroconta):
        super().__init__(agencia, numeroconta)

    def deposito(self, valor):
        try:
            valor = float(valor)

            if valor <= 0:
                print('Valor inválido, tente novamente.')
                return False
            
            self._saldo += valor
            print(f'Valor R$ {valor:.2f} depositado com sucesso!')
            return True

        except ValueError:
            print('Valor inválido, tente novamente.')
            return False
        
    
    def saque(self, valor):
        try:
            valor = float(valor)
            saque_realizado = False

            if valor <= 0:
                print('Valor inválido, tente novamente.')
                return False
            
            elif valor <= self._saldo:
                self._saldo -= valor
                print(f'Saque no valor R$ {valor:.2f} realizado com sucesso!')
                return True

            else:
                print('Saque negado! Valor do saldo insuficientes para saque.')
                return False
                

        except ValueError:
            print('Valor inválido')
            return False
        
    def __repr__(self):
        class_name = type(self).__name__
        return class_name
        


class Pessoa:

    def __init__(self):
        self._nome = None
        self._idade = None

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

    def __init__(self):
        super().__init__()
        self._contas = []
        self._contacorrente = False
        self._contapoupanca = False

    @property
    def contas(self):
        return self._contas
    
    @property
    def contacorrente(self):
        return self._contacorrente
    
    @property
    def contapoupanca(self):
        return self._contapoupanca

    def inserir_conta(self, conta):
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


    def tipo_conta(self):
        if self._contas:
            for conta in self._contas:
                if isinstance(conta, ContaCorrente):
                    print('Conta corrente')
                    print(type(conta).__name__)
                else:
                    print('Conta poupança')
                    print(type(conta).__name__)
                return
        print('Não possui conta')


    def possui_conta(self):
        if self._contas:
            print('Possui conta')
            return
        
        print('Não possui conta')

            

class Banco:
    
    def __init__(self):
        self._contas = []
        self._clientes = []
        self._agencia = [1001,1002]
        self._contas_clientes = []

    def inserir_cliente(self, cliente):
        self._clientes.append(cliente)
        print(f'{cliente.nome} cadastrado com sucesso!')
    
    def inserir_conta(self, cliente):
        if not cliente.contas:
            print(f'Prezado {cliente.nome}, senhor(a) não possuí conta, tente novamente.')
            return False
        
        for conta in cliente.contas:
            if conta.agencia not in self._agencia:
                print(f'{repr(conta)} inválida.')
                return False
            
            self._contas.append(conta)
            print(f'{repr(conta)} do cliente cadastrado com sucesso!')

    def autenticar(self, cliente):
        if cliente not in self._clientes:
            print('Cliente não identificado.')
            return False
        
        elif not cliente.contas:
            print(f'Prezado {cliente.nome}, senhor(a) não possuí conta, tente novamente.')
            return False
        
        for conta in cliente.contas:
            if conta not in self._contas or conta.agencia not in self._agencia:
                print(f'{repr(conta)} não identificado.')

            else:
                print(f'Seja bem vindo a sua {repr(conta)} {cliente.nome}!')
                

        
        

    

cliente1 = Cliente()
cliente1.nome = 'Eiji'
cliente1.idade = 25



conta1 = ContaCorrente(1001, 123456)
conta2 = ContaPoupanca(1002, 123456)
conta3 = ContaCorrente(1003, 123456)
conta4 = ContaPoupanca(1004, 123456)



conta2.deposito(1000)
conta2.saldo
conta2.saque(1200)
conta2.saque(1000)



conta1.deposito(500)
conta1.mostrar_saldo
conta1.saque(800)
conta1.saque(300)
conta1.deposito(1000)
conta1.mostrar_saldo
conta1.saque(300)
conta1.saque(500)
conta1.saque(400)
conta1.deposito(200)
conta1.saque(180)



cliente1.inserir_conta(conta1)
cliente1.inserir_conta(conta2)
cliente1.inserir_conta(conta3)
cliente1.inserir_conta(conta4)

banco1 = Banco()
banco1.inserir_cliente(cliente1)
banco1.inserir_conta(cliente1)
banco1.autenticar(cliente1)






    


from contas import Conta, ContaCorrente, ContaPoupanca
from pessoas import Pessoa, Cliente

class Banco:
    
    def __init__(self, agencias : list[int] | None = None,
                 clientes : list[Pessoa] | None = None,
                 contas : list[Conta] | None = None
                 ) -> None:
        self.agencias: list[int] = agencias or []
        self.clientes: list[Pessoa] = clientes or []
        self.contas: list[Conta] = contas or []

    def _checar_agencia(self, conta):
        if conta.agencia in self.agencias:
            print('_checar_agencia', True)
            return True
        print('_checar_agencia', False)
        return False
        
    def _checar_cliente(self, cliente):
        if cliente in self.clientes:
            print('_checar_cliente', True)
            return True
        print('_checar_cliente', False)
        return False
        
    def _checar_conta(self, conta):
        if conta in self.contas:
            print('_checar_conta', True)
            return True
        print('_checar_conta', False)
        return False
        

    def _checa_se_conta_e_do_cliente(self,cliente, conta):
        for cliente_conta in cliente.contas:
            if cliente_conta is conta:
                print('_checa_se_conta_e_do_cliente', True)
                return True
        print('_checa_se_conta_e_do_cliente', False)
        return False


    def autenticar(self, cliente: Cliente, conta: Conta) -> bool:
        return self._checar_agencia(conta) and \
            self._checar_cliente(cliente) and \
            self._checar_conta(conta) and \
            self._checa_se_conta_e_do_cliente(cliente, conta)
            
if __name__ == '__main__':
    c1 = Cliente('Eiji', 25)
    cc1 = ContaCorrente(111, 12345, 0, 300)
    cp1 = ContaPoupanca(112, 12345,100)
    c1.inserir_conta(cc1)
    c1.inserir_conta(cp1)
    c2 = Cliente('Maria', 40)
    cc2 = ContaCorrente(111, 67854, 0, 300)
    cp2 = ContaPoupanca(113, 98745,100)
    c2.inserir_conta(cc2)
    c2.inserir_conta(cp2)


    banco = Banco()
    banco.clientes.extend([c1,c2])
    banco.contas.extend([cc1, cp1, cc2, cp2])
    banco.agencias.extend([111,113])

    # print(banco.autenticar(c2, cc1))
    # print(banco.autenticar(c2, cc2))
    # print(banco.autenticar(c2, cp2))
    # print(banco.autenticar(c1, cc1))
    # print(banco.autenticar(c1, cp1))

    if banco.autenticar(c2, cc2):
        cc2.depositar(1000)
        cc2.sacar(100)

    else:
        ('Conta inválida')

    if banco.autenticar(c2, cc1):
        cc2.depositar(1000)
        cc2.sacar(100)

    else:
        print('Conta inválida')



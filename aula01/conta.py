class Conta():
    def __init__(self, nconta, saldo=0):
        self.conta = nconta
        self.saldo = saldo

    def sacar(self, valor):
        self.saldo -= valor
        return self.saldo

    def depositar(self, valor):
        self.saldo += valor
        return self.saldo

    def transferir(self, valor, conta):
        self.depositar(valor)
        return conta.sacar(valor)
        
    def getsaldo(self):
        '''isto e um teste'''
        return self.saldo

class Poupanca(Conta):
    def metodo(self):
        print('heranca')

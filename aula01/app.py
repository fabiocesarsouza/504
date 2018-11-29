
from conta import Conta, Poupanca

c1 = Conta('123',1000)
c2 = Poupanca('456', 500)

print('sacar da conta 1 ', c1.sacar(200))
print('saldo conta1', c1.getsaldo())

print('saldo apos deposito: ', c1.depositar(100))
print('saldo apos transferencia: ', c1.transferir(100,c2))
print('saldo conta1', c1.getsaldo())
print('saldo conta2', c2.getsaldo())
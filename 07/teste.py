from clientes import Cliente
from contas import Conta

joão = Cliente("João da Silva", "777-1234")
maria = Cliente("Maria da Silva", "555-4321")

conta = Conta([maria, joão], 3000, 2000)
conta.resumo()
operacoes = []
TAM = 1000
contador = 0

class TipoTransacao:
    def __init__(self, descrição, dia, mês, ano, tipo, valor):
        self.descrição = descrição
        self.dia = dia
        self.mês = mês
        self.ano = ano
        self.tipo = tipo
        self.valor = valor

import copy

def registrar_operacao(op, operacoes):
    if len(operacoes) < TAM:
      nova_operacao = TipoTransacao(op.descrição, op.dia, op.mês, op.ano, op.tipo, op.valor)
      operacoes.append(copy.copy(nova_operacao))
      return True
    return False

def consultar_extrato(operacoes):
    for op in operacoes:
        print("Descrição:", op.descrição)
        print("Data:, {:02d}/{:02d}/{}".format(op.dia,op.mês,op.ano))
        print("Tipo:", op.tipo)
        print("Valor:","{:.3f}".format(op.valor))
        print("------------------------------------")

while True:
    print("\n\tBem vindo ao Banco UniBank\n")
    print(" 1 - Efetuar operação")
    print(" 2 - Consultar extrato")
    print(" 3 - Sair")

    opcao = int(input("\nDigite a opção desejada: "))

    if opcao == 1:
        descricao = input("Digite a descrição: ")
        dia = int(input("Digite o dia: "))
        mes = int(input("Digite o mês: "))
        ano = int(input("Digite o ano: "))
        tipo = input("Digite o tipo (C ou D): ")
        valor = float(input("Digite o valor: "))
        valor_formatado = "{:.3f}". format(valor)

        operacao = TipoTransacao(descricao, dia, mes, ano, tipo, valor)

        if registrar_operacao(operacao, operacoes):
            print("Operação registrada")
        else:
            print("Nao foi possivel registrar a operacao. O limite de transacoes foi atingido.")

    elif opcao == 2:
        if operacoes:
            consultar_extrato(operacoes)
        else:
            print("Nenhuma operacao registrada no extrato.")

    elif opcao == 3:
        print("\n Operações finalizadas...\n\n")
        break

    else:
        print("\nOpcao invalida! Tente novamente!")

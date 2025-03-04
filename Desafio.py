menu = """

[1] = Depositar
[2] = Sacar
[3] = Extrato
[0] = Sair

Escolha a Opção: """

def depositar():
    global extrato, saldo, teve_movimentacao


    valor_deposito = float(input("Informe o Valor do Depósito: "))
    if valor_deposito < 0 or valor_deposito == 0:
        print("Valor Inválido para Depositar!")
    else:
        teve_movimentacao += 1
        saldo += valor_deposito
        extrato += f"Depósito...... {SIGLA_MOEDA}{valor_deposito:16,.2f}\n"
        
def sacar():
    global saldo, extrato, limite, numero_saques, LIMITE_SAQUES, teve_movimentacao

    if numero_saques == LIMITE_SAQUES:
        print("Execedeu o Limite de Saques no Dia!")
    else:
        valor_saque = float(input("Informe o Valor do Saque: "))

        if valor_saque < 0 or valor_saque == 0:
            print("Valor Inválido para Saque!")
        elif valor_saque > limite:
            print("Limite de Saque Excedido!")
        elif valor_saque > saldo:
            print("Não há Saldo Suficiente para Saque!")
        else:
            teve_movimentacao += 1
            numero_saques += 1
            saldo -=valor_saque
            extrato += f"Saque......... {SIGLA_MOEDA}{valor_saque:16,.2f}-\n"

SIGLA_MOEDA = "R$ "
saldo = 0
limite = 500
extrato = "\n======== Extrato Bancário ========\n"
numero_saques = 0
LIMITE_SAQUES = 3
teve_movimentacao = 0

while True:
    opcao = int(input(menu))

    if opcao == 1:
        print("Depósito")
        depositar()
    elif opcao == 2:
        print("Saque")
        sacar()
    elif opcao == 3:
        if teve_movimentacao == 0:
            print("\n======== Extrato Bancário ========\n")
            print("Não Houve Nenhuma Movimentação\n")
            print(f"\nSALDO......... {SIGLA_MOEDA}{saldo:16,.2f}")
        else:
            extrato_exibir = extrato
            extrato_exibir  += f"\nSALDO......... {SIGLA_MOEDA}{saldo:16,.2f}"
            print(extrato_exibir)
    elif opcao == 0:
        break
    else:
        print("Opção Inválida! Seleciona a Opção Correta Novamente.")

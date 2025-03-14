from datetime import datetime

def depositar(contas, movimentos):
    print("\nDepósito")

    print("-----------------------------------------")
    nconta = input("Informe a Conta: ")
    if not nconta:
        print("\nNecessário Informar Conta!")
        return
    
    cpf = input("Informe o CPF (somente números): ")
    if not cpf:
        print("\nNecessário Informar o CPF!")
        return

    nconta = int(nconta)
    cpf = int(cpf)

    existe_conta_cpf = testa_conta_cpf(contas, cpf, nconta)
    if not existe_conta_cpf:
        print("\nConta e CPF Inexistente!")
        return

    existe_cliente = testa_cliente(cpf, clientes)
    nome_cliente = existe_cliente[1]["nome"]
    print("_________________________________________")
    print(f"   Data: {datetime.now().strftime(mascara_ptbr)}")
    print(f"Agência: {AGENCIA}    -    Conta: {nconta}")
    print(f"Cliente: {nome_cliente}")
    print("_________________________________________")

    registro_movimento, limite_diario_movimentacao, limite_saques, limite_valor_saque, saldo, extrato, movimentacao, movimentacao_saque = posicao_movimento(cpf, nconta, movimentos)
    
    if limite_diario_movimentacao == movimentacao:
        print("\nLimite de Movimentação Diário Excedido!")
        return

    valor_deposito = float(input("Informe o Valor do Depósito: "))
    if valor_deposito < 0 or valor_deposito == 0:
        print("\nValor Inválido para Depositar!")
        return
    
    movimentacao += 1
    saldo += valor_deposito
    extrato += f"{datetime.now().strftime(mascara_ptbr)} Depósito...... {SIGLA_MOEDA}{valor_deposito:16,.2f}\n"
    movimentos.update({registro_movimento: {"cpf": cpf, "conta": nconta, "limite_diario_movimentacao": limite_diario_movimentacao, "limite_saques": limite_saques, "limite_valor_saque": limite_valor_saque, "saldo": saldo, "extrato": extrato, "movimentacao": movimentacao, "movimentacao_saque": movimentacao_saque}})
    print("\n*** Depósito Realizado com Sucesso!")
        
def sacar(contas, movimentos):
    print("\nSaque")

    print("-----------------------------------------")
    nconta = input("Informe a Conta: ")
    if not nconta:
        print("\nNecessário Informar Conta!")
        return
    
    cpf = input("Informe o CPF (somente números): ")
    if not cpf:
        print("\nNecessário Informar o CPF!")
        return

    nconta = int(nconta)
    cpf = int(cpf)

    existe_conta_cpf = testa_conta_cpf(contas, cpf, nconta)
    if not existe_conta_cpf:
        print("\nConta e CPF Inexistente!")
        return

    existe_cliente = testa_cliente(cpf, clientes)
    nome_cliente = existe_cliente[1]["nome"]
    print("_________________________________________")
    print(f"   Data: {datetime.now().strftime(mascara_ptbr)}")
    print(f"Agência: {AGENCIA}    -    Conta: {nconta}")
    print(f"Cliente: {nome_cliente}")
    print("_________________________________________")

    registro_movimento, limite_diario_movimentacao, limite_saques, limite_valor_saque, saldo, extrato, movimentacao, movimentacao_saque = posicao_movimento(cpf, nconta, movimentos)
    
    if limite_diario_movimentacao == movimentacao:
        print("\nLimite de Movimentação Diário Excedido!")
        return

    if movimentacao_saque == limite_saques:
        print("\nExecedeu o Limite de Saques no Dia!")
    else:
        valor_saque = float(input("Informe o Valor do Saque: "))

        if valor_saque < 0 or valor_saque == 0:
            print("\nValor Inválido para Saque!")
        elif valor_saque > limite_valor_saque:
            print("\nLimite de Saque Excedido!")
        elif valor_saque > saldo:
            print("\nNão há Saldo Suficiente para Saque!")
        else:
            movimentacao += 1
            movimentacao_saque +=1
            saldo -= valor_saque
            extrato += f"{datetime.now().strftime(mascara_ptbr)} Saque......... {SIGLA_MOEDA}{valor_saque:16,.2f}-\n"
            movimentos.update({registro_movimento: {"cpf": cpf, "conta": nconta, "limite_diario_movimentacao": limite_diario_movimentacao, "limite_saques": limite_saques, "limite_valor_saque": limite_valor_saque, "saldo": saldo, "extrato": extrato, "movimentacao": movimentacao, "movimentacao_saque": movimentacao_saque}})
            print("\n*** Saque Realizado com Sucesso!")

def extrato_bancario(contas, movimentos):
    print("\nExtrato Bancário")
    print("-----------------------------------------")
    nconta = input("Informe a Conta: ")
    if not nconta:
        print("\nNecessário Informar Conta!")
        return
    
    cpf = input("Informe o CPF (somente números): ")
    if not cpf:
        print("\nNecessário Informar o CPF!")
        return

    nconta = int(nconta)
    cpf = int(cpf)

    existe_conta_cpf = testa_conta_cpf(contas, cpf, nconta)
    if not existe_conta_cpf:
        print("\nConta e CPF Inexistente!")
        return

    existe_cliente = testa_cliente(cpf, clientes)
    nome_cliente = existe_cliente[1]["nome"]
    print("\n==================================================")
    print(f"   Data: {datetime.now().strftime(mascara_ptbr)}")
    print(f"Agência: {AGENCIA}    -    Conta: {nconta}")
    print(f"Cliente: {nome_cliente}")

    registro_movimento, limite_diario_movimentacao, limite_saques, limite_valor_saque, saldo, extrato, movimentacao, movimentacao_saque = posicao_movimento(cpf, nconta, movimentos)

    if movimentacao == 0:
        print("\n================ Extrato Bancário ================\n")
        print("Não Houve Nenhuma Movimentação\n")
        print(f"\nSALDO......................... {SIGLA_MOEDA}{saldo:16,.2f}")
    else:
        extrato_exibir = extrato
        extrato_exibir += f"\nSALDO........................ {SIGLA_MOEDA}{saldo:16,.2f}\n"
        extrato_exibir += f"\nData: {datetime.now().strftime(mascara_ptbr)}"
        extrato_exibir += f"\n==================================================\n"
        print(extrato_exibir)

def cadastro_cliente(clientes):
    print("\nCadastro de Cliente")
    print("-----------------------------------------")
    
    cpf = input("Informe o CPF (somente números): ")
    
    if not cpf:
        print("\nNecessário Informar o CPF!")
        return
    
    cpf = int(cpf)

    existe_cliente = testa_cliente(cpf, clientes)

    if existe_cliente:
        print("\nJá existe cliente com esse CPF!")
        return
    
    nome = input("Nome Completo: ")
    if not nome:
        print("\nNecessário Informar o Nome!")
        return

    data_nascimento = input("Data Nascimento (dd-mm-aaaa): ")
    if not data_nascimento:
        print("\nNecessário Informar Data de Nascimento!")
        return
    
    endereco = input("Endereço (logradouro, número, bairro, cidade/UF): ")
    if not endereco:
        print("\nNecessário Informar Endereço!")
        return
    
    registro_cliente = len(clientes) + 1
    cliente = {registro_cliente: {"cpf": cpf, "nome": nome, "data_nascimento": data_nascimento, "endereco": endereco}}
    clientes.update(cliente)
    print("\n*** Cliente Cadastrado com Sucesso!")

        
def cadastro_contas(numera_contas, clientes, contas):
    print("\nCadastro de Conta")
    print("-----------------------------------------")
    cpf =input("Informe o CPF (somente números): ")

    if not cpf:
        print("\nNecessário Informar o CPF!")
        return
    
    cpf = int(cpf)

    existe_cliente = testa_cliente(cpf, clientes)
    
    if not existe_cliente:
        print("\ncliente com esse CPF Inexistente!")
        return
    
    registro_conta = len(contas) + 1
    conta = {registro_conta: {"cpf": cpf, "conta": numera_contas}}
    contas.update(conta)

    registro_movimento = len(movimentos) + 1
    limite_diario_movimentacao = 10
    limite_saques = 3
    limite_valor_saque = 500
    saldo = 0
    extrato = "================ Extrato Bancário ================\n"
    movimentacao = 0
    movimentacao_saque = 0
    
    movimento = {registro_movimento: {"cpf": cpf, "conta": numera_contas, "limite_diario_movimentacao": limite_diario_movimentacao, "limite_saques": limite_saques, "limite_valor_saque": limite_valor_saque, "saldo": saldo, "extrato": extrato, "movimentacao": movimentacao, "movimentacao_saque": movimentacao_saque}}
    movimentos.update(movimento)

    print("\n*** Conta Cadastrada com Sucesso!")
    nome_cliente = existe_cliente[1]["nome"]
    print("_________________________________________")
    print(f"Agência: {AGENCIA}    -    Conta: {numera_contas}")
    print(f"Cliente: {nome_cliente}")
    print("_________________________________________")

def testa_cliente(cpf, clientes):
    clientes_consulta = [cliente for cliente in clientes.items() if cliente[1]["cpf"] == cpf]
    return clientes_consulta[0] if clientes_consulta else None

def testa_conta_cpf(contas, cpf, nconta):
#    for cpf_conta_consulta in contas.items():
#        print(cpf_conta_consulta)
#        if cpf_conta_consulta[1]["cpf"] == cpf and cpf_conta_consulta[1]["conta"] == nconta:
#            print("Achou")
#            return True
    cpf_conta_consulta = [conta for conta in contas.items() if conta[1]["cpf"] == cpf and conta[1]["conta"] == nconta]
    return cpf_conta_consulta[0] if cpf_conta_consulta else None

def posicao_movimento(cpf, nconta, movimentos):
    for chave, posicao in movimentos.items():
        if posicao["cpf"] == cpf and posicao["conta"] == nconta:
            return chave, posicao["limite_diario_movimentacao"], posicao["limite_saques"], posicao["limite_valor_saque"], posicao["saldo"], posicao["extrato"], posicao["movimentacao"], posicao["movimentacao_saque"]


mascara_ptbr = "%d/%m/%y %H:%M"
SIGLA_MOEDA = "R$ "
AGENCIA = "0001"
clientes = {}
contas = {}
movimentos = {}
numera_contas = 0

menu = """

[1] = Depositar
[2] = Sacar
[3] = Extrato
[4] = Cadastro de Clientes
[5] = Cadastro de Contas
[0] = Sair

Escolha a Opção: """

while True:
    opcao = int(input(menu))

    if opcao == 1:
        depositar(contas, movimentos)
    elif opcao == 2:
        sacar(contas, movimentos)
    elif opcao == 3:
        extrato_bancario(contas, movimentos)
    elif opcao == 4:
        cadastro_cliente(clientes)
    elif opcao == 5:
        numera_contas = len(contas) + 1
        cadastro_contas(numera_contas, clientes, contas)
    elif opcao == 0:
        break
    else:
        print("Opção Inválida! Seleciona a Opção Correta Novamente.")

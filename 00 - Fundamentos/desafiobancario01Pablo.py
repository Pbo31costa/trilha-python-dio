menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>  """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print ("Deposito")
        dinheiro_depositado = float(input("Informe o valor do depósito: "))
        if dinheiro_depositado > 0:
            saldo += dinheiro_depositado
            extrato += f"Deposito R$: {dinheiro_depositado:.2f}\n"
        
        else:
            print ("Operação falhou, o valor informado é invalido")

    elif opcao == "s":
        print ("Sacar")
        dinheiro_sacar = float(input("Informe o valor do saque: "))

        excedeu_saldo = dinheiro_sacar > saldo
        excedeu_limite = dinheiro_sacar > limite
        excedeu_limite_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print ("Operação falhou, Saldo insuficiente.")
        
        elif excedeu_limite:
            print ("Operação falhou, Valor de saque excede limite.")
        
        elif excedeu_limite_saque:
            print ("Operação falhou, Excedeu limite de saques diarios.")
        
        elif dinheiro_sacar > 0:
            saldo -= dinheiro_sacar
            extrato += f"Saque R$: {dinheiro_sacar:.2f}\n"
            numero_saques += 1
        
        else:
            print("Operação falhou, o valor informado é invalido")


    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
    
    elif opcao == "q":
        break

    else:
        print ("Operação invalida, por favor selecione novamente a operação desejada")

print ("Obrigado por utilizar nossos serviços")
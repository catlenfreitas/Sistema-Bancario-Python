from datetime import datetime

menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
ultima_data_saque = None
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        deposito = float(input("Informe o valor para depósito: "))
        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
        else:
            print("Falha na operação. Valor inválido!")
    
    elif opcao == "2":
        data_atual = datetime.now().date()  # Obter a data atual

        # Verifica se o saque é no mesmo dia
        if ultima_data_saque != data_atual:
            ultima_data_saque = data_atual
            numero_saques = 0  # Reseta o contador de saques para o novo dia

        if numero_saques >= LIMITE_SAQUES:
            print("Limite de saques diários atingido.")
            
        saque = float(input("Informe o valor que deseja sacar: "))

        if saque > saldo:
            print("Saldo insuficiente.")
        elif saque > limite:
            print("Falha na operação. O valor do saque excede o limite.")
        elif numero_saques >= LIMITE_SAQUES:
            print("Falha na operação. Número máximo de saques diários atingido.")
        elif saque > 0:
            saldo -= saque
            extrato += f"Saque: R$ {saque:.2f}\n"
            numero_saques += 1
        else:
            print("Falha na operação. Valor inválido!")
    
    elif opcao == "3":
        print("\n********************** EXTRATO BANCÁRIO **********************")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("**************************************************************")
    
    elif opcao == "4":
        break
    
    else:
        print("Opção inválida.")

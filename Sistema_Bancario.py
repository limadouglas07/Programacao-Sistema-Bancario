menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Saida

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3  # Maiúscula constante..

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor do seu depósito:"))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito:R${valor:.2f}\n'
            print(
                f"Depósito no valor de R${valor:.2f} efetuado com sucesso!!!")
        else:
            print("Operação falhou! o valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Digite o valor do saque:"))

        excedeu_saldo = valor > saldo

        excedeu_limite_saque = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite_saque:
            print("Operação falhou! Você excedeu o limite de retirada por dia.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques por dia excedido!")

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque:R${valor:.2f}\n'
            numero_saques += 1
            print(f"Saque no valor de {valor:.2f} efetuado com sucesso!!!")

        else:
            print("Operação falhou! o valor informado é inválido.")

    elif opcao == "e":
        print("\n===============EXTRATO===============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("=======================================")

    elif opcao == 'q':
        print("Obrigado por utilizar nossos serviços!!")

        break

    else:
        print("Operação inválida, por favor selecione a opção desejada")

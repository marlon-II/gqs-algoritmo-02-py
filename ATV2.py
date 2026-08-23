valorIn = 0.0
valorIn2 = 0.0
resultado = 0.0
operador = ""

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("  Bem vindo a calculadora 67K!!")
print("  Infome os valores e operadores um por vez:")
print("  Digite == para finalizar a conta")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

while(operador != "=="):
    valorIn = int(input("Digite o primeiro valor: "))
    operador = input("Digite o operador da conta: ")
    valorIn2 = int(input("Digite o segundo valor: "))

    if operador == "==":
        break

    match operador:
        case "+":
            resultado = valorIn + valorIn2
        case "-":
            resultado = valorIn - valorIn2
        case "*":
            resultado = valorIn * valorIn2
        case "/":
            if valorIn == 0 or valorIn2 == 0:
                print("Erro: divisão por zero")
                continue
            resultado = valorIn / valorIn2
        case _:
            print("Opção inválida, tente novamente a partir do último número")
            continue

    
    print("----------")
    print(resultado)
    print("----------")
    print("  " )
    print("Se dejesa parar digite '==', para continuar digite qualquer coisa.")
    operador = input(" ")


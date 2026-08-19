valorIn = 0.0
resultado = 0.0
operador = ""

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("  Bem vindo a calculadora 67K!!")
print("  Infome os valores e operadores um por vez:")
print("  Digite == para finalizar a conta")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

while(operador != "=="):
    valorIn = input("")
    operador = input("")

    match operador:
        case "+":
            resultado = resultado + valorIn
        case "-":
            resultado = resultado - valorIn
        case "*":
            resultado = resultado * valorIn
        case "/":
            resultado = resultado / valorIn
        case "=":
            print("----------")
            print(resultado)
        case _:
            print("Opçõa enválida, tente novamente a parti do ultimo número")


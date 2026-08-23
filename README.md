# Calculadora 67K

### Como executar o código:

Para executar esse código você pode utilizar o VScode com a extensão de python.
Ao rodar o código você vai ter o nome e as informações do código e depois você vai digitar o primeiro valor da operação, depois o operador (+, -, / e *) e o segundo número da operação, depois disso o código vai mostrar o resultado da conta.
Após isso o código vai perguntar se você vai querer continuar com a conta, caso queira parar a conta basta digitar "**==**" e caso queira realizar outros cálculos basta digitar qualquer caractere.

### O que o código faz:

O código realiza operações matemáticas simples entre dois valores, mostra o resultado e pergunta se você quer realizar outra conta antes de encerrar o código.

### Detalhamento do código:

As principais funções utilizadas no código foram o **print()**, o **input()**, o **while** e o **match**. A forma como eles foram utilizados está explicado abaixo:

. **print()**: Foi utilizado para realizar a impressão na tela as mensagens desejadas no código, como saída de resultados ou informações, segue com o exemplo escrita no código e a saída:

**Código**: 
```
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("  Bem vindo a calculadora 67K!!")
print("  Infome os valores e operadores um por vez:")
print("  Digite == para finalizar a conta")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
```
**Saída**:
```
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
  Bem vindo a calculadora 67K!!
  Infome os valores e operadores um por vez:
  Digite == para finalizar a conta
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
```

. **input()**: Foi utilizado para receber os valores escrito no terminal para as variáveis do sistema.

. **while**: A função dele é para que o código pare apenas quando o usuário decida, esse comando gera um loop até o usuário digitar o valor que fecha ele.

. **match**: Serve para realizar um menu de escolha, a utilização dele foi para saber qual operador utilizar durante a conta.

### Exemplo de saída:

Como o código é uma calculadora a saída é a resposta do calculo, abaixo se encontra um exemplo de toda a saída do terminal em uma utilização:
```
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
  Bem vindo a calculadora 67K!!
  Infome os valores e operadores um por vez:
  Digite == para finalizar a conta
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Digite o primeiro valor: 10
Digite o operador da conta: + 
Digite o segundo valor: 5
----------
15
----------
  
Se dejesa parar digite '==', para continuar digite qualquer coisa.
 g
Digite o primeiro valor: 12
Digite o operador da conta: *
Digite o segundo valor: 5
----------
60
----------
  
Se dejesa parar digite '==', para continuar digite qualquer coisa.
 ==
```

## Sobre

Esse código e documentação foi desenvolvido por **Marlon Andrade Bartoli**, aluno do curso Ciência da Computação na UNA Contagem.

Algoritmo "IAL002- Exercícios Introdutórios EX07"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Carmen Lucia de Bartolo Costa
// Descrição   : Calcula operações aritméticas
// Autor(a)    : Gabriela Calazans Andrade Nogueira
// Data atual  : 02/03/2024
Var
        i:      inteiro
        resultado: real
Inicio
   MudaCor("Vermelho", "FRENTE")
escreval("******** OPERAÇÕES ARITMÉTICAS ************")
Escreval()
// a) escreva (O resultado da expressão 5 * 3 - 2 + 4 / 2 é = (5*3-2+(4/2))
escreval ("O resultado da expressão 5 * 3 - 2 + 4 / 2 é = ", (5*3-2+(4/2))
//b) Imprima na tela o resultado do mod 6
resultado <- 5*3-2+(4/2)
escreval("O resultado da expressão 5*3-2+(4/2) em mod 6 é igual a: ", resultado mod 6)
Escreval()
Escreval()
//c) imprima o resultado da Tabuada do 2
i <- 0
escreval("** TABUADA DO 2 **")
para i de 0 até 10 faca
     escreval ("2 X ", i, " = ", 2*i)
fimpara
Escreval()
Escreval()
//d) imprima o resultado da express�o: 4 x (2+34-7) /2
escreval("O resultado da express�o 4 x (2+34-7)/2 � ", 4*(2+34-7)/2)
Fimalgoritmo

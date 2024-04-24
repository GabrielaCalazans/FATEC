Algoritmo "IAL002- Exercicios Introdutórios EX 06"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Carmen Lucia de Bartolo Costa
// Descrição   : Calcula o MOD e DIV.
// Autor(a)    : Gabriela Calazans Andrade Nogueira
// Data atual  : 02/03/2024
Var
   operacao: caracter
   n1,n2,op: inteiro

Inicio
MudaCor("Vermelho", "FRENTE")
// EX 06
escreval("O resultado de 12 DIV 3 é: ", 12 div 3)
escreval("O resultado de 15 DIV 4 é: ", 15 DIV 4)
escreval("O resultado de 15 MOD 4 é: ", 15 MOD 4)
escreval("O resultado de 15 MOD 4 é: ", 12 mod 3)

Escreval("***********************************************")
Escreval("*       Seja Bem vindo(a) á Calculadora       *")
Escreval("*                DIV ou MOD                   *")
Escreval("***********************************************")
Escreval()
Escreval("Escreva em letras maiúsculas qual operação que deseja realiza (MOD ou DIV).")
leia(operacao)

SE pos(operacao, "MOD") = 1 ENTAO
   op <- 1
SENAO
   SE pos(operacao, "DIV") = 1 ENTAO
      op <- 2
   SENAO
      op <- 0
      Escreval("A operaçãoo ", operacao, " não existe nesta calculadora.")
   fimse
FIMSE
SE op > 0 ENTAO
   Escreval("Escreva dois numeros para a operação ", operacao, ".")
   Escreval()
   leia(n1, n2)
SENAO
    Escreval()
FIMSE
SE op = 1  ENTAO
   Escreval("O resultado de ", n1, " " ,operacao, " ", n2, " = ", n1 mod n2)
   SENAO
        SE op = 2 ENTAO
                Escreval("O resultado de ", n1, " " ,operacao, " ", n2, " = ", n1 div n2)
        SENAO
            Escreval()
        fimse
FIMSE
Fimalgoritmo

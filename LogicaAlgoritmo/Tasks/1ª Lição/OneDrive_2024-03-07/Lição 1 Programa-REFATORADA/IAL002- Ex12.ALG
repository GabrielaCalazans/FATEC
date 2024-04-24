Algoritmo "IAL002- Exercícios Introdutórios EX12"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Carmen Lucia de Bartolo Costa
// Descrição   : Recebe o valor de fabrica do carro e calcula o curso final ao consumidor
// Autor(a)    : Gabriela Calazans Andrade Nogueira
// Data atual  : 02/03/2024
Var
   valorcarro,valorfabrica: real

Inicio
MudaCor("Azul", "FRENTE")
// EX12
Escreval("***********************************************")
Escreval("*          Seja Bem vindx ao Programa         *")
Escreval("*          Custo final do Carro               *")
Escreval("***********************************************")
Escreval("Digite o valor de f�brica do carro")
leia(valorfabrica)
valorcarro <-((valorfabrica*28)/100)+((valorfabrica*45)/100)+valorfabrica
Escreval("O valor final do carro ser� de ", valorcarro)

Fimalgoritmo

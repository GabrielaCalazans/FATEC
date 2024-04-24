Algoritmo "IAL002- Exercícios Introdutórios EX11"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Carmen Lucia de Bartolo Costa
// Descrição   : Recebe o valor do salario mensal e a taxa de reajuste mensal e devolve o valor do novo salario reajustado
// Autor(a)    : Gabriela Calazans Andrade Nogueira
// Data atual  : 02/03/2024
Var
   salario,reajuste: real

Inicio
MudaCor("Vermelho", "FRENTE")
// EX11
Escreval("***********************************************")
Escreval("*          Seja Bem vindx ao Programa         *")
Escreval("*          Calculo de Reajuste Salarial       *")
Escreval("***********************************************")
Escreval("Digite o seu salario mensal e a taxa de reajuste mensal.")
Escreval("Ex.: 1000 1,5")
leia(salario, reajuste)
Escreval("O valor do seu novo salario ser� de ", ((salario*reajuste)/100)+salario)
Escreval()
Escreval()

Fimalgoritmo

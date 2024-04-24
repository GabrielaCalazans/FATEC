Algoritmo "IAL002- Exercícios Introdutórios EX10"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Carmen Lucia de Bartolo Costa
// Descrição   : Recebe dois número e verifica qual � maior.
// Autor(a)    : Gabriela Calazans Andrade Nogueira
// Data atual  : 02/03/2024
Var
   num,ndois: inteiro

Inicio
MudaCor("Vermelho", "FRENTE")

//EX10
Escreval("Digite um número.")
leia(num)
Escreval("Digite um segundo número.")
leia(ndois)
SE num > ndois ENTAO
   escreval("O número ", num, " é maior que ", ndois)
SENAO
   SE num > ndois ENTAO
      escreval("O número ", num, " é menor que ", ndois)
   SENAO
      escreval("Os números ", num, " e ", ndois, " são iguais.")
      fimse
   FIMSE
Fimalgoritmo
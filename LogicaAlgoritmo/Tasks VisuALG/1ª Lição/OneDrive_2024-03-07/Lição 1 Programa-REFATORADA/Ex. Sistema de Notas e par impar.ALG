Algoritmo "IAL002- Exercicios Introdutorios"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Carmen Lucia de Bartolo Costa
// Descrição   : Recebe o nome e as notas dos alunos e informa se a nota é par ou impar e se o aluno está aprovado ou reprovado.
// Autor(a)    : Gabriela Nogueira
// Data atual  : 22/02/2024
Var
   i: inteiro
   nome:vetor [1..3] de caracter
   nota:vetor [1..3] de inteiro

Inicio
MudaCor("Vermelho", "FRENTE")
Escreval("**** Welcome to FATEC Grade System *****")
i <- 1
para i de 1 ate 3 faca
   Escreval("Digite o nome do aluno.")
   leia(nome[i])
   Escreval("Digite a nota do aluno.")
   leia(nota[i])
fimpara

i <- 1
para i de 1 ate 3 faca
   Escreval ("Nome: ", nome[i], " Nota: ", nota[i])
   SE nota[i] % 2 = 0 ENTAO
      Escreval("A nota de ", nome[i], " é par.")
      Escreval()
   SENÃO
      Escreval("A nota de ", nome[i], " é impar.")
      Escreval()
   FIMSE
fimpara

i <- 1
para i de 1 ate 3 faca
   Escreval ("Nome: ", nome[i], " Nota: ", nota[i])
   SE nota[i] >= 7 ENTAO
      Escreval("O aluno ", nome[i], " está aprovado.")
      Escreval()
   SENÃO
      Escreval("O aluno ", nome[i], " está reprovado.")
      Escreval()
   FIMSE
fimpara

Fimalgoritmo

Algoritmo "IAL002- Exercicios Introdutorios"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Carmen Lucia de Bartolo Costa
// Descri��o   : Recebe o nome e as notas dos alunos e informa se a nota � par ou impar e se o aluno est� aprovado ou reprovado.
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
      Escreval("A nota de ", nome[i], " � par.")
      Escreval()
   SEN�O
      Escreval("A nota de ", nome[i], " � impar.")
      Escreval()
   FIMSE
fimpara

i <- 1
para i de 1 ate 3 faca
   Escreval ("Nome: ", nome[i], " Nota: ", nota[i])
   SE nota[i] >= 7 ENTAO
      Escreval("O aluno ", nome[i], " est� aprovado.")
      Escreval()
   SEN�O
      Escreval("O aluno ", nome[i], " est� reprovado.")
      Escreval()
   FIMSE
fimpara

Fimalgoritmo

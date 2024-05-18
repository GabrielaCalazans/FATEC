//Algoritmo "IAL002- Exercícios Apostila Algoritmos"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Carmen Lucia de Bartolo Costa
// Descrição   : Recebe o nome e as notas dos alunos e informa se a nota � par ou impar
// Autor(a)    : Gabriela Nogueira
// Data atual  : 22/02/2024
Var
		contador,i,par,impar,base,altura,num,ndois: inteiro
		modulo,salario,reajuste,valorcarro,valorfabrica: real
		nome:vetor [1..3] de caracter
		nota:vetor [1..3] de inteiro
		myname,colega: caracter

Inicio
	MudaCor("Vermelho", "FRENTE")
	Escreval("Welcome to FATEC Grade System")
	i <- 1
	para i de 1 ate 3 faca
		Escreval("Digite o nome do aluno.")
		leia(nome[i])
		Escreval("Digite a nota do aluno.")
		leia(nota[i])
	fimpara
	Escreval("Fim.")
	limpaTela()

	i <- 1
	para i de 1 ate 3 faca
	Escreval ("Nome: ", nome[i], " Nota: ", nota[i])
	SE nota[i] % 2 = 0 ENTAO
		Escreval("A nota de ", nome[i], " é par.")
		 Escreval()
	SENAO
		Escreval("A nota de ", nome[i], " é impar.")
		Escreval()
	FIMSE
	fimpara

Fimalgoritmo
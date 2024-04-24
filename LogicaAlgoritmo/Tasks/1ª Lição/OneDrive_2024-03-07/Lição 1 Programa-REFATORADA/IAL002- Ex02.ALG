Algoritmo "IAL002- Exercicios Introdutórios - EX 02"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Carmen Lucia de Bartolo Costa
// Descrição   : Recebe o nome de duas pessoas e imprime os nomes na mesma linha.
// Autor(a)    : Gabriela Calazans Andrade Nogueira
// Data atual  : 02/03/2024
Var
	nomeColega,seuNome:	caracter
	suaIdade,colegaIdade:	inteiro

Inicio
   MudaCor("Vermelho", "FRENTE")

// EX 02
escreval ("Escreva o seu nome e o nome de seu(sua) colega.")
leia(seuNome, nomeColega)
escreval (seuNome, " e ", nomeColega)
escreval ("Escreva a idade de ", nomeColega, " primeiro e depois escreva a sua idade.")
leia(colegaIdade,suaIdade)

SE suaIdade > colegaIdade ENTAO
	escreval(seuNome, " você tem ", suaIdade, " anos, logo, você é mais velho(a) que ", nomeColega, ".")
SENAO
	se suaIdade < colegaIdade ENTAO
		escreval(nomeColega, " tem ", colegaIdade, " anos, então, ", nomeColega, " é mais velho(a) que você ", seuNome, ".")
	senao
		escreval(seunome, ", você e ", nomeColega, " têm a mesma idade.")
	fimse
FIMSE

Fimalgoritmo

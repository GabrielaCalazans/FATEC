Algoritmo "IAL002- Exercícios Apostila Logi	ca de Programação - Repetição - Lista 4" 
// Disciplina: [Linguagem e Logica de Programação] 
// Professor: Carmen Lúcia de Bartolo Costa 
// Descrição: EX01 - Recebe um número e escreve na tela o dia da semana ao qual corresponde, considerando que o domingo é o primeiro dia da semana e corresponde ao número um.
// Autor(a): Gabriela Nogueira
// Data atual: 18/03/2024
Var
n1,i: inteiro

Inicio
escreval("Digite um número de 1 a 7.")
leia(n1)
escolha n1
	caso 1
		escreva(n1:2, "corresponde a Domingo.")
	caso 2
		escreva(n1:2, "corresponde a Segunda-feira.")
	caso 3
		escreva(n1:2, "corresponde a Terça-feira.")
	caso 4
		escreva(n1:2, "corresponde a Quarta-feira.")
	caso 5
		escreva(n1:2, "corresponde a Quinta-feira.")
	caso 6
		escreva(n1:2, "corresponde a Sexta-feira.")
	caso 7
		escreva(n1:2, "corresponde a Sábado.")
fimescolha

Fimalgoritmo
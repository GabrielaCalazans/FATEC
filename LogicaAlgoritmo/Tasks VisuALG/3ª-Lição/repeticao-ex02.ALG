Algoritmo "IAL002- Exercícios Apostila Logica de Programação - Repetição" 
// Disciplina: [Linguagem e Logica de Programação] 
// Professor: Carmen Lúcia de Bartolo Costa 
// Descrição: Efetua a soma de todos os números ímpares que são múltiplos de três e que se encontram no conjunto dos números de 1 até 500. 
// Autor(a): Gabriela Nogueira
// Data atual: 18/03/2024
Var
i,soma: inteiro

Inicio
para i de 1 ate 500 faca
	se i % 3 = 0 entao
		se i % 2 = 1 entao
			soma <- soma + i
			// escreva(i:3, "SOMA: ", soma:3)
		fimse
	fimse
fimpara
escreva(" Resultada da soma dos números ímpares de 1 até 500: ", soma)
Fimalgoritmo
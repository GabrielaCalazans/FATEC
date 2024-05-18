Algoritmo "IAL002- Exercícios Apostila Logica de Programação - Repetição - Lista 4" 
// Disciplina: [Linguagem e Logica de Programação] 
// Professor: Carmen Lúcia de Bartolo Costa 
// Descrição: EX03 - Possui um menu com 4 opções de programas e encerra na opção 9. 
// Autor(a): Gabriela Nogueira
// Data atual: 18/03/2024
Var
n1,i: inteiro
ordem: caractere

	procedimento caso1()
	var
		i:inteiro
	inicio
		para i de 100 ate 200 faca
			se i % 2 = 1 entao
				escreva (i:3)
			fimse
		fimpara
		escreval()
	fimprocedimento

	procedimento caso2()
	var
		i,soma:inteiro
	inicio
		escreval("A soma de todos os números ímpares, que são múltiplos de três, no conjunto de 251 até 555 é:")
		para i de 251 ate 555 faca
			se i % 3 = 0 entao
				se i % 2 = 1 entao
					soma <- soma + i
				fimse
			fimse
		fimpara
		escreval(" Resultada da soma dos números ímpares, que são múltiplos de três, no conjunto de de 251 até 555: ", soma)
	fimprocedimento

	procedimento caso3(j:inteiro)
	var
		i,r1:inteiro
	inicio
		escreval(i:3, "em ordem decrescente.")
		r1 <- j
		para i de r1 ate 0 faca
			escreva(i:3)
		fimpara
		escreval()
	fimprocedimento

	procedimento caso4()
	var
		i:inteiro
	inicio
		escreval("Os números pares entre 50 e 150 são:")
		para i de 50 ate 150 faca
			se i % 2 = 0 entao
				escreva (i:3)
			fimse
		fimpara
		escreval()
	fimprocedimento

Inicio
enquanto (n1 <> 9) faca
	escreval("Digite um número entre 1 e 4. Caso queira encerrar o programa digite 9")
	leia(n1)
	escolha n1
		caso 1
			caso1()
		caso 2
			caso2()
		caso 3
			caso3(55)
		caso 4
			caso4()
		caso 9
			escreval("Encerrando...")
	fimescolha
fimenquanto
Fimalgoritmo
Algoritmo "IAL002- Exercícios Apostila Logica de Programação - Repetição" 
// Disciplina: [Linguagem e Logica de Programação] 
// Professor: Carmen Lúcia de Bartolo Costa 
// Descrição: Recebe uma temperatura em graus Celsius. Converte a temperatura recebida em graus Kelvin ou graus Fahrenheit, enquanto o usuário desejar continuar.
// Autor(a): Gabriela Nogueira
// Data atual: 18/03/2024
Var
ordem: caractere
i,tipo: inteiro
celsius,kelvin,fahrenheit: real

Inicio
ordem <- "sim"
enquanto (pos(ordem, "sim") = 1) faca
	escreval ("Digite uma temperatura em grau Celsius a ser convertida.")
	leia(celsius)
	escreval(celsius)
	escreval ("Para qual temperatura deseja converter? - Digite 1 para Kelvin ou digite 2 para Fahrenheit")
	leia(tipo)
	se (tipo = 1) entao
		kelvin <- celsius + 273.15
		escreval ("A temperatura ", celsius, " Celsius, em Kelvin corresponde a ", kelvin, "K.")
	senao
		se (tipo = 2) entao
			fahrenheit <- ((celsius*9)/5)+32
			escreval ("A temperatura ", celsius, " Celsius, em Fahrenheit corresponde a ", fahrenheit, "F.")
		senao
			escreval("Escolha desconhecida pelo programa.")
		fimse
	fimse

	escreval ("Deseja inserir outra temperatura para conversão? - Responda se 'sim' ou se 'não'")
	leia(ordem)
	escreval(ordem)
fimenquanto
Fimalgoritmo

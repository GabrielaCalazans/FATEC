Algoritmo "IAL002- Exercicios Apostila Logica de Programação - Lista 1 e Lista 2"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Carmen Lucia de Bartolo Costa
// Descrição   : 
// Autor(a)    : Gabriela Nogueira
// Data atual  : 12/03/2024
Var
	num,n1,n2,n3,base,altura,r1,r2,i: inteiro
	nome:vetor [1..3] de caracter
	num:vetor [1..3] de inteiro
	result:vetor [1..3] de inteiro


Inicio
MudaCor("Vermelho", "FRENTE")
// // // EX 01
Escreval("Digite um número.")
leia(num)
Escreval(num, " + 5 = ", num + 5)
timer(4000)
timer(0)
limpaTela()

// // // EX 02
Escreval("Digite um número.")
leia(num)
Escreval(num, " - 3 * 2 = ", (num - 3)*2)
timer(4000)
timer(0)
limpaTela()

// // // EX 03
Escreval("Digite dois números.")
leia(n1,n2)
Escreval(n1, " + ", n2, " = ", n1+n2)
timer(4000)
timer(0)
limpaTela()

// // // EX 04
Escreval("Digite um número.")
leia(n1)
Escreval(n1, " + 10 = ", n1 + 10)
Escreval("Digite outro número.")
leia(n1)
Escreval(n2, " / 2 = ", n2 / 2)
timer(4000)
timer(0)
limpaTela()

// // // EX 05
Escreval("Digite dois números.")
leia(n1,n2)
Escreval(n1, " + ", n2, " + 10 é = ", (n1-n2)+10)
timer(4000)
limpaTela()
Escreval("***********************************************")
Escreval("*       Seja Bem vinda(o) ao Programa         *")
Escreval("*       Cálculo da área do triangulo          *")
Escreval("***********************************************")
Escreval()
Escreval()
Escreval("Digite o valor da base.")
leia(base)
Escreval("Digite o valor de altura.")
leia(altura)
Escreval("A área do triangulo é: ", (base*altura)/2)
timer(4000)
timer(0)
limpaTela()

// // // EX 06
Escreval("Digite um número.")
leia(n1)
r1 <- n1 - 3
Escreval(n1, " - 3 = ", r1)
Escreval("Digite outro número.")
leia(n1)
r2 <- n2 + 2
Escreval(n2, " + 2 = ", r2)
Escreval("(", r1, " + ", r2, ") - 1 = ", (r1+r2)-1)
timer(4000)
timer(0)
limpaTela()

// // //EX 07
Escreval("Digite um número para a tabuada.")
leia(n1)
escreval("** TABUADA DO ", n1, " **")
para i de 0 ate 10 faça
	escreval (n1, " X ", i, " = ", n1*i)
fimpara


// // EX 08 
Escreval("Digite um número.")
leia(n1)
result[1] <- (n1 + 10)
Escreval("Digite outro número.")
leia(n2)
result[2] <- (n2 - 5)
Escreval("Digite um terceiro número.")
leia(n3)
result[3] <- (n3 * 2)

PARA i de 1 ate 3 faca
	
	se (i = 1) entao
		escreval (n1, " + 10 = ", result[i])
	senao
		se (i = 2) entao
			escreval (n2, " - 5 = ", result[i])
		senao
			escreval (n3, " * 2 = ", result[i])
		fimse
	fimse
	SE result[i] % 2 = 0 ENTAO
		Escreval("O resultado desta operação é par.")
	SENAO
		Escreval("O resultado desta operação é impar.")
	FIMSE
FIMPARA
Fimalgoritmo

// // para i de 1 ate 3 faca
// // 	Escreval("Digite um número.")
// // 	leia(num[i])
// // 	SE i = 1 ENTAO
// // 		result[1] <- num[i] + 10
// // 		Escreval(num[1], " + 10 = ", result[1])
// // 	SENAO
// // 		SE i = 2 ENTAO
// // 			result[i] <- num[i] - 5
// // 			Escreval(num[i], " - 5 = ", result[i])
// // 		SENAO
// // 			result[i] <- num[i] * 3
// // 			Escreval(num[i], " * 3 = ", result[i])
// // 		FIMSE
// // 	FIMSE
// // FIMPARA

// // para i de 10 ate 1 faca
// // 	escreva (i:3)
// // fimpara

// // // EX 09
Escreval("Digite um número.")
leia(n1)
r1 <- n1 - 3
escreval (n1, " - 3 = ", r1)
Escreval("Digite o expoente para realizar a potenciação deste resultado")
leia(n2)
escreval (r1, " na potência ", n2, " = ", r1 ^ n2)

// // // EX 10
Escreval("Digite um número.")
leia(n1)
r1 <- (n1 / 2) + 3
r2 <- (n1 / 2) + 5
escreval ("(",n1, " / 2) + 3 = ", r1)
escreval ("(",n1, " / 2) + 5 = ", r2)
Escreval("Digite o expoente para realizar a potenciação de ", r1)
leia(n2)
escreval (r1, " na potência ", n2, " = ", r1 ^ n2)
escreval ("A raiz quadrada de ", r2, " é ", RaizQ(r2))

Fimalgoritmo

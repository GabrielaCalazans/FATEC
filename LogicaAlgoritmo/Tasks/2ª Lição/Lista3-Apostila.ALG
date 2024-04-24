Algoritmo "IAL002- Exercicios Apostila Logica de Programação - Lista 3"
Disciplina   : [Linguagem e Logica de Programacao]
Professor   : Carmen Lucia de Bartolo Costa
Descrição   : 
Autor(a)    : Gabriela Nogueira
Data atual  : 12/03/2024
Var
	idade,n1,n2,n3,r1,r2,r3,verifica,i,p: inteiro
	seno,cosseno,tang:real
	ordem: caractere
	nums:vetor [1..3] de inteiro

Inicio
MudaCor("Verde", "FRENTE")
MudaCor("Cinza", "FUNDO")
// // // EX 01
Escreval("Digite sua idade.")
leia(idade)
se (idade < 18) entao
	escreval ("O filme é proibido para menores de 18 anos. Contudo, você acaba de ganhar uma pipoca por ter vindo!")
senao
	escreval ("Parabéns! Você acaba de ganhar o ticket do filme e a pipoca.")
fimse
timer(4000)
timer(0)
limpaTela()

// // // EX 02
Escreval("Digite um número.")
leia(n1)
r1 <- n1 + 45
Escreval(n1, " + 45 = ", r1)
seno <- sen(r1)
cosseno <- cos(r1)
tang <- tan(r1)

escreva("Resultados seno de ", r1, " = ", seno)
escreva(" Cosseno de ", r1, " = ", cosseno)
escreva(" Tangente de ", r1, " = ", tang)
timer(4000)
timer(0)
limpaTela()

// // // // EX 03
verifica <- 1
i <- 0
p <- 0
enquanto (verifica = 1) faca
	escreva("Digite um número")
	leia(n1)
	se (n1 = 0) entao
		escreva("")
	senao
		se (n1 % 2 = 0) entao
			p <- p + 1
			escreval (" ", n1, " é par. Números pares digitados até o momento: ", p)
		senao
			i <- i + 1
			escreval (" ", n1, " é ímpar. Números impares digitados até o momento: ", i)
		fimse
	fimse
	escreva("Deseja continuar inserindo números? Responda se 'sim' ou se 'não'.")
	leia(ordem)
	se (pos(ordem, "sim") = 1) entao
		escreval (" OK")
	senao
		escreval("Totais:")
		verifica <- 2
	fimse
fimenquanto

escreval("Você digitou ", p + i, " números.")
escreval("Sendo ", p, " números pares")
escreval("Sendo ", i, " números ímpares")

// // // // EX 04
enquanto (i < 3) faca
	escreval("Digite um número")
	leia(nums[i])
	se (nums[i] + 5 > 10) entao
		escreval("Resultado acima de 10. ", nums[i], " + 5 = ", nums[i]+5)
	fimse
	i <- i + 1
fimenquanto

// // // // EX 05
escreva("Digite 2 números")
leia(n1,n2)
se ((n1 + n2) < 20) entao
	escreval()
	escreval("A soma de ", n1, " + ", n2, " inferior a 20.")
	escreval(n1, " x 10  = ", n1 * 10)
	escreval(n2, " x 10  = ", n2 * 10)
	escreval(n1, " + ", n2, " x 10  = ", (n1 + n2) * 10)
fimse

// // // // EX 06
escreva("Digite um número")
leia(n1)
se (n1 * 3 > 15) entao
	escreval()
	escreval("A multiplicação de ", n1, " x  3 = ", n1 * 3, ". Este resultado é superior a 15.")
fimse

// // // // EX 07
escreva("Digite 3 números")
leia(n1,n2,n3)
se ((n1 + n2 + n3) > 20) entao
	escreval()
	escreval("A soma de ", n1, " + ", n2, " + ", n3, " = ", n1+n2+n3, ". Resultado superior a 20.")
fimse

// // // // EX 08
escreva("Digite 2 números")
leia(n1,n2)
se (n1 = n2) entao
	escreval()
	escreval(n1, " é igual a ", n2)
fimse

// // // // EX 09
escreva("Digite um número")
leia(n1)
escreval()
escreval ("A raiz quadrada de ", n1, " é ", RaizQ(n1))

// // // // EX 10
enquanto (pos(ordem, "sim") = 1) faca
	escreval()
	Escreva("Digite um número para a tabuada.")
	leia(n1)
	escreval("** TABUADA DO ", n1, " **")
	para i de 0 ate 10 faça
		escreval (n1, " X ", i, " = ", n1*i)
	fimpara
	escreva("Deseja ver outra tabuada? Responda se 'sim' ou se 'não'.")
	leia(ordem)
fimenquanto

// // // // EX 11
enquanto (pos(ordem, "sim") = 1) faca
	escreval()
	Escreva("Digite 2 números")
	leia(n1,n2)
	escreval()
	escreval(n1, " x ", n2, " = ", n1*n2)
	escreval("Para a potenciação escolha qual será o expoente. Digite 1 para (", n1, ") 2 para (", n2, ")")
	leia(r1)
	se (r1 = 1) entao
		escreval (n2, " na potência ", n1, " = ", n2^n1)
	senao
		escreval (n1, " na potência ", n2, " = ", n1^n2)
	fimse
	r1 <- RaizQ(n1)
	r2 <- RaizQ(n2)
	se (r1 > r2) entao
		escreval ("A raiz quadrade de ", n1, " = ", r1, ". E é maior que a raiz quadrade de ", n2, " que é = ", r2)
	senao
		escreval ("A raiz quadrade de ", n2, " = ", r2, ". E é maior que a raiz quadrade de ", n1, " que é = ", r1)
	fimse

	escreva("Deseja realizar mais cálculos? Responda se 'sim' ou se 'não'.")
	leia(ordem)
fimenquanto

// // // // EX 12
escreva("Digite um número para calcular seu fatorial")
leia(n1)
i <- n1 - 1
escreval()
escreva(n1, "! = ", n1)
para i de i ate 1 faca
	escreva(" · ", i)
	n1 <- n1 * i
fimpara
escreva(" = ", n1)

// // // // EX 13
escreva("Digite um número para saber seu valor na terceira potência")
leia(n1)
r1 <- n1 ^ 3
escreval()

para i de 0 ate r1 faca
	se (i % 2 = 0) faca
		MudaCor("Vermelho", "FRENTE")
	senao
		MudaCor("Azul", "FRENTE")
	fimse
	escreva(i:3)
fimpara
Fimalgoritmo
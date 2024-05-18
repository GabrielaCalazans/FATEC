Algoritmo "IAL002- Exercícios Apostila Logica de Programação - Repetição" 
// Disciplina: [Linguagem e Logica de Programação] 
// Professor: Carmen Lúcia de Bartolo Costa 
// Descrição: Lê a altura de 15 pessoas. Este programa verificar e devolve quantas destas pessoas são mulheres/homens com altura > 1,65/1,85, respectivamente. Ao final mostrar todos os totais separados por sexo e descreve qual a maior altura registrada.
// Autor(a): Gabriela Nogueira
// Data atual: 18/03/2024
Var
i,somaMulher,mulheresAltas,somaHomem,homensAltos: inteiro
altura,maiorAltura:real
sexo,maiorAlturaSexo:caractere

Inicio
somaHomem <- 0
somaMulher <- 0
maiorAltura <- 0
homensAltos <- 0
mulheresAltas <- 0
i <- 1
para i de 1 ate 15 faca
	escreval("Digite primeiro uma altura (metros e centimetros devem ser separados por ponto. Ex.: 1.70 e depois o sexo da pessoa.")
	leia(altura, sexo)
	escreval(altura:3, sexo)
	se (altura > maiorAltura) entao
		maiorAltura <- altura
		maiorAlturaSexo <- sexo
	fimse
	se (pos(sexo,"feminino") = 1) entao
		somaMulher <- somaMulher + 1
		se (altura > 1.65) entao
			mulheresAltas <- mulheresAltas + 1
		fimse
	senao
		se (pos(sexo,"masculino") = 1) entao
			somaHomem <- somaHomem + 1
			se (altura > 1.85) entao
				homensAltos <- homensAltos + 1
			fimse
		senao
			escreval("Sexo desconhecido pelo programa.")
		fimse
	fimse
fimpara
escreval("Soma do número de altura de mulheres digitados: ", somaMulher:3, "Soma de mulheres mais altas que 1.65: ", mulheresAltas)
escreval("Soma do número de altura de homens digitados: ", somaHomem:3, "Soma de homens mais altos que 1.85: ", homensAltos)
escreval("Maior altura digitada: ", maiorAltura:3, "Sexo desta pessoa: ", maiorAlturaSexo)
Fimalgoritmo
Algoritmo "IAL002- Exercicios Introdutorios"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Carmen Lucia de Bartolo Costa
// Descri��o   : Recebe o nome e as notas dos alunos e informa se a nota � par ou impar
// Autor(a)    : Gabriela Nogueira
// Data atual  : 22/02/2024
Var
   contador,i,par,impar,base,altura,num,ndois: inteiro
   modulo,salario,reajuste,valorcarro,valorfabrica: real
   nome:vetor [1..3] de caracter
   nota:vetor [1..3] de inteiro
   myname,colega,nomeColega,seuNome: caracter

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
Escreval()
Escreval()

// EX 02
escreval ("Escreva o seu nome e do seu colega. Ex.: Gabriela Tadeu")
leia(seuNome, nomeColega)
escreval (seuNome, " ", nomeColega)

// EX 06
escreval("O resultado de 12 DIV 3 �: ", 12 div 3)
escreval("O resultado de 15 DIV 4 �: ", 15 DIV 4)
escreval("O resultado de 15 MOD 4 �: ", 15 MOD 4)
escreval("O resultado de 15 MOD 4 �: ", 12 mod 3)

// EX 07
// a) escreva (�O resultado da express�o 5 * 3 � 2 + 4 / 2 � = (5*3-2+(4/2))�
escreval ("O resultado da express�o 5 * 3 - 2 + 4 / 2 � = ", 5*3-2+(4/2))
//b) Imprima na tela o resultado do mod 6
modulo <- 5*3-2+(4/2)
escreval(modulo mod 6)
Escreval()
Escreval()
//c) imprima o resultado da Tabuada do 2
i <- 0
escreval("Tabuada do 2")
para i de 0 at� 10 faca
   escreval ("2 X ", i, " = ", 2*i)
fimpara
Escreval()
Escreval()
//d) imprima o resultado da express�o: 4 x (2+34-7) /2
escreval("O resultado da express�o 4 x (2+34-7)/2 � ", 4*(2+34-7)/2)

// EX08
Escreval("Escreva o seu nome.")
leia(myname)
Escreval("Escreva o nome do seu colega ao lado.")
leia(colega)
Escreval()
Escreval(myname, " ", colega)

//EX09
Escreval()
Escreval("         FATEC ZONA SUL         ")
Escreval("               =                ")

para i de 1 at� 3 faca
   Escreval()
fimpara
Escreval("Digite o valor da base.")
leia(base)
Escreval("Digite o valor de altura.")
leia(altura)
Escreval("C�lculo da �rea do triangulo : ", base*altura/2)
Escreval()
Escreval()


//EX10
//         escreval("Os n�meros ", num, " e ", ndois, " s�o iguais.")
Escreval("Digite um n�mero.")
leia(num)
Escreval("Digite um segundo n�mero.")
leia(ndois)
SE num > ndois ENTAO
   escreval("O n�mero ", num, " � maio que ", ndois)
SEN�O
   escreval("O n�mero ", num, " � menor que ", ndois)
FIMSE
Escreval()
Escreval()

// EX11
Escreval("Bem vindx ao Programa de Calculo de Reajuste Salarial.")
Escreval("Digite o seu salario mensal e a taxa de reajuste mensal. Ex.: 1000 1,5")
leia(salario, reajuste)
Escreval("O seu novo salario ser� de ", salario*reajuste+salario)
Escreval()
Escreval()

// EX12
Escreval("Digite o valor de f�brica do carro")
leia(valorfabrica)
valorcarro <-(valorfabrica*28%)+(valorfabrica*45%)+valorfabrica
Escreval("O valor final do carro ser� de ", valorcarro)

Fimalgoritmo

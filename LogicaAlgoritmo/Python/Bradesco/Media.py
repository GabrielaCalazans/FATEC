notaA = float(input("Informe a primeira nota: "))
notaB = float(input("Informe a segunda nota: "))

#calcular média
mediafinal = (notaA + notaB) / 2

#verificação
if mediafinal >= 7.0:
	print("A média %.1f - Aprovado"% mediafinal)
else:
	print("A média %.1f - Reprovado"% mediafinal)


idade = int(input("Digite a idade da pessoa: "))
if idade >= 18:
	print("maior idade")
elif idade > 16:
	print("Infanto juvenil")
else:
	print("menor idade")

def	lernotas():
	n = float(input('Digite uma nota para o aluno(a):\t'))
	return n

def	resultado(n1, n2):
	media = (n1 + n2) / 2
	print("Nota 1: ", n1)
	print("Nota 2: ", n2)
	print("Média: ", media, "Resultado:\t", end="")
	if media >= 7:
		print("Aprovado")
	else:
		print("Reprovado")

a = lernotas()
b = lernotas()
resultado(a, b)


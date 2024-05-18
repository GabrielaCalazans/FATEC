qtd = 0
soma = 0
media = 0
valor = float(input("Difite um valor:\t"))

while (valor > 0.0):
	soma = soma + valor
	qtd = qtd + 1
	# Entrada de valores
	valor = float(input("Digite um valor:\t"))

#Caso digite um valor negativo o laço encerra

media = soma / qtd
print("\n Total da Soma:\t", soma)
print("\n Quantidade de valores digitados:\t", qtd)
print("\n Média dos valores:\t", media)
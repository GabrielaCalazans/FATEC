# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex02.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/18 17:29:41 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/23 17:52:29 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Altere o exercício 1. Pule duas linhas. 
# Digite o nome da sua namorada e a do seu amigo. 
# Pule mais algumas linhas e faça um retângulo com o nome do seu amigo e o da namorada dele dentro do retângulo. 

print("\n\nJim, Jimi Hendrix, Erykah Badu, Derrick Green\n\n\n")
print("Nina")
print("Jimi Hendrix")
print("Erykah Badu")
print("Derrick Green\n\n")

i = 0
k = 0
while (i < 11):
	for x in range(11 - i):
		print(" ", end="")
	if (i == 0):
		print("*")
	if (i > 0):
		print("*", end="")
		if i > 1:
			k += 1
			j = i + k
		else:
			j = i
		if (i == 6):
			print("    Nina   ", end="")
		elif (i == 7):
			print(" Erykah Badu ", end="")
		elif (i == 9):
			print("  Jimi Hendrix   ", end="")
		elif (i == 10):
			print("   Derrick Green   ", end="")
		else:
			for x in range(j):
				print(" ", end="")
		print("*")
	i += 1

for x in range(12):
	print("* ", end="")

print("\n\n")

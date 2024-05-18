# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex02.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/18 17:29:41 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/18 17:53:21 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Altere o exercício 1. Pule duas linhas. 
# Digite o nome da sua namorada e a do seu amigo. 
# Pule mais algumas linhas e faça um retângulo com o nome do seu amigo e o da namorada dele dentro do retângulo. 

print("\n\nAdele, Angelina Jolie, Brad Pitt, Jennifer Aniston\n\n\n")
print("Adele")
print("Brad Pitt")
print("Angelina Jolie")
print("Jennifer Aniston\n\n")

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
			print("   Adele   ", end="")
		elif (i == 7):
			print("  Brad Pitt  ", end="")
		elif (i == 9):
			print(" Angelina Jolie  ", end="")
		elif (i == 10):
			print(" Jennifer Aniston  ", end="")
		else:
			for x in range(j):
				print(" ", end="")
		print("*")
	i += 1

for x in range(12):
	print("* ", end="")

print("\n\n")

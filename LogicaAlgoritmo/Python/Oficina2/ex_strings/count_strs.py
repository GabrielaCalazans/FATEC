# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count_strs.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/07 13:56:22 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/07 16:27:34 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# -*- coding: utf-8 -*-
import os
import time 
import sys

nomePrograma = "Tamanho de strings\n"
print (nomePrograma)
time.sleep(5)
os.system("clear")

phrase1 = str(input('Digite uma frase: '))
phrase2 = str(input('Digite uma segunda frase: '))
len1 = len(phrase1)
len2 = len(phrase2)

print(f"\nPrimeira frase: {phrase1} | Tamanho da primeira frase : {len1}")
print(f"Segunda frase: {phrase2} | Tamanho da segunda frase: {len2}")

if len1 == len2:
	print("As frases possuem o mesmo tamanho.")
if len1 > len2:
	print("A primeira frase é maior que segunda frase.")
if len1 < len2:
	print("A segunda frase é maior que primeira frase.")

if phrase1 == phrase2:
	print("O conteúdo das frases é igual\n.")
else:
	print("O conteúdo das frases é diferente\n.")

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count_space_vowels.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/07 16:24:16 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/07 16:55:13 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# -*- coding: utf-8 -*-
import os
import time 
import sys

nomePrograma = "Conta espaços e vogais\n"

print (nomePrograma)
time.sleep(2)
os.system("clear")

phrase = str(input('Digite uma frase: '))
len1 = len(phrase)
v_letters = ['a', 'e', 'i', 'o', 'u']
vowels = 0
spaces = 0

for x in phrase:
	if x == ' ':
		spaces += 1
	if x.lower() in v_letters:
		vowels += 1

if spaces == 1:
	print (f"Existe {spaces} espaço em branco na frase")
if spaces > 1:
	print (f"Existem {spaces} espaços em branco na frase")
else:
	print (f"Não há espaços em branco na frase")

if vowels == 1:
	print (f"Existe {vowels} vogal na frase")
if vowels > 1:
	print (f"Existem {vowels} vogais na frase")
else:
	print (f"Não há vogais na frase")

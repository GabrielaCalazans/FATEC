# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    date.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/07 14:17:00 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/07 16:27:41 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# -*- coding: utf-8 -*-
import os
import time 
import sys

nomePrograma = "Data por extenso\n"
print (nomePrograma)
time.sleep(5)
os.system("clear")

data = str(input('Digite sua data de nascimento: '))
print(data)
split = data.split('/')

day = split[0]
month = split[1]
year = split[2]

all_month = {'01':'janeiro', '02':'fevereiro', '03':'março', '04':'abril', 
			'05':'maio', '06':'junho', '07':'julho', '08':'agosto', 
			'09':'setembro', '10':'outubro', '11':'novembro', '12':'dezembro'}

month = month.replace(month, all_month[month])

print('\n')
print (f"Você nasceu em {day} de {month} de {year}.")
print('\n')



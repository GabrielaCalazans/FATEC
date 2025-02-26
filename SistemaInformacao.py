# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    SistemaInformacao.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/10/23 09:55:56 by gacalaza          #+#    #+#              #
#    Updated: 2024/10/23 09:55:56 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Função de controle de acesso
import time

usuarios = {
	'admin': {'senha': '1234', 'area': 'Contabilidade'},
	'beltranin': {'senha': 'abcd', 'area': 'RH'},
	'ads': {'senha': 'zeushelpus', 'area': 'TI'},
	'fulanin': {'senha': 'abcd', 'area': 'RH'}
}


def registrar_log(usuario, status):
	with open("logs_acesso.txt", "a") as log:
		hora = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		log.write(f"[{hora}] Usuario: {usuario}, Status: {status}\n")


def controlar_acesso(usuario, senha, tentativas):
	if usuario in usuarios:
		if usuarios[usuario]['senha'] == senha:
			status = "Acesso permitido"
			area = usuarios[usuario]['area']
			registrar_log(usuario, status)
			return f"Acesso permitido. Bem-vindo à área de {area}!"
		else:
			tentativas += 1
			status = "Senha incorreta"
			registrar_log(usuario, status)
			if tentativas >= 3:
				return "Acesso bloqueado após várias tentativas falhas."
			return "Senha incorreta. Tente novamente."
	else:
		status = "Usuário não encontrado"
		registrar_log(usuario, status)
		return "Usuário não encontrado."

def login():
	tentativas = 0
	while tentativas < 3:
		usuario = input("Digite seu usuário: ")
		senha = input("Digite sua senha: ")
		
		resultado = controlar_acesso(usuario, senha, tentativas)
		print(resultado)
		
		if "Acesso permitido" in resultado or "Acesso bloqueado" in resultado:
			break
		tentativas += 1


login()

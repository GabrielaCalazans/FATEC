#include <iostream>
#include <cmath>
#include <iomanip>
#include <cstdlib>
#include <vector>
#include <limits>
#include <regex>
#include <sstream>

// a) Ler 10 elementos de uma matriz tipo vetor e apresentá-los.
int	readAndDisplayArray(void) {
	system("cls");
	std::cout << "** a) LÊ VALORES E RETORNA OS VALORES LIDOS **" << std::endl;

	std::vector<int>	values;
	std::string			input;
	std::regex			numberPattern("[-+]?[0-9]+");

	std::cout << "Digite um número por vez (digite 'q' para parar): \n";

	while (true) {
		std::cout << "Digite um número: ";
		std::getline(std::cin, input);

		if (std::cin.eof() || std::cin.bad()) {
			std::cerr << "Erro ao ler entrada.\n";
			return 1;
		}

		if (input == "q") {
			break;
		}

		if (!std::regex_match(input, numberPattern)) {
			std::cerr << "Entrada inválida. Digite um número ou 'q' para sair.\n";
			continue;
		}

		try {
			int num = std::stoi(input);
			values.push_back(num);
		} catch (...) { 
			std::cerr << "Erro inesperado ao converter o número.\n";
			return 1;
		}
	}

	std::cout << "\nValores lidos:\n";
	for (int num : values) {
		std::cout << num << " ";
	}
	std::cout << std::endl;

	system("pause");
	return 0;
}


// b) Ler 8 elementos em uma matriz A tipo vetor. Construir uma matriz B de mesma dimensão com os
// elementos da matriz A multiplicados por 3. O elemento B[i] deverá ser implicado pelo elemento
// A[i]*3, o elemento B[2] implicado pelo elemento A[2]*3 e assim por diante, até 8. Apresentar o vetor B.
int	multbythree(void) {
	system("cls");
	std::cout << "** b) DIGITE 8 NÚMEROS PARA A MATRIZ A E SERÁ GERADA A MATRIZ B COM SEUS ELEMENTOS MULTIPLICADOS POR 3 **" << std::endl;

	int a[8], b[8];

	while (true) {
		std::cout << "Digite 8 números separados por espaço: ";
		std::string input;
		std::getline(std::cin, input);

		if (std::cin.eof() || std::cin.bad()) {
			std::cerr << "Erro ao ler entrada.\n";
			return 1;
		}

		std::istringstream stream(input);
		std::vector<int> values;
		int num;

		while (stream >> num) {
			values.push_back(num);
		}

		if (values.size() == 8) {
			for (int i = 0; i < 8; i++) {
				a[i] = values[i];
				b[i] = a[i] * 3;
			}
			break;
		}

		std::cerr << "Entrada inválida. Certifique-se de inserir exatamente 8 números separados por espaço.\n";
	}

	std::cout << "\nMatriz B (valores multiplicados por 3):\n";
	for (int num : b) {
		std::cout << num << " ";
	}
	std::cout << std::endl;

	system("pause");
	return 0;
}



// c) Ler duas matrizes A e B do tipo vetor com 20 elementos. Construir uma matriz C, onde cada
// elemento de C é a subtração do elemento correspondente de A com B. Apresentar a matriz C.
int	subtractArrays(void) {
	system("cls");
	std::cout << "** c) SUBTRAI ELEMENTOS DAS MATRIZES A E B PARA GERAR A MATRIZ C **" << std::endl;
	int		check = 0;
	int		a[10], b[10], c[10];

	while (true) {
		std::string		input;

		if (check == 0) {
			std::cout << "Digite 10 números separados por espaço para a matriz A: ";
		}
		else if (check == 1) {
			std::cout << "Digite 10 números separados por espaço para a matriz B: ";
		}
		std::getline(std::cin, input);
		if (std::cin.eof() || std::cin.bad()) {
			std::cerr << "Erro ao ler entrada.\n";
			return 1;
		}

		std::istringstream	stream(input);
		std::vector<int>	values;
		int					num;

		while (stream >> num) {
			values.push_back(num);
		}
		if (values.size() == 10) {
			if (check == 0) {
				for (int i = 0; i < 10; i++) {
					a[i] = values[i];
				}
				check = 1;
				continue;
			}
			if (check == 1) {
				for (int i = 0; i < 10; i++) {
					b[i] = values[i];
				}
				check = 2;
			}
			if (check > 1) {
				for (int i = 0; i < 10; i++) {
					c[i] = a[i] - b[i];
				}
				break;
			}
		}
		std::cerr << "Entrada inválida. Certifique-se de inserir exatamente 8 números separados por espaço.\n";
	}

	std::cout << "\nMatriz C = valores da matriz A - B :\n";
	for (int num : c) {
		std::cout << num << " ";
	}
	std::cout << std::endl;

	system("pause");
	return 0;
}


// d) Ler 15 elementos de uma matriz tipo vetor. Construir uma matriz B de mesmo tipo, observando a
// seguintes lei de formação: “Todo elemento de B deverá ser o quadrado do elemento de A
// correspondente”. Apresentar as matrizes A e B.

int	squareMatrix(void) {
	system("cls");
	std::cout << "** d) DIGITE 15 NÚMEROS PARA A MATRIZ A E SERÁ GERADA A MATRIZ B COM SEUS ELEMENTOS AO QUADRADO **" << std::endl;

	int a[15], b[15];

	while (true) {
		std::cout << "Digite 15 números separados por espaço: ";
		std::string input;
		std::getline(std::cin, input);

		if (std::cin.eof() || std::cin.bad()) {
			std::cerr << "Erro ao ler entrada.\n";
			return 1;
		}

		std::istringstream stream(input);
		std::vector<int> values;
		int num;

		while (stream >> num) {
			values.push_back(num);
		}

		if (values.size() == 15) {
			for (int i = 0; i < 15; i++) {
				a[i] = values[i];
				b[i] = a[i] * a[i];
			}
			break;
		}

		std::cerr << "Entrada inválida. Certifique-se de inserir exatamente 8 números separados por espaço.\n";
	}

	std::cout << "\nMatriz A: ";
	for (int num : a) {
		std::cout << num << " ";
	}
	std::cout << "\nMatriz B (valores de A ao quadrado):\n";
	for (int num : b) {
		std::cout << num << " ";
	}
	std::cout << std::endl;

	system("pause");
	return 0;
}

// e) Ler duas matrizes A e B do tipo vetor com 15 elementos cada. Construir uma matriz C, sendo esta a
// junção das duas outras matrizes. Desta forma, C deverá ter o dobro de elementos, ou seja, 30.
// Apresentar a matriz C.
int	mergeArrays(void) {
	system("cls");
	std::cout << "** e) LÊ 15 ELEMENTOS PARA AS MATRIZES A E B E COMBINA-OS NA MATRIZ C **" << std::endl;
	int		check = 0;
	int		a[15], b[15];
	std::vector<int> c;

	while (true) {
		std::string		input;

		if (check == 0) {
			std::cout << "Digite 15 números separados por espaço para a matriz A: ";
		}
		else if (check == 1) {
			std::cout << "Digite 15 números separados por espaço para a matriz B: ";
		}
		std::getline(std::cin, input);
		if (std::cin.eof() || std::cin.bad()) {
			std::cerr << "Erro ao ler entrada.\n";
			return 1;
		}

		std::istringstream	stream(input);
		std::vector<int>	values;
		int					num;

		while (stream >> num) {
			values.push_back(num);
		}
		if (values.size() == 15) {
			if (check == 0) {
				for (int i = 0; i < 15; i++) {
					a[i] = values[i];
				}
				check = 1;
				std::istringstream	stream(input);
				while (stream >> num) {
					c.push_back(num);
				}
				continue;
			}
			if (check == 1) {
				for (int i = 0; i < 15; i++) {
					b[i] = values[i];
				}
				std::istringstream	stream(input);
				while (stream >> num) {
					c.push_back(num);
				}
				check = 2;
			}
			if (check > 1) {
				break;
			}
		}
		std::cerr << "Entrada inválida. Certifique-se de inserir exatamente 8 números separados por espaço.\n";
	}

	std::cout << "\nMatriz C:\n";
	for (int num : c) {
		std::cout << num << " ";
	}
	std::cout << std::endl;

	system("pause");
	return 0;
}

// f) Ler duas matrizes do tipo vetor, sendo A com 20 elementos e B com 30 elementos. Construir uma
// matriz C, sendo esta a junção das duas outras matrizes. Desta forma, C deverá ter a capacidade de
// armazenar 50 elementos. Apresentar a matriz C.
std::vector<int> a, b, c;
std::string input;
int num;

// Função para ler números
bool	readNumbers(std::vector<int>& vec, int count, const std::string& prompt) {
	while (true) {
		std::cout << prompt;
		std::getline(std::cin, input);
		std::istringstream stream(input);
		vec.clear();

		while (stream >> num) {
			vec.push_back(num);
		}
		if (vec.size() == count) {
			return true;
		}
		std::cerr << "Entrada inválida. Certifique-se de inserir exatamente " << count << " números separados por espaço.\n";
	}
}

int	mergeArraysAgain(void) {
	system("cls");
	std::cout << "** f) LÊ 20 ELEMENTOS PARA A MATRIZ A, 30 PARA B E COMBINA-OS NA MATRIZ C **" << std::endl;

	// Ler os números para A e B
	if (!readNumbers(a, 20, "Digite 20 números separados por espaço para a matriz A: ")) {
		return 1;
	}
	if (!readNumbers(b, 30, "Digite 30 números separados por espaço para a matriz B: ")) {
		return 1;
	}

	// Combinar os vetores A e B na matriz C
	c.insert(c.end(), a.begin(), a.end());
	c.insert(c.end(), b.begin(), b.end());

	// Exibir a matriz C
	std::cout << "\nMatriz C (resultado da junção de A e B):\n";
	for (int value : c) {
		std::cout << value << " ";
	}
	std::cout << std::endl;

	system("pause");
	return 0;
}


// g) Ler 20 elementos de uma matriz A tipo vetor e construir uma matriz B de mesma dimensão com os
// mesmo elementos da matriz A, sendo que deverão estar invertidos. Ou seja, o primeiro elemento de
// A passa a ser o último de B, o segundo elemento de A passa a ser o penúltimo elemento de B e
// assim por diante. Apresentar as matrizes A e B lado a lado.
int	reverseArrays(void) {
	system("cls");
	std::cout << "** g) LÊ 20 ELEMENTOS PARA A MATRIZ A E CONSTRUÍ A MATRIZ B COM OS MESMOS ELEMENTOS, MAS INVERTIDOS **" << std::endl;

	std::vector<int> a(20), b(20);

	// Ler os números para A
	if (!readNumbers(a, 20, "Digite 20 números separados por espaço para a matriz A: ")) {
		return 1;
	}

	// Construir a matriz B invertendo os elementos de A
	for (int i = 0; i < 20; ++i) {
		b[i] = a[19 - i];  // Invertendo os elementos
	}

	// Exibir as matrizes A e B lado a lado
	std::cout << "\nMatriz A e B (invertida) lado a lado:\n";
	for (int i = 0; i < 20; ++i) {
		std::cout << "A[" << i << "] = " << a[i] << " | B[" << i << "] = " << b[i] << std::endl;
	}

	system("pause");
	return 0;
}



int	main (void) {
	int result;

	// a)
	if (readAndDisplayArray()) {
		std::cerr << "Erro ao executar a função readAndDisplayArray.\n";
		return 1;
	}
	// b)
	if (multbythree()) {
		std::cerr << "Erro ao executar a função multbythree.\n";
		return 1;
	}
	// c)
	if (subtractArrays()) {
		std::cerr << "Erro ao executar a função subtractArrays.\n";
		return 1;
	}
	// d)
	if (squareMatrix()) {
		std::cerr << "Erro ao executar a função squareMatrix.\n";
		return 1;
	}
	// e)
	if (mergeArrays()) {
		std::cerr << "Erro ao executar a função mergeArrays.\n";
		return 1;
	}
	f)
	if (mergeArraysAgain()) {
		std::cerr << "Erro ao executar a função mergeArraysAgain.\n";
		return 1;
	}
	// g)
	if (reverseArrays()) {
		std::cerr << "Erro ao executar a função reverseArrays.\n";
		return 1;
	}


	return (0);
}
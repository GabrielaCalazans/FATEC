#include <iostream>
#include <cmath>
#include <iomanip>
#include <cstdlib>

// h) Elaborar um programa que calcule e apresente o volume de uma caixa
// retangular, por meio da fórmula VOLUME ← COMPRIMENTO * LARGURA * ALTURA.
void	calculateRectangularBoxVolume(void) {
	system("cls");
	double width, height, length;

	std::cout << "** h) CALCULADORA DE VOLUME DE UMA CAIXA RETANGULAR **" << std::endl;
	std::cout << "Digite o comprimento da caixa:\t";
	std::cin >> length;
	std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
	std::cout << "Digite a altura da caixa:\t";
	std::cin >> height;
	std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
	std::cout << "Digite a largura da caixa:\t";
	std::cin >> width;
	std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
 
	std::cout << "O volume da caixa retangular de altura " << height << " , comprimento " << length 
	<< " e largura " << width << " é de " << length * width * height << "." << std::endl;
 
	std::cout << std::endl << std::endl;
	system("pause");
}


// i) Ler dois inteiros (variáveis A e B) e imprimir o resultado do quadrado da diferença do primeiro valor pelo
// segundo.
int	squareOfDifference(int a, int b) {
	return (pow(a - b, 2));
}


// j) Elaborar um programa que efetue a apresentação do valor da conversão em real de um valor lido em
// dólar. O programa deve solicitar o valor da cotação do dólar e também a quantidade de dólares
// disponível com o usuário, para que seja apresentado o valor em moeda brasileira.
double	convertDollarToReal(double dollar, double rate) {
	return (dollar * rate);
}

// k) Elaborar um programa que efetue a apresentação do valor da conversão em dólar de um valor lido em
// real. O programa deve solicitar o valor da cotação do dólar e também a quantidade de reais disponível
// com o usuário, para que seja apresentado o valor em moeda americana.
double	convertRealToDollar(double real, double rate) {
	return (real / rate);
}


// l) Elaborar um programa que efetue a leitura de três valores (A, B e C) e apresente como resultado final à
// soma dos quadrados dos três valores lidos.

int	sumOfSquares(int a, int b, int c) {
	return (pow(a, 2) + pow(b, 2) + pow(c, 2));
}


// m) Elaborar um programa que efetue a leitura de três valores (A,B e C) e apresente como resultado final o
// quadrado da soma dos três valores lidos.

int	squareOfSum(int a, int b, int c, int result) {
	system("cls");
	std::cout << "** m) LÊ 3 VALORES E RETORNA O QUADRADO DA SOMA DOS 3 VALORES LIDOS **" << std::endl;

	std::cout << "Digite três números inteiros:\n";
	std::cin >> a >> b >> c;
	std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
	result = pow(a + b + c, 2);
	std::cout << "O quadrado da soma de " << a << ", " << b << " e " << c << " é ";

	std::system("pause");
	return (result);
}

int	main (void) {
	int a, b, c, result;
	double dollar, rate, real;

	// // h)
	calculateRectangularBoxVolume();
	// i)
	system("cls");
	std::cout << "** i) RECEBE DOIS VALORES E RETORNA O QUADRADO DA DIFERENÇA ENTRE O PRIMEIRO E O SEGUNDO VALOR **" 
			<< std::endl;
	std::cout << "Digite dois números inteiros:\n";
	std::cin >> a >> b;
	std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
	result = squareOfDifference(a, b);
	std::cout << "O quadrado da diferença entre " << a << " e " << b << " é " << result << std::endl;
	std::system("pause");
	// j)
	system("cls");
	std::cout << "** j) CONVERTE O VALOR DE DÓLAR PARA REAIS **" << std::endl;
	std::cout << "Digite o valor do dólar e a cotação atual:\n";
	std::cin >> dollar >> rate;
	std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
	std::cout << "O valor de " << dollar << " dólares em reais é de " << convertDollarToReal(dollar, rate) << std::endl;
	std::system("pause");

	// k)
	system("cls");
	std::cout << "** k) CONVERTE O VALOR REAIS PARA DÓLAR **" << std::endl;
	std::cout << "Digite o valor em reais a ser convertido:\n";
	std::cin >> real;
	std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
	std::cout << "Digite cotação atual do dólar:\n";
	std::cin >> rate;
	std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
	std::cout << "O valor de " << real << " reais em dólares é de " << std::fixed << std::setprecision(2) << convertRealToDollar(real, rate) << std::endl;
	std::system("pause");

	// l)
	system("cls");
	std::cout << "** l) LÊ 3 VALORES E RETORNA A SOMADOS QUADRADOS DOS 3 VALORES LIDOS **" << std::endl;
	std::cout << "Digite três números inteiros:\n";
	std::cin >> a >> b >> c;
	std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
	result = sumOfSquares(a, b, c);
	std::cout << "A soma dos quadrados de " << a << ", " << b << " e " << c << " é " << result << std::endl;
	std::system("pause");

	// m)
	result = squareOfSum(a, b, c, result);
	std::cout << "O quadrado da soma dos três valores é " << result << std::endl;


	return (0);
}
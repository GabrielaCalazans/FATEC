// REFERENCIA PARA AULA: https://cplusplus.com/reference/cmath/
// TESTES EM: https://www.onlinegdb.com/

#include <iostream>
#include <cmath>
#include <cstdlib>
# define pi 3.14

using namespace std;

// int	main (void)
// {
// 	system("cls");
// 	setlocale(LC_ALL, "Portuguese");

// 	double resultado;
// 	resultado = pi * 10;
// 	cout << "\nO resultado será: " << resultado << endl;

// 	system("pause");

// 	return (0);
// }



void	averageTwoGrades(void) {
	double nota1=0, nota2=0, media=0;

	system("cls");
	cout << "\nDigite a nota 1\t";
	cin >> nota1;
	cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
	cout << "\nDigite a nota 2\t";
	cin >> nota2;
	cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
	media = (nota1 + nota2)/2;
	cout << "\nO resultado será :\t" << media;
	cout << endl << endl;
	system("pause");
}

// a) Ler uma temperatura em graus Celsius e apresentá-la convertida em graus
// Fahrenheit. A fórmula de conversão é F ← (9 * C + 160) / 5, sendo F a
// temperatura em Fahrenheit e C a temperatura em Celsius

void	celsiusToFahrenheit(void) {
	double	degree, fahrenheit;
	
	system("cls");
	std::cout << "*** a) CONVERSOR DE TEMPERATURA °C PARA °F ***" << std::endl;
	std::cout << "Digite uma temperatura em Celsius:\t";
	std::cin >> degree;
	cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
	fahrenheit = (9 * degree + 160) / 5;

	std::cout << "A temperatura " << degree << " Celsius equivale a " <<
			fahrenheit << " Fahrenheit." << std::endl;

	std::cout << std::endl << std::endl;
	system("pause");
}

// b) Ler uma temperatura em graus Fahrenheit e apresentá-la convertida em graus
// Celsius. A fórmula de conversão é C ← (F - 32) * (5/9) , sendo F a
// temperatura em Fahrenheit e C a temperatura em Celsius

void	FahrenheitToCelsius(void) {
	double degree, celsius;

	system("cls");
	std::cout << "*** b) CONVERSOR DE TEMPERATURA °F PARA °C ***" << std::endl;
	std::cout << "Digite uma temperatura em Fahrenheit:\t";
	std::cin >> degree;
	cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
	celsius = (degree - 32) * 5 / 9;

	std::cout << "A temperatura " << degree << " Fahrenheit equivale a "
				<< celsius << " Celsius." << std::endl;

	std::cout << std::endl << std::endl;
	system("pause");
}

// c) Calcular e apresentar o valor do volume de uma lata de óleo, utilizando a
// fórmula: Volume Raio ** Altura 2 ←π
void	calculateCylinderVolume(void) {
	system("cls");
 
	double radius, height, volume;

	std::cout << "** c) CALCULADORA DE VOLUME DE LATA DE ÓLEO **" << std::endl;
	std::cout << "Digite o raio da lata:\t";
	std::cin >> radius;
	cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
	std::cout << "Digite a altura da lata:\t";
	std::cin >> height;
	cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
	volume = pi * pow(radius, 2) * height;
 
	std::cout << "O volume da lata de altura " << height << " e de raio " << radius << " é de "
			  << volume << "." << std::endl;
 
	std::cout << std::endl << std::endl;
	system("pause");
}


// d) Efetuar o cálculo da quantidade de litros de combustível gasta em uma
// viagem, utilizando um automóvel que faz 12 Km por litro. Para obter o
// cálculo, o usuário deve fornecer o tempo gasto (TEMPO) e a velocidade média
// (VELOCIDADE) durante a viagem. Desta forma, será possível obter a distância
// percorrida com a fórmula DISTANCIA ← TEMPO * VELOCIDADE. Possuindo o valor da
// distância, basta calcular a quantidade de litros de combustível utilizada na
// viagem com a fórmula LITROS_USADOS ← DISTANCIA / 12. Ao final, o programa
// deve apresentar os valores da velocidade média (VELOCIDADE), tempo gasto na
// viagem.

void	calculateTripFuel(void) {
	system("cls");
 
	double time, distance, speed, fuel;

	std::cout << "** d) CALCULADORA LITROS DE COMBUSTÍVEL PARA CARRO DE CONSUMO 12KM POR LITRO **" << std::endl;
	std::cout << "Digite o tempo gasto na viagem:\t";
	std::cin >> time;
	cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
	std::cout << "Digite a velocidade média da viagem:\t";
	std::cin >> speed;
	cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
	distance = time * speed;
	fuel = distance / 12;

	std::cout << "O combustível gasto na viagem de velocidade média " << speed << "km/h no tempo de " << time << " é de "
			  << fuel << "." << std::endl;
 
	std::cout << std::endl << std::endl;
	system("pause");
}

// e) Efetuar o cálculo e a apresentação do valor de uma prestação em atraso,
// utilizando a fórmula PRESTACAO ← VALOR + (VALOR * TAXA/100) * TEMPO).
void	calculateLatePayment(void) {
	system("cls");
 
	double amount, rate, time, installment;

	std::cout << "** e) CALCULADORA DE PRESTAÇÃO EM ATRASO **" << std::endl;
	std::cout << "Digite o valor da prestação:\t";
	std::cin >> amount;
	std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
	std::cout << "Digite os dias de atraso:\t";
	std::cin >> time;
	std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
	std::cout << "Digite a taxa do financiamento:\t";
	std::cin >> rate;
	std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

	amount += (amount * rate / 100) * time;
	std::cout << "O valor da parcela em atraso por " << time << " dias é de: " << amount << std::endl;
 
	std::cout << std::endl << std::endl;
	system("pause");
}


// f) Ler dois valores (inteiros, reais ou caracteres) para as variáveis A e B,
// e efetuar a troca dos valores de forma que a variável A passe a possuir o
// valor da variável B e a variável B passe a possuir o valor da variável A.
// Apresentar os valores trocados
void	swapValue(void) {
	system("cls");
 
	double a, b, temp;

	std::cout << "** f) TROCA DE VALOR DAS VARIÁVEIS **" << std::endl;
	std::cout << "Digite um número para variavel 'a':\t";
	std::cin >> a;
	std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
	std::cout << "Digite um número para variavel 'b':\t";
	std::cin >> b;
	std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

	temp = a;
	a = b;
	b = temp;
	// std::swap(a, b);
	std::cout << "Novo valor da variável a: " << a << " novo valor da variável b: " << b << std::endl;
 
	std::cout << std::endl << std::endl;
	system("pause");
}

// g) Ler quatro números inteiros e apresentar o
// resultado da adição e multiplicação, baseando-se na utilização do conceito da
// propriedade distributiva. Ou seja, se forem lidas as variáveis A, B, C, e D,
// devem ser somadas e multiplicadas A com B, A com C e A com D. Depois B com C,
// B com D e por fim C com D. Perceba que será necessário efetuar seis operações
// de adição e seis operações de multiplicação e apresentar doze resultados de
// saída.
void	calculateDistributiveOperations(void) {
	system("cls");
 
	int a, b, c, d;

	std::cout << "** g) MULTIPLICAÇÃO E SOMA DE VALORES **" << std::endl;
    std::cout << "Digite 4 números inteiros:\n"; 
    std::cin >> a >> b >> c >> d;
	std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

    std::cout << "\nResultados da Adição:\n";
    std::cout << "A + B = " << (a + b) << std::endl;
    std::cout << "A + C = " << (a + c) << std::endl;
    std::cout << "A + D = " << (a + d) << std::endl;
    std::cout << "B + C = " << (b + c) << std::endl;
    std::cout << "B + D = " << (b + d) << std::endl;
    std::cout << "C + D = " << (c + d) << std::endl;

    std::cout << "\nResultado da Multiplicação:\n";
    std::cout << "A * B = " << (a * b) << std::endl;
    std::cout << "A * C = " << (a * c) << std::endl;
    std::cout << "A * D = " << (a * d) << std::endl;
    std::cout << "B * C = " << (b * c) << std::endl;
    std::cout << "B * D = " << (b * d) << std::endl;
    std::cout << "C * D = " << (c * d) << std::endl;
 
	std::cout << std::endl << std::endl;
	system("pause");
}

// h) Elaborar um programa que calcule e apresente o volume de uma caixa
// retangular, por meio da fórmula VOLUME ← COMPRIMENTO * LARGURA * ALTURA.
void	calculateRectangularBoxVolume(void) {
	system("cls");
	double width, height, length;

	std::cout << "** h) CALCULADORA DE VOLUME DE UMA CAIXA RETANGULAR **" << std::endl;
	std::cout << "Digite o comprimento da caixa:\t";
	std::cin >> length;
	cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
	std::cout << "Digite a altura da caixa:\t";
	std::cin >> height;
	cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
	std::cout << "Digite a largura da caixa:\t";
	std::cin >> width;
	cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
 
	std::cout << "O volume da caixa retangular de altura " << height << " , comprimento " << length 
	<< " e largura " << width << " é de " << length * width * height << "." << std::endl;
 
	std::cout << std::endl << std::endl;
	system("pause");
}


int	main (void) {
	// a)
	celsiusToFahrenheit();
	// b)
	FahrenheitToCelsius();
	// c)
	calculateCylinderVolume();
	// d)
	calculateTripFuel();
	// e)
	calculateLatePayment();
	// f)
	swapValue();
	// g)
	calculateDistributiveOperations();
	// h)
	calculateRectangularBoxVolume();

	return (0);
}
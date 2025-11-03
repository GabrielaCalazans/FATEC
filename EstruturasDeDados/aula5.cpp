#include <iostream>
#include <cmath>
#include <iomanip>
#include <cstdlib>
#include "string.h"


// A) Elaborar um programa de computador que efetue a leitura de quatro valores inteiros (variáveis A, B, C e
// D). Ao final o programa deve apresentar o resultado do produto (variável P) do primeiro com o terceiro
// valor, e o resultado do produto (variável P) do primeiro com o terceiro valor, e o resultado da soma
// (variável S) do segundo com o quarto valor.

	// a) Os dados de entrada e saída deverão ser armazenados em um struct com várias colunas; 
	// b) Deverá conter menu com switch case, funções para leitura dos dados
	// de entrada e as respectivas funções para calcular os dados de saída; 
	// c) Tanto os dados de entrada quando os dados de saída deverão ser armazenados dentro de structs.

typedef struct	intOperations opt;

using namespace std;

struct	intOperations {
	int	A;
	int	B;
	int	C;
	int	D;
	int	P;
	int	S;
};

void	lerInt(opt &dados) {
	cout << "Digite 4 números inteiros separados por espaço (Ex.: 20 4 500 1):\n";
	cin >> dados.A >> dados.B >> dados.C >> dados.D;
	cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
	cout << "Os números digitados foram: " << dados.A << " " << dados.B << " " << dados.C << " " << dados.D << endl;
	system("pause");
}

void	processar_opt(opt &dados) {
	dados.P = dados.A * dados.C;
	dados.S = dados.B + dados.D;
}

void	exibirResultados_opt(const opt &dados) {
	cout << "Produto de A(" << dados.A << ") e C(" << dados.C << "): " << dados.P << endl;
	cout << "Soma de B(" << dados.B << ") e D(" << dados.D << "): " << dados.S << endl;
	cout << endl;
	system("pause");
}

void	programA(void) {
	opt	dados;
	int	tecla;

	MENU:
		system("cls");
		cout << "** A) PROGRAMA PRODUTO E SOMA DE VALORES **" << endl;
		cout << "* Menu *\n1 ler valores\n2 exibir resultados\n3 sair\nitem: ";
		cin >> tecla;
		switch ( tecla )
		{
			case 1:
				lerInt(dados);
				processar_opt(dados);
				break;
			case 2: exibirResultados_opt(dados);
				break;
			case 3:
				cout << "Programa encerrando..." << endl << endl;
				return;
		}
		goto MENU;
	system("pause");
}

// B) Ler o valor correspondente ao salário mensal (variável SM) de um trabalhador e também o valor do
// percentual de reajuste (variável PR) a ser atribuído. Apresentar o valor do novo salário (variável NS).

	// a) Os dados de entrada e saída deverão ser armazenados em um struct com várias colunas; 
	// b) Deverá conter menu com switch case, funções para leitura dos dados
	// de entrada e as respectivas funções para calcular os dados de saída; 
	// c) Tanto os dados de entrada quando os dados de saída deverão ser armazenados dentro de structs.

typedef struct	salarioMensal sal;

struct	salarioMensal {
	float	SM;
	float	PR;
	float	NS;
};

void	lerFloat(sal &dados) {
	cout << "Digite o salário mensal:\t";
	cin >> dados.SM;
	cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
	cout << "Digite o percentual de reajuste:\t";
	cin >> dados.PR;
	cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
	cout << "Os valores digitados foram salário mensal: " << dados.SM << " percentual de reajuste: " << dados.PR << endl;
	system("pause");
}

void	processar_salario(sal &dados) {
	dados.NS = dados.SM + (dados.SM * (dados.PR / 100));
}

void	exibirResultados_salario(const sal &dados) {
	cout << fixed << setprecision(2);
	cout << "O novo salário é: " << dados.NS << endl;
	cout << "O valor do reajuste foi: " << (dados.SM * (dados.PR / 100)) << endl;
	cout << endl;
	system("pause");
}

void	programB(void) {
	sal	dados;
	int	tecla;

	MENU:
		system("cls");
		cout << "** B) SALÁRIO MENSAL E REAJUSTE **" << endl;
		cout << "* Menu *\n1 ler valores\n2 exibir resultados\n3 sair\nitem: ";
		cin >> tecla;
		switch ( tecla )
		{
			case 1:
				lerFloat(dados);
				processar_salario(dados);
				break;
			case 2: exibirResultados_salario(dados);
				break;
			case 3:
				cout << "Programa encerrando..." << endl << endl;
				return;
		}
		goto MENU;
	system("pause");
}


int	main (void) {

	programA();
	programB();

	return (0);
}

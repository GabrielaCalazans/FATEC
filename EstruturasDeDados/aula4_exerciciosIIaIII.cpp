#include "iostream"
#include "cstdlib"
#include <tuple>

using namespace std;

// II - Faça o algoritmo para calcular o valor de uma prestação em atraso
// com base na multa de 2% e também do juros mensal de 1% sobre o valor
// principal. Declare vetores não explícitos para entrada do valor da dívida, Divida
// [5] e da quantidade de dias em atraso: Dias [5]. Crie os vetores de saída,
// ValorMulta[5], ValorJuros[5] e ValorPagar [5]. Ao final imprima todos os vetores
// de saída. Faça um menu de controle para controlar o programa.
int		Dias   [5];
float	Divida [5], ValorMulta [5], ValorJuros [5], ValorPagar [5];
int		linha = -1;


double lerDivida(void) {
	double divida;

	cout << "\nValor da Dívida: ";
	cin >> divida;
	return divida;
}

int	lerDias(void) {
	int	dias;

	cout << "\nDias de atraso: ";
	cin >> dias;
	return dias;
}

void	guardarDadosEntrada ( int dias, double divida ) {
	linha ++;
	Dias[linha] = dias;
	Divida[linha] = divida;
}

void	guardarDadosSaida ( double valorMula, double valorJuros, double valorPagar ) {
	ValorMulta[linha] = valorMula;
	ValorJuros[linha] = valorJuros;
	ValorPagar[linha] = valorPagar;
}

void	listarDadosSaida(void) {
	for ( int i = 0; i<= linha; i++) {
		cout << "Divida: " << i+1 << "\tvalor da multa: " << ValorMulta[i] << " - valor do juros " << ValorJuros[i] << " - valor total a pagar " << ValorPagar[i] << endl;
	}
	system("pause");
}

void	listarDadosEntrada (void) {
	for ( int i = 0; i<= linha; i++) {
		cout << "Divida: " << i+1 << "\tvalor da dívida: " << Divida[i] << " - dias de atraso " << Dias[i] << endl;
	}
	system("pause");
}

std::tuple<double, double, double>	processarDados( int dias, double divida ) {
	double valorMulta, valorJuros, valorPagar;

	valorMulta = divida * 0.02;
	valorJuros = divida * 0.01 * dias;
	valorPagar = divida + valorMulta + valorJuros;
	return std::make_tuple(valorMulta, valorJuros, valorPagar);
}

// III - Crie um algoritmo que tenha um vetor de idades e um vetor de nomes,
// cujos dados deverão ser lidos pelo teclado. Ao final Exiba o nome da pessoa
de maior idade, menor idade, a média das idades e o saldo das idades.
string	Nome   [5];
int		Idade  [5];

string	lerNome(void) {
	string	nome;

	cout << "\nNome: ";
	cin.ignore( );
	getline(cin, nome);
	return nome; 
}

int	lerIdade(void) {
	int	idade;

	cout << "\nIdade: ";
	cin >> idade;
	return idade;
}

void	guardarDados ( string nom, int ida ) {
	linha ++;
	Nome[linha] = nom;
	Idade[linha] = ida;
}

void	listarDados(void) {
	for ( int i = 0; i<=linha; i++) {
		cout << Nome[i] << " - " << Idade[i] << endl;
	}
	system("pause");
}

void	processarDadosIdades() {
	int		maior, menor;
	string	maiorNome, menorNome;
	float	media, soma = 0;
	int tot = sizeof(Idade)/sizeof(int);
	for (int i = 0; i< tot; i++) {
		if ( Idade[i] > maior || i == 0 ) {
			maior = Idade[i];
			maiorNome = Nome[i];
		}
		if ( Idade[i] < menor || i == 0 ) {
			menor = Idade[i];
			menorNome = Nome[i];
		}
		soma += Idade[i];
	}
	media = soma / tot;
	cout << "\nMaior idade: " << maiorNome << " - " << maior << " anos." << endl;
	cout << "\nMenor idade: " << menorNome << " - " << menor << " anos." << endl;
	cout << "\nMédia de idades: " << media << endl;
	system("pause");
}

int	main (void) {
	int		tecla;
	int		dias_; double divida_;
	string	nome_; int idade_;

	// PROGRAMA II
	cout << "PROGRAMA II - valor de uma prestação em atraso\n";
	MENU:
		system("cls");
		cout << "* Menu *\n1 ler dívida\n2 exibir dívidas inseridas\n3 exibir valores a pagar\n4 sair\nitem: ";
		cin >> tecla;
		switch ( tecla )
		{
			case 1:
				divida_ = lerDivida();
				dias_ = lerDias();
				guardarDadosEntrada( dias_, divida_ );
				{
					auto [valorMulta, valorJuros, valorPagar] = processarDados(dias_, divida_);
					guardarDadosSaida(valorMulta, valorJuros, valorPagar);
				}
				break;
			case 2: listarDadosEntrada();
				break;
			case 3: listarDadosSaida();
				break;
			case 4: listarDadosSaida();
				exit(0);
				break;
		}
		goto MENU;

	PROGRAMA III
	cout << "PROGRAMA III - Idades e Nomes\n";
	MENU:
		system("cls");
		cout << "* Menu *\n1 ler\n2 exibir resultados\n3 listar dados inseridos\n4 sair\nitem: ";
		cin >> tecla;
		switch ( tecla )
		{
			case 1:
				nome_ = lerNome();
				idade_ = lerIdade();
				guardarDados( nome_, idade_ );
				break;
			case 2: processarDadosIdades();
				break;
			case 3: listarDados();
				break;
			case 4:
				exit(0);
				break;
		}
		goto MENU;
	return (0);
}



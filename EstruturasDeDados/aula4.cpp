#include "iostream"
#include "cstdlib"

using namespace std;

int			xy [ ] = { 1, 5, 10, -1 };

void	maiorMenor (void) {
	int maior, menor;
	int tot = sizeof(xy)/sizeof(int);
	for (int i = 0; i< tot; i++) {
		if ( xy[i] > maior || i == 0 ) maior = xy[i];
		if ( xy[i] < menor || i == 0 ) menor = xy[i]; }
	cout << "\nMaior: " << maior;
	cout << "\nMenor: " << menor << endl;
	system("pause");
}

int			vet [ ] = {1, 3, 4, -1 };

float	MediaVetor (void) {
	float soma, media = 0;
	int n = sizeof(vet)/sizeof(int);
	for (int i = 0; i<n; i++)
	{ 
		soma += vet[i]; 
	}
	media = soma / n ;
	return media ;
}

int			linha = -1;
std::string	nome[4];
int			idade[4];
float		salario[4];

string lerNome(void) {
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

double lerSalario(void) {
	double sal;

	cout << "\nSalário: ";
	cin >> sal;
	return sal;
}

void	guardarDados ( string nom, int ida, double sal ) {
	linha ++;
	nome[linha] = nom ;
	idade[linha] = ida;
	salario[linha] = sal; 
}

void	listar (void) {
	for ( int i = 0; i<=linha; i++) {
		cout << nome[i] << " - " << idade[i] << " - " << salario [i] << endl ;
	}
	system("pause");
}

int	main (void) {
	//PROGRAMA 1
	system("cls");
	cout << "PROGRAMA 1\n";
	string nome_; int idade_; double salario_;
	maiorMenor ( );

	//PROGRAMA 2
	cout << "PROGRAMA 2\n";
	float vlmedia = MediaVetor();
	cout << vlmedia << endl;
	system("pause");

	//PROGRAMA 3
	system("cls");
	cout << "PROGRAMA 3\n";
	int tecla;
	MENU:
		system("cls");
		cout << "* Menu *\n1 ler\n2 exibir\n3 sair\nitem: ";
		cin >> tecla;
		switch ( tecla )
		{
			case 1:
			nome_ = lerNome();
				idade_ = lerIdade();
				salario_= lerSalario();
				guardarDados ( nome_, idade_,salario_);
				break;
			case 2: listar ();
				break;
			case 3: exit(0); break;
		}
		goto MENU;
	return (0);
}



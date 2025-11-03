#include <iostream>
#include <cmath>
#include <iomanip>
#include <cstdlib>
#include "string.h"

typedef struct	firstData pessoa;

using namespace std;

struct firstData {
	string nome;
	int idade;
	string endereco;
};

void	unsingStructs(void) {
	pessoa	gabriela;

	gabriela.idade = 36;
	gabriela.nome = "Gabriela";
	gabriela.endereco = "Av. Hum, número zero";

	std::cout << "Bora ver resultados" << gabriela.idade << " " << gabriela.nome << " " << gabriela.endereco << endl;
}

// //PROGRAMA 1
int const n=5; int linha=-1;

struct	disciplinas {
	string nome[n];
	double media[n];
};

struct	disciplinas tb;

// função para ler nomes
string ler_nome() {
	string nome;
	cout<<"\nNome:";
	cin.ignore(); getline( cin, nome);
	return nome;
}

// função para ler a média do aluno
double	ler_media() {
	double media;
	cout<<"\nMedia:";
	cin>>media;
	return media;
}
 
void	guardarDados ( ) {
	linha++;
	tb.nome [linha] = ler_nome();
	tb.media [linha] = ler_media();
}

void	exibir() {
	system("cls");
 
	for ( int i=0;i<=linha;i++) {
		cout<<endl<<tb.nome[i];
		cout<<"-"<<tb.media[i] << endl;
	}
	system("pause");
}

//PROGRAMA 2

struct	disciplinas {
	string nome [n];
	double nota1 [n];
	double nota2 [n];
	double media [n];
};

struct disciplinas tbmedias;

string	ler_nome () {
	string nome;
	cout<<"\nnome:"; cin.ignore(); 
	getline(cin,nome);
	return nome;
}
 
double	ler_nota1() {
	double m;
	cout<<"\nNota1:"; cin>>m;
	return m;}
 
double	ler_nota2 () {
	double m;
	cout<< "\nNota2:"; cin>> m;
	return m;
}

void guardarDados () {
	linha++;
	string nom_temp = ler_nome();
	tbmedias.nome[linha]= nom_temp;
	tbmedias.nota1[linha]= ler_nota1();
	tbmedias.nota2[linha]= ler_nota2();}
	
void	processar ( ) {
	system("clear");
	for (int i=0; i<=linha;i++) {
		tbmedias.media[i]=(tbmedias.nota1[i] + tbmedias.nota2[i])/2;
	}
	cout << "processando...." << endl;
	system("sleep 2");
	}

void	exibir () { system("clear");
	for ( int i=0; i<= linha; i++) {
		cout << tbmedias.nome[i];
		cout<< " - " << tbmedias.nota1[i];
		cout<< " - " << tbmedias.nota2[i];
		cout<< " - " << tbmedias.media[i] << endl;
	}
	system("sleep 3");
}
	

int	main(void) {
	int tecla=0;

	unsingStructs();
	system("pause");
	//PROGRAMA 1
	while (tecla != 3) {
		system("clear");
		cout<< "\n1 Ler\n2 Exibir\n3 Sair\nitem:";
		cin >> tecla;
		switch(tecla) {
			case 1: guardarDados ( ); break;
			case 2: exibir ( ); break;
			case 3: exit ( 0 ) ; break; 
		}
	}
	//PROGRAMA 2
	guardarDados ( );
	guardarDados ( );
	guardarDados ( );
	processar ( );
	exibir ( );

	return 0;
}
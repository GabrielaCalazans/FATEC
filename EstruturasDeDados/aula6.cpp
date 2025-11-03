#include "iostream"
#define max 4

using namespace std;

struct Registro {
	string	nome;
	float	salario;
	int		idade;
};

typedef struct lifo funcionarios;

struct lifo {
    Registro	dado[max];
    int			topo;
};

Registro lerRegistro(void) {
    Registro	reg;

    cout << "\nDigite o nome do funcionário: ";
    cin.ignore();
    getline(cin, reg.nome);
    cout << "Digite a idade do funcionário: ";
    cin >> reg.idade;
    cout << "Digite o salário do funcionário: ";
    cin >> reg.salario;
    return reg;
}


bool	cheia(funcionarios p) {
	return p.topo == max - 1;
}

bool	vazia(funcionarios p) {
	return p.topo == -1;
}

funcionarios	push (Registro reg, funcionarios p) {
	if ( cheia ( p ) == true) {
		cout << "\nPilha Cheia\n";
		system("pause");
		return p;
	}
	p.topo ++;
	p.dado[p.topo] = reg;
	cout << "\nRegistro empilhado com sucesso!\n";
	system("pause");
	return p;
}

funcionarios	pop (funcionarios p) {
	if (vazia(p) == true) {
		cout << "\nA pilha já está vazia!";
		system("pause"); return p;
	}
	cout << "\nRegistro desempilhado:\n";
	cout << "Nome: " << p.dado[p.topo].nome << "\n";
	cout << "Idade: " << p.dado[p.topo].idade << "\n";
	cout << "Salário: " << p.dado[p.topo].salario << "\n";
	system("pause");
	p.topo--;
	return p;
}

void	mostrar (funcionarios p) {
	if (vazia(p) == true) {
		cout << "\nA pilha está vazia!";
		system("pause");
		return;
	}
	cout << "\nRegistros na pilha:\n";
	for (int i=p.topo; i>=0; i--) {
	cout << "Nome: " << p.dado[i].nome << "\n";
	cout << "Idade: " << p.dado[i].idade << "\n";
	cout << "Salário: " << p.dado[i].salario << "\n";
	cout << "----------------------\n";
	}
	system("pause");
}

int tela(void) {
		int	tecla;
		system("cls");

		cout << "\nMenu\n1 Inserir dados do funcionário\n2 Pop\n3 Mostrar registros\n4 Sair\nItem: ";
		cin >> tecla;
		return tecla;
}

void	Controle( funcionarios p1 ) {
	int			tecla, valor;
	Registro	reg;

	p1.topo = -1;
	do {
		tecla = tela();
		switch(tecla) {
			case 1:
				reg = lerRegistro();
				p1 = push(reg, p1);
				break;
			case 2:
				p1 = pop(p1);
				break;
			case 3:
				mostrar ( p1 );
				break;
		}
} while (tecla != 4);
	cout << "\nPrograma Finalizado...!\n";
}

// Faça o código estruturado para controlar uma LIFO com arranjo não
// dinâmico contendo os atributos: nome, idade e salário. Você deverá
// implementar as seguintes sub rotinas obrigatŕias :
// A. push() para empilhar o registro
// B. pop() para remover registros
// C. int mostrar() para mostrar os registros da LIFO
// D. bool cheia() verificar se a LIFO está cheia
// E. bool vazia() verificar se a LIFO está vazia
// F. int tela () exibe a tela e armazena a opção de escolha do menu
// G. void Controle() controla o menu de controle da LIFO

int	main() {
	funcionarios p1;
	Controle ( p1 );
	return 0;
}


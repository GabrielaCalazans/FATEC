#include "iostream"
#define max 3

using namespace std;

typedef struct lifo pilha;

struct lifo {
	int topo;
	int dado[max];
};
int	lerValor(void) {
	int	valor;

	cout << "\nDigite o valor a ser empilhado: ";
	cin >> valor; return valor;
}

bool	pilhaCheia(pilha p) {
	if (p.topo == max - 1)
		return true;
	return false;
}

bool	pilhaVazia(pilha p) {
	if (p.topo==-1)
		return true;
	return false; 
}

pilha push (int valor, pilha p) {
	if ( pilhaCheia ( p ) == true) {
		cout << "\nPilha Cheia\n";
		system("pause");
		return p;
	}
	p.topo ++;
	p.dado[p.topo] = valor;
	cout << "\nO valor empilhado foi " << valor << endl;
	system("pause");
	return p;
}

pilha pop (pilha p) {
	if (pilhaVazia(p) == true)
	{
		cout << "\nA pilha já está vazia!";
		system("pause"); return p;
	}
	cout << "\nO valor desempilhado será: " << p.dado[p.topo] << endl;
	system("pause");
	p.dado[p.topo] = '\0';
	p.topo --;
	return p;
}

void	mostrarPilha (pilha p) {
	if (pilhaVazia(p) == true)
	{
		cout << "\nA pilha está vazia!";
		system("pause"); return; }
		for (int i=p.topo; i>=0; i--)
			cout << p.dado[i] << endl; system("pause");
}

int tela(void) {
		int	tecla;
		system("cls");

		cout << "\nMenu\n1 Push\n2 Pop\n3 Mostrar pilha\n4 Sair\nItem: ";
		cin >> tecla;
		return tecla;
}

void	controlarPilha ( pilha p1 ) {
	int tecla, valor;
	p1.topo = -1;
	do {
		tecla = tela();
		switch(tecla) {
			case 1: valor = lerValor();
				p1 = push(valor, p1);
				break;
			case 2: p1 = pop(p1); break;
			case 3: mostrarPilha ( p1 );
		}
} while (tecla != 4);
	cout << "\nPrograma Finalizado...!\n";
}

int	main() {
	pilha p1;
	controlarPilha ( p1 );
	return 0;
}


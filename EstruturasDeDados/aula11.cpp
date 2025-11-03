#include <iostream>
#include <cstdlib>

using namespace std;

int	total;			// contar o total de elementos

struct	noFifo {
	int		chave;	// Sequencial número
	noFifo	* prox;	//ponteiro para guardar o próximo elemento da fifo
};

noFifo*	primeiroNo;	// endereço do primeiro elemento
noFifo*	ultimoNo;	// endereço do último elemento

void	construtor () {
	primeiroNo = ultimoNo = NULL;
	total = 0;
	cout << "\nFIFO iniciada!\n";
	system("pause");
}

bool	vazia () {
	if ( primeiroNo == NULL)
		return true;
	return false;
}

void	inserirNo ( int valor ) {
	noFifo*	novoNo = ( noFifo * )malloc ( sizeof ( noFifo ) );

	if ( novoNo == NULL ) {
		cout << "\nErro de alocação!" << endl;
		system("pause");
		return ;
	}
	// Configurar os atributos internos
	novoNo->chave = valor; // coloca o valor
	novoNo->prox = NULL;   // configurar o ponteiro interno
	total ++;  // incrementa o total
	// configura atributos internos do novo Nó
	if ( vazia () == true ) {
		cout << "\nFIFO vazia, inserindo o primeiro elemento!" << endl;
		primeiroNo = ultimoNo = novoNo;
	}  else  {
		ultimoNo->prox = novoNo;
		ultimoNo = novoNo;
		cout << "\nElemento inserido com sucesso!" << endl;
		cout << "\nTotal de elementos na FIFO: " << total << endl;
	}
	system("pause");
}

void	plotar () {
	noFifo*	temp;

	if (primeiroNo == NULL) {
		cout << "\nFIFO vazia!" << endl;
		system("pause");
		return;
	}
	temp = primeiroNo;
	while ( temp != NULL )  {
		cout << temp->chave << endl;
		temp = temp->prox;
	}
	cout << endl;
	system("pause");
}

void	destrutor() {
	noFifo*	temp = primeiroNo;

	while (temp != NULL) {
		noFifo* prox = temp->prox;
		free(temp);
		temp = prox;
	}
	primeiroNo = NULL;
	ultimoNo = NULL;
	total = 0;
	cout << "\nFIFO destruída...!" << endl;
	system("pause");
}

void removerNo() {
	if (vazia()) {
		cout << "\nFila já está vazia!" << endl;
		system("pause");
		return;
	}
	noFifo* temp = primeiroNo;
	primeiroNo = temp->prox;
	if (primeiroNo == NULL) {
		ultimoNo = NULL;
	}
	free(temp);
	total--;
	cout << "\nElemento removido com sucesso!" << endl;
	system("pause");
}

void controle() {
	int item, valor;
	construtor();
	while (true) {
		system("cls");
		cout << "1 Inserir\n2 Remover\n3 Plotar\n4 sair\nitem:\t";
		cin >> item;

		if (cin.fail()) {
            cin.clear();
            cin.ignore(10000, '\n');
            cout << "\nEntrada inválida! Tente novamente.\n";
            system("pause");
            continue;
        }
		switch (item)
		{
			case 1:
				cout << "Digite o valor a ser enfileirado:\t";
				cin >> valor;
				if (cin.fail()) {
					cin.clear();
					cin.ignore(10000, '\n');
					cout << "\nValor inválido!\n";
					system("pause");
					break;
				}
				inserirNo ( valor );
				break;
			case 2:
				removerNo();
				break;
			case 3:
				plotar();
				break;
			case 4:
				destrutor();
				cout << "\nSaindo do programa...\n";
				system("pause");
				exit(0);
				break;
			default:
				cout << "\nOpção inválida! Tente novamente.\n";
				system("pause");
				break;
		}
	}
}

int	main() {
	controle();

	return 0; 
}

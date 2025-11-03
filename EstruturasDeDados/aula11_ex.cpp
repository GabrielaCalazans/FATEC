#include <iostream>
#include <cstdlib>
#include <cstring>

using namespace std;

struct Pessoa {
	char cpf[15];
	char nome[100];
	char email[100];
	char telefone[20];
};

struct noFifo {
	Pessoa pessoa;
	noFifo* prox;
};

noFifo* primeiroNo = NULL;
noFifo* ultimoNo = NULL;
int total = 0;

void construtor() {
	primeiroNo = ultimoNo = NULL;
	total = 0;
	cout << "\nFIFO iniciada!\n";
	system("pause");
}

bool vazia() {
	return (primeiroNo == NULL);
}

void inserirNo() {
	noFifo* novoNo = (noFifo*)malloc(sizeof(noFifo));
	if (novoNo == NULL) {
		cout << "\nErro de alocação!" << endl;
		system("pause");
		return;
	}

	cout << "Digite o CPF: ";
	cin.ignore();
	cin.getline(novoNo->pessoa.cpf, 15);

	cout << "Digite o nome: ";
	cin.getline(novoNo->pessoa.nome, 100);

	cout << "Digite o email: ";
	cin.getline(novoNo->pessoa.email, 100);

	cout << "Digite o telefone: ";
	cin.getline(novoNo->pessoa.telefone, 20);

	novoNo->prox = NULL;
	total++;

	if (vazia()) {
		primeiroNo = ultimoNo = novoNo;
	} else {
		ultimoNo->prox = novoNo;
		ultimoNo = novoNo;
	}
	cout << "\nPessoa inserida com sucesso!\n";
	cout << "Total de pessoas na FIFO: " << total << endl;
	system("pause");
}

void plotar() {
	if (vazia()) {
		cout << "\nFIFO vazia!" << endl;
		system("pause");
		return;
	}
	noFifo* temp = primeiroNo;
	int i = 1;
	while (temp != NULL) {
		cout << "\nPessoa " << i++ << ":\n";
		cout << "CPF: " << temp->pessoa.cpf << endl;
		cout << "Nome: " << temp->pessoa.nome << endl;
		cout << "Email: " << temp->pessoa.email << endl;
		cout << "Telefone: " << temp->pessoa.telefone << endl;
		temp = temp->prox;
	}
	cout << endl;
	system("pause");
}

void destrutor() {
	noFifo* temp = primeiroNo;
	while (temp != NULL) {
		noFifo* prox = temp->prox;
		free(temp);
		temp = prox;
	}
	primeiroNo = ultimoNo = NULL;
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
	cout << "\nPessoa removida:\n";
	cout << "CPF: " << temp->pessoa.cpf << endl;
	cout << "Nome: " << temp->pessoa.nome << endl;
	cout << "Email: " << temp->pessoa.email << endl;
	cout << "Telefone: " << temp->pessoa.telefone << endl;
	free(temp);
	total--;
	system("pause");
}

void controle() {
	int item;
	construtor();
	while (true) {
		system("cls");
		cout << "1 Inserir pessoa\n2 Remover pessoa\n3 Listar pessoas\n4 Sair\nitem:\t";
		cin >> item;

		if (cin.fail()) {
			cin.clear();
			cin.ignore(10000, '\n');
			cout << "\nEntrada inválida! Tente novamente.\n";
			system("pause");
			continue;
		}
		switch (item) {
			case 1:
				inserirNo();
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

int main() {
	controle();
	return 0;
}
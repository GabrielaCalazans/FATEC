// #include <iostream>
// #include <cstdlib>
// #include <stdlib.h>
// using namespace std;

// typedef struct nopilha pilha;
// struct nopilha {
// 	int		valor;
// 	pilha	*ant;
// };

// pilha * topo = NULL;

// void	push ( int valor ) {
// 	pilha	* newpilha = ( pilha * ) malloc ( sizeof( pilha ) );

// 	if ( newpilha == NULL ) {
// 		cout << "Alocação não realizada!Error!" << endl;
// 		system("sleep 2");
// 		return;
// 	}

// 	newpilha->valor = valor;
// 	newpilha->ant = topo; /* Na primeira alocação o topo ainda será nulo */
// 	topo = newpilha;
// }

// void	pop () {
// 	pilha	*temp;

// 	temp = topo; /*Guarda o topo em temp */
// 	topo = temp->ant; /* muda o topo para o elemento anterior*/
// 	free ( temp ); /* Exclui o temp anterior */
// }

// void	plotar () {
// 	pilha	*temp;

// 	temp = topo;
// 	system("clear");

// 	while ( temp != NULL ) {
// 	cout << "\n" << temp->valor << endl;
// 	temp = temp->ant;
// 	}
// 	system("sleep 2");
// }

// void	destrutor() {
// 	pilha	*temp, *aux;

// 	temp = topo;
// 	while ( temp != NULL ) {
// 	aux = temp;
// 	temp = temp->ant;
// 	free ( aux );
// 	}
	
// 	cout << "\na pilha foi destruida!" << endl;
// 	system("sleep 3");
// }

// void	controle() {
// 	int	item, valor;

// 	while (true){
// 		system("clear");
// 		cout << "1 push() ";
// 		cout << "\n2 plotar()";
// 		cout << "\n3 pop()";
// 		cout << "\n4 sair";
// 		cout << "\nitem:";
// 		cin >> item;
// 		switch (item) {
// 		case 1: cout << "Digite o valor:";
// 				cin >> valor;
// 				push ( valor );
// 				break;
// 		case 2: plotar();
// 				break;
// 		case 3: pop();
// 				break;
// 		case 4: destrutor();
// 				exit(0);
// 				break;
// 		}
// 	}
// }

// int	main() {
// 	controle();
// }

#include <iostream>
#include <cstdlib>
#include <cstring>
using namespace std;

struct NoPilha {
    char nome[50];
    float salario;
    NoPilha* ant;
};

NoPilha* topo = nullptr;

void empilhar(const char* nome, float salario) {
    NoPilha* novo = (NoPilha*) malloc(sizeof(NoPilha));

    if (!novo) {
        cout << "Erro ao alocar memória!" << endl;
        return;
    }

    strcpy(novo->nome, nome);
    novo->salario = salario;
    novo->ant = topo;
    topo = novo;
}

void desempilhar() {
    if (!topo) {
        cout << "Pilha vazia!" << endl;
        return;
    }

    NoPilha* temp = topo;
    topo = topo->ant;
    free(temp);
}

void mostrarPilha() {
    if (!topo) {
        cout << "A pilha está vazia!" << endl;
        return;
    }

    NoPilha* atual = topo;
    cout << "\n=== PILHA DE FUNCIONÁRIOS ===" << endl;
    while (atual) {
        cout << "Nome: " << atual->nome << ", Salário: R$ " << atual->salario << endl;
        atual = atual->ant;
    }
}

void destruirPilha() {
    while (topo) {
        NoPilha* temp = topo;
        topo = topo->ant;
        free(temp);
    }
}

void menuControle() {
    int opcao;
    char nome[50];
    float salario;

    do {
        cout << "\nMenu:\n1 - Empilhar funcionário\n2 - Mostrar pilha\n3 - Desempilhar\n4 - Sair\nOpção: ";
        cin >> opcao;
        cin.ignore();

        switch (opcao) {
            case 1:
                cout << "Nome: ";
                cin.getline(nome, 50);
                cout << "Salário: R$ ";
                cin >> salario;
                empilhar(nome, salario);
                break;

            case 2:
                mostrarPilha();
                break;

            case 3:
                desempilhar();
                break;

            case 4:
                cout << "Encerrando o programa..." << endl;
                break;

            default:
                cout << "Opção inválida!" << endl;
        }

    } while (opcao != 4);

    destruirPilha();
}

int main() {
    cout << "\n=== CONTROLE DE PILHA DINÂMICA ===" << endl;
    menuControle();
    return 0;
}

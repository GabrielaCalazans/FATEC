#include <iostream>
#include <cstdlib>
#include <ctime>
#include <limits>

using namespace std;

void gerarValores(double* &array, int &qtd) {
    std::cout << "Quantos valores deseja gerar? ";
    std::cin >> qtd;

    array = reinterpret_cast<double*>(calloc(qtd, sizeof(double)));
    if (!array) {
        std::cerr << "Erro ao alocar memória.\n";
        exit(1);
    }

    srand(time(0));

    for (int i = 0; i < qtd; i++) {
        array[i] = (double(rand()) / RAND_MAX) * 100.0;
    }

    std::cout << qtd << " valores gerados com sucesso!\n";
    std::cout << "Valores gerados: ";
    for (int i = 0; i < qtd; i++) {
        std::cout << array[i] << " ";
    }
}

void mostrarRelatorio(double* array, int qtd) {
    if (qtd == 0 || !array) {
        std::cout << "Nenhum dado disponivel.\n";
        return;
    }

    double soma = 0, maior = array[0], menor = array[0];

    for (int i = 0; i < qtd; i++) {
        soma += array[i];
        if (array[i] > maior) maior = array[i];
        if (array[i] < menor) menor = array[i];
    }

    double media = soma / qtd;

    std::cout << "\nRelatorio dos valores:\n";
    std::cout << "Soma: " << soma << "\n";
    std::cout << "Media: " << media << "\n";
    std::cout << "Maior valor: " << maior << "\n";
    std::cout << "Menor valor: " << menor << "\n";
}

void menuControle() {
    double* dados = nullptr;
    int qtd = 0;
    int opcao;

    do {
        std::cout << "\nMenu:\n1 - Gerar valores\n2 - Mostrar relatorio\n3 - Sair\nOpcao: ";
        std::cin >> opcao;

        switch (opcao) {
            case 1:
                if (dados) free(dados); // libera se já tiver alocado antes
                gerarValores(dados, qtd);
                break;
            case 2:
                mostrarRelatorio(dados, qtd);
                break;
            case 3:
                std::cout << "Encerrando...\n";
                break;
            default:
                std::cout << "Opção inválida!\n";
        }
    } while (opcao != 3);

    if (dados) free(dados); // libera memória ao final
}

int gerarNumeros () {
    return rand() % 100;
}

int main() {

    cout << "Um tipo int tem " << sizeof(int) << " bytes " << endl;
    cout << "Um tipo float tem " << sizeof(float) << " bytes " << endl;
    cout << "Um tipo double tem " << sizeof(double) << " bytes " << endl;
    cout << "Um tipo char tem " << sizeof(char) << " bytes " << endl;
    cout << "Um tipo bool tem " << sizeof(bool) << " bytes " << endl;
    system("pause");


    setlocale (LC_ALL, "Portuguese");
    int * ptx = (int *) malloc( sizeof ( int ) ); // aloca 4 bytes para um inteiro
    if (ptx == NULL) cout << "\nNão foi possível a alocação de memória!";
    else { *ptx = 10;
    cout << "O valor " << *ptx << " será armazenado na memória " << ptx << endl;
    }
    system("pause");
    free (ptx);


    int n;
    srand (time(NULL)); //zerar o tempo da função rand() para números diferentes
    printf("Digite a qtde de numeros:");
    scanf("%i", &n);
    int *ai = (int *) calloc (n, sizeof(int));// memoria para n elementos int
    for (int i=0;i<n;i++) ai [i] = gerarNumeros ();
    for (int i=0;i<n;i++) printf( "%i \n", ai[i] );
    system("pause");

    std::cout << "\n=== PROGRAMA DE CONTROLE DE VALORES ALEATORIOS ===\n";
    menuControle();
    return 0;
}

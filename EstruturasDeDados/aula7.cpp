#include "iostream"
#include "math.h"




// TAREFA / AVALIAÇÃO CONTINUADA
// I - Responda as questões a seguir
// 1.	Defina o que seria um ponteiro. Explique e dê exemplos.
// Ponteiro é uma variável que armazena o endereço de outra variável. Ele é utilizado para manipular dados de forma indireta, permitindo acessar e modificar o valor da variável apontada. Por exemplo, se temos uma variável inteira `int x = 10;`, podemos declarar um ponteiro `int *p;` e fazer `p = &x;`, onde `&` é o operador que retorna o endereço da variável `x`. Assim, `p` agora aponta para o endereço de `x` na memória.
// O ponteiro pode ser utilizado para acessar o valor de `x` através do operador de desreferenciação `*`, como em `*p = 20;`, que mudaria o valor de `x` para 20. Portanto, ponteiros são fundamentais para manipulação eficiente de memória e estruturas de dados dinâmicas.

// 2.	O que seria o endereço de uma variável. Explique como é criado e como posso exibi-lo.
// O endereço de uma variável é a localização na memória onde o valor dessa variável está armazenado. Cada variável em um programa ocupa um espaço específico na memória, e esse espaço tem um endereço único. O endereço é criado automaticamente pelo compilador quando a variável é declarada. Para exibir o endereço de uma variável, utilizamos o operador `&`, que retorna o endereço da variável. Por exemplo, se temos `int x = 10;`, podemos exibir o endereço de `x` com `cout << &x;`. Isso mostrará o endereço de memória onde `x` está armazenado.
// O endereço é geralmente representado em formato hexadecimal, e pode variar a cada execução do programa, dependendo de como o sistema operacional aloca memória.

// 3.	Como posso acessar o conteúdo de uma variável usando um ponteiro. Explique e dê exemplo.
// Para acessar o conteúdo de uma variável usando um ponteiro, utilizamos o operador de desreferenciação `*`. Quando declaramos um ponteiro, ele inicialmente não contém um valor válido até que seja atribuído o endereço de uma variável. Após isso, podemos acessar o valor da variável apontada pelo ponteiro utilizando `*`. Por exemplo:

void	ex_03() {
	int x = 10; // variável
	int *p; // ponteiro para inteiro
	p = &x; // p agora aponta para o endereço de x
	std::cout << "VALOR DE X: " << x << std::endl; // exibe o valor de x diretamente
	std::cout << "VALOR DE X ATRAVES DO PONTEIRO: " << *p << std::endl; // exibe o valor de x através do ponteiro p, que será 10
}


// 4.	Como posso acessar o endereço de uma variável usando ponteiro. Explique e dê exemplo.
// Para acessar o endereço de uma variável usando um ponteiro, podemos simplesmente atribuir o endereço da variável ao ponteiro. O ponteiro armazenará o endereço da variável, e podemos exibi-lo utilizando o operador `&`. Por exemplo:  
void	ex_04() {
	int x = 10; // variável
	int *p; // ponteiro para inteiro
	p = &x; // p agora aponta para o endereço de x
	std::cout << "ENDERECO DE X DIRETAMENTE: " << &x << std::endl; // exibe o endereço de x diretamente, que será o mesmo que p
	std::cout << "ENDERECO DE X ATRAVÉS DO PONTEIRO 'p': " << p << std::endl; // exibe o endereço de x através do ponteiro p, que será o mesmo que &x
}

// 5.	Qual seria o tipo de ponteiro para a STRUCT PESSOA?
// É  um ponteiro que pode apontar para uma variável do tipo Pessoa.
// typedef struct pessoa { 
// 	char nome[3]; 
// 	int idade; 
// 	char sexo; 
// 	float salario; 
// } PESSOA;
void	ex_05() {
	typedef struct pessoa *PESSOAPTR; // tipo de ponteiro para a struct PESSOA
	std::cout << "EXIBINDO O TAMANHO DO PONTEIRO PARA A STRUCT PESSOA: " << sizeof(PESSOAPTR) << std::endl; // exibe o tamanho do ponteiro para a struct PESSOA
	// Resultado: EXIBINDO O TAMANHO DO PONTEIRO PARA A STRUCT PESSOA: 8 (em sistemas de 64 bits) ou 4 (em sistemas de 32 bits)
}

// 6.	Declare duas variáveis e dois ponteiros. Exiba o resultado da soma dessas variáveis somando os seus ponteiros (com Asterisco).
void	ex_06() {	
	int a = 15, b = 10; // variáveis
	int *p1, *p2; // ponteiros para inteiro
	p1 = &a; // p1 aponta para a
	p2 = &b; // p2 aponta para b
	int soma = *p1 + *p2; // soma das variáveis e dos ponteiros
	std::cout << "Resultado da operação contido na variavel soma: " << soma; // exibe o resultado da soma
}

// II - Faça um programa com menu de três opções (1 - ler linha, 2 – mostrar e 3 – sair), contendo um STRUCT para cadastrar o nome, 
// a idade, o sexo, salário e salarioNovo de pelo menos duas pessoas. Crie um ponteiro para manipular o STRUCT. 
// O programa deverá conter as seguintes sub rotinas abaixo: (use switch case)
// a)	void NovaLinhaStruct()
// b)	void listarLinhasStruct()
// c)	ler_idade()
// d)	ler_sexo()
// e)	ler_nome()
// f)	ler_salario()
// g)	getAumento(double *salario)  // aumento de 10% sobre o salário digitado]

typedef struct pessoa { 
	std::string nome; 
	int idade; 
	char sexo; 
	float salario; 
} PESSOA;

void	NovaLinhaStruct(PESSOA *pessoa) {
	std::cout << "Digite o nome: ";
	std::cin >> pessoa->nome;
	std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
	std::cout << "Digite a idade: ";
	std::cin >> pessoa->idade;
	std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
	std::cout << "Digite o sexo: ";
	std::cin >> pessoa->sexo;
	std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
	std::cout << "Digite o salário: ";
	std::cin >> pessoa->salario;
	std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
}

void	listarLinhasStruct(PESSOA *pessoa) {
	std::cout << "Nome: " << pessoa->nome << std::endl;
	std::cout << "Idade: " << pessoa->idade << std::endl;
	std::cout << "Sexo: " << pessoa->sexo << std::endl;
	std::cout << "Salário: " << pessoa->salario << std::endl;
}

void	ler_idade(PESSOA *pessoa) {
	std::cout << "Digite a idade: ";
	std::cin >> pessoa->idade;
}
void	ler_sexo(PESSOA *pessoa) {
	std::cout << "Digite o sexo: ";
	std::cin >> pessoa->sexo;
}
void	ler_nome(PESSOA *pessoa) {
	std::cout << "Digite o nome: ";
	std::cin >> pessoa->nome;
}
void	ler_salario(PESSOA *pessoa) {
	std::cout << "Digite o salário: ";
	std::cin >> pessoa->salario;
}
void	getAumento(double *salario) {
	*salario += *salario * 0.10;
	std::cout << "Salário com aumento: " << *salario << std::endl;
}

void	ControleStruct() {
    int opcao;
    const int MAX_PESSOAS = 2;
    PESSOA pessoas[MAX_PESSOAS];
    int contador = 0;


	MENU:
		system("cls");
		std::cout << "Menu:\n1 - Nova Linha\n2 - Listar Linhas\n3 - Sair\nEscolha uma opção: ";
		std::cin >> opcao;

		switch (opcao) {
			case 1:
				if (contador < MAX_PESSOAS) {
					NovaLinhaStruct(&pessoas[contador]); // Cadastra uma nova pessoa
					contador++;
				} else {
					std::cout << "Limite de pessoas atingido!\n";
				}
				break;
			case 2:
				if (contador == 0) {
					std::cout << "Nenhuma pessoa cadastrada!\n";
				} else {
					for (int i = 0; i < contador; i++) {
						std::cout << "\nPessoa " << i + 1 << ":\n";
						listarLinhasStruct(&pessoas[i]); // Exibe os dados de cada pessoa
					}
				}
				break;
			case 3:
				std::cout << "Saindo..."<< std::endl << std::endl;
				return;
			default:
				std::cout << "Opção inválida!\n";
				break;
		}
		system("pause");
	goto MENU;
}

int	main() {

	std::cout << "\n\nEXERCICIOS DE PONTEIROS\n\n"; // exibe o título do exercício
	std::cout << "EX03 - Exibir o valor de x diretamente e através do ponteiro p\n";
	ex_03(); // Exibe o valor de x diretamente e através do ponteiro p

	std::cout << "\n\n\nEX04 - Exibir o endereço de x diretamente e através do ponteiro p\n";
	ex_04(); // Exibe o endereço de x diretamente e através do ponteiro p

	std::cout << "\n\n\nEX05 - Exibir o tamanho do ponteiro para a struct PESSOA\n";
	ex_05(); // Exibe o tamanho do ponteiro para a struct PESSOA

	std::cout << "\n\n\nEX06 - Exibir o resultado da soma das variáveis e dos ponteiros\n";
	ex_06(); // Exibe o resultado da soma das variáveis e dos ponteiros

	std::cout << "\n\n\nEX.II - Programa para cadastrar ao menos 2 pessoas\n";
	system("pause");
	ControleStruct();

	return 0;
}
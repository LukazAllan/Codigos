#include <stdio.h>
#include <stdlib.h>

typedef struct{
    char nome[20];
    int idade;
    char endereco[30];
}pessoas;

int main(int argc, char const *argv[]) {
    pessoas pessoa;
    printf("-------------------------------\n");
    printf("-----------Cadastro------------\n");
    printf("-------------------------------\n");
    printf("Digite seu nome (limite 20 caracteres): ");
    scanf("%s", &pessoa.nome);
    printf("Digite sua idade: ");
    scanf("%d", &pessoa.idade);
    printf("Digite seu endereço (limite 30 caracteres): ");
    scanf("%s", &pessoa.endereco);
    printf("Olá, %s!\n");
    if (pessoa.idade < 18){
        printf("Que jovem! Você tem %d anos.\n");
    } else if (pessoa.idade < 50){
        printf("Você tem %d anos.\n");
    } else {
        printf("Na melhor idade! Você tem %d anos.\n");
    }
    printf("E você mora em: %s\n", pessoa.endereco);
    
    return 0;
}
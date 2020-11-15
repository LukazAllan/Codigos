#include <stdio.h>
#include <stdlib.h>

typedef struct{
    char nome[20];
    char mat[4];
} alunos;

int main() {
    alunos aluno[5];
    char c;
    int i;
    printf("-------------------------------\n");
    printf("-----------Cadastro------------\n");
    printf("-------------------------------\n");
    for (i = 0; i < 5; i++){
        printf("\n");
        printf("Digite seu nome (limite 20 caracteres): ");
        scanf("%s", aluno[i].nome);
        // scanf("%c", c);
        printf("Digite sua matrícula (4 dígitos): ");
        scanf("%s", aluno[i].mat);
        // scanf("%c", c);
    }
    
    printf("-------------------------------\n");
    printf("------------Alunos-------------\n");
    printf("-------------------------------\n");
    for (i = 0; i < 5; i++){
        printf("%i. %s %s\n", i+1, aluno[i].nome, aluno[i].mat);
    }
    return 0;
}
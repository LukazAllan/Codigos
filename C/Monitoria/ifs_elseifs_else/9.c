/*
9. Crie um programa que receba a matrícula 
de um aluno, 03 notas obtidas em avaliação
e calcule a média de aproveitamento e a
situação do aluno:
Média >= 7.0 (aprovado)
Média < 7.0 (reprovado)
*/
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[]) {
  float nota1, nota2, nota3, media;
  printf("Digite a primeira nota: ");
  scanf("%f", &nota1);
  printf("Digite a segunda nota: ");
  scanf("%f", &nota2);
  printf("Digite a terceira nota: ");
  scanf("%f", &nota3);
  media = (nota1 + nota2 + nota3) / 3;
  printf("Média: %.2f ", media);
  if (media < 7){
    printf("Reprovado");
    return 0;
  }
  printf("Aprovado");
  return 0;
}
/*
Faça um programa que receba a idade de uma pessoa e determine sua
classificação segundo a seguinte tabela:
- Maior de idade;
- Menor de idade;
- Pessoa idosa (idade superior ou igual a 65 anos).
*/
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
  int idade;
  printf("Digite a sua idade: ");
  scanf("%d", &idade);

  if (idade < 0){
    printf("Você está vivo?");
  } else if (idade < 18)
  {
    printf("Menor de Idade!");
  } else if (idade < 65)
  {
    printf("Maior de Idade!");
  } else {
    printf("Idoso");
  }
  return 0;
}

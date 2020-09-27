/*
Crie um programa que receba a idade de uma pessoa e 
informe a sua classe eleitoral:
- Não eleitor (abaixo de 16 anos);
- Eleitor obrigatório (entre a faixa de 18 e menor de 65 anos);
- Eleitor facultativo (de 16 até 18 anos e maior de 65 anos, 
  inclusive).
*/
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
  int idade;
  printf("CLASSE ELEITORAL -------------------\n");
  printf("Para saber sua classe eleitoral \nDigite a sua idade: ");
  scanf("%d", &idade);

  if (idade < 0){
    printf("Você está vivo?");
  } else if (idade < 16)
  {
    printf("Pela lei brasileira, você é NÃO ELEITOR.");
  } else if ((idade >= 16) && (idade < 18) || (65 < idade))
  {
    printf("Pela lei brasileira, você é ELEITOR FACULTATIVO.");
  } else {
    printf("Pela lei brasileira, você é ELEITOR OBRIGATÓRIO.");
  }
  return 0;
}
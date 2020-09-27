/*
4. Depois da liberação do governo para as mensalidades 
dos planos de saúde, as pessoas começaram a fazer 
pesquisas para descobrir um bom plano, não muito caro. 
Um vendedor de um plano de saúde apresentou a tabela 
a seguir. Crie um programa que receba a idade de uma 
pessoa e imprima o valor que ela deverá pagar, 
segundo a seguinte tabela:
  Idade   | Valor
  >=10    |  30
 10<x<=29 |  60
 29<x<=45 |  120
 45<x<=59 |  150
 59<x<=65 |  250
 65<x     |  400
*/
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
  int idade;
  printf("PLANO DE SAÚDE -------------------\n");
  printf("Para saber o quanto vai pagar,\nDigite a sua idade: ");
  scanf("%d", &idade);

  if (idade < 0){
    printf("Você está vivo?");
  } else if (idade <= 10)
  {
    printf("Com esta idade, você pagará R$30,00.");
  } else if ((10 < idade) && (idade <=29)){
    printf("Com esta idade, você pagará R$60,00.");
  } else if ((29 < idade) && (idade <= 45)){
    printf("Com esta idade, você pagará R$120,00.");
  } else if ((45 < idade) && (idade <= 59)){
    printf("Com esta idade, você pagará R$150,00.");
  } else if ((59 < idade) && (idade <= 65)){
    printf("Com esta idade, você pagará R$250,00.");
  } else {
    printf("Com esta idade, você pagará R$400,00.");
  }
  return 0;
}
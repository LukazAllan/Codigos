/*
7. O IMC – Indice de Massa Corporal é um critério 
da Organização Mundial de  Saúde para dar uma 
indicação sobre a condição de peso de uma pessoa 
adulta. A fórmula é IMC = peso / ( altura )^2.
Elabore um programa que receba o peso e a altura
de um adulto e mostre sua condição de acordo com
a tabela abaixo:
*/
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[]) {
  float peso, altura, imc;
  printf("CÁLCULO DO IMC -------------------\n");
  printf("Digite seu peso (em kg): ");
  scanf("%f", &peso);
  printf("Digite sua altura (em m): ");
  scanf("%f", &altura);

  imc = peso / (altura * altura);
  if (imc < 20)  {
    printf("Sua Situação: ABAIXO DO PESO");
  } else if ((20 <= imc) && (imc < 25))  {
    printf("Sua Situação: PESO NORMAL");
  } else if ((25 <= imc) && (imc < 30))  {
    printf("Sua Situação: SOBREPESO");
  } else if ((30 <= imc) && (imc < 40))  {
    printf("Sua Situação: OBESO");
  } else {
    printf("Sua Situação: OBESO MÓRBIDO");
  }
  return 0;
}
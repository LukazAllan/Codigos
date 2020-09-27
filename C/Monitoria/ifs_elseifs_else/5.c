/*
Faça um programa que receba dois valores inteiros 
A e B, se os valores forem iguais deverá somar os 
dois, caso contrário multiplique A por B. Ao final,
de qualquer um dos cálculos deve-se atribuir o resul-
tado para uma variável C e mostrar seu conteúdo na tela.
*/
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
  int a,b,c;
  printf("Digite um n° inteiro: ");
  scanf("%d", &a);
  printf("Digite outro n° inteiro: ");
  scanf("%d", &b);
  if (a == b) {
    c = a+b;
  } else {
    c = a*b;
  }
  printf("O resultado é: %d", c);
  return 0;
}
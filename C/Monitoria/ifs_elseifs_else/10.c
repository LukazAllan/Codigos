/*
10. A equação de segundo grau é definida pela
expressão ax^2 +bx + c. Faça um programa que 
calcula as raízes da equação, para isso o 
programa deverá receber os valores de a, b e c.
Informações adicionais:
Δ = b^2 – 4a. c
Se, Δ > 0 a equação possui duas raízes;
Se, Δ = 0 a equação possui apenas uma raiz;
Se, Δ < 0 a equação não possui raiz;
*/
#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main(int argc, char const *argv[]) {
  float a, b, c, delta, x1, x2;
  printf("Digite um valor para A: ");
  scanf("%f", &a);
  printf("Digite um valor para B: ");
  scanf("%f", &b);
  printf("Digite um valor para C: ");
  scanf("%f", &c);
  
  delta = powf(b, 2.0) - 4.0 * a *c;

  if (delta > 0) {
    printf("A função toca o eixo X.\nEsta equação possui 2 raízes reais.");
    x1 = (-b + sqrtf(delta))/(2.0*a);
    x2 = (-b - sqrtf(delta))/(2.0*a);
    printf("x¹ = %.3f | x² = %.3f", x1, x2);
  } else if (delta == 0) {
    printf("A função toca o eixo X.\nEsta equação possui 1 raíz real.");
    x1 = (-b + sqrtf(delta))/(2.0*a);
    printf("x¹ = %.3f", x1);
  } else {
    printf("A função não toca o eixo X.\nEsta equação não possui raízes reais.");
  }
  
  return 0;
}
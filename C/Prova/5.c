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
  if (a != 0){
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
  } else {
    printf("Não é equação de segundo grau!\n");
  }
  return 0;
}
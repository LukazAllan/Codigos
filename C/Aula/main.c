#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
  int a, b;
  printf("Digite um inteiro:");
  scanf("%i", &a);
  printf("Digite outro inteiro:");
  scanf("%i", &b);
  if (b == 0) {
    printf("Impossivel divisao por zero!");
  } else {
    float div = a / b;
    printf("A divisão entre %i e %i eh %f", a, b, div);
  }
  return 0;
}
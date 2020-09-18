#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

int main()
{
  float a = 10.24;
  int tamanho = sizeof(a);
  printf("A Variavel 'a' vale %f\nE precisa de %d bytes de armaz.", a, tamanho);
  return 0;
}

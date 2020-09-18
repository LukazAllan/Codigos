#include <stdio.h>
#include <stdlib.h>
#define CONST 0.6214
int main(int argc, char const *argv[])
{
  float km;
  printf("Digite um distancia em km:");
  scanf("%f", &km);

  printf("Quilometros para milhas %f => %f", km, km * CONST);
  return 0;
}

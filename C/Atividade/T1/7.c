#include <stdio.h>
#include <stdlib.h>

/*UTF-8 REQUIRED*/

int main() {
  char ji;
  printf("Digite um caractere: ");
  scanf("%c", &ji);
  printf("O equivalente em ASCII de \"%c\", corresponde a %i.", ji, ji);
  return 0;
}
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[]) {
  int x, y, i = 0;
  printf("TABUADA ------------------------------\n");
  printf("Digite qual tabuada você quer: ");
  scanf("%i", &x);
  printf("Digite até qual número: ");
  scanf("%i", &y);

  do {
    printf("%i * %i == %i\n", x, i, x*i);
    i++;
  } while (i < y+1);

  return 0;
}
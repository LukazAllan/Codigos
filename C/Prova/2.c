#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[]) {
  int num, notPrimo = 1, c;
  printf("PRIMOS  ----------------------------\n");
  printf("Digite um número: ");
  scanf("%d", &num);
  if (num > 2){
    for (c = 2; c < num; c++)
    {
      if (num%c == 0){
        printf("O número que vc digitou não é primo!");
        c = num;
        notPrimo = 0;
      }
    }
    if (notPrimo == 1){
      printf("O número que vc digitou é primo!");
    }
  } else if (num == 2){
    printf("O número que vc digitou é primo!");
  } else {
    printf("O número que vc digitou não é primo!");
  }
  
  return 0;
}
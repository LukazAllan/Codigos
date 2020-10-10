#include <stdio.h>
#include <stdlib.h>

#define XEROX 0.25

int main(int argc, char const *argv[]) {
  int copias;
  printf("Digite quantas xerox você quer: ");
  scanf("%d", &copias);
  if (copias <= 100){
    printf("Para %d copias, serão necessários R$%f", copias, copias*XEROX);
  } else {
    printf("Para %d copias - desconto, serão necessários R$%f", copias, copias*(XEROX - 0.05));
  }
  
  return 0;
}
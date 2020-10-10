#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[]) {
  int n = 0, c = 0, i = 1, limit = 1, num = 0;
  while (!(n >= 1)){
    if (c != 0){
      printf("Por favon, n precisa ser maior que 0\n");
    }
    printf("Digite numero de linha n para o triângulo de Floyd: ");
    scanf("%d", &n);
    c++;
  }
  n++;
  for (; i < n; i++){
    limit = i + num;
    for (; num < limit; num++){
      printf("%d ", num+1);
    }
    printf("\n");
  }
  
  return 0;
}
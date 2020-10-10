#include <stdio.h>
#include <stdlib.h>

int main(){
  double har = 0.0, i, num;

  printf("Digite um inteiro para a série harmônica: ");
  scanf("%lf", &num);

  for (i=0; i < num; i++){
    har = har + (1/(i+1));
  }
  printf("%.16lf", har);
  return 0;
}
#include <stdio.h>
#include <stdlib.h>

/*2. Faça um programa que leia dois números 
inteiros, encontre o maior deles e imprima 
para o usuário.*/

int main(){
  int suuji1, suuji2;
  printf("Digite um número, 数字を入力してください。\n");
  scanf("%i", &suuji1);
  printf("Digite outro número, 他の数字を入力してください。\n");
  scanf("%i", &suuji2);
  if (suuji1 > suuji2){
    printf("%i > %i", suuji1, suuji2);
    return 0;
  }
  printf("%i < %i", suuji1, suuji2);
  return 0;
}
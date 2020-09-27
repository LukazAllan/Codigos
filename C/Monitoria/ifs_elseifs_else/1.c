/*
Faça um programa que receba três valores
inteiros e diferentes e mostre-os em
ordem crescente.
*/
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[]){
  int n1 = 0, n2 = 0, n3 = 0, c = 0;

  do {
    if (c > 0){
      printf("Por favor, digite 3 números diferentes.\n");
    }
    printf("Digite o primeiro número inteiro: ");
    scanf("%d", &n1);
    printf("Digite o segundo número inteiro: ");
    scanf("%d", &n2);
    printf("Digite o terceiro número inteiro: ");
    scanf("%d", &n3);
    c++;
  } while ((n1 == n2) || (n2 == n3) || (n3 == n1));

  if ((n1 > n2) && (n2 > n3)){
    printf("%d < %d < %d", n3, n2, n1);
  } else if ((n1 > n3) && (n3 > n2)){
    printf("%d < %d < %d", n2, n3, n1);
  } else if ((n2 > n1) && (n1 > n3)){
    printf("%d < %d < %d", n3, n1, n2);
  } else if ((n2 > n3) && (n3 > n1)){
    printf("%d < %d < %d", n1, n3, n2);
  } else if ((n3 > n1) && (n1 > n2)){
    printf("%d < %d < %d", n2, n1, n3);
  } else {
    printf("%d < %d < %d", n1, n2, n3);
  }
  return 0;
}

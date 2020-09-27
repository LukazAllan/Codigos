/*
Uma loja fornece 20% de desconto para funcionários 
e 10% de desconto para clientes vips. Faça um 
programa que calcule o valor total a ser pago por 
uma pessoa. O programa deverá ler o valor total da
compra efetuada e um código que identifique se o 
comprador é um cliente comum (1), funcionário (2) 
ou vip (3).
*/
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[]) {
  int prod = 1000, pag;
  printf("Produto: R$1000,00\nCliente - 1\nFuncionário - 2\nVIP - 3\n>> ");
  scanf("%d", &pag);

  if (pag == 2){
    printf("20%% de desconto!\n");
    prod = prod - prod / 20;
  } else if (pag == 3){
    printf("10%% de desconto!\n");
    prod = prod - prod / 10;
  }
  printf("A pagar: R$%d,00", prod);
  return 0;
}
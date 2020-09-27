/*
Em uma loja, o valor final do produto é alterado
pela forma de pagamento a vista ou a prazo. Se
o produto for pago à vista deve ser aplicado um
desconto de 10% no valor final, senão se for a
prazo será o mesmo valor do produto. Diante
disso, faça um programa que receba o valor do
produto e a forma de pagamento, por fim informe
o valor final do produto.
*/
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[]) {
  int prod = 1000, pag;
  printf("Produto: R$1000,00\nÀ Vista - 1\nParcelado - 2\n>> ");
  scanf("%d", &pag);

  if (pag == 1){
    printf("10%% de desconto!\n");
    prod = prod - prod / 10;
  }
  printf("A pagar: R$%d,00", prod);
  return 0;
}
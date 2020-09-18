#include <stdio.h>
#include <string.h>

/*UTF-8 REQUIRED*/

int main() {
  int n, rev = 0, passo;
  printf("Digite um inteiro: ");
  scanf("%d", &n);
  while (n != 0) {
      passo = n % 10;
      rev = rev * 10 + passo;
      n /= 10;
  }
  printf("Número inverso = %d", rev);
  return 0;
}
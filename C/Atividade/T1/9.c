#include <stdio.h>
#include <string.h>

/*UTF-8 REQUIRED*/

int main() {
  char num_one[100], num_two[100];
  printf("Digite um número real; Enter an float\n:");
  scanf("%s", num_one);

  printf("Digite outro número real; Enter another float\n:");
  scanf("%s", num_two);

  int lnum_one, lnum_two;

  printf("os números invertidos são: ");

  for( lnum_one = strlen(num_one); lnum_one >= 0; lnum_one = lnum_one - 1) {
    printf("%c", num_one[lnum_one]);
  }

  printf(", ");

  for( lnum_two = strlen(num_two); lnum_two >= 0; lnum_two = lnum_two - 1) {
    printf("%c", num_two[lnum_two]);
  }

  printf(" .");
  return 0;
}
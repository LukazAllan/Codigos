#include <stdlib.h>
#include <stdio.h>

/*UTF-8 REQUIRED*/

int main() {
  char ji;
  int suuji;
  float shousuu;
  printf("Digite um caractere|Enter a character|字を入力してください。\n");
  scanf("%c", &ji);
  printf("Digite um n° inteiro|Enter an integer|数字を入力してください。\n");
  scanf("%i", &suuji);
  printf("Digite um n° real|Enter a float|少数を入力してください。\n");
  scanf("%f", &shousuu);

  printf("Muito Obrigado|Thank you very much|ありがあとうございました。\n");
  printf("letra/letter/字: \"%c\"\ninteiro/integer/整数: %i\nreal/float/実数: %f", ji, suuji, shousuu);
  return 0;
}
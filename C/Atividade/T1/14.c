#include <stdlib.h>
#include <stdio.h>

/*UTF-8 REQUIRED*/

int main() {
  char ji1, ji2, ji3;
  printf("Digite um caractere|Enter a character|字を入力してください。\n");
  scanf("%c", &ji1);
  printf("Digite outro caractere|Enter another character|他の字を入力してください。\n");
  scanf("%c", &ji2);
  printf("Digite outro caractere|Enter another character|他の字を入力してください。\n");
  scanf("%c", &ji3);

  printf("Muito Obrigado|Thank you very much|ありがあとうございました。\n");
  printf("letras/字: \n\"%c\"\n\"%c\"\n\"%c\"", ji1, ji2, ji3);
  return 0;
}
#include <stdio.h>
#include <stdlib.h>

/*UTF-8 REQUIRED*/

void limparBuffer(void){
  /*
  Foi necessário usar uma função para limpar o buffer
  caso contrário, */
  char c;
  while(((c=getchar()) != '\n') && (c != EOF));
}

int	main(int argc, char **argv){
  void limparBuffer(void);
  int idioma;
  float num1, num2;
  char op;

  
  printf("Escolha um idioma |言語を選択してください。\n1. Português\n2. 日本語\n>> ");
  scanf("%i", &idioma);
  if (idioma == 1){
    printf("Calculadora\n");
    printf("Seja Bem-vindo!\n\n");
    printf("Operadores permitidos:\n");
    printf("+ Soma\n");
    printf("- Subtração\n");
    printf("* Multiplicação\n");
    printf("/ Divisão\n\n");
    printf("Digite um número, por favor.");
    scanf("%f", &num1);
    limparBuffer();
    printf("Digite outro número, por favor.");
    scanf("%f", &num2);
    limparBuffer();
    printf("Digite uma operação, por favor.");
    scanf("%c", &op);

    printf("Calculando...\n");

    switch (op)
    {
    case '+':
      printf("%f + %f = %f", num1, num2, num1 + num2);
      break;
    case '-':
      printf("%f - %f = %f", num1, num2, num1 - num2);
      break;
    case '*':
      printf("%f * %f = %f", num1, num2, num1 * num2);
      break;
    case '/':
      if(num2 == 0){
        printf("Impossível divisão por zero");
        break;
      }
      printf("%f / %f = %f", num1, num2, num1 / num2);
      break;
    
    default:
      printf("Impossível calcular");
      break;
    }
    printf("\nObrigado, volte sempre");
  } else if (idioma == 2){
    printf("電卓\n");
    printf("いらっしゃいませ！\n\n");
    printf("許可された算術演算子:\n");
    printf("+ 足し算\n");
    printf("- 引き算\n");
    printf("* 掛け算\n");
    printf("/ 割り算\n\n");
    printf("数字を入力してください。");
    scanf("%f", &num1);
    limparBuffer();
    printf("他の数字を入力してください。");
    scanf("%f", &num2);
    limparBuffer();
    printf("演算子を入力してください。");
    scanf("%c", &op);

    printf("計算中。。。\n");

    switch (op)
    {
    case '+':
      printf("%f + %f = %f", num1, num2, num1 + num2);
      break;
    case '-':
      printf("%f - %f = %f", num1, num2, num1 - num2);
      break;
    case '*':
      printf("%f * %f = %f", num1, num2, num1 * num2);
      break;
    case '/':
      if(num2 == 0){
        printf("0で割ることができません。");
        break;
      }
      printf("%f / %f = %f", num1, num2, num1 / num2);
      break;
    
    default:
      printf("計算ことができません。");
      break;
    }
    printf("\nありがあとうございました、いってらっしゃい。");
  }
  return 0;
}
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
  float num1, num2;
  char op;

  printf("Calculadora                    | 電卓\n");
  printf("Seja Bem-vindo                 | いらっしゃいませ！\n\n");
  printf("Operadores permitidos          | 許可された算術演算子:\n");
  printf("+ Soma                           + 足し算\n");
  printf("- Subtração                      - 引き算\n");
  printf("* Multiplicação                  * 掛け算\n");
  printf("/ Divisão                        / 割り算\n\n");
  printf("Digite um número, por favor.   | 数字を入力してください。");
  scanf("%f", &num1);
  limparBuffer();
  printf("Digite outro número, por favor.| 他の数字を入力してください。");
  scanf("%f", &num2);
  limparBuffer();
  printf("Digite uma operação, por favor.| 演算子を入力してください。");
  scanf("%c", &op);

  printf("Calculando... | 計算中。。。\n");

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
    printf("Impossível calcular | 計算できません。");
    break;
  }
  printf("\nObrigado, volte sempre|ありがあとうございました、いってらっしゃい。");
  return 0;
}
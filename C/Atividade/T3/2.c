#include <stdio.h>
#include <stdlib.h>

void limparBuffer(void){
  /*
  Foi necessário usar uma função para limpar o buffer
  caso contrário, */
  char c;
  while(((c=getchar()) != '\n') && (c != EOF));
}

int main(){
    void limparBuffer(void);
    float i = 0, har = 0;
    int num =0;
    printf("%f %d %f\n", i,num,har);
    printf("n: ");
    limparBuffer();
    scanf("%d", num);
    limparBuffer();
    printf("%f %d %f\n", i,num,har);
    
    return 0;
}
#include <stdlib.h>
#include <stdio.h>

char* input(char msg[100]){
  char inpat[100];
  printf("%s", msg);
  scanf("%s", &inpat);
  return inpat;
}

int main(int argc, char const *argv[])
{
  printf("pegando com input\n");
  char* str = input("Input: ");
  printf("%s\n", str);
  return 0;
}
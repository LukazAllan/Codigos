#include <stdio.h>
#include <stdlib.h>

/*UTF-8 REQUIRED*/

int main() {
  int dd, mm, yyyy;
  printf("Qual dia do mês é hoje?:");
  scanf("%i", &dd);

  printf("Qual o n° do mês de hoje?:");
  scanf("%i", &mm);
  
  printf("Qual ano estamos?:");
  scanf("%i", &yyyy);

  printf("Hoje é %i/%i/%i", dd, mm, yyyy);
  return 0;
}
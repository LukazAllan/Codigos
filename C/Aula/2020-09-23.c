#include <stdlib.h>
#include <stdio.h>

int	main(int argc, char **argv)
{
  /*int i;
  for (i = 0; i < 10; i++)
  {
    printf("%d %f %f\n", i, sqrt(i), pow(i,2));
  }*/

  int m,i,l;

  printf("Digite quantas estrelas: ");
  scanf("%d", &m);

  for (i = 1; i <= m; i++){
    for (l = 0; l < i; l++){
      printf("*");
    }
    printf("\n");
  }
  
  return 0;
}

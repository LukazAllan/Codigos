#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

int main (void){
  int c = 0, f = 0, sex, pop = 50;
  float alt, menor_altura, maior_altura, med_pop = 0.0, med_f = 0.0, m= 0, pc_h;

  do {
    printf("digite sua altura: ");
    scanf("%f", &alt);

    printf("0 - Masculino\n1 Feminino\n>> ");
    scanf("%d", &sex);

    if (c == 0){
      menor_altura = alt;
      maior_altura = alt;
    } else {
      if (alt < menor_altura){
        menor_altura = alt;
      }
      if (alt > maior_altura){
        maior_altura = alt;
      }
    }

    med_pop = med_pop + alt;

    if (sex == 1){
      f++;
      med_f = med_f + alt;
    } else {
      m++;
    }

    c++;

  } while (c < pop);
  med_pop = med_pop / pop;
  med_f = med_f / f;
  pc_h = (m / pop) * 100;
  printf("Resultados:\nmaior altura encontrada           : %.2f\nmenor altura encontrada           : %.2f\nmédia de altura das mulheres      : %f\nmédia de altura da população      : %f\npercentual de homens na população : %.2f %%", maior_altura, menor_altura, med_f, med_pop, pc_h);
  return 0;
}
#include <stdio.h>
#include <stdlib.h>

//1 m = 39.3701 pol
//1 m = 3.28084 ft
//1 m = 0.001 km

int main(int argc, char const *argv[]) {
  float m, pol, ft, km;
  printf("Digite a distância em metros: ");
  scanf("%f", &m);
  
  pol = m * 39.3701;
  ft = m * 3.28084;
  km =  m * 0.001;
  printf("Distância:\n%.3fm\n%.3fpol\n%.3fft\n%.3fkm\n", m,pol,ft,km);
  return 0;
}
#include <stdlib.h>
#include <stdio.h>

/*UTF-8 REQUIRED*/

int main() {
  float salary, taxRate, deduction;
  printf("Calcule o imposto sobre seu salário!\nDigite seu salário: ");
  scanf("%f", &salary);
  if (salary < 1903.98){
    //No taxes, great!
    taxRate = 0.0;
	  deduction = 0.0;
  } else if ((1903.98 < salary) && (salary < 2826.65)){
    taxRate = 7.5;
	  deduction = 142.8;
  } else if ((2826.65 < salary) && (salary < 3751.05)){
    taxRate = 15.0;
	  deduction = 354.8;
  } else if ((3751.05 < salary) && (salary < 4664.68)){
    taxRate = 22.5;
	  deduction = 636.13;
  } else {
    taxRate = 27.5;
    deduction = 869.36;
  }
  float tax = salary * (taxRate/100) - deduction;
  printf("O Imposto do IRRF para você: %.2f", tax);
  return 0;
}
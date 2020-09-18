#include <stdio.h>
#include <stdlib.h>

/*UTF-8 REQUIRED*/

int main() {
    double decimal;
    printf("Digite um número decimal: ");
    scanf("%lf", &decimal);
    printf("Valor lido: %lf, Notação Científica: %e", decimal, decimal);
    return 0;
}
#include <stdio.h>
#include <stdlib.h>

int main(){
    int a,b,c;
    printf("Digite o cateto a de um triângulo: ");
    scanf("%i", &a);
    printf("Digite o cateto b de um triângulo: ");
    scanf("%i", &b);
    printf("Digite a hipotenusa c de um triângulo: ");
    scanf("%i", &c);
    printf("Para valores a = %i; b = %i; c = %i\n", a, b, c);

    if ( 
        (  (abs(b-c) < a) && (a < (b+c))   ) && 
        (  (abs(a-c) < b) && (b < (a+c))   ) && 
        (  (abs(a-b) < c) && (c < (a+b))   )
        )
    {
        printf("É triangulo");
        return 0;
    }
    printf("Não é triangulo");
    return 0;
}
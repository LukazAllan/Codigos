#include <stdio.h>
#include <stdlib.h>

/*Construa uma função que receba como parâmetro o valor 
do raio de uma circunferência e retorne o valor da área 
da mesma. O usuário deve digitar o valor em questão e 
considere pi=3.14*/
#define PI 3.14
float circunferencia(float raio);

int main(int argc, char const *argv[]) {
    float Raio, circ;
    printf("Digite um valor de raio para uma circunferência: ");
    scanf("%f", &Raio);
    circ = circunferencia(Raio);
    printf("Para raio: %f temos circunferencia: %f\n", Raio, circ);
    return 0;
}

float circunferencia(float raio){
    return 2.0 * PI * raio;
}
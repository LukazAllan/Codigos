#include <stdio.h>
#include <stdlib.h>

int main(){
    float chico = 1.5, ze = 1.1;
    float cr_chico = 0.02, cr_ze = 0.03;
    int c;

    for (c = 0; chico > ze; ++c) {
        chico = chico + cr_chico;
        ze = ze + cr_ze;
    }
    printf("Serão Precisos %i anos para Zé > Chico.", c);
    return 0;
}
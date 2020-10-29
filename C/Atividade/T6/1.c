#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[]) {
    float saldo = 1000, money, mov[200];
    int i = 0, esc, limit, c;
    
    printf("Banco Alana Corp.\n");
    printf("Acessando Conta\n");
    printf("Saldo: %f\n", saldo);

    while (i < 200){
        printf("Sua conta tem direito à %i movimentações.\n", 200 - i);
        printf("1- Depósito | 2 - Saque | 3 - Saída: ");
        scanf("%d", &esc);
        switch (esc)
        {
          case 1:
            printf("De quanto será o depósito: ");
            scanf("%f", &money);
            mov[i] = money;
            i++;
            break;
          case 2:
            printf("De quanto será o saque: ");
            scanf("%f", &money);
            mov[i] = -money;
            i++;
            break;
          case 3:
            limit = i;
            i = 201;
          default:
            break;
        }
    }
    for (c = 0; c < limit; c++){
        saldo = saldo + mov[c];
    }
    printf("\n\nNo final do mês seu saldo é: %.2f\n", saldo);
    return 0;
}
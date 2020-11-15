#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[]) {
    int matriz[3][3] = {
        {1,0,0},
        {0,1,0},
        {0,0,1}
    };
    int i, j;
    for (i = 0; i < 3; i++)
    {
        printf("|");
        for (j = 0; j < 2; j++)
        {
            printf("%i  ", matriz[i][j]);
        }
        printf("%i|\n", matriz[i][3]);
    }
    
    return 0;
}
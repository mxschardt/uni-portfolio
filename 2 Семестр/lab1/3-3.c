#include <stdio.h>

int main(void)
{
    int matrix[3][3] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    int matrix_trans[3][3];

    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            matrix_trans[i][j] = matrix[j][i];

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
            printf("%d ", matrix_trans[i][j]);
        printf("\n");
    }
}
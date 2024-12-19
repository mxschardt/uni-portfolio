#include <stdio.h>

#define MATRIX_SIZE 3

int main(void)
{
    int matrix[MATRIX_SIZE][MATRIX_SIZE] = {1, 2, 3, 4, 5, 6, 7, 8, 9};

    for (int i = 0; i < MATRIX_SIZE; i++)
    {
        int row_sum = 0;
        for (int j = 0; j < MATRIX_SIZE; j++)
            row_sum += matrix[i][j];
        matrix[i][0] = row_sum / MATRIX_SIZE;
    }

    for (int i = 0; i < MATRIX_SIZE; i++)
    {
        for (int j = 0; j < MATRIX_SIZE; j++)
            printf("%d ", matrix[i][j]);
        printf("\n");
    }

    return 0;
}
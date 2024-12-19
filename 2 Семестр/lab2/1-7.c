/*
Выделите память под двумерный динамический массив, используя
массив указателей на строки (см. лекции). Затем освободите корректно оперативную память.
*/
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void)
{
    srand(time(0));

    int **matrix = NULL;
    int n_rows = 3;
    int n_columns = 3;

    matrix = (int **)malloc(n_rows * sizeof(int));

    for (int i = 0; i < n_rows; i++)
        matrix[i] = (int *)malloc(n_columns * sizeof(int));

    for (int i = 0; i < n_rows; i++)
        for (int j = 0; j < n_columns; j++)
            matrix[i][j] = rand() % 100;

    printf("Matrix:\n");
    for (int i = 0; i < n_rows; i++)
    {
        for (int j = 0; j < n_columns; j++)
            printf("%d ", matrix[i][j]);
        printf("\n");
    }

    for (int i = 0; i < n_rows; i++)
        free(matrix[i]);
    free(matrix);
    return 0;
}
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

double *alloc_matrix(int n_rows, int n_columns)
{
    double *matrix = (double **)malloc(n_rows * sizeof(double));

    for (int i = 0; i < n_rows; i++)
        matrix[i] = (double *)malloc(n_columns * sizeof(double));

    return matrix;
}

void free_matrix(double *matrix, int n_rows, int n_columns)
{
    for (int i = 0; i < n_rows; i++)
        free(matrix[i]);
    free(matrix);
}

void fill_matrix(double *matrix, int n_rows, int n_columns)
{
    srand(time(NULL));
    for (int i = 0; i < n_rows; i++)
        for (int j = 0; j < n_columns; j++)
            matrix[i][j] = random() % 101;
}

void print_matrix(double *matrix, int n_rows, int n_columns)

    printf("Matrix:\n");
for (int i = 0; i < n_rows; i++)
{
    for (int j = 0; j < n_columns; j++)
        printf("%3.0lf ", matrix[i][j]);
    printf("\n");
}
}

int main(void)
{
    int n_rows = 10, n_columns = 10;
    double *matrix = alloc_matrix(n_rows, n_columns);

    fill_matrix(matrix, n_rows, n_columns);

    print_matrix(matrix, n_rows, n_columns);

    free_matrix(matrix, n_rows, n_columns);

    return 0;
}
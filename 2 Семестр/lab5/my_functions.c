#include <stdlib.h>
#include <stdio.h>
#include <time.h>

double **alloc_array(int block_count)
{
    return (double **)malloc(sizeof(double) * block_count);
}

double **alloc_matrix(int n_rows, int n_columns)
{
    double **matrix = (double **)malloc(n_rows * sizeof(double));

    for (int i = 0; i < n_rows; i++)
        matrix[i] = (double *)malloc(n_columns * sizeof(double));

    return matrix;
}

void fill_matrix(double **matrix, int n_rows, int n_columns)
{
    srand(time(NULL));
    for (int i = 0; i < n_rows; i++)
        for (int j = 0; j < n_columns; j++)
            matrix[i][j] = random() % 101;
}

void print_matrix(double **matrix, int n_rows, int n_columns)
{
    printf("Matrix:\n");
    for (int i = 0; i < n_rows; i++)
    {
        for (int j = 0; j < n_columns; j++)
            printf("%3.0lf ", matrix[i][j]);
        printf("\n");
    }
}
void free_matrix(void **matrix, int n_rows)
{
    for (int i = 0; i < n_rows; i++)
        free(matrix[i]);
    free(matrix);
}

void multiply_matrix(int M, int N, int K, double **target, double **matrix_a, double **matrix_b)
{
    for (int i = 0; i < M; i++)
    {
        for (int j = 0; j < N; j++)
        {
            target[i][j] = 0;
            for (int k = 0; k < K; k++)
                target[i][j] += matrix_a[i][k] * matrix_b[k][j];
        }
    }
}
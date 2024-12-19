#include "functions.h"
#include <stdio.h>

int main(void)
{
    double **matrix_a = alloc_matrix(3, 3);
    fill_matrix(matrix_a, 3, 3);
    double **matrix_b = alloc_matrix(3, 3);
    fill_matrix(matrix_b, 3, 3);
    double **matrix_c = alloc_matrix(3, 3);
    multiply_matrix(3, 3, 3, matrix_c, matrix_a, matrix_b);

    print_matrix(matrix_a, 3, 3);
    print_matrix(matrix_b, 3, 3);
    print_matrix(matrix_c, 3, 3);

    return 0;
}
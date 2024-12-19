#ifndef FUNCTIONS
#define FUNCTIONS

double *alloc_array(int block_count);

double **alloc_matrix(int n_rows, int n_columns);

void fill_matrix(double **matrix, int n_rows, int n_columns);

void print_matrix(double **matrix, int n_rows, int n_columns);

void free_matrix(void **matrix, int n_rows);

void multiply_matrix(int M, int N, int K, double **target, double **matrix_a, double **matrix_b);

#endif
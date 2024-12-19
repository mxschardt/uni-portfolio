#include <stdio.h>

void cross_product(int *a, int *b, int *target)
{
    target[0] = a[1] * b[2] - a[2] * b[1];
    target[1] = a[0] * b[2] - a[2] * b[0];
    target[2] = a[0] * b[1] - a[1] * b[0];
}

int main(void)
{

    int a[] = {-1, 2, -3};
    int b[] = {0, -4, 1};
    int vector[2];
    cross_product(a, b, vector);

    printf("cross: %d %d %d \n", vector[0], vector[1], vector[2]);

    return 0;
}
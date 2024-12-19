#include <stdio.h>

int main(void)
{
    int vector_x[2];
    scanf("%d%d", &vector_x[0], &vector_x[1]);
    int vector_y[2] = {vector_x[0] * vector_x[0], vector_x[1] * vector_x[1]};

    printf("%s %d, %d\n", "Vector Y:", vector_y[0], vector_y[1]);
    return 0;
}
#include <stdio.h>
#include <stdlib.h>
#define ARRAY_SIZE 12

void array_swap(int *array, int size)
{
    for (int i = 0; i < size; i += 2)
    {
        int temp = array[i];
        array[i] = array[i + 1];
        array[i + 1] = temp;
    }
}
int main(void)
{
    int *array = (int *)malloc(sizeof(int) * ARRAY_SIZE);

    for (int i = 0; i < ARRAY_SIZE; i++)
        array[i] = i + 1;

    array_swap(array, ARRAY_SIZE);

    for (int i = 0; i < ARRAY_SIZE; i++)
        printf("[%d]: %d\n", i, array[i]);

    free(array);
    return 0;
}

#undef ARRAY_SIZE
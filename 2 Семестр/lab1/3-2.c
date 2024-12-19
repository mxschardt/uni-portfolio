#include <stdio.h>

int main(void)
{
    int array_size;
    printf("Enter array size: ");
    scanf("%d", &array_size);

    int initial_array[array_size], reversed_array[array_size];
    printf("Enter array: ");
    for (int i = 0; i < array_size; i++)
    {
        scanf("%d", &initial_array[i]);
        reversed_array[array_size - i - 1] = initial_array[i];
    }
    printf("Reversed array: ");
    for (int i = 0; i < array_size; i++)
        printf("%d ", reversed_array[i]);
    printf("\n");

    return 0;
}
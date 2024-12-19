#include <stdio.h>
#define ARRAY_SIZE 10

int main(void)
{
    // Заполняем массив значениями от 100 до 1.
    int arr[ARRAY_SIZE];
    for (int i = ARRAY_SIZE; i > 0; i--)
        arr[ARRAY_SIZE - i] = i;

    for (int i = 1; i < ARRAY_SIZE; i++)
        for (int j = i; (j > 0) && (arr[j - 1] > arr[j]); j--)
        {
            int temp = arr[j];
            arr[j] = arr[j - 1];
            arr[j - 1] = temp;
        }

    for (int i = 0; i < ARRAY_SIZE; i++)
        printf("%d ", arr[i]);
    printf("\n");
}
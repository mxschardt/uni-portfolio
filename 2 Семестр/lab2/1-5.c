/*
Вывести элементы динамического массива целых чисел в обратном
порядке, используя указатель и операцию декремента (−−).
*/
// NOTE: Возможно стоит объединить с 1-4.
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int length;
    printf("Enter length of array: ");
    scanf("%d", &length);

    double array[length];
    double input;
    for (double *start = array; start < &array[length]; start++)
    {
        printf("[%ld]: ", ((start - array)));
        scanf("%lf", &input);

        *start = input;
    }
    printf("\nArray: [");
    for (double *start = &array[length - 1]; start >= array; start--)
        printf("%lf, ", *start);
    printf("]\n");

    return 0;
}
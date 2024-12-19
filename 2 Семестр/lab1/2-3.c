#include <stdio.h>

#define ARRAY_SIZE 78

int main(void)
{
    int m;
    printf("Enter m: ");
    scanf("%d", &m);

    int padovan_sequence[ARRAY_SIZE];
    padovan_sequence[0] = padovan_sequence[1] = padovan_sequence[2] = 1;

    for (int i = 3; i < ARRAY_SIZE; i++)
    {
        padovan_sequence[i] = padovan_sequence[i - 2] + padovan_sequence[i - 3];
        if (padovan_sequence[i] > m)
            break;
    }

    for (int i = 0; padovan_sequence[i] < m; i++)
        printf("%d\n", padovan_sequence[i]);

    return 0;
}

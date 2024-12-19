#include <stdio.h>

int main(void)
{
    char str[] = "string";
    for (int i = 0; str[i]; i++)
    {
        printf("%c", str[i]);
    }

    printf("\n");
    return 0;
}
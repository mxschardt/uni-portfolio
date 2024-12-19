#include <stdio.h>

int main(void)
{
    int number;
    int sum = 11;
    while (sum > 10)
    {
        sum = 0;
        printf("Enter a number: ");
        scanf("%d", &number);
        while (number > 0)
        {
            sum += number % 10;
            number = number / 10;
        }
    }
}
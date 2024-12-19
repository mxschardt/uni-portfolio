#include <stdio.h>

long int fact(long int n)
{
    if (n == 0)
        return 1;

    long int result = 1;
    for (int i = 1; i <= n; i++)
    {
        result *= i;
    }

    return result;
}

long int fact_recursive(long int n)
{
    if (n == 0 || n == 1)
        return 1;
    else
        return n * fact_recursive(n - 1);
}
int main(void)
{

    printf("fact(5): %ld\n", fact(5));
    printf("fact(5) rec: %ld\n", fact_recursive(5));
    return 0;
}
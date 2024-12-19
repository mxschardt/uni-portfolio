#include <complex.h>
#include <stdio.h>
#include <math.h>

long fact(int n)
{
    long result = 1;
    for (int i = 1; i <= n; i++)
        result *= i;
    return result;
}

int main(void)
{
    complex cNumber = 1.0 + 2.0 * I;
    int n = 12;

    complex exp = 1 + cNumber;
    complex temp = cpow(cNumber, 3);

    for (int i = 2; i <= n; i++)
        exp += 1.0 / fact(i) * cpow(cNumber, i);

    printf("complex number: %.1f + %.1fi\n", creal(cNumber), cimag(cNumber));
    printf("exp: %.5f + %.5fi\n", creal(exp), cimag(exp));

    return 0;
}
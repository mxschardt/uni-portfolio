#include <stdio.h>
#include <math.h>
#include <stdlib.h>

double f(double x)
{
    return 1 / x;
}

int main(void)
{
    const int SUB_INTERBALS = 1000;

    double a, b;
    printf("Enter a and b\n");
    scanf("%lf%lf", &a, &b);

    double h = fabs(b - a) / SUB_INTERBALS;
    double sum = 0;

    for (int i = 1; i < SUB_INTERBALS; i++)
    {
        double x = a + i * h;
        sum = sum + f(x);
    }

    double result = (h / 2) * (f(a) + f(b) + 2 * sum);
    printf("The integral is: %lf\n", result);

    return 0;
}

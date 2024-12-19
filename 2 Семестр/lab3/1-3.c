#include <stdio.h>
#include <math.h>

struct complex
{
    double real; // a
    double imag; // b
};

// a + bi

// z^n = r^n (cos n * phi + i * sin n * phi) - правило возвыщения комл. чисел в степень
// т.к. r * cos phi = a, r * sin phi = b, r = sqrt(a * a + b * b) то
// z^n = sqrt(a * a + b * b)^n * cos n * phi + sqrt(a * a + b * b)^n * sin n * phi

int main(void)
{
    int n = 12;
    int fact = 1;
    struct complex cNumber = {1.0, 2.0};                   // 1 + 2i
    struct complex exp = {cNumber.real + 1, cNumber.imag}; // 1 + z

    for (int i = 2; i <= n; i++)
    {
        fact *= i;
        //
        // NOTE:
        // Считать степень с нуля каждый раз очень дорого.
        // Лучше умножать число само на себя каждый раз.
        double arctgAB = atan(cNumber.imag / cNumber.real);
        double r = pow(sqrt(cNumber.real * cNumber.real + cNumber.imag * cNumber.imag), i);
        struct complex result = {r * cos(arctgAB * i), r * sin(arctgAB * i)};

        exp.real += 1.0 / fact * result.real;
        exp.imag += 1.0 / fact * result.imag;
    }

    printf("exp(%.2lf + %.2lfi) = %.5lf + %.5lfi\n", cNumber.real, cNumber.imag, exp.real, exp.imag);

    return 0;
}
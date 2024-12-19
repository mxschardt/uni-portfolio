#include <stdio.h>

struct foo
{
    int (*bar)(int);
};
int func(int x)
{
    return x + 2;
}
int main(void)
{
    struct foo ptr = {func};
    int result = ptr.bar(2);
    printf("result: %d\n", result);

    return 0;
}

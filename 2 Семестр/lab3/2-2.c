#include <stdio.h>

union Byte
{
    char value;
};

int main(void)
{

    unsigned long number = 1234567890123456789;
    union Byte byte;
    for (char *p = (char *)&number; p < (char *)&number + sizeof(unsigned long); p++)
    {
        byte.value = *p;
        printf("%hhx ", byte.value);
    }
    printf("\n");
    return 0;
}
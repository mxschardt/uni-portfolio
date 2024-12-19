#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main(void)
{
    char str[] = "~`1!@#$^&*()_Qq{}:\",./?";

    for (int i = 0; str[i]; i++)
    {
        printf("%c\n", str[i]);
        printf("isalnum  %d\n", isalnum(str[i]));
        printf("isalpha  %d\n", isalpha(str[i]));
        printf("islower  %d\n", islower(str[i]));
        printf("isupper  %d\n", isupper(str[i]));
        printf("isdigit  %d\n", isdigit(str[i]));
        printf("isxdigit %d\n", isxdigit(str[i]));
        printf("iscntrl  %d\n", iscntrl(str[i]));
        printf("isgraph  %d\n", isgraph(str[i]));
        printf("isspace  %d\n", isspace(str[i]));
        printf("isblank  %d\n", isblank(str[i]));
        printf("isprint  %d\n", isprint(str[i]));
        printf("ispunct  %d\n", ispunct(str[i]));
    }
    return 0;
}
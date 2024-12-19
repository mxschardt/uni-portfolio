#include <stdio.h>
#include <locale.h>
#include <string.h>
#include <ctype.h>

#define MY_SIZE 10

int main(void)
{
    setlocale(LC_ALL, "en_US.iso88591");

    char my_string[MY_SIZE];
    printf("Enter string: ");
    fscanf(stdin, "%s", my_string);

    int string_size = 0;
    // Первый способ нахождения длинны
    for (int i = 0; my_string[i]; i++)
    {
        string_size = i;
    }
    // Второй
    string_size = 0;
    int i = 0;
    for (char *p = my_string; *p; p++)
    {
        string_size = i;
        i++;
    }
    // Третий
    size_t s = strlen(my_string);

    printf("String size: %d\n", string_size);

    char my_string_copy[MY_SIZE];
    strcpy(my_string_copy, my_string);

    char first_str[] = "foo";
    char second_str[] = "bar";
    char third_str[6];
    strcat(third_str, first_str);
    strcat(third_str, second_str);

    printf("Compare result: %d\n", strcmp(first_str, second_str));

    printf("Enter another string: ");
    fscanf(stdin, "%s", my_string);

    for (int i = 0; my_string[i]; i++)
        my_string[i] = tolower(my_string[i]);
    printf("%s\n", my_string);

    for (int i = 0; my_string[i]; i++)
        my_string[i] = toupper(my_string[i]);
    printf("%s\n", my_string);

    return 0;
}
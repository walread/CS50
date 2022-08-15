#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

bool only_digits(string argv);
char rotate(char c, int k);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    bool d = only_digits(argv[1]);
    if (d == false)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    int k = atoi(argv[1]);
    string pt = get_string("plaintext: ");
    printf("ciphertext: ");
    for (int i = 0, n = strlen(pt); i < n; i++)
    {
        char c = (char) pt[i];
        printf("%c", rotate(c, k));
    }
    printf("\n");
}

bool only_digits(string argv)
{
    int i = 0;
    while (isdigit((char) argv[i]))
    {
        i++;
    }
    if (i == strlen(argv))
    {
        return true;
    }
    else
    {
        return false;
    }
}

char rotate(char c, int k)
{

    if (isalpha(c))
    {
        if (isupper(c))
        {
            c = c - 65;
            c = (c + k) % 26;
            c = c + 65;
            return c;
        }
        else
        {
            c = c - 97;
            c = (c + k) % 26;
            c = c + 97;
            return c;
        }
    }
    else
    {
        return c;
    }
}
#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

int count_letters(string text);
int l = 0;
int count_words(string text);
int w = 1;
int count_sentences(string text);
int s = 0;

int main(void)
{
    string text = get_string("Text: ");
    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);
    float index = ((0.0588 * ((float) letters / (float) words * 100)) - (0.296 * ((float) sentences / (float) words * 100)) - 15.8);
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    if (index >= 1 && index < 16)
    {
        printf("Grade %i\n", (int) round(index));
    }
}

int count_letters(string text)
{
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (isalpha(text[i]))
        {
            l++;
        }
        else
        {
            l = l + 0;
        }
    }
    return l;
}

int count_words(string text)
{
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (isspace(text[i]))
        {
            w++;
        }
        else
        {
            w = w + 0;
        }
    }
    return w;
}

int count_sentences(string text)
{
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            s++;
        }
        else
        {
            s = s + 0;
        }
    }
    return s;
}

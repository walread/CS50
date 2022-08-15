#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1 || n > 8);

    //for each row
    for (int i = 0; i < n; i++)
    {

        //space for each column
        for (int j = i + 1; j < n; j++)
        {
            //print a space
            printf(" ");
        }

        //# for each column
        for (int x = -1; x < i; x++)
        {
            //print a brick
            printf("#");
        }

        //move to next row
        printf("\n");
    }
}
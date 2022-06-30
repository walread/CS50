#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

//Global variables
typedef uint8_t BYTE;
int BLOCK_SIZE = 512;
int counter = 0;
FILE *img;

int main(int argc, char *argv[])
{
    //Check command-line arguments
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    //Open and check memory card file
    FILE *raw_file = fopen(argv[1], "r");
    if (raw_file == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    //Read 512 byte into a buffer
    BYTE *buffer = malloc(BLOCK_SIZE * sizeof(BYTE));
    while (fread(buffer, (BYTE)1, BLOCK_SIZE, raw_file) == BLOCK_SIZE)
    {

        //Check if start of new JPEG
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff)
        {

            //If first JPEG
            if (counter == 0)
            {
                char *filename = malloc(8 * sizeof(char));
                sprintf(filename, "%03i.jpg", counter);
                img = fopen(filename, "w");
                if (img == NULL)
                {
                    printf("Could not open file.\n");
                    return 1;
                }
                fwrite(buffer, (BYTE)1, BLOCK_SIZE, img);
                free(filename);
                counter++;
            }

            //Else if not first JPEG
            else
            {
                fclose(img);
                char *filename = malloc(8 * sizeof(char));
                sprintf(filename, "%03i.jpg", counter);
                img = fopen(filename, "w");
                if (img == NULL)
                {
                    printf("Could not open file.\n");
                    return 1;
                }
                fwrite(buffer, (BYTE)1, BLOCK_SIZE, img);
                free(filename);
                counter++;
            }
        }

        //Else if already found start of JPEG
        else if (counter > 0)
        {
            fwrite(buffer, (BYTE)1, BLOCK_SIZE, img);
        }
    }

    //Close all files and free memory 
    fclose(img);
    fclose(raw_file);
    free(buffer);
}
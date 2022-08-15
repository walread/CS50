// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

//Counter for number of words in dictionary
int counter = 0;

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Choose number of buckets in hash table
const unsigned int N = ((LENGTH + 1) * 'z');

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    //Make cursor and set equal to first item in linked list
    node *c = table[hash(word)];

    //Move cursor until you get to NULL, checking each node for the word
    while (c != NULL)
    {
        if (strcasecmp(c->word, word) == 0)
        {
            return true;
        }
        c = c->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    int sum = 0;
    for (int i = 0; i < strlen(word); i++)
    {
        sum += tolower(word[i]);
    }
    return sum;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{

    //Open dictionary file
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        return false;
    }

    //Read strings from file into buffer
    char word[LENGTH + 1];
    while (fscanf(file, "%s", word) != EOF)
    {

        //Create new node
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            return false;
        }

        //Copy string from buffer into new node
        strcpy(n->word, word);

        //Hash word and insert into hash table
        n->next = table[hash(word)];
        table[hash(word)] = n;

        counter++;
    }
    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return counter;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        node *c = table[i];
        node *t = c;
        while (c != NULL)
        {
            c = c->next;
            free(t);
            t = c;
        }
    }
    return true;
}

#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

int is_palindrome(listint_t **head)
{
    int len = 0, i = 0;
    listint_t *tmp;
    int a[10000];

    tmp = *head;
    if((*head) == NULL)
        return (1);
    while (tmp != NULL)
    {
        len++;
        tmp = tmp->next;
    }
    if (len == 1)
        return (1);
    tmp = *head;
    while (tmp != NULL)
    {
        a[i] = tmp->n;
        tmp = tmp->next;
        i++;
    }
    for (i = 0; i <= len / 2; i++)
    {
        if (a[i] != a[len - i - 1])
            return (0);
    }
    return (1);
}
#include <stdio.h>
#include "lists.h"

/**
  * check_cycle - Checks if a singly linked list has a cycle in it
  * @list: The singly linked list to check
  *
  * Return: 1 if it has a cycle in it or 0 if not
  */
int check_cycle(listint_t *list)
{
    listint_t *turtle = list, *hare = list;

    while (hare && hare->next)
    {
        turtle = turtle->next;
        hare = hare->next->next;

        if (turtle == hare)
            return 1; /* Cycle detected */
    }

    return 0; /* No cycle found */
}
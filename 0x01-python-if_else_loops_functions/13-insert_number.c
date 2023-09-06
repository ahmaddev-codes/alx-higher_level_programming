#include "lists.h"
#include <stdlib.h>

/**
  * insert_node - Inserts a number into a sorted singly linked list
  * @head: The head of the sorted singly linked list
  * @number: The number to inserts in the singly linked list
  *
  * Return: The singly linked list with the new number added
  */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
        return NULL;

    new_node->n = number;
    new_node->next = NULL;

    if (*head == NULL || number <= (*head)->n)
    {
        new_node->next = *head;
        *head = new_node;
        return *head;
    }

    listint_t *current = *head;
    while (current->next && current->next->n < number)
    {
        current = current->next;
    }

    new_node->next = current->next;
    current->next = new_node;

    return *head;
}

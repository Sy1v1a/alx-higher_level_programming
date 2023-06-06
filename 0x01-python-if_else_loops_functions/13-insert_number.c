#include "lists.h"
/**
 * insert_node - a function to insert a node
 * @head: head pointer
 * @number: new insert
 *
 * return: address of new node or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *nn = malloc(sizeof(listint_t));
    listint_t *place = *head;
    if (nn == NULL)
    {
        return (NULL);
    }
    nn->n = number;
    nn->next = NULL;
    if (*head == NULL || number < (*head)->n)
    {
        nn->next = *head;
        *head = nn;
        return (nn);
    }
    while (place->next != NULL && number > place->next->n)
    {
        place = place->next;
    }

    nn->next = place->next;
    place->next = nn;
    return nn;
}

#include "lists.h"
listint_t *rev_listint(listint_t **head);
/**
 * is_palindrome - a function that checks palindrome
 * @head: singly list head
 *
 * return: 1 if palindrome 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *one, *last, *mid;
	size_t lent = 0, i;
	if(*head == NULL || (*head)->next ==NULL)
		return (1);
	one = *head;
	while(one)
	{
		lent++;
		one = one->next;
	}
	one = *head;
	for (i = 0; i < (lent / 2) - 1; i++)
		one = one->next;
	if ((lent % 2) == 0 && one->n != one->next->n)
		return (0);
	one = one->next->next;
	last = rev_listint(&one);
	mid = last;

	one = *head;
	while (last)
	{
		if (one->n != last->n)
			return (0);
		one = one->next;
		last = last->next;
	}
	rev_listint(&mid);
	return (1);
}

/**
 * rev_listint - Reverses a singly-linked listint_t list.
 * @head: singly list head
 *
 * return: A pointer to the head of the reversed list.
 */
listint_t *rev_listint(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}

	*head = prev;
	return (*head);
}


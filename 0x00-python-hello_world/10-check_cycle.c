#include "lists.h"
/**
 * check_cycle - function to check a loop circle
 * @list: linled list
 *
 * return 0 for no cycle 1 for a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;
    if (list == NULL || list->next == NULL)
    {
        return 0;
    }

    while (fast != NULL && fast->next != NULL)
    {
        slow = slow->next;
        fast = fast->next->next;

        if (slow == fast)
	{
            return 1;
        }
    }
    return 0;
}

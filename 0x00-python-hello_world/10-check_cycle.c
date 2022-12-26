#include "lists.h"

/**
 * check_cycle - a function in C that checks if a singly linked list has a 
 * cycle in it.
 * @list: pointer to head of list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *check;
	unsigned int n;

	check = list;
	n = 0;
	while (check != NULL)
	{
		if (check->next == list)
		{
			n++;
			break;
		}
		check = check->next;
	}

	if (n > 0)
		return (1);

	return (0);
}

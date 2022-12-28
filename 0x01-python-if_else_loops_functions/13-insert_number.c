#include "lists.h"

/**
 * insert_node - a function in C that inserts a number into a sorted singly
 * linked list.
 * @head: singly linked list
 * @number: the data
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *insert;
	listint_t *current = *head;
	listint_t *temp;

	insert = malloc(sizeof(listint_t));
	if (insert == NULL)
		return (NULL);

	insert->n = number;

	if (*head == NULL)
	{
		insert->next = NULL;
		*head = insert;
	}

	while (current != NULL)
	{
		temp = current->next;
		if (number < current->next->n)
		{
			insert->next = temp;
			if (temp == *head)
			{
				*head = insert;
			}
			else
			{
				current->next = insert;
			}
			break;
		}
		current = current->next;
	}
	return (insert);
}

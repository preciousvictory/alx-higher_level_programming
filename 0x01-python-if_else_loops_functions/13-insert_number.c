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
	listint_t *current;
	listint_t *temp;

	insert = malloc(sizeof(listint_t));
	if (insert == NULL)
		return (NULL);

	insert->n = number;

	if (head == NULL)
		return (0);

	current = *head;
	while (current != NULL)
	{
		temp = current->next;
		if (number < current->next->n)
		{
			current->next = insert;
			insert->next = temp;
			break;
		}
		current = current->next;
	}
	return (insert);
}

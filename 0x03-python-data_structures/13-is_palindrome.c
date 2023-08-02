#include <stdio.h>
#include "lists.h"
#include <stdbool.h>

/**
 * is_palindrome - function that checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head) {
	int len = 0, half = 0, i = 0, num = 0, pal_num = 0, a, b;
	bool p = true;
	listint_t *current = *head, *now;

	if (head == NULL) {
		return 1;
	}
	
	while (current != NULL) {
		current = current->next;
		len += 1;
	}
	if ((len % 2) != 0) {
		return 0;
	}

	current = *head;
	half = len / 2;
	i = len - 1;

	for (a = 0; a < half; a++) {
		now = current;
		num = current->n;	
		for (b = 0; b < i; b++) {
			now = now->next;
		}		
		pal_num = now->n;		
		if (num != pal_num) {
			p = false;
		}
		i -= 2;
		current = current->next;
	}


	if (!p) {
		return 0;
	}
	return 1;
}

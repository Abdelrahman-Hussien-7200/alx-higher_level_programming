#include "lists.h"

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_listint - Reverses a singly-linked listint_t
 *
 * @head: A pointer
 *
 * Return: A pointer
*/

listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head, *next, *prevs = NULL;

	while (node)
	{
		next = node->next;
		node->next = prevs;
		prevs = node;
		node = next;
	}

	*head = prevs;
	return (*head);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 *
 * @head: A pointer to the head of the linked list.
 *
 * Return: not a palindrome - 0.
 *         a palindrome - 1.
*/

int is_palindrome(listint_t **head)
{
	listint_t *temp, *revs, *middle;
	size_t size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	temp = *head;
	while (temp)
	{
		size++;
		temp = temp->next;
	}

	temp = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		temp = temp->next;

	if ((size % 2) == 0 && temp->n != temp->next->n)
		return (0);

	temp = temp->next->next;
	revs = reverse_listint(&temp);
	middle = revs;

	temp = *head;
	while (revs)
	{
		if (temp->n != revs->n)
			return (0);
		temp = temp->next;
		revs = revs->next;
	}
	reverse_listint(&middle);

	return (1);
}

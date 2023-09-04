#include "lists.h"

/**
 * check_cycle - Entry point
 *
 * @list: pointer to link
 *
 * Return: integer
*/

int check_cycle(listint_t *list)
{
	listint_t *s = list, *f = list;

	while (f && f->next)
	{
		s = s->next;
		f = f->next->next;
		if (s == f)
			return (1);
	}
	return (0);
}

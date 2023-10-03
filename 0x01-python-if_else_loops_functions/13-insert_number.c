#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp, *node;

	tmp = *head;
	node = malloc(sizeof(listint_t));
	if(node == NULL)
		return (NULL);
	node->n = number;
	node->next = NULL;
	if((*head) == NULL)
	{
		*head = node;
		return (node);
	}
	else if((*head)->n >= number)
	{
		node->next = *head;
		*head = node;
		return (node);
	}
	else
	{
		while(tmp->next != NULL)
		{
			if(tmp->next->n >= number)
			{
				node->next = tmp->next;
				tmp->next = node;
				return (node);
			}
			tmp = tmp->next;
		}
		node->next = NULL;
		tmp->next = node;
		return (node);
	}
	return (NULL);
}
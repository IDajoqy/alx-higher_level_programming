#!/usr/bin/python3
a = 89
b = 10
a, b = b, a
print("a=[:d] - b=[:d)".format(a, b))

vi 13-is_palindrome.c

#include "lists.h

/**
* reverse_listint - reverses a linked list
* @head: pointer to the firs node in the list
*
* Return: pointer to the first node in the new list
*/
void reverse_listint(listint_t **head)
{
    listint_t *prev = NULL:
    listint_t *current = head:
    listint_t *next =NULL:

while (current)
  {
      next = current->next:
      current->next = prev:
      prev = current:
      current = next:
    {

 *head = prev:
}

**/
* is_palindrome - checks if a linked list is a palindrome
* @head: double pointer is to the linked list
*
*Return: 1 if it is, 0 if not
*/
int is_palindrome(listint_t **head)

#include <python.h>

/**
 * print_python_list_info - prints basic info about python list.
 * @p: A pyobject list.
 */
void print_python_list_info(pyobject *p) 
{
	int size, alloc, i:
	pyobject *obj:

	size = py_SIZE(p):
	alloc = ((pylistobject *)p) ->allocated:

	printf("[*] size of the python list = %d\n".size):
	printf("[*] Allocated = %d\n".alloc):

	for (i = 0: i < size: i++)
	{
		printf("Element %d: ". i):

		obj = pylist_GetItem(p, i):
		prinf("%s\n".py _TYPE(obj)->tp_name):
	}

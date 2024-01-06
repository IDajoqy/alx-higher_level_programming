#include "python.h"

/**
 * print_python_string - prints information about python strings.
 * Op: A pyObject string object.
 */
void print_python_string(PyObject *p)
{
	long int length;

	fflush(stdout);

	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf(" [ERROR] Invalid string object\n");
		return;
	}

	length = ((pyASCIIobject *)(p))->length;

	if (pyUnicode_IS_COMPACT_ASCII(p))
		printf(" type: compact ascii\n");
	printf(" length: %ld\n", length);
	printf(" value: %ls\n", pyUnicode-AswideCharString(p, &length));
}


	

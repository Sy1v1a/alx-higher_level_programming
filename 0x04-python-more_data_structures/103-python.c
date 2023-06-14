#include <stdio.h>
#include <Python.h>
/**
 * print_python_bytes - Prints bytes info
 * @p: Python Object
 *
 * return: no return
 */
void print_python_bytes(PyObject *p)
{
	char *string;
	long int sizeb, i, l;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", sizeb);
	printf("  trying string: %s\n", string);

	if (sizeb >= 10)
		l = 10;
	else
		l = sizeb + 1;

	printf("  first %ld bytes:", l);

	for (i = 0; i < l; i++)
		if (string[i] >= 0)
			printf(" %02x", string[i]);
		else
			printf(" %02x", 256 + string[i]);

	printf("\n");
}


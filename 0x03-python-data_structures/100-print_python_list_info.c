#include <Python.h>
#include <stdlib.h>
#include <stdio.h>
/**
 * print_python_list_infor - prints info of python list
 * @p: object list
 *
 */
void print_python_list_info(PyObject *p)
{
	int i, j, k;
	Pyobject *objecti;
	i = Py_SIZE(p);
	j = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n",i);
	printf("[*] Allocated = %d\n", j);

	for (k = 0; k < i; k++)
	{
		printf("Element %d: ",k);
		objecti = PyList_Getitem(p, k);
		printf("%s\n",Pt_TYPE(object1)->tp_narme);
	}
}

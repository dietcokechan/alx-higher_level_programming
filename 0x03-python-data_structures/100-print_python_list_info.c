#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

void print_python_list_info(PyObject *p)
{
	int i;
	int list_len = (int)PyList_Size(p);

	printf("[*] Size of the Python List = %d\n", list_len);
	printf("[*] Allocated = %d\n", (int)((PyListObject *)p)->allocated);
	for (i = 0; i < list_len; i++)
	{
		printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}

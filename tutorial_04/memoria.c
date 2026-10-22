#include <stdio.h>

int main(void) {
	int numero = 10;
	int *puntero = &numero;
	
	printf("Valor inicial: %d\n", numero);
	printf("Direccion de numero: %p\n", (void *)&numero);
	printf("Direccion guardada en puntero: %p\n", (void *)puntero);
	printf("Tamaño de numero: %zu buytes\n", sizeof(numero));

	*puntero = 25;
	
	printf("Valor final: %d\n", numero);

	return 0;
}

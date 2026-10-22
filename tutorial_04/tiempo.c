#include <stdio.h>
#include <time.h>

int main(void) {
	volatile long long suma = 0;
	const long long N = 100000000;
	volatile long long suma2 = 0;

	clock_t inicio = clock();

	for (long long i = 0; i < N; i++) {
		suma += i;
		suma2 = suma*suma;
	}

	clock_t fin = clock();
	double tiempo = (double)(fin - inicio) / CLOCKS_PER_SEC;

	printf("Resultado: %lld\n", suma);
	printf("Tiempo de CPU: %.6f s\n", tiempo);
	
	return 0;
}

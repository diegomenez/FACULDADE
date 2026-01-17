#include <stdio.h>
// função recursiva que imprime números de n até 1
void recursiveloop(int n) {
    if (n > 0) {
        printf("%d ", n);
        recursiveloop(n - 1); // chamada recursiva
        
    }
}

int main() {
    int numero = 5; // exemplo de número inicial
    printf("Contagem regressiva:");
    recursiveloop(numero); // chamada da função recursiva
    return 0;
}
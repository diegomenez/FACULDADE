#include <stdio.h>
 
int main() {
    int matriz[3][3];  // Declaração de uma matriz 3x3 de inteiros
 
    // Inicializando os elementos da matriz
    matriz[0][0] = 1;
    matriz[0][1] = 2;
    matriz[0][2] = 3;
    matriz[1][0] = 4;
    matriz[1][1] = 5;
    matriz[1][2] = 6;
    matriz[2][0] = 7;
    matriz[2][1] = 8;
    matriz[2][2] = 9;
 
    // Acessando elementos da matriz
    printf("O elemento na posição [0][0] é %d\n", matriz[0][0]);
    printf("O elemento na posição [1][1] é %d\n", matriz[1][1]);

     printf("\n---------------------------------------------\n\n");

     // --- Exemplo 2: Inicializando a matriz de forma direta ---
    printf("--- Exemplo 2: Inicializacao direta ---\n");
    // Esta forma é mais rápida e limpa de escrever
    int matriz_exemplo2[3][3] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };

    // Acessando e imprimindo elementos da segunda matriz
    printf("O elemento na posicao [0][0] e %d\n", matriz_exemplo2[0][0]);
    printf("O elemento na posicao [1][1] e %d\n", matriz_exemplo2[1][1]);
    printf("O elemento na posicao [2][2] e %d\n", matriz_exemplo2[2][2]);
        printf("\n---------------------------------------------\n\n");
    
        // --- Exemplo 3: Imprimindo a matriz completa ---      

    printf("--- Exemplo 3: ---\n");
    
    char *nomesAlunos [3] [3] ={
        {"Aluno 0", "Pt:9.0", "Mat:8.5"},
        {"Aluno 1", "Pt:7.5", "Mat:6.0"},
        {"Aluno 2", "Pt:8.0", "Mat:9.5"}
    };
    
        int index;
        printf("Digite o numero do aluno que queira ver as notas... \n");
        printf("Para o aluno 0, digite 0 \n");
        printf("Para o aluno 1, digite 1 \n");
        printf("Para o aluno 2, digite 2 \n");
        scanf("%d", &index);
        printf("As notas do %s sao: %s , %s ...\n", nomesAlunos[index][0], nomesAlunos[index][1], nomesAlunos[index][2]);

    
    
     printf("\n---------------------------------------------\n\n"); 

    
 
    return 0;
}


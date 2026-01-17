#include <stdio.h>

int main() {
    // Declaração de variáveis que serão usadas como contadores
    int bispo = 0;
    int rainha = 0;
    int cavalo = 0;


    //  Movimento da Torre com 'for' 
    printf("--- Movimento da Torre (5 casas para a direita) ---\n");
    
    for (int i = 0; i < 5; i++) {
        printf("Torre moveu: Direita\n");
    }

    printf("\n"); // Linha em branco para separar os movimentos

    //  Movimento do Bispo com 'while' 
    printf("--- Movimento do Bispo (5 casas na diagonal superior direita) ---\n");
    
    while (bispo < 5) {
        printf("Bispo moveu: Cima, Direita\n");
        bispo++; 
    }

    printf("\n"); // Linha em branco para separar os movimentos

    //  Movimento da Rainha com 'do-while' 
    printf("--- Movimento da Rainha (8 casas para a esquerda) ---\n");
    
    do {
        printf("Rainha moveu: Esquerda\n");
        rainha++; 
    } while (rainha < 8);
    printf("\n"); // Linha em branco para separar os movimentos

    //  Movimento do Cavalo com 'for' 
    printf("--- Movimento do Cavalo (1 movimento em 'L') ---\n");
    
    for (cavalo ; cavalo <= 2; cavalo++) {
        printf("Cavalo moveu: para baixo\n");
        cavalo++; 
        for (cavalo; cavalo <2; cavalo++) {
            printf("Cavalo moveu: para baixo\n");
            cavalo++;
        }
    //  Movimento do Cavalo com 'while' 
    
    int cavalo = 0;
    while ( cavalo < 1){
        printf("Cavalo moveu: para esquerda\n");
        cavalo++;
    }
    
    }

    return 0; 
}
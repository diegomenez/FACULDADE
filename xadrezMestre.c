#include <stdio.h>

// --- Funções Recursivas ---

// Função recursiva para o movimento da Torre
void moverTorreRecursivo(int casas) {
    // Caso Base: se não houver mais casas para mover, a função para.
    if (casas <= 0) {
        return;
    }
    // Passo Recursivo: imprime o movimento e chama a si mesma com uma casa a menos.
    printf("Torre moveu: Direita\n");
    moverTorreRecursivo(casas - 1);
}

// Função recursiva para o movimento do Bispo
void moverBispoRecursivo(int casas) {
    // Caso Base:
    if (casas <= 0) {
        return;
    }
    // Passo Recursivo:
    printf("Bispo moveu: Cima, Direita\n");
    moverBispoRecursivo(casas - 1);
}

// Função recursiva para o movimento da Rainha
void moverRainhaRecursivo(int casas) {
    // Caso Base:
    if (casas <= 0) {
        return;
    }
    // Passo Recursivo:
    printf("Rainha moveu: Esquerda\n");
    moverRainhaRecursivo(casas - 1);
}


// --- Função Principal ---

int main() {
    // --- 1. Movimento da Torre com Recursividade ---
    printf("--- Movimento da Torre (5 casas para a direita) ---\n");
    moverTorreRecursivo(5);
    printf("\n");

    // --- 2. Movimento do Bispo (duas implementações) ---
    // a) Com Recursividade
    printf("--- Movimento do Bispo (5 casas na diagonal - Recursivo) ---\n");
    moverBispoRecursivo(5);
    printf("\n");

    // b) Com Loops Aninhados
    printf("--- Movimento do Bispo (5 casas na diagonal - Loops Aninhados) ---\n");
    // Loop externo controla o movimento vertical (5 casas para cima)
    for (int vertical = 0; vertical < 5; vertical++) {
        // Loop interno controla o movimento horizontal (1 casa para a direita por vez)
        for (int horizontal = 0; horizontal < 1; horizontal++) {
            printf("Bispo moveu: Cima, Direita\n");
        }
    }
    printf("\n");

    // --- 3. Movimento da Rainha com Recursividade ---
    printf("--- Movimento da Rainha (8 casas para a esquerda) ---\n");
    moverRainhaRecursivo(8);
    printf("\n");

    // --- 4. Movimento do Cavalo com Loops Complexos ---
    printf("--- Movimento do Cavalo (2 para cima, 1 para a direita) ---\n");
    int passos_cima = 0;
    int passos_direita = 0;

    // Um loop projetado para rodar até 10 vezes, mas que será interrompido antes.
    for (int i = 0; i < 10; i++) {
        // Lógica para os movimentos para cima
        if (passos_cima < 2) {
            printf("Cavalo moveu: Cima\n");
            passos_cima++;
            // 'continue' pula para a próxima iteração, pois ainda não terminamos os passos para cima.
            continue;
        }

        // Lógica para o movimento para a direita
        if (passos_direita < 1) {
            printf("Cavalo moveu: Direita\n");
            passos_direita++;
        }

        // Se todos os movimentos (2 para cima, 1 para a direita) foram concluídos...
        if (passos_cima == 2 && passos_direita == 1) {
            printf("Movimento em 'L' concluído!\n");
            // 'break' encerra o loop, pois o movimento já está completo.
            break;
        }
    }

    return 0;
}
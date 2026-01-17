#include <stdio.h>

struct Carta {
    char estado[3];
    char codigo[4];
    char nome_da_cidade[50];
    unsigned long int populacao;
    float area;
    float pib;
    int pontos_turisticos;
    float densidade_populacional;
    float pib_per_capita;
    float super_poder; // Adicionando campo para super poder
};

int main() {
    struct Carta carta1;
    struct Carta carta2;

    printf("\n--- Cadastro da Carta 1 ---\n");
    printf("Estado (sigla): ");
    scanf("%2s", &carta1.estado);
    printf("Código (sigla): ");
    scanf("%3s", &carta1.codigo);
    printf("Nome da Cidade: ");
    scanf(" %[^\n]", &carta1.nome_da_cidade);
    printf("População: ");
    scanf("%lu", &carta1.populacao);
    printf("Área (km²): ");
    scanf("%f", &carta1.area);
     while (carta1.area == 0) {
     printf("Área não pode ser zero! Digite novamente: ");
    scanf("%f", &carta1.area);}
    printf("PIB (bilhões): ");
    scanf("%f", &carta1.pib);
    printf("Número de pontos turísticos: ");
    scanf("%d", &carta1.pontos_turisticos);
    // calculo do PIB per capita
    carta1.pib_per_capita = carta1.pib * 1e9 / carta1.populacao;
  
    // calculo da densidade populacional
    carta1.densidade_populacional = (float)carta1.populacao / carta1.area;

    // calculo super poder
    carta1.super_poder = (float)carta1.populacao + carta1.area + carta1.pib + carta1.pontos_turisticos + carta1.pib_per_capita + (1.0f/carta1.densidade_populacional) ;

    printf("\n--- Cadastro da Carta 2 ---\n");
    printf("Estado (sigla): ");
    scanf("%2s", &carta2.estado);
    printf("Código (sigla): ");
    scanf("%3s", &carta2.codigo);
    printf("Nome da Cidade: ");
    scanf(" %[^\n]", &carta2.nome_da_cidade);
    printf("População: ");
    scanf("%lu", &carta2.populacao);
    printf("Área (km²): ");
    scanf("%f", &carta2.area);
     while (carta2.area == 0) {
     printf("Área não pode ser zero! Digite novamente: ");
    scanf("%f", &carta2.area);}
    printf("PIB (bilhões): ");
    scanf("%f", &carta2.pib);
    printf("Número de pontos turísticos: ");
    scanf("%d", &carta2.pontos_turisticos);
    
    // calculo do PIB per capita
    carta2.pib_per_capita = carta2.pib * 1e9 / carta2.populacao;
    
    // calculo da densidade populacional
    carta2.densidade_populacional = (float)carta2.populacao / carta2.area;
    
    // calculo super poder
    carta2.super_poder = (float)carta2.populacao + carta2.area + carta2.pib + carta2.pontos_turisticos + carta2.pib_per_capita + (1.0f/carta2.densidade_populacional) ;

    printf("\n--- Dados da Carta 1 ---\n");
    printf("Estado: %s\n", carta1.estado);
    printf("Código: %s\n", carta1.codigo);  
    printf("Nome da Cidade: %s\n", carta1.nome_da_cidade);
    printf("População: %d\n", carta1.populacao);
    printf("Área: %.2f km²\n", carta1.area);
    printf("PIB: %.2f bilhões\n", carta1.pib);
    printf("Pontos Turísticos: %d\n", carta1.pontos_turisticos);
    printf("PIB per capita: R$ %.2f\n", carta1.pib_per_capita);
    printf("Densidade Populacional: %.2f hab/km²\n", carta1.densidade_populacional);
    printf("Super Poder: %.2f\n", carta1.super_poder);

    printf("\n--- Dados da Carta 2 ---\n");
    printf("Estado: %s\n", carta2.estado);
    printf("Código: %s\n", carta2.codigo);  
    printf("Nome da Cidade: %s\n", carta2.nome_da_cidade);
    printf("População: %d\n", carta2.populacao);
    printf("Área: %.2f km²\n", carta2.area);
    printf("PIB: %.2f bilhões\n", carta2.pib);
    printf("Pontos Turísticos: %d\n", carta2.pontos_turisticos);
    printf("PIB per capita: R$ %.2f\n", carta2.pib_per_capita);
    printf("Densidade Populacional: %.2f hab/km²\n", carta2.densidade_populacional);
    printf("Super Poder: %.2f\n", carta2.super_poder);

    // Exibir duelo das cartas
    if (carta1.populacao > carta2.populacao) {
        printf("\nCarta 1 vence no critério de população!\n");
    } else if (carta1.populacao < carta2.populacao) {
        printf("\nCarta 2 vence no critério de população!\n");
    } else {
        printf("\nEmpate no critério de população!\n");
    }
    if (carta1.area > carta2.area) {
        printf("Carta 1 vence no critério de área!\n");
    } else if (carta1.area < carta2.area) {
        printf("Carta 2 vence no critério de área!\n");
    } else {
        printf("Empate no critério de área!\n");
    }
    if (carta1.pib > carta2.pib) {
        printf("Carta 1 vence no critério de PIB!\n");
    } else if (carta1.pib < carta2.pib) {
        printf("Carta 2 vence no critério de PIB!\n");
    } else {
        printf("Empate no critério de PIB!\n");
    }
    
    if (carta1.pontos_turisticos > carta2.pontos_turisticos) {
        printf("Carta 1 vence no critério de pontos turísticos!\n");
    } else if (carta1.pontos_turisticos < carta2.pontos_turisticos) {
        printf("Carta 2 vence no critério de pontos turísticos!\n");
    } else {
        printf("Empate no critério de pontos turísticos!\n");
    }
    if (carta1.densidade_populacional < carta2.densidade_populacional) {
        printf("Carta 1 vence no critério de densidade populacional!\n");
    } else if (carta1.densidade_populacional > carta2.densidade_populacional) {
        printf("Carta 2 vence no critério de densidade populacional!\n");
    } else {
        printf("Empate no critério de densidade populacional!\n");
    }
    if (carta1.pib_per_capita > carta2.pib_per_capita) {
        printf("Carta 1 vence no critério de PIB per capita!\n");
    } else if (carta1.pib_per_capita < carta2.pib_per_capita) {
        printf("Carta 2 vence no critério de PIB per capita!\n");
    } else {
        printf("Empate no critério de PIB per capita!\n");
    }
    if (carta1.super_poder > carta2.super_poder) {
        printf("Carta 1 vence no critério de super poder!\n");
    } else if (carta1.super_poder < carta2.super_poder) {
        printf("Carta 2 vence no critério de super poder!\n");
    } else {
        printf("Empate no critério de super poder!\n");
    }


    return 0;
}

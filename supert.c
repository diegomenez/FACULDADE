#include <stdio.h>

struct Carta {
    char estado[3];
    char codigo[4];
    char nome_da_cidade[50];
    int populacao;
    float area;
    float pib;
    int pontos_turisticos;
    float densidade_populacional;
    float pib_per_capita;
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
    scanf("%d", &carta1.populacao);
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
    carta1.densidade_populacional = carta1.populacao / carta1.area;

    printf("\n--- Cadastro da Carta 2 ---\n");
    printf("Estado (sigla): ");
    scanf("%2s", &carta2.estado);
    printf("Código (sigla): ");
    scanf("%3s", &carta2.codigo);
    printf("Nome da Cidade: ");
    scanf(" %[^\n]", &carta2.nome_da_cidade);
    printf("População: ");
    scanf("%d", &carta2.populacao);
    printf("Área (km²): ");
    scanf("%f", &carta2.area);
     while (carta1.area == 0) {
     printf("Área não pode ser zero! Digite novamente: ");
    scanf("%f", &carta1.area);}
    printf("PIB (bilhões): ");
    scanf("%f", &carta2.pib);
    printf("Número de pontos turísticos: ");
    scanf("%d", &carta2.pontos_turisticos);
    // calculo do PIB per capita
    carta2.pib_per_capita = carta2.pib * 1e9 / carta2.populacao;
    // calculo da densidade populacional
    carta2.densidade_populacional = carta2.populacao / carta2.area;

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


    return 0;
}

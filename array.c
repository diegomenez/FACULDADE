#include <stdio.h>

int main() {
    // A forma correta de declarar uma lista de nomes (strings):
    // [10] -> teremos 10 nomes na lista.
    // [50] -> cada nome pode ter até 49 caracteres + o caractere final '\0'.
    // Usamos aspas duplas " " para strings.
    char *nomes[] = {"Amanda", "Bruna", "Carla", "Daniela", "Eduarda","Fabiana", "Gabriela", "Helena", "Isabela", "Juliana"};

    printf("Lista de Nomes:\n");

    // O loop continua o mesmo, mas a variável 'i' deve ser 'int' por convenção.
    for (int i = 0; i < 10; i++)
    {
        // Usamos "%s" para imprimir uma string (o nome completo).
        // nomes[i] acessa o nome inteiro na posição 'i' da lista.
        printf("%s\n", nomes[i]);
        
    }
    printf("\n"); // Linha em branco para melhor visualização
    float notas[3] = {85.5, 90.0, 78.0};  // Array de notas de 3 alunos
 
    printf("Nota do primeiro aluno: %.1f\n", notas[0]);
    printf("Nota do segundo aluno: %.1f\n", notas[1]);
    printf("Nota do terceiro aluno: %.1f\n", notas[2]);
    printf("\n"); // Linha em branco para melhor visualização

    char letras[4] = {'A', 'B', 'C', 'D'};  // Array de caracteres
 
    printf("Primeira letra: %c\n", letras[0]);
    printf("Segunda letra: %c\n", letras[1]);
    printf("Terceira letra: %c\n", letras[2]);
    printf("Quarta letra: %c\n", letras[3]);

 return 0;
}
#include <stdio.h>


int main() {

  float nota, soma = 0, media;


  for (int i = 0; i < 5; i++) {

    printf("Digite a nota %d: ", i + 1);

    scanf("%f", &nota);
    soma += nota;
    media = soma / (i + 1);
    printf("A media ate agora e: %.2f\n", media);       
    media = soma / 5;
    printf("A media final e: %.2f\n", media);
    if (media >= 7) {
        printf("Aprovado\n");
    } else if (media >= 5) {
        printf("Recuperacao\n");
    } else {
        printf("Reprovado\n");
    
    

    }
    }
  return 0;

} 
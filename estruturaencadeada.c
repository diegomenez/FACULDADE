#include <stdio.h>
int main() {
int nota;
printf("Digite a nota: ");
scanf("%d",&nota);
// estrutura encadeada
// A>= 90
// B>= 80
// C>= 70
// D>= 60
// F< 60
if (nota >= 90) {
    printf("A\n");
} else if (nota >= 80) {
    printf("B\n");
} else if (nota >= 70) {
    printf("C\n");
} else if (nota >= 60) {
    printf("D\n");
} else {
    printf("F\n");  
}

   
    return 0;
}

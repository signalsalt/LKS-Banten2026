#include <stdio.h>
#include <string.h>

int main() {
    char input[64];
    printf("Input: ");
    fgets(input, sizeof(input), stdin);
    input[strcspn(input, "\n")] = '\0';
    if (strcmp(input, "LKS{tuh-kan-baby-kan}") == 0) {
        printf("Benar\n");
    } else {
        printf("Salah\n");
    }
    return 0;
}

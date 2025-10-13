//AK 7th  my family loop practice

#include <stdio.h>
#include <string.h>


int main(void) {
    char family[5][20] = {"Mom", "Dad", "Sister", "Brother", "Grandma"};

    for (int i = 0; i < 5; i++) {
        printf("Hello, %s!\n", family[i]);
    }
    return 0;
}
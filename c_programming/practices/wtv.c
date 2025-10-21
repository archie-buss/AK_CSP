


make a hangman game in c

#include <stdio.h>
#include <string.h>


void display_word(const char* word, const int* guessed, int length) {
    for (int i = 0; i < length; i++) {
        if (guessed[i]) {
            printf("%c ", word[i]);
        } else {
            printf("_ ");
        }
    }
    printf("\n");
}


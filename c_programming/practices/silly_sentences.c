//AK 7th silly sentence

#include <stdio.h>
#include <string.h>

int main(void) {
    char adjective[20];
    char noun[20];
    char verb[20];
    printf("give an adjective: ");
    scanf("%19s", adjective);
    printf("give a noun: ");
    scanf("%19s", noun);
    printf("give me a verb (past tense): ");
    scanf("%19s", verb);
    char story[200] = "The new robot chef was a ";
    strcat(story, adjective);
    strcat(story, " contraption with a shiny ");
    strcat(story, noun);
    strcat(story, " for a hand. It ");
    strcat(story, verb);
    strcat(story, " the pizza dough right into the ceiling.");
    printf("%s\n", story);




    return 0;
}
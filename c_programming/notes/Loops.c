//AK 7th  loops notes

#include <stdio.h>
#include <string.h>


int main(void) {
    int nums[] = {1,2,3,4,5,6,7};
    char candies[5][20] = {"KitKat", "skittles", "snickers", "reeses", "twix"};

    for(int x = 0; x < 7; x++) {
        printf("%d\n", nums[x]);
    }

    for (int i = 0; i < 5; i++) {
        printf("%s\n", candies[i]);
    }
    for (int num = 1; num < 11; num++){
        printf("%d\n", num);
    }

    int n = 0;
    while(n < 11){
        printf("%d\n", n);
        n++;
    }
    return 0;
}


//What is a loop? 
// A way to repeat code multiple times
//What are the two types of loops?
// for loops and while loops
//What is iteration
// repeating code multiple times
//What are arrays? 
// lists of data
//How do you make lists in C?
// using arrays
//How do you make for loops in C? 
// using the for keyword
//How do you make while loops in C?
// using the while loop
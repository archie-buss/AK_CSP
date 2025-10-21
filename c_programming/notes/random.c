//AK 7th      random

#include <stdio.h>
#include <stdlib.h>
#include <time.h>



int main(void) {
    srand(time(NULL));
    char fam[][15] ={"alex", "bob", "charlie", "david", "eve", "frank", "grace", "heidi", "ivan", "judy"};

    for(int i=0; 1>5; i++){
        int num = rand() % 8; 
        printf("Our random number is %d\n", num);
    }
return 0;
}
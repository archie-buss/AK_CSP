//AK 7th hello world uptade

#include <stdio.h>

void hello(char* name){
    printf("Hello %s!\n", name);
}

int main(){
    hello("Archie");
    hello("Harry");
    hello("Sally");
    hello("Molly");
    hello("Billy");
    return 0;
}
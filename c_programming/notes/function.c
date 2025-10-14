//AK 7th  functions notes

#include <stdio.h>
#include <string.h>
void birthday(char* name, int age){
    printf("Happy Birthday to you!\n");
    printf("Happy Birthday to you!\n");
    printf("Happy Birthday to %s!\n", name);
    printf("Happy Birthday to you!\n");
    printf("Happy Birthday %s you are %d!\n", name, age);
}


int mul(int x, int y){
    return x * y;
}

float get_number(char* type){
    float value;
    printf("How many %s do you have?\n", type);
    scanf("%f", &value);
    return value;

}




int main(void){
    birthday("Jesus", 15);
    birthday("Qwen", 14);
    birthday("Cecily", 16);
    int product = mul(8, 5);
    printf("%d\n", product);
    printf("%d\n", mul(4, 6));
    float pencils = get_number("pencils");
    float notebooks = get_number("notebooks");
    printf("you have %.2f pencils and %.2f notebooks\n", pencils, notebooks);
    return 0;
}
//What a function is
// a function is code that performs a specific task

//Why we use functions
// to make code smaller

//How to write a function in C
// you write the return type, the name of the function, and the parameters in parentheses

//What are arguments and parameters?
// an argument is the value of the variable and the parameter is the name of the variable

//How do arguments and parameters work together?
// the argument is passed to the parameter when the function is called

//How to use parameters and arguments in C
// you define the parameter in the function definition and you pass the argument in the function call

//What are return statements?
// a return statement is a statement that ends a function and returns a value to the caller

//How do return statements change how you define a function in C?
// you have to specify the return type of the function in the function definition

//What do return statements do with the information?
// they return the value to the caller
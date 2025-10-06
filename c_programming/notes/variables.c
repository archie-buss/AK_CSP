// AK 7th Variables notes!
#include <stdio.h>

int main(void){
    int grade; // 4 bytes
    float pi = 3.14; //4 bytes
    double long_pi = 3.141592653; //8 bytes
    char letter_grade; //1 byte
    char name[50];
    printf("What is your name?:\n");
    fgets(name, sizeof(name), stdin);

     //User input
    printf("What is your grade percentage as a whole number?:\n");
    scanf("%d", &grade); 
    while (getchar() != '\n');


    printf("What is letter grade?:\n");
    scanf(" %c", &letter_grade);


    printf("%s did it!\n", name);
    printf("You have a %d, in the class. That is an %c\n", grade, letter_grade);


    return 0;
}

//What is the main difference between declaring variables in Python and C?
// :All variables take the same amount of space! Integers take up 4 bytes of space and a character takes up 1 byte of space.
//In C, what is the purpose of specifying a data type when declaring a variable?
// : The amount of bytes you can have in a line
//List three common data types used in C and their corresponding format specifiers for printf().
// : strings %s, integers %d, characters %c
//How do you declare and initialize an integer variable named "age" with the value 25 in C?
// :  int age = 25;
//What is the difference between printf() and scanf() functions in C?
// : printf is for output, scanf is for input 
//How do you add comments in C? What are the two types of comments?
// : // single line // multi line /* */
//What is the purpose of the #include <stdio.h> line at the beginning of a C program?
// : standard library, input output. To be able to use.
//In C, what is the significance of the main() function?
// : main function is where the program starts
//What is the difference between %d and %f format specifiers in printf()?
// : %d is for integers, %f is for floating point numbers
//How do you print a newline character in C?
// : \n
//What is the purpose of the & symbol when using scanf() to get user input?
// : It is used to get the address of the variable
//How do you declare a constant in C? Provide an example.
// :const. sets the variable to be unchangeable.
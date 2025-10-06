//AK 7th expression notes

#include <stdio.h>
#include <math.h>

int main(void){
    int year = 2025;
    float pi = 3.14;
    double long_pi = 3.141592653;

    printf("%d\n", 8/3); 
    printf("%f.2\n", 8.0/3); 
    printf("%d\n", (int) pow(2, 4));
    
    year += 1;
    printf("%d\n", year);
    year++; //increment operator
    printf("%d\n", year);





    return 0;
}



//What is the difference between an integer and a float in C?
// ;An integer is a whole number, a float is a decimal number
//How does C handle integer division compared to float division?
// ;Integer division truncates the decimal, float division keeps the decimal
//List the arithmetic operators available in C and their functions.
// ;+, -, *, /, %
//What is the modulus operator, and how is it used?
// ;It gives the remainder of a division operation.
//How do you round a float to the nearest integer in C?
// ;use the round() function from math.h
//What is type casting in C? Provide an example of explicit type casting.
// ;Type casting is converting one data type to another. Example: (int) 3.14 converts the float 3.14 to the integer 3.
//How do compound assignment operators work in C? List three examples.
// ;They combine an arithmetic operation with assignment. Examples: +=, -=, *=
//What is the purpose of the math.h library? Name three functions it provides.
// ;It provides mathematical functions. Examples: pow(), round(), sqrt()
//How do you print a float with a specific number of decimal places using printf()?
// ;Use %.nf where n is the number of decimal places. Example: %.2f prints a float with 2 decimal places.
//What happens when you mix integer and float operations in C?
// ;The integer is promoted to a float and the operation is performed as a float operation. 
//AK 7th expression practice

#include <stdio.h>
#include <math.h>

int main(void) {
	int num_2 = 2;
	int num_8 = 8;

	printf("7-24/num_8*4+6 = %d\n", 7 - 24 / num_8 * 4 + 6);
	printf("18/3-7+2num_2*5 = %d\n", 18 / 3 - 7 + num_2 * 5);
	printf("6*4/12+72/num_8-9 = %d\n", 6 * 4 / 12 + 72 / num_8 - 9);
	printf("(17-6/2)+4*3 = %d\n", (17 - 6 / 2) + 4 * 3);
	printf("-2*(1*4-2/2)+(6+2-3) = %d\n", -2 * (1 * 4 - 2 / 2) + (6 + 2 - 3));
	printf("(3*5**2/15)-(5-2**2) = %d\n", (3.0 * pow(5, 2) / 15.0) - (5.0 - pow(2, 2)));
	printf("(1**4*2**2+3**3)-2**5/4 = %d\n", (pow(1, 4) * pow(2, 2) + pow(3, 3)) - (pow(2, 5) / 4.0));
	printf("(22/2-2*5)**2 + (4-6/6)**2 = %d\n", pow((22.0/2 - 2*5), 2) + pow((4 - 6.0/6), 2));

	return 0;
}
#include<stdio.h>
//#include<stdint.h>
#include<inttypes.h>
int main()
{
	uint8_t x = 200;
	//printf("%d\n",x);

	int y = (int)x;
	//unsigned char y = (unsigned char)x;
	//char y = (char)x;

	printf("%d\n",y);
	return 0;
}

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <fcntl.h>

/*
UNIX time: 1498422148 
ais3{5m411_R4N93~_345Y~}
*/

int main(){

	FILE *fd = fopen( "./enc" , "r" );

	char flag[24];

	fread( flag , 1 , 24 , fd );

	unsigned int seed = time(0) , crack = 1498406400;

	while( crack++ && crack < 1498492800 ){
		srand( crack );
		char ans[24];
		for( int i = 0 ; i < 24 ; i++ ) ans[i] = flag[i] ^ rand();

		char check[5] = "AIS3" , check2[5] = "ais3";
		if( !memcmp( check , ans , 4 ) || !memcmp( check2 , ans , 4 ) ) printf( "%d %s\n" , crack , ans );
	}

	return 0;

}
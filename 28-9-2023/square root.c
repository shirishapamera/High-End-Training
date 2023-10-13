//the numbers from 1 to 10 whose square root lies betwwen 40 to 200
#include<stdio.h>
#include<math.h>
int main(){
	int i,j;
	for(j=0;j<=10;j++){
	for(i=40;i<=200;i++){
	if(j*j==i){
		printf("%d  ",i);
	}	
	}
}
	
}

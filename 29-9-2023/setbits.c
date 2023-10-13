#include<stdio.h>
//set bits in a number
int main(){
	int a,count=0;
	scanf("%d",&a);
	while(a){
		count++;
		a=a&(a-1);
	}   
	printf("%d",count);

}  
	


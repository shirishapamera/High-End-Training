//determine a number is power of 2 or not
#include<math.h>
int main(){
	int count=0,n;
	printf("enter a number:")
	scanf("%d",&n);
	while(n){
		count++;
		n=n&(n-1);
		
	}
	if(count==1)
	printf("true");
	else
	printf("false");
}

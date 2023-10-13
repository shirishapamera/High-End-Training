//print 1 if all elements in row or coloumn or digonal is 1
//print 1 if all elements in row or coloumn or digonal is 0

#include<stdio.h>
int main(){
	int i,j,a[4][4];
	int count1=0,count2=0,k1=0,k2=0,k3=0,k4=0,count4=0,count5=0;
	
	for(i=0;i<4;i++){
		for(j=0;j<4;j++){
			scanf("%d",&a[i][j]);
		}
	}
	for(i=0;i<4;i++){
		printf("\n");
		for(j=0;j<4;j++){
			printf("%d",a[i][j]);
		}
	}
	for(i=0;i<4;i++){
		for(j=0;j<4;j++){
			if(i==j){
				if(a[i][j]==1){
				count1+=1;
				if(a[i][j]==0)
				count4+=1;
			}
			}
		}
	}
	if(count1==4)
	printf("\n 1's left diagonal is 1");
	else
	printf("\n1's left diagonal is 0");
	if(count4==4)
	printf("\n 0's left diagonal is 1");
	else
	printf("\n0's left diagonal is 0");
	
	for(i=0;i<4;i++){
		for(j=0;j<4;j++){
			if((i+j)==(4-1)){
				if(a[i][j]==1){
					count2+=1;
				}
				else if(a[i][j]==0)
				count5+=1;
			}
		}
	}
	if(count2==4)
	printf("\n1's right diagonal is 1");
	else
	printf("\n1's right diagonal is 0");
	if(count5==4)
	printf("\n0's right diagonal is 1");
	else
	printf("\n0's right diagonal is 0");
	for(i=0;i<4;i++){
		int count3=0;
		int count6=0;
		for(j=0;j<4;j++){
			if(a[i][j]==1)
			count3+=1;
			if(count3==4)
			k1++;
			else if(a[i][j]==0)
			count6+=1;
			if(count6==4)
			k2++;
			
		}
	}
	if(k1>0)
	printf("\n1's horizontal count is:%d",k1);
	else
	printf("\n1's horizontal count is 0");
	if(k2>0)
	printf("\n0's horizontal count is:%d",k2);
	else
	printf("\n0's horizontal count is 0");
	for(i=0;i<4;i++){
		int count7=0,count8=0;
		for(j=0;j<4;j++){
				if(a[j][i]==1)
					count7+=1;
				if(count7==4)
				k3++;
				if(a[j][i]==0)
					count8+=1;
				if(count8==4)
				k4++;
		}
	}
	if(k3>0)
	printf("\n1's vertical count is:%d",k3);
	else
	printf("\n1's vertical count is 0");
	if(k4>0)
	printf("\n0's vertical countis:%d",k4);
	else
	printf("\n0's vertical count is 0");
	
	
}

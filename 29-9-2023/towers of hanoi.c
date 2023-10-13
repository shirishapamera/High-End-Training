#include<stdio.h>
void tower(int n,char src,char aux,char dest);
int main()
{
	int n;
	printf("enter number of disks:");
	scanf("%d",&n);
	tower(n,'A','B','C');
}
void tower(int n,char src,char aux,char dest)
{
	if(n==1)
	printf("\nmove disk-%d from %c to %c",n,src,dest);
	else
	{
		tower(n-1,src,dest,aux);
		printf("\nmove disk-%d from %c to %c",n,src,dest);
		tower(n-1,aux,src,dest);
	}
}

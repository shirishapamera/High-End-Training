#find missing number in the array
int main(){
	int a[]={1,2,3,5,6};
	int x=0,i=0;
	for(i=0;i<=6;i++)
	x=x^i;
	for(i=0;i<6-1;i++)
	x=x^abs(a[i]);
	printf("%d",x);
}

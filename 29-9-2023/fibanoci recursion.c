//fibanocii series using recursion
int fib(long long int n){
if(n==0)
return 0;
else if(n==1 ||n==2)
return 1;
else
return fib(n-1)+fib(n-2);	
}
int main(){
           long long int n,res;
	scanf("%lld",&n);
	/*res=fib(n);
	printf("%d",res);*/
	int i;
	for(i=0;i<n;i++)
	printf("%lld  ",fib(i));
	
}

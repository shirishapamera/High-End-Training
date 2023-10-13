int fact(long long int n){
	if(n==0 || n==1)
	return 1;
	return n*fact(n-1);
}
int main(){
	long long int n,res;
	scanf("%lld",&n);
            res=fact(n);
	printf("%lld",res);
}


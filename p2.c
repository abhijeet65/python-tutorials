#include<stdio.h>
#include<math.h>

int a[100];

void prime(int n)
{
int i,p,j;
for(i=2;i<=n;i++)
a[i]=i;
for(p=2;p<=sqrt(n);p++)
{
if(a[p]!=0)
j=p*p;
while(j<=n)
{
a[j]=0;
j+=p;
}
}

}

void main()
{
int n,i;
printf("enter the number\n");
scanf("%d",&n);
prime(n);
for(i=1;i<=n;i++){
if(a[i]!=0)
printf("%d ",a[i]);
}
}


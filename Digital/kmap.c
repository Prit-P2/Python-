#include<stdio.h>
#include<math.h>
#include<string.h>
int main()
{
    int nv,no,v[10][10],o[10][10],mid,w;
    printf("Enter number of varable of input:");
    scanf("%d",&nv);
    printf("You want to enter the value of varable?\nif Yes then enter 1 if No the enter 0: ");
    scanf("%d",&w);
    printf("Enter number of varable of output:");
    scanf("%d",&no);
    if(w==1){
    printf("Enter variable in rgformat:\n");
    for(int i=0;i<nv;i++)
    {
        printf("enter for new variable:\n");
        for(int j=0;j<pow(2,nv);j++)
        {
            scanf("%d",&v[j][i]);
        }
    }
    }
    for(int i=0;i<pow(2,nv);i++)
    {	int k=0;
	for(int j=nv-1;j>=0;j--)
	{
		v[i][k]=(i>>j)&1;
		k++;
	}
    }
    for(int i=0;i<no;i++)
    {   
        printf("Enter output in rg format:\n");
        for(int j=0;j<pow(2,nv);j++)
        {
            scanf("%d",&o[j][i]);
        }
    }
    char e[100];
    int in=0;
    int first_term = 1;
    for(int i=0;i<no;i++)
    {e[in++]='\n';
     first_term=1;
        for(int j=0;j<pow(2,nv);j++)
        {
            if(o[j][i]==1)
            {
                if (!first_term) {
                    e[in++] = '+';
                }
                first_term = 0;

                char c='A';
                for(int k=0;k<nv;k++)
                {
                    if(v[j][k]==0)
                    {
                        e[in++]=c;
                        e[in++]='\'';
                    }else if(v[j][k]==1)
                    {
                        e[in++]=c;
                    }
                    c++;
                }
            }
        }
    }
    e[in]='\0';
    printf("%s\n",e);
    return 0;
}

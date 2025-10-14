#include<stdio.h>
#include<math.h>
#include<string.h>
int main()
{
    int nv,no,v[10][10],o[10][10],mid;
    printf("Enter number of varable of input:");
    scanf("%d",&nv);
    printf("Enter number of varable of output:");
    scanf("%d",&no);
    printf("Enter variable in rgformat:\n");
    for(int i=0;i<nv;i++)
    {
        printf("enter for new variable:\n");
        for(int j=0;j<pow(2,nv);j++)
        {
            scanf("%d",&v[j][i]);
        }
    }
    printf("Enter output in rg format:\n");
    for(int i=0;i<no;i++)
    {
        for(int j=0;j<pow(2,nv);j++)
        {
            scanf("%d",&o[j][i]);
        }
    }
    char e[50];
    int in=0;
    int first_term = 1;
    for(int i=0;i<pow(2,nv);i++)
    {
        for(int j=0;j<no;j++)
        {
            if(o[i][j]==1)
            {
                if (!first_term) {
                    e[in++] = '+';
                }
                first_term = 0;

                char c='A';
                for(int k=0;k<nv;k++)
                {
                    if(v[i][k]==0)
                    {
                        e[in++]=c;
                        e[in++]='\'';
                    }else if(v[i][k]==1)
                    {
                        e[in++]=c;
                    }
                    c++;
                }
            }
        }
    }
    e[in]='\0';
    printf("%s",e);
    return 0;
    
}

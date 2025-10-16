#include<stdio.h>
#include<math.h>
#include<string.h>
#include<stdlib.h>
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
    for (int i = 0; i < no; i++) {
        char command[2048] = "";
        // Start building the command to call the python script
        sprintf(command, "python kmap_solver.py %d", nv);

        int has_minterms = 0;
        for (int j = 0; j < pow(2, nv); j++) {
            if (o[j][i] == 1) {
                has_minterms = 1;
                // Append the minterm index to the command
                char minterm_str[10];
                sprintf(minterm_str, " %d", j);
                strcat(command, minterm_str);
            }
        }

        printf("\nFor output %d, the simplified expression is: ", i + 1);
        if (has_minterms) {
            // Execute the command and print its output
            fflush(stdout); // Ensure the printf above is displayed first
            system(command);
        } else {
            printf("0\n");
        }
    }
    return 0;
}

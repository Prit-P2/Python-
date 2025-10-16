#include <stdio.h>
#include <math.h>
#include <string.h>

int main() {
    int nv, no;
    int v[10][10], o[10][10];
    int rows;

    printf("Enter number of variables of input: ");
    scanf("%d", &nv);
    printf("Enter number of variables of output: ");
    scanf("%d", &no);

    rows = pow(2, nv);

    printf("Enter input variables in rg format (each column for a variable, %d rows):\n", rows);
    for (int i = 0; i < nv; i++) {
        printf("Enter values for variable %d:\n", i + 1);
        for (int j = 0; j < rows; j++) {
            scanf("%d", &v[j][i]);
        }
    }

    printf("Enter output in rg format (each column for an output, %d rows):\n", rows);
    for (int i = 0; i < no; i++) {
        printf("Enter values for output %d:\n", i + 1);
        for (int j = 0; j < rows; j++) {
            scanf("%d", &o[j][i]);
        }
    }

    // Example: print the input and output tables
    printf("\nInput Table:\n");
    for (int j = 0; j < rows; j++) {
        for (int i = 0; i < nv; i++) {
            printf("%d ", v[j][i]);
        }
        printf("\n");
    }

    printf("\nOutput Table:\n");
    for (int j = 0; j < rows; j++) {
        for (int i = 0; i < no; i++) {
            printf("%d ", o[j][i]);
        }
        printf("\n");
    }

    char e[50];
    int in = 0;
    for (int i = 0; i < rows; i++) {
        char c = 'A';
        for (int j = 0; j < no; j++) {
            if (o[i][j] == 1) {
                for (int k = 0; k < nv; k++) {
                    if (v[i][k] == 0) {
                        e[in++] = c;
                        c++;
                        e[in++] = "'";
                    } else if (v[i][k] == 1) {
                        e[in++] = c;
                        c++;
                    }
                    if (i + 1 < rows) {
                        e[in++] = '+';
                    }
                }
            }
        }
    }
    e[in] = '\0';
    printf("%s", e);

    return 0;
}
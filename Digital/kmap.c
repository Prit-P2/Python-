#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int nv, no;
    printf("Enter number of variables of input: ");
    scanf("%d", &nv);

    printf("Enter number of variables of output: ");
    scanf("%d", &no);

    int num_combinations = 1 << nv;

    // Dynamically allocate arrays
    int **v = (int **)malloc(num_combinations * sizeof(int *));
    for (int i = 0; i < num_combinations; i++) {
        v[i] = (int *)malloc(nv * sizeof(int));
    }

    int **o = (int **)malloc(num_combinations * sizeof(int *));
    for (int i = 0; i < num_combinations; i++) {
        o[i] = (int *)malloc(no * sizeof(int));
    }

    // Populate the input variable combinations
    for (int i = 0; i < num_combinations; i++) {
        for (int j = 0; j < nv; j++) {
            v[i][j] = (i >> (nv - 1 - j)) & 1;
        }
    }

    // Get the output values from the user
    for (int i = 0; i < no; i++) {
        printf("Enter output for output variable %d in colum:\n", i + 1);
        for (int j = 0; j < num_combinations; j++) {
            scanf("%d", &o[j][i]);
        }
    }

    // Process each output variable
    for (int i = 0; i < no; i++) {
        char command[4096] = ""; // Increased buffer size
        sprintf(command, "python3 /root/Python-/Digital/kmap_solver.py %d", nv);

        int has_minterms = 0;
        for (int j = 0; j < num_combinations; j++) {
            if (o[j][i] == 1) {
                has_minterms = 1;
                char minterm_str[12];
                sprintf(minterm_str, " %d", j);
                strcat(command, minterm_str);
            }
        }

        printf("\nFor output %d, the simplified expression is: ", i + 1);
        if (has_minterms) {
            fflush(stdout);
            system(command);
        } else {
            printf("0\n");
        }
    }

    // Free dynamically allocated memory
    for (int i = 0; i < num_combinations; i++) {
        free(v[i]);
        free(o[i]);
    }
    free(v);
    free(o);

    return 0;
}

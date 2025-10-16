# Digital Logic Projects

This directory contains code and executables for digital logic simplification, especially focusing on Karnaugh Map (K-map) minimization using both C and Python.

## Contents

- **kmap.c**  
  C program that:
  - Interacts with the user to input variables and output truth tables.
  - Calls the Python script to compute minimized Boolean expressions for each output using the Quine-McCluskey algorithm.

- **kmap_solver.py**  
  Python script that:
  - Receives the number of variables and minterms as command-line arguments.
  - Uses the Quine-McCluskey algorithm to produce minimized Boolean expressions.

- **k** and **kmap**  
  Compiled ELF binaries for Linux.  
  - `kmap` is likely compiled from `kmap.c`.
  - `k` may be an alternative or legacy binary.

## Usage

### 1. Compile the C Program

```sh
gcc kmap.c -o kmap -lm
```

### 2. Ensure Python Script Is Present

Make sure `kmap_solver.py` is in the same directory and Python 3 is installed.

### 3. Run the Program

```sh
./kmap
```
Follow the prompts to enter the number of variables and their truth table values. The program will output minimized Boolean expressions.

## Requirements

- GCC (for compiling C code)
- Python 3 (for the minimizer script)

## Notes

- Binaries (`k`, `kmap`) are platform-dependent and may need recompiling on your system.
- The Python script is called by the C program to handle Boolean minimization.
- These files are for educational use.

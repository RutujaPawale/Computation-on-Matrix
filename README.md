Title: Matrix Operations

Objective:
• To introduce the basics of Matrices and some of its applications.
• To study the representation, implementation and applications of 2D Array data structures
• To understand the how to pass 2D arrays as parameters to functions.

Problem Statement
Write a python program to compute following computation on matrix:
1. Addition of matrices
2. Subtraction of matrices
3. Multiplication of matrices
4. Transpose of matrix

Problem Definition:
Matrix: A matrix is an m x n rectangular 2-D array of numbers with m rows and n columns.
Or A matrix is an ordered set of numbers listed in rectangular form.

                  Column 0     Column 1     Column 2     Column 3
    row 0         a[0][0]      a[0][1]       a[0][2]      a[0][3]
    row 1         a[1][0]      a[1][1]       a[1][2]      a[1][3]
    row 2         a[2][0]      a[2][1]       a[2][2]      a[2][3]


Initializing Two-Dimensional arrays:
Two-Dimensional arrays may be initialized by providing a list of initial values & it looks like
this:
int A[4][4] ={ {0,1,2,3}, {3,2,1,0}, {3,5,6,1}, {3,8,3,4} };
We might write the two-dimensional array out as:
int A[4][4] = { {0, 1, 2, 3} , {3, 2, 1, 0} , {3, 5, 6, 1} , {3, 8, 3, 4} };
For a two-dimensional array, in order to reference every element, we must use two nested
loops.

Theory:
• 2-Dimentional Array
• Row major and column major storage representation for array
• Address calculation for two dimensional array

Algorithms:
Write down algorithms for following modules:
1. Accepting a Matrix
2. Displaying a Matrix
3. Finding Transpose of matrix
4. Adding two matrices
5. Subtraction of two matrices
6. Multiplication of two matrices

1. Addition of Two Matrices
If A and B are two matrices of same order m x n (to be read as m by n matrix) then their
addition is defined by A + B. For example if A is a matrix of order 2×3 and B is a matrix of
same order 2×3 then addition is possible and the resultant matrix will be of order 2×3. If a
matrix A has its order 2×3 and another matrix B has its order 3×2 then addition is not
possible. So before adding any number of matrices we must check that whether each of the
matrices are of same order or not then we need to proceed further.

Algorithm:
Suppose A and B are two matrix arrays of order m x n, and C is another matrix array to store
the addition result. i, j are counters.
Step1: Start
Step2: Read: m and n
Step3: Read: Take inputs for Matrix A[1:m, 1:n] and Matrix B[1:m, 1:n]
Step4: Repeat for i := 1 to m by 1:
              Repeat for j := 1 to n by 1:
                     C[i, j] := A[i, j] + B[i, j]
              [End of inner for loop]
       [End of outer for loop]
Step5: Print: Matrix C
Step6: Exit.

2. Subtraction of Two Matrices
If A and B are two matrices having same order m x n and C be the resultant Matrix then we
can write C = A – B. The order of Matrix C will also be m x n. To perform subtraction, order
of each matrix should be same otherwise subtraction is not possible as it stated above in the
case of Matrix Addition.

Algorithm:
Suppose A and B are two matrix arrays of order m x n, and C is another matrix array to store
the addition result. i, j are counters.
1: Start
2: Read: m and n
3: Read: Take inputs for Matrix A[1:m, 1:n] and Matrix B[1:m, 1:n]
4: Repeat for i := 1 to m by 1:
          Repeat for j := 1 to n by 1:
                C[i, j] := A[i, j] – B[i, j]
          [End of inner for loop]
   [End of outer for loop]
5: Print: Matrix C[1:m, 1:n]
6: Exit.

3. Matrix Multiplication
If A and B are two matrices of order m x n and p x q then their multiplication possible only if
the number of columns in first matrix is equal to the number of rows in second matrix.
Suppose C a matrix where the result of A x B will be stored then the order of C is m x p.

Algorithm:
1. Start
2. Declare variables and initialize necessary variables
3. Enter the element of matrices by row wise using loops
4. Check the number of rows and column of first and second matrices
5. If number of rows of first matrix is equal to the number of columns of second
matrix, go to step 6. Otherwise, print matrix multiplications are not possible and go
to step 3.
6. Multiply the matrices using nested loops.
7. Print the product in matrix form as console output.
8. Stop

Pseudo Code:
Suppose A and B are two matrices and their order are respectively m x n and p x q. i, j and k
are counters. And C to store result.
1. Start.
2. Read: m, n, p and q
3. Read: Inputs for Matrices A[1:m, 1:n] and B[1:p, 1:q].
4. If n ≠ p then:
        Print: Multiplication is not possible.
   Else
   {
        For( i =1 to n by 1)
        {
             For( j =1 to q bt 1)
                    C[i, j] := 0 [Initializing]
                    for( k=1 to n by 1)
                         C[i, j] := C[i, j] + A[i, k] x B[k, j]
         }
    }
6. Display C
7. Exit.

4. Transpose of A Matrix
A transpose of matrix can be formed by turning all the rows of a given matrix into columns
and vice-versa. First read a matrix of size mxn and then find its transpose by just interchanging the rows and
columns i.e. rows become columns and columns become rows.

Algorithm:
Suppose A is a matrix array of order m x n. And B is a matrix array of order n x m to store
result. i and j are two counters.
Step1: Start.
Step2: Read: m and n
Step3: Read: Take inputs for Matrix A[1:m, 1:n].
Step4: If m == n then:
          Repeat for i = 1 to m by 1
             Repeat for j = 1 to n by 1
                B[i, j] = A[j, i]
             [End of for loop]
          [End of for loop]
       Else:
            temp = m
            m = n
            n = temp
        Repeat for i = 1 to m by 1
          Repeat for j = 1 to n by 1
             B[i, j] = A[j, i]
           [End of for loop]
       [End of for loop]
       [End of If structure]
Step5: Print: B[1:m, 1:n]
Step6: Exit

Conclusion:
Thus we have learnt to declare a two dimensional array, read the elements of the array and
print the elements of the array using static method.
1. Addition of matrices
2. Subtraction of matrices
3. Multiplication of matrices
4. Transpose of matrix

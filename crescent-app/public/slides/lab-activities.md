---
layout: title
eyebrow: Course GEE 1101
title: PPS Laboratory Activities
subtitle: 20 Practical Syllabus Experiments
lede: Write, run, and visually trace standard C library applications from your PPS Lab Manual.
---
layout: agenda
eyebrow: Syllabus Index
title: Laboratory Experiments
facts:
  - num: 01-05
    title: Basic Logic & Loops
    desc: Simple interest, quadratic roots, largest of three, calculator, swapping.
  - num: 06-10
    title: Iterations & Arrays
    desc: Factorials, Fibonacci series, primes, reversals, array statistics.
  - num: 11-15
    title: Searches & Matrices
    desc: Linear search, binary search, matrix add/multiply, string length.
  - num: 16-20
    title: Pointers & Structures
    desc: String merge, recursion stack, Fibonacci tree, pointer swaps, employee structure.
---
layout: code
eyebrow: Exercise 01
title: Simple Interest Calculator
lede: Write a C program to compute simple interest based on Principal, Rate, and Time.
code: |
  #include <stdio.h>
  int main() {
      float principal = 10000.0, rate = 5.0, time = 2.0;
      float interest = (principal * rate * time) / 100.0;
      printf("Simple Interest = %f\n", interest);
      return 0;
  }
---
layout: code
eyebrow: Exercise 02
title: Roots of a Quadratic Equation
lede: Evaluate math roots using coefficients (a, b, c) and discriminant testing.
code: |
  #include <stdio.h>
  #include <math.h>
  int main() {
      float a = 1, b = -5, c = 6; // x^2 - 5x + 6 = 0
      float disc = b*b - 4*a*c;
      float r1 = (-b + sqrt(disc)) / (2*a);
      float r2 = (-b - sqrt(disc)) / (2*a);
      printf("Roots are: %f and %f\n", r1, r2);
      return 0;
  }
---
layout: code
eyebrow: Exercise 03
title: Largest of Three Numbers
lede: Identify the largest integer using nested if-else structures.
code: |
  #include <stdio.h>
  int main() {
      int a = 15, b = 45, c = 20;
      if (a >= b && a >= c) printf("Largest is %d\n", a);
      else if (b >= a && b >= c) printf("Largest is %d\n", b);
      else printf("Largest is %d\n", c);
      return 0;
  }
---
layout: code
eyebrow: Exercise 04
title: Switch-Case Arithmetic Calculator
lede: Perform basic calculations using a switch choice block.
code: |
  #include <stdio.h>
  int main() {
      char op = '*';
      int a = 10, b = 5;
      switch(op) {
          case '+': printf("Sum = %d\n", a+b); break;
          case '*': printf("Product = %d\n", a*b); break;
          default: printf("Invalid Operator\n");
      }
      return 0;
  }
---
layout: trace
type: swapping
eyebrow: Exercise 05
title: Value Swapping Simulator
lede: Click step to trace how two variables swap contents using a Temp container.
---
layout: code
eyebrow: Exercise 06
title: Factorial Calculations
lede: Calculate the factorial of a number using entry-controlled while loops.
code: |
  #include <stdio.h>
  int main() {
      int n = 5, fact = 1, i = 1;
      while (i <= n) {
          fact = fact * i;
          i++;
      }
      printf("Factorial of %d = %d\n", n, fact);
      return 0;
  }
---
layout: quiz
eyebrow: Exercise 06 Quiz
question: What is the value of i after exiting the loop for n = 5?
options:
  - text: 5
    correct: false
    feedback: The loop runs while i <= 5. i becomes 6 to exit.
  - text: 6
    correct: true
    feedback: Correct! i is incremented to 6, which fails the test i <= 5, exiting the loop.
  - text: 120
    correct: false
    feedback: 120 is the factorial result, not the variable i.
---
layout: code
eyebrow: Exercise 07
title: Fibonacci Sequence Generation
lede: Generate the first N terms of the Fibonacci sequence.
code: |
  #include <stdio.h>
  int main() {
      int n = 6, t1 = 0, t2 = 1, nextTerm;
      for (int i = 1; i <= n; ++i) {
          printf("%d, ", t1);
          nextTerm = t1 + t2;
          t1 = t2;
          t2 = nextTerm;
      }
      return 0;
  }
---
layout: code
eyebrow: Exercise 08
title: Primality Test Check
lede: Check if a positive integer is prime.
code: |
  #include <stdio.h>
  int main() {
      int n = 29, isPrime = 1;
      for (int i = 2; i <= n/2; ++i) {
          if (n % i == 0) { isPrime = 0; break; }
      }
      if (isPrime) printf("%d is Prime\n", n);
      else printf("%d is Composite\n", n);
      return 0;
  }
---
layout: code
eyebrow: Exercise 09
title: Reverse a Number
lede: Reverse the digits of an integer using modulo divisions.
code: |
  #include <stdio.h>
  int main() {
      int n = 1234, rev = 0, rem;
      while (n != 0) {
          rem = n % 10;
          rev = rev * 10 + rem;
          n /= 10;
      }
      printf("Reversed = %d\n", rev);
      return 0;
  }
---
layout: code
eyebrow: Exercise 10
title: Array Statistics
lede: Calculate the sum and average of elements in a 1D array.
code: |
  #include <stdio.h>
  int main() {
      int arr[5] = {10, 20, 30, 40, 50};
      float sum = 0, avg;
      for(int i=0; i<5; i++) sum += arr[i];
      avg = sum / 5.0;
      printf("Sum = %f, Average = %f\n", sum, avg);
      return 0;
  }
---
layout: trace
type: arrayMath
eyebrow: Exercise 11
title: Array Memory Calculation
lede: Trace how elements are indexed and mapped to physical memory offsets.
---
layout: code
eyebrow: Exercise 12
title: Binary Search algorithm
lede: Search for a target value inside a sorted array using divide-and-conquer logic.
code: |
  #include <stdio.h>
  int main() {
      int arr[5] = {12, 24, 36, 48, 60};
      int target = 48, low = 0, high = 4, mid;
      while (low <= high) {
          mid = (low + high) / 2;
          if (arr[mid] == target) { printf("Found at %d\n", mid); break; }
          else if (arr[mid] < target) low = mid + 1;
          else high = mid - 1;
      }
      return 0;
  }
---
layout: code
eyebrow: Exercise 13
title: Matrix Addition
lede: Add two 2D matrices index-by-index.
code: |
  #include <stdio.h>
  int main() {
      int a[2][2] = {{1,2},{3,4}}, b[2][2] = {{5,6},{7,8}}, c[2][2];
      for(int i=0; i<2; i++) {
          for(int j=0; j<2; j++) {
              c[i][j] = a[i][j] + b[i][j];
              printf("%d ", c[i][j]);
          }
      }
      return 0;
  }
---
layout: code
eyebrow: Exercise 14
title: Matrix Multiplication
lede: Perform row-by-column multiplication of two 2D matrices.
code: |
  #include <stdio.h>
  int main() {
      int a[2][2] = {{1,2},{3,4}}, b[2][2] = {{5,6},{7,8}}, c[2][2] = {0};
      for(int i=0; i<2; i++) {
          for(int j=0; j<2; j++) {
              for(int k=0; k<2; k++) {
                  c[i][j] += a[i][k] * b[k][j];
              }
          }
      }
      return 0;
  }
---
layout: code
eyebrow: Exercise 15
title: String Length Count
lede: Find string length manually by looking for the null character \0.
code: |
  #include <stdio.h>
  int main() {
      char str[] = "Crescent";
      int length = 0;
      while (str[length] != '\0') {
          length++;
      }
      printf("Length = %d\n", length);
      return 0;
  }
---
layout: trace
type: stringTracer
eyebrow: Exercise 15 Trace
title: String Null Terminator Check
lede: Step through the string garland to see where the Null Character exits the length loop.
---
layout: code
eyebrow: Exercise 16
title: String Concatenation
lede: Concatenate two character garlands manually.
code: |
  #include <stdio.h>
  int main() {
      char s1[20] = "Hi ", s2[] = "CSE";
      int i = 0, j = 0;
      while (s1[i] != '\0') i++;
      while (s2[j] != '\0') {
          s1[i] = s2[j];
          i++; j++;
      }
      s1[i] = '\0';
      printf("Result = %s\n", s1);
      return 0;
  }
---
layout: trace
type: recursion
eyebrow: Exercise 17
title: Factorial recursion Stack
lede: Observe recursion stack frames piling up during factorial execution.
---
layout: code
eyebrow: Exercise 18
title: Fibonacci Series recursion
lede: Generate terms recursively.
code: |
  #include <stdio.h>
  int fib(int n) {
      if (n <= 1) return n;
      return fib(n-1) + fib(n-2);
  }
  int main() {
      printf("Fib(5) = %d\n", fib(5));
      return 0;
  }
---
layout: trace
type: pointers
eyebrow: Exercise 19
title: Pointer Swap simulator
lede: Trace pointer references pointing to values in memory address blocks.
---
layout: code
eyebrow: Exercise 20
title: Employee Structure Database
lede: Map employee database records using C structures.
code: |
  #include <stdio.h>
  struct Employee {
      int id;
      char name[20];
      float salary;
  };
  int main() {
      struct Employee emp = {101, "Arun", 75000.0};
      printf("ID: %d, Name: %s, Salary: %f\n", emp.id, emp.name, emp.salary);
      return 0;
  }

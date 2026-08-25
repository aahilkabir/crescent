export const modules = [
  {
    id: 'intro',
    title: 'Module 1: C Fundamentals',
    description: 'Origins, compilers vs interpreters, program structure, and basic operators.',
    slides: [
      {
        type: 'title',
        eyebrow: 'Crescent Institute of Science & Technology · CSE',
        title: 'C Programming',
        subtitle: 'The Language That Built Modern Computing',
        lede: "An introduction to structure, syntax, and the machine underneath — Dennis Ritchie's gift to the operating systems of the world."
      },
      {
        type: 'agenda',
        eyebrow: 'Roadmap',
        title: "What we'll build today",
        facts: [
          { num: '01', title: 'Origins & History', desc: "Dennis Ritchie's Bell Labs breakthrough." },
          { num: '02', title: 'Source → Machine', desc: 'How code becomes binary electrical signals.' },
          { num: '03', title: 'Program Structure', desc: 'The six anatomical sections of C code.' },
          { num: '04', title: 'Vocabulary & Tokens', desc: 'Reserved words, identifiers, and variables.' },
          { num: '05', title: 'Operators', desc: 'Arithmetic, relational, logical, and bitwise logic.' },
          { num: '06', title: 'Terminal I/O', desc: 'Talking to users with printf and scanf.' }
        ]
      },
      {
        type: 'bullets',
        eyebrow: 'Part 01 · Origins & Nature',
        title: 'What is C?',
        lede: 'A structured, third-generation programming language. It is a unique bridge: high-level enough to be human-readable, yet low-level enough to control raw hardware directly.',
        bullets: [
          { bold: 'System Language:', text: 'Used to build OS cores like Unix, Linux, Windows, and MacOS.' },
          { bold: 'Embedded Powerhouse:', text: 'Controls everything from refrigerator chips to space rockets.' },
          { bold: 'Foundation:', text: 'C++, Java, Python, and JavaScript compilers are all written in C.' }
        ]
      },
      {
        type: 'timeline',
        eyebrow: 'Part 01 · Origins & Nature',
        title: 'The 12-Year Ancestry',
        timeline: [
          { yr: '1960', title: 'ALGOL 60', desc: 'The mathematical grand-ancestor of structured code.' },
          { yr: '1963', title: 'CPL', desc: "Cambridge's high-level but complex system experiment." },
          { yr: '1967', title: 'BCPL', desc: 'Basic CPL — stripped down to make compiler building possible.' },
          { yr: '1970', title: 'B', desc: 'Ken Thompson writes a typing-less, byte-oriented version for Unix.' },
          { yr: '1972', title: 'C', desc: 'Dennis Ritchie introduces data types and rewrites Unix completely in C.' }
        ]
      },
      {
        type: 'hero',
        eyebrow: 'Part 02 · Source → Machine',
        title: 'The Catering Analogy',
        lede: 'A Compiler translates the entire code at once before running it.',
        highlight: 'Like hiring a Catering Service: You order the full menu beforehand. They cook the entire feast and deliver it all at once.',
        image: 'samayal_chef.jpg'
      },
      {
        type: 'bullets',
        eyebrow: 'Part 02 · Source → Machine',
        title: 'How Compilers Work',
        lede: 'Compilers act as global code translators.',
        bullets: [
          { bold: 'Whole Pass:', text: 'Reads the entire C source code (.c) in one pass.' },
          { bold: 'Binary Output:', text: 'Generates an independent machine binary executable (.exe / .out).' },
          { bold: 'Execution Speed:', text: 'Pre-compiled code runs blazing fast on the CPU.' },
          { bold: 'Error Handling:', text: 'Reports all compilation errors at once at the very end.' }
        ]
      },
      {
        type: 'hero',
        eyebrow: 'Part 02 · Source → Machine',
        title: 'The Dosa Master Analogy',
        lede: 'An Interpreter reads and executes code line-by-line on the fly.',
        highlight: 'Like a Live Dosa Master: He pours batter, cooks one dosa, serves it, then immediately starts the next one.',
        image: 'dosa_master.jpg'
      },
      {
        type: 'bullets',
        eyebrow: 'Part 02 · Source → Machine',
        title: 'How Interpreters Work',
        lede: 'Interpreters act as on-the-fly execution engines.',
        bullets: [
          { bold: 'Line-by-Line:', text: 'Reads and runs C / scripting code one line at a time.' },
          { bold: 'No Executable:', text: 'Does NOT output an executable binary file.' },
          { bold: 'Execution Speed:', text: 'Slower because conversion happens on-demand during runtime.' },
          { bold: 'Error Handling:', text: 'Stops executing instantly the moment it hits any line with a bug.' }
        ]
      },
      {
        type: 'table',
        eyebrow: 'Part 02 · Source → Machine',
        title: 'Catering vs. Dosa Master',
        headers: ['Metric', 'Compiler (C)', 'Interpreter (Python)'],
        rows: [
          ['Process', 'Translates all code at once', 'Translates line-by-line'],
          ['Output File', 'Generates executable (.exe)', 'No executable created'],
          ['Speed', 'Blazing Fast (Pre-cooked)', 'Slower (Cook-on-demand)'],
          ['Errors', 'Shows all errors at the end', 'Stops at the first error line']
        ]
      },
      {
        type: 'structure',
        eyebrow: 'Part 03 · Anatomy',
        title: 'The 6 Core Sections',
        code: `/* 1. Documentation Section */
#include <stdio.h>    /* 2. Preprocessor Link */
#define TAX 5        /* 3. Definition Section */
int globalScore;     /* 4. Global Declaration */

int main()           /* 5. Main Function Entry */
{
    int localVal = 5;
    printf("Value: %d", localVal);
    return 0;
}
void subProgram()    /* 6. Subprograms Section */
{ }`,
        sections: ['Documentation', 'Preprocessor Link', 'Definitions', 'Global Decl.', 'main() Function', 'Subprograms']
      },
      {
        type: 'hero',
        eyebrow: 'Part 04 · Vocabulary',
        title: 'The Spice Box Analogy',
        lede: 'A Variable is a named storage container in memory.',
        highlight: 'Like an Anjarai Petti (South Indian spice box): Dedicated cups for mustard, cumin, and cardamom. You store specific things in specific cups.',
        image: 'anjarai_petti.jpg'
      },
      {
        type: 'bullets',
        eyebrow: 'Part 04 · Vocabulary',
        title: 'C Variables & Types',
        lede: 'Variables are typed boxes in computer RAM memory.',
        bullets: [
          { bold: 'Type Declarations:', text: "You must declare a variable's data type before storing data." },
          { bold: 'int:', text: 'Whole numbers (e.g. 15, -200).' },
          { bold: 'float:', text: 'Decimal numbers (e.g. 3.14, 9.8).' },
          { bold: 'char:', text: "Single characters inside single quotes (e.g. 'A', '9')." }
        ]
      },
      {
        type: 'hero',
        eyebrow: 'Part 05 · Operators',
        title: 'The Change Analogy',
        lede: 'The Modulo operator (%) returns the remainder of division.',
        highlight: 'Like buying Tea: You buy tea for Rs. 15. You give a Rs. 50 note. Modulo calculates the leftover change (Rs. 5) you get back.',
        image: 'tea_shop_change.jpg'
      },
      {
        type: 'bullets',
        eyebrow: 'Part 05 · Operators',
        title: 'Modulo in C Code',
        lede: 'Modulo math focuses on remainders.',
        bullets: [
          { bold: 'Remainder Math:', text: 'Returns the absolute integer remainder of a division.' },
          { bold: 'Integers Only:', text: 'Must only be used with integers (floats are invalid).' },
          { bold: '50 % 15 = 5:', text: 'Since 15 * 3 = 45, remainder is 5.' },
          { bold: '10 % 3 = 1:', text: 'Since 3 * 3 = 9, remainder is 1.' }
        ]
      },
      {
        type: 'terminal',
        eyebrow: 'Part 06 · Terminal Simulator',
        title: 'scanf() Execution Tracing',
        code: `#include <stdio.h>
int main() {
    int score;
    printf("Enter score: ");
    scanf("%d", &score);
    printf("You passed!\\n");
    return 0;
}`
      }
    ]
  },
  {
    id: 'control',
    title: 'Module 3: Control & Arrays',
    description: 'Decision making, loop structures, 1D/2D arrays, and string manipulations.',
    slides: [
      {
        type: 'title',
        eyebrow: 'Crescent Institute of Science & Technology · CSE',
        title: 'Control Structures',
        subtitle: 'Logic Loops & Arrays in C',
        lede: 'Mastering logic flow, repeat cycles, matrices, and text strings — from building loops to handling multi-dimensional data blocks.'
      },
      {
        type: 'bullets',
        eyebrow: 'Part 01 · Decision Making',
        title: 'if-else: The Helmet Checkpoint',
        lede: 'The if-else statement evaluates a condition. If true, path A is taken; otherwise, path B is taken.',
        bullets: [
          { bold: 'Checkpoint Logic:', text: 'Imagine a traffic police helmet checkpoint.' },
          { bold: 'True (if block):', text: 'Rider wearing helmet → Proceed safely home.' },
          { bold: 'False (else block):', text: 'No helmet → Stop and pay fine of Rs. 1000.' }
        ]
      },
      {
        type: 'hero',
        eyebrow: 'Part 02 · Loops & Iteration',
        title: 'The Wet Grinder Analogy',
        lede: 'A while loop repeats actions while a condition remains True.',
        highlight: 'Like grinding batter: You dump rice inside. As long as it is still coarse, the stone keeps rotating (repeats loop).',
        image: 'wet_grinder.jpg'
      },
      {
        type: 'bullets',
        eyebrow: 'Part 02 · Loops & Iteration',
        title: 'while Loops: Entry-Controlled',
        lede: 'Loops evaluate checking conditions at entry.',
        bullets: [
          { bold: 'Condition Checked First:', text: 'Loop body executes only if the test matches.' },
          { bold: 'Zero executions:', text: 'If the condition starts as False, the loop executes exactly 0 times.' },
          { bold: 'Infinite loops:', text: 'Always ensure the loop variable updates inside the body to avoid lockups.' }
        ]
      },
      {
        type: 'loopTracer',
        eyebrow: 'Part 02 · Interactive Trace',
        title: 'for Loop Variable Tracking',
        code: `for (int i = 1; i <= 3; i++) {
    printf("i is %d\\n", i);
}`
      },
      {
        type: 'arrayMath',
        eyebrow: 'Part 03 · Interactive Address Math',
        title: 'Calculating Seat Addresses',
        lede: "Let's calculate addresses for int J[5] starting at base address 1000 (int = 4 bytes)."
      },
      {
        type: 'hero',
        eyebrow: 'Part 05 · Strings',
        title: 'The Flower Garland Analogy',
        lede: 'A String is a sequence of characters terminated by a null character \\0.',
        highlight: "Like tying a flower garland: Each flower represents a character ('C','o','d','e'). The final knot at the end represents the Null Terminator \\0, which prevents the flowers from falling off.",
        image: 'flower_garland.jpg'
      },
      {
        type: 'bullets',
        eyebrow: 'Part 05 · Strings',
        title: 'Strings in C Code',
        lede: 'Strings are character arrays with an ending terminator.',
        bullets: [
          { bold: 'Char Arrays:', text: 'Declared as character arrays: char name[10];.' },
          { bold: 'Null Terminator:', text: 'Always allocate one extra slot for the null character \\0.' },
          { bold: 'Memory representation:', text: '"CSE" takes 4 bytes in memory: C, S, E, and \\0.' }
        ]
      },
      {
        type: 'stringTracer',
        eyebrow: 'Part 05 · Interactive String Visualizer',
        title: "Null Terminator String End Check",
        lede: 'See how C reads char msg[] = "HI"; in memory, character by character.'
      }
    ]
  },
  {
    id: 'lab',
    title: 'PPS Lab Activities',
    description: '20 practical programming challenges from the syllabus with visual code tracers.',
    slides: [
      {
        type: 'title',
        eyebrow: 'Crescent Institute of Science & Technology · CSE',
        title: 'PPS Laboratory',
        subtitle: '20 Interactive Practical Challenges',
        lede: 'Fulfill all syllabus experiments using guided code compilers and visual simulator animations.'
      },
      {
        type: 'code',
        eyebrow: 'Ex 01 · Terminal I/O',
        title: 'My First C Program',
        lede: 'Objective: Write a C program to display the message "This is my first C Program" on the terminal screen.',
        code: `#include <stdio.h>

int main() 
{
    printf("This is my first C program");
    return 0;
}`
      },
      {
        type: 'accumulator',
        eyebrow: 'Ex 02 · Math Operators',
        title: 'Sum & Average of Three Numbers',
        code: `#include <stdio.h>
int main() {
    int a, b, c, sum;
    float avg;
    printf("Enter three numbers: ");
    scanf("%d %d %d", &a, &b, &c);
    
    sum = a + b + c;
    avg = sum / 3.0; // float division
    
    printf("Sum = %d\\nAvg = %.2f\\n", sum, avg);
    return 0;
}`
      },
      {
        type: 'code',
        eyebrow: 'Ex 03 · Constants',
        title: 'Circle Area & Circumference',
        lede: 'Objective: Write a C program to calculate area and circumference of a circle.',
        code: `#include <stdio.h>
#define PI 3.14159 // Unchangeable constant

int main() {
    int radius;
    float area, circumference;
    
    printf("Enter radius: ");
    scanf("%d", &radius);
    
    area = PI * radius * radius;
    circumference = 2 * PI * radius;
    
    printf("Area = %.2f\\nCircumference = %.2f\\n", area, circumference);
    return 0;
}`
      },
      {
        type: 'code',
        eyebrow: 'Ex 04 · Decision Making',
        title: 'Greatest of Three Numbers',
        lede: 'Objective: Write a C program to input three numbers and display the maximum number.',
        code: `#include <stdio.h>
int main() {
    int num1, num2, num3;
    printf("Enter three integers: ");
    scanf("%d %d %d", &num1, &num2, &num3);
    
    if (num1 >= num2 && num1 >= num3) {
        printf("%d is largest\\n", num1);
    } else if (num2 >= num1 && num2 >= num3) {
        printf("%d is largest\\n", num2);
    } else {
        printf("%d is largest\\n", num3);
    }
    return 0;
}`
      },
      {
        type: 'swapping',
        eyebrow: 'Ex 05 · Variables',
        title: 'Swapping Values of Two Variables',
        lede: 'Interchanging values with Cup Swapping logic.'
      },
      {
        type: 'todo',
        eyebrow: 'Challenge 01 · Practice Task',
        title: 'Swapping Three Variables',
        desc: 'Write a C program to swap the values of three variables (a, b, c) such that a becomes b, b becomes c, and c becomes a.',
        hint: 'Hint: You still need only one temporary storage container (temp = a; a = b; b = c; c = temp;).'
      },
      {
        type: 'code',
        eyebrow: 'Ex 06 · Sizing',
        title: 'Size of Data Types (sizeof)',
        lede: 'Objective: Write a C program to display the size of every data type using the sizeof operator.',
        code: `#include <stdio.h>

int main() {
    printf("char   : %lu bytes\\n", sizeof(char));
    printf("int    : %lu bytes\\n", sizeof(int));
    printf("float  : %lu bytes\\n", sizeof(float));
    printf("double : %lu bytes\\n", sizeof(double));
    printf("pointer: %lu bytes\\n", sizeof(void *));
    return 0;
}`
      },
      {
        type: 'quiz',
        eyebrow: 'Interactive Quiz Card',
        question: 'True or False: A C variable name can start with a digit (for example: int 2roll_num;).',
        options: [
          { text: 'True', correct: false, feedback: '✔ Correct! Variable names must begin with a letter or an underscore.' },
          { text: 'False', correct: true, feedback: '✔ Correct! Variable names cannot begin with digits (e.g. 2var is invalid).' }
        ]
      },
      {
        type: 'ternary',
        eyebrow: 'Ex 07 · Ternary Operator',
        title: 'Voting Eligibility Checker',
        lede: 'Using conditional operator to evaluate eligibility: (age >= 18) ? "Eligible" : "Not".'
      },
      {
        type: 'blank',
        eyebrow: 'Interactive Code Completion',
        title: 'scanf Address Operator',
        lede: 'Complete the line to read keyboard input into the variable score:',
        blankVal: '&score',
        code: `#include <stdio.h>
int main() {
    int score;
    printf("Enter score: ");
    scanf("%d", ______ );
    return 0;
}`
      },
      {
        type: 'code',
        eyebrow: 'Ex 08 · Unary Operators',
        title: 'Prefix & Postfix Operations',
        lede: 'Objective: Write a C program to illustrate the use of unary prefix and postfix increment and decrement operators.',
        code: `#include <stdio.h>
int main() {
    int a = 5, b = 5, c = 5, d = 5;
    a++; // postfix increment (value updated after evaluation)
    ++b; // prefix increment (value updated before evaluation)
    c--; // postfix decrement
    --d; // prefix decrement
    
    printf("a = %d, b = %d, c = %d, d = %d\\n", a, b, c, d);
    return 0;
}`
      },
      {
        type: 'quiz',
        eyebrow: 'Interactive Quiz Card',
        question: 'True or False: y = ++x; and y = x++; yield the exact same value of y.',
        options: [
          { text: 'True', correct: false, feedback: '✔ Correct! ++x increments first, while x++ assigns the original value before adding.' },
          { text: 'False', correct: true, feedback: '✔ Correct! Prefix (++x) increments first, whereas Postfix (x++) assigns first.' }
        ]
      },
      {
        type: 'code',
        eyebrow: 'Ex 09 · Iteration Logic',
        title: 'Prime Number Checker',
        lede: 'Objective: Write a C program to check whether a given number is prime or not.',
        code: `#include <stdio.h>
int main() {
    int n, flag = 0;
    printf("Enter number: ");
    scanf("%d", &n);
    
    for (int i = 2; i <= n/2; i++) {
        if (n % i == 0) {
            flag = 1; // found divider factor
            break;
        }
    }
    if (flag == 0) printf("%d is Prime\\n", n);
    else printf("%d is Not Prime\\n", n);
    return 0;
}`
      },
      {
        type: 'code',
        eyebrow: 'Ex 10 · Decisions',
        title: 'Leap Year Checker',
        lede: 'Objective: Write a C program to check whether the entered year is leap year or not.',
        code: `#include <stdio.h>
int main() {
    int yr;
    printf("Enter year: ");
    scanf("%d", &yr);
    
    if ((yr % 400 == 0) || ((yr % 4 == 0) && (yr % 100 != 0))) {
        printf("%d is a Leap Year\\n", yr);
    } else {
        printf("%d is Not a Leap Year\\n", yr);
    }
    return 0;
}`
      },
      {
        type: 'todo',
        eyebrow: 'Challenge 10 · Practice Task',
        title: 'Divisibility Check',
        desc: 'Write a C program to check whether a user-input number is divisible by both 5 and 11.',
        hint: 'Hint: Use the logical AND operator (num % 5 == 0 && num % 11 == 0).'
      },
      {
        type: 'code',
        eyebrow: 'Ex 11 · Loop Accumulation',
        title: 'Factorial of a Number',
        lede: 'Objective: Write a C program to find the factorial of a number.',
        code: `#include <stdio.h>
int main() {
    int n;
    unsigned long long fact = 1;
    printf("Enter integer: ");
    scanf("%d", &n);
    
    if (n < 0) printf("Negative values invalid.\\n");
    else {
        for (int i = 1; i <= n; i++) {
            fact *= i; // multiply loop
        }
        printf("Factorial of %d = %llu\\n", n, fact);
    }
    return 0;
}`
      },
      {
        type: 'code',
        eyebrow: 'Ex 12 · Modulo & Loops',
        title: 'Armstrong Number Checker',
        lede: 'Objective: Write a C program to check number is Armstrong or not.',
        code: `#include <stdio.h>
int main() {
    int num, originalNum, remainder, result = 0;
    printf("Enter 3-digit integer: ");
    scanf("%d", &num);
    
    originalNum = num;
    while (originalNum != 0) {
        remainder = originalNum % 10; // get last digit
        result += remainder * remainder * remainder; // sum cube
        originalNum /= 10; // remove last digit
    }
    if (result == num) printf("%d is Armstrong\\n", num);
    else printf("%d is Not Armstrong\\n", num);
    return 0;
}`
      },
      {
        type: 'code',
        eyebrow: 'Ex 13 · Multi-Way Decision',
        title: 'Positive, Negative, or Zero',
        lede: 'Objective: Write a C program to check whether a number is positive, negative or zero using switch case.',
        code: `#include <stdio.h>
int main() {
    int num;
    printf("Enter number: ");
    scanf("%d", &num);
    
    switch (num > 0) {
        case 1: printf("%d is Positive\\n", num); break;
        case 0:
            switch (num < 0) {
                case 1: printf("%d is Negative\\n", num); break;
                case 0: printf("%d is Zero\\n", num); break;
            }
            break;
    }
    return 0;
}`
      },
      {
        type: 'code',
        eyebrow: 'Ex 14 · 2D Arrays',
        title: 'Matrix Addition (2D Arrays)',
        lede: 'Objective: Write a C program to calculate the sum of all elements in a matrix (2D array).',
        code: `#include <stdio.h>
int main() {
    int r=2, c=2, a[2][2]={{1,2},{3,4}}, b[2][2]={{5,6},{7,8}}, sum[2][2], i, j;
    
    for (i = 0; i < r; ++i)
        for (j = 0; j < c; ++j) {
            sum[i][j] = a[i][j] + b[i][j]; // element sum
        }
    printf("Sum matrix:\\n");
    for (i = 0; i < r; ++i) {
        for (j = 0; j < c; ++j) {
            printf("%d   ", sum[i][j]);
        }
        printf("\\n");
    }
    return 0;
}`
      },
      {
        type: 'todo',
        eyebrow: 'Challenge 14 · Practice Task',
        title: 'Matrix Transpose',
        desc: 'Write a C program to calculate and display the transpose of a 2x2 matrix.',
        hint: 'Hint: Swapping row and column coordinates: transpose[c][r] = original[r][c].'
      },
      {
        type: 'code',
        eyebrow: 'Ex 15 · Modularity',
        title: 'Arithmetic Operations via Functions',
        lede: 'Objective: Write a C program to add, subtract, multiply and divide two integers using user defined type function with return type.',
        code: `#include <stdio.h>

int addition(int a, int b) { return a + b; }
int subtract(int a, int b) { return a - b; }
int multiply(int a, int b) { return a * b; }
float division(float a, float b) { return a / b; }

int main() {
    int x = 8, y = 3;
    printf("Add: %d\\n", addition(x, y));
    printf("Sub: %d\\n", subtract(x, y));
    printf("Mul: %d\\n", multiply(x, y));
    printf("Div: %f\\n", division(x, y));
    return 0;
}`
      },
      {
        type: 'blank',
        eyebrow: 'Interactive Code Completion',
        title: 'Function Return Types',
        lede: 'Define a function that multiplies two integers and returns the integer result:',
        blankVal: 'int',
        code: `#include <stdio.h>

______ multiply(int a, int b) 
{
    return a * b;
}`
      },
      {
        type: 'recursion',
        eyebrow: 'Ex 16 · Recursion',
        title: 'Sum of Digits (Recursive Stack)',
        lede: 'Objective: Write a C program to find sum of digits of the number using Recursive Function.',
        code: `#include <stdio.h>
int sumOfDigits(int n) {
    if (n == 0) return 0; // base case
    return (n % 10) + sumOfDigits(n / 10);
}
int main() {
    int num = 123;
    printf("Sum = %d\\n", sumOfDigits(num));
    return 0;
}`
      },
      {
        type: 'code',
        eyebrow: 'Ex 17 · Structures',
        title: 'Student Record Structure',
        lede: 'Objective: Write a C Program to Calculate Total and Percentage marks of a student using structure.',
        code: `#include <stdio.h>
struct Student {
    char name[50];
    int score;
    float pct;
};
int main() {
    struct Student s = {"Arun", 450, 90.0};
    printf("Name: %s\\nScore: %d\\nPct: %.2f%%\\n", s.name, s.score, s.pct);
    return 0;
}`
      },
      {
        type: 'code',
        eyebrow: 'Ex 18 · Unions',
        title: 'Union Memory Sharing',
        lede: 'Objective: Write a C program to declare and initialize a union.',
        code: `#include <stdio.h>
union Data {
    int i;
    float f;
};
int main() {
    union Data d;
    d.i = 10;
    d.f = 220.5; // overwrites d.i shared memory!
    printf("Shared space overwrite: d.i = %d, d.f = %f\\n", d.i, d.f);
    return 0;
}`
      },
      {
        type: 'quiz',
        eyebrow: 'Interactive Quiz Card',
        question: 'True or False: A union allocates separate memory blocks for all its members simultaneously.',
        options: [
          { text: 'True', correct: false, feedback: '✔ Correct! Unions share the same memory space to optimize sizing.' },
          { text: 'False', correct: true, feedback: '✔ Correct! Unlike structs, unions allocate memory only for the largest member, sharing space.' }
        ]
      },
      {
        type: 'pointers',
        eyebrow: 'Ex 19 · Pointers',
        title: 'Array Traversal via Pointers',
        lede: 'Objective: Write a C program to input and print array elements using pointer.',
        code: `#include <stdio.h>
int main() {
    int arr[3] = {10, 20, 30};
    int *ptr = arr; // ptr points to arr[0]
    
    for (int i = 0; i < 3; i++) {
        printf("Addr: %p, Val: %d\\n", (ptr+i), *(ptr+i));
    }
    return 0;
}`
      },
      {
        type: 'blank',
        eyebrow: 'Interactive Code Completion',
        title: 'Pointer Dereferencing',
        lede: 'Complete the line to display the integer value pointed to by ptr:',
        blankVal: '*ptr',
        code: `#include <stdio.h>
int main() {
    int val = 99;
    int *ptr = &val;
    printf("Value is %d\\n", ______ );
    return 0;
}`
      },
      {
        type: 'code',
        eyebrow: 'Ex 20 · File Handling',
        title: 'File Write Operations (emp.rec)',
        lede: 'Objective: Write a program to create a file called emp.rec and store information about a person, in terms of his name, age and salary.',
        code: `#include <stdio.h>
int main() {
    FILE *fptr = fopen("emp.rec", "w");
    if (fptr == NULL) return 1;
    
    char name[] = "Raj"; int age = 28; float sal = 75000;
    fprintf(fptr, "Name: %s, Age: %d, Salary: %.2f\\n", name, age, sal);
    
    fclose(fptr); // close file
    printf("Employee records saved successfully in emp.rec.\\n");
    return 0;
}`
      }
    ]
  }
];

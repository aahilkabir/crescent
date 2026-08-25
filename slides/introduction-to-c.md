---
layout: title
eyebrow: Course GEE 1101 · CSE
title: Introduction to C
subtitle: Programming for Problem Solving
lede: Master C programming logic, compilation pipelines, variables, operators, and terminal inputs using visual simulators and interactive plays.
---
layout: agenda
eyebrow: Part 01 · Roadmap
title: Agenda & Syllabus
facts:
  - num: 01
    title: Origins & Legacy
    desc: History of Dennis Ritchie, Bell Labs Unix development, and Core traits.
  - num: 02
    title: Source → Machine
    desc: Transducers, binary machine code, Compilers vs. Interpreters.
  - num: 03
    title: Anatomy of a C Program
    desc: Structural sections, preprocessor headers, main() entry, and comments.
  - num: 04
    title: C Vocabulary & Storage
    desc: Character sets, keywords, constants, and variables in RAM storage.
  - num: 05
    title: CPU Logic Operators
    desc: Arithmetic, relational, logical, conditional, and bitwise logic.
  - num: 06
    title: Talking to the User
    desc: Standard formatted printf/scanf and unformatted gets/puts helpers.
---
layout: title
eyebrow: Course Section 1
title: Part 01
subtitle: Origins & Nature of C
---
layout: study
eyebrow: Part 01 · Origins
title: What is C?
lede: A structured, high-level, general-purpose programming language.
C acts as a unique bridge in software:
* **High-Level enough** to be easily readable and writeable by human developers using standard English words.
* **Low-Level enough** to manage physical computer registers, map memory addresses directly, and write operating system cores.

#### Key Applications:
- **Operating Systems**: Unix, Linux, Windows, and MacOS kernels.
- **Embedded Hardware**: Microcontroller chips in automotive, aviation, and IoT devices.
- **Virtual Machines & Compilers**: Python, Java, JavaScript engines are compiled with C.
---
layout: hero
eyebrow: Part 01 · Origins & Legacy
title: Dennis Ritchie & Unix
lede: In 1972, at AT&T Bell Labs, computer scientist Dennis Ritchie designed C to rewrite the Unix operating system.
highlight: "\"C is quirky, flawed, and an enormous success.\""
image: retro_computer_lab.jpg
---
layout: study
eyebrow: Part 01 · Heritage
title: The 12-Year Ancestry
The lineage that led to the creation of C:
1. **ALGOL 60** (1960): The mathematical ancestor that introduced block-structured logic.
2. **CPL** (1963): Combined high-level logic with system control, but was too complex to use.
3. **BCPL** (1967): "Basic CPL" — stripped away complexity to write compilers.
4. **B** (1970): Ken Thompson wrote a typing-less, byte-addressable version for Unix.
5. **C** (1972): Dennis Ritchie added data types (int, char, float) and compiled it to machine code.
---
layout: bullets
eyebrow: Part 01 · Core Traits
title: Core Strengths of C
bullets:
  - bold: Direct memory access:
    text: Manipulate hardware RAM addresses using Pointers.
  - bold: High Performance:
    text: Compiles directly to CPU machine code with no garbage collector lag.
  - bold: Portability:
    text: C code written for one computer can compile on other processors with minimal edits.
  - bold: Structured Logic:
    text: Code is grouped into functions and modules, making debugging simple.
---
layout: title
eyebrow: Course Section 2
title: Part 02
subtitle: Source Code to Machine Code
---
layout: study
eyebrow: Part 02 · Translators
title: What is Programming?
Computers are electrical devices. At the hardware layer, microprocessors do not understand English or letters.
- **Voltage Gates**: CPUs only process electrical signals: High voltage representing a **1** and Low voltage representing a **0**.
- **Translator Role**: A programming language acts as a translator. It lets you write logic commands in human terms and compiles them to CPU-executable binary.
---
layout: hero
eyebrow: Part 02 · Source → Machine
title: The Language of Electricity
lede: Microprocessors represent all calculations, images, and characters as massive streams of binary numbers.
highlight: "C acts as a compiler bridge, translating your readable logic commands into this raw electrical binary language."
image: binary_matrix.jpg
---
layout: bullets
eyebrow: Part 02 · Translators
title: Machine Language (Binary)
bullets:
  - bold: Direct CPU Code:
    text: Raw binary sequences like `10110000 01100001` read directly by memory controllers.
  - bold: Extreme Complexity:
    text: Impossible for humans to write, maintain, or debug without error.
  - bold: Hardware Bound:
    text: Machine binary compiled for an Intel CPU cannot run on an ARM phone chip.
---
layout: hero
eyebrow: Part 02 · Compilers
title: The Catering Analogy
lede: A Compiler translates the entire source code (.c) into machine binary (.exe) all at once before running it.
highlight: "Analogy: Like hiring a Catering Service. You order the full menu beforehand. They cook the entire feast and deliver it all at once."
image: samayal_chef.jpg
---
layout: bullets
eyebrow: Part 02 · Compilers
title: How Compilers Work
bullets:
  - bold: Whole Pass Translation:
    text: Reads the entire source file from top to bottom, checking syntax.
  - bold: Output Executable:
    text: Generates an independent machine binary file (.exe or .out).
  - bold: Execution Speed:
    text: Runs at full native hardware speeds since no translations happen during run.
  - bold: Error Log:
    text: Reports all warnings and errors at the very end after scanning the file.
---
layout: hero
eyebrow: Part 02 · Interpreters
title: The Dosa Master Analogy
lede: An Interpreter translates and executes scripting code line-by-line on the fly during runtime.
highlight: "Analogy: Like a Live Dosa Master. He pours batter, cooks one dosa, serves it, then immediately starts the next one."
image: dosa_master.jpg
---
layout: bullets
eyebrow: Part 02 · Interpreters
title: How Interpreters Work
bullets:
  - bold: On-Demand Execution:
    text: Translates and runs scripting code lines one at a time.
  - bold: No Binary File:
    text: Does not output an executable file; requires source files to run.
  - bold: Performance Lag:
    text: Execution is slower because translation overhead happens during run.
  - bold: Instant Crash:
    text: Stops execution immediately on the first line containing a bug.
---
layout: table
eyebrow: Part 02 · Comparison
title: Compiler vs Interpreter
headers:
  - Feature
  - Compiler (C)
  - Interpreter (Python)
rows:
  - [Process, Translates all code at once, Translates line-by-line]
  - [Output File, Generates executable (.exe), No executable created]
  - [Speed, Blazing Fast (Pre-cooked), Slower (Cook-on-demand)]
  - [Errors, Shows all errors at the end, Stops at the first error line]
---
layout: title
eyebrow: Course Section 3
title: Part 03
subtitle: Anatomy of a C Program
---
layout: structure
eyebrow: Part 03 · Structure
title: The 6 Core Sections
code: |
  /* 1. Documentation Section */
  #include <stdio.h>    /* 2. Link / Preprocessor */
  #define TAX 5        /* 3. Definition Section */
  int globalScore;     /* 4. Global Declaration */

  int main()           /* 5. Main Function Entry */
  {
      int localVal = 5;
      printf("Value: %d", localVal);
      return 0;
  }
  void subProgram()    /* 6. Subprogram Section */
  { }
sections:
  - Documentation Section (Comments describing program)
  - Link Section (Preprocessor directives like #include)
  - Definition Section (Constants defined via #define)
  - Global Declarations (Variables visible to all functions)
  - Main Function (Where CPU execution starts)
  - Subprograms (Helper functions called by main)
---
layout: hero
eyebrow: Part 03 · Preprocessor
title: Preprocessor: Importing Helpers
lede: Writing standard inputs/outputs from scratch is too hard. We need pre-built standard helper code.
highlight: "Analogy: Importing side-dishes. Instead of making Sambar or Chutney in your home kitchen, you just order a parcel from a nearby mess."
image: samayal_chef.jpg
---
layout: bullets
eyebrow: Part 03 · Preprocessor
title: Header Files in C
bullets:
  - bold: #include Directive:
    text: Tells the preprocessor to load library headers (like stdio.h).
  - bold: stdio.h:
    text: Standard Input Output library containing printf() and scanf() commands.
  - bold: Linker Phase:
    text: Merges imported helper libraries with your compiled code to make an executable.
---
layout: study
eyebrow: Part 03 · Main Entry
title: main() : The Starting Point
In C, the main function is the anchor starting point.
- **Thalaivar Entry (The anchor starting point)**: When the operating system launches your program, the CPU immediately jumps to the first line of `main()`. Execution always starts here, regardless of where the function is positioned in the file.
- **Return Type**: `int main()` returns an integer value to the operating system at exit.
- **Return Code 0**: Returning `0` tells the OS that the program ran successfully without any crashes.
---
layout: code
eyebrow: Part 03 · Syntax
title: A Simple C Program
lede: A basic program that prints text to the terminal window.
code: |
  #include <stdio.h>

  int main() 
  {
      printf("Welcome to Crescent!\n");
      return 0;
  }
---
layout: study
eyebrow: Part 03 · Pipeline
title: The Compilation Journey
When you run a C file, it passes through four distinct phases:
1. **Preprocessor**: Expands header files, replaces constants, and strips comments. Output: `.i` file.
2. **Compiler**: Translates C syntax into raw CPU Assembly instructions. Output: `.s` file.
3. **Assembler**: Translates assembly instructions into object machine code. Output: `.obj` / `.o` file.
4. **Linker**: Combines your object file with standard libraries (like stdio) to output the executable binary. Output: `.exe` / `.out` file.
---
layout: title
eyebrow: Course Section 4
title: Part 04
subtitle: C Vocabulary & Storage
---
layout: bullets
eyebrow: Part 04 · Syntax Rules
title: C Character Set
bullets:
  - bold: Alphabets:
    text: Uppercase A-Z and Lowercase a-z characters.
  - bold: Digits:
    text: Numbers 0 through 9.
  - bold: Special Characters:
    text: Arithmetic symbols (+, -, *, /), punctuation (, , ; , .), and bracket braces ({, }, [, ]).
  - bold: White Spaces:
    text: Spaces, tabs, and newline carriage returns (ignored by the compiler compiler).
---
layout: study
eyebrow: Part 04 · Comments
title: Writing Comments in C
Comments are notes written for humans that are completely ignored by the compiler.
* **Single-Line Comments**: Begin with `//` and extend to the end of the line.
  ```c
  int score = 100; // Stores student test score
  ```
* **Multi-Line Comments**: Enclosed between `/*` and `*/`. Useful for block descriptions or documentation.
  ```c
  /* 
     This function calculates the simple interest
     based on principal, rate, and time in years.
  */
  ```
---
layout: hero
eyebrow: Part 04 · Vocabulary
title: Code Building Blocks
lede: A C program is like a structure built out of lego bricks. The compiler cannot understand your sentences all at once.
highlight: "Instead, it scans your code and breaks it down into individual, indivisible items called Tokens."
image: code_tokens.jpg
---
layout: agenda
eyebrow: Part 04 · Vocabulary
title: The 6 Classes of Tokens
facts:
  - num: 01
    title: Keywords
    desc: Reserved compiler words like int, float, return.
  - num: 02
    title: Identifiers
    desc: Named custom variables and functions like main, sum, name.
  - num: 03
    title: Constants
    desc: Fixed data values like 100, 3.14, 'A'.
  - num: 04
    title: Strings
    desc: Character arrays enclosed in double quotes.
  - num: 05
    title: Special Symbols
    desc: Braces and statement terminators like ;, {}, [].
  - num: 06
    title: Operators
    desc: Arithmetic and logic symbols like +, -, *, /, %.
---
layout: table
eyebrow: Part 04 · Vocabulary
title: Breaking Down a Statement
headers:
  - Token Item
  - Token Classification
rows:
  - [if, Keyword]
  - [( ), Special symbols]
  - [salary, Identifier (Variable name)]
  - [>=, Comparison Operator]
  - [50000, Numeric Constant]
---
layout: study
eyebrow: Part 04 · Keywords
title: C Keywords
Keywords are reserved words that have predefined meanings inside the C compiler.
- **Strictly Reserved**: You cannot use keywords as custom variable names (e.g. you cannot declare `int float;`).
- **Standard Count**: C89 contains 32 standard keywords:
  ```c
  auto, break, case, char, const, continue, default, do,
  double, else, enum, extern, float, for, goto, if,
  int, long, register, return, short, signed, sizeof, static,
  struct, switch, typedef, union, unsigned, void, volatile, while
  ```
---
layout: hero
eyebrow: Part 04 · Storage
title: The Spice Box Analogy
lede: A Variable is a named storage container in computer memory (RAM) where you store active program data.
highlight: "Analogy: Anjarai Petti (South Indian spice box). Dedicated compartments for mustard, cumin, and cardamom. You store specific items in specific cups."
image: anjarai_petti.jpg
---
layout: trace
type: swapping
eyebrow: Part 04 · Swapping
title: Value Swapping Simulator
lede: Click step to trace how two variables swap contents using a Temp container.
---
layout: bullets
eyebrow: Part 04 · Variable Names
title: Variable Naming Rules
bullets:
  - bold: Alphabetic Start:
    text: Must begin with a letter (a-z, A-Z) or an underscore (_).
  - bold: No Special Symbols:
    text: Cannot contain spaces or punctuation (e.g., `student age` or `sum$` are invalid).
  - bold: Case Sensitive:
    text: `score`, `Score`, and `SCORE` are three completely different variables in RAM.
  - bold: No Keywords:
    text: Reserved words cannot be used as variable names.
---
layout: study
eyebrow: Part 04 · Constants
title: C Constants
Constants are variables whose values cannot be modified during program execution.
* **Literal Constants**: Direct values typed in code, such as `42` (integer), `3.14` (float), `'A'` (character), or `"Crescent"` (string).
* **const Keyword**: Declares a variable as read-only.
  ```c
  const float PI = 3.14159;
  ```
* **#define preprocessor**: Defines symbolic constants.
  ```c
  #define LIMIT 100
  ```
---
layout: title
eyebrow: Course Section 5
title: Part 05
subtitle: CPU Logic Operators
---
layout: study
eyebrow: Part 05 · Operators
title: C Operators Overview
An operator is a symbol that tells the compiler to perform mathematical or logical manipulations on data variables.
- **Arithmetic**: Math operations (+, -, *, /, %).
- **Relational**: Comparison checks (>, <, >=, <=, ==, !=).
- **Logical**: Boolean evaluations (&&, ||, !).
- **Bitwise**: Low-level bit manipulations (&, |, ^, ~, <<, >>).
- **Conditional**: Ternary decision gate (? :).
- **Increment/Decrement**: Scaling values by 1 (++, --).
---
layout: study
eyebrow: Part 05 · Math
title: Arithmetic Operators
Standard math symbols used to compute arithmetic:
* `+` Addition: `a + b`
* `-` Subtraction: `a - b`
* `*` Multiplication: `a * b`
* `/` Division: `a / b` (Integer division truncates decimals: `5 / 2 = 2`).
* `%` Modulo: Calculates integer division remainder (`5 % 2 = 1`).
---
layout: hero
eyebrow: Part 05 · Modulo
title: The Change Analogy
lede: The Modulo operator (%) calculates the remainder leftover after an integer division.
highlight: "Analogy: Leftover tea change. You buy tea for Rs. 15. You hand over a Rs. 50 note. Modulo calculates the leftover change (Rs. 5) you get back."
image: tea_shop_change.jpg
---
layout: study
eyebrow: Part 05 · Comparisons
title: Relational Operators
Used to compare two values, returning True (1) or False (0):
* `>` Greater than: `5 > 3` is True (1)
* `<` Less than: `5 < 3` is False (0)
* `==` Equal check: `a == b` (checks if values match)
* `!=` Not Equal check: `a != b` (checks if values differ)
* `>=` Greater than or equal: `score >= 50`
* `<=` Less than or equal: `cost <= 100`
---
layout: study
eyebrow: Part 05 · Logic
title: Logical Operators
Used to combine multiple condition gates:
* `&&` Logical AND: Returns True only if **both** inputs are True (`age >= 18 && hasID == 1`).
* `||` Logical OR: Returns True if **at least one** input is True (`marks > 90 || sportsQuota == 1`).
* `!` Logical NOT: Inverts the boolean value (`!1` becomes 0).
---
layout: study
eyebrow: Part 05 · Increments
title: Increment & Decrement
C shortcuts to scale integer variables by 1:
- **Prefix (++x)**: Increments the variable first, then evaluates it in the statement.
- **Postfix (x++)**: Evaluates the variable in the statement first, then increments it in memory.
```c
int a = 5;
int b = a++; // b gets 5, then a becomes 6
int c = ++a; // a becomes 7, then c gets 7
```
---
layout: trace
type: ternary
eyebrow: Part 05 · Ternary
title: Ternary Voting Gate Simulator
lede: Adjust the age slider to trace how the ternary operator (? :) routes values.
---
layout: hero
eyebrow: Part 05 · Operators
title: Modifying Bits Directly
lede: Variables are stored in memory as binary bits. Bitwise Operators let you interact with and manipulate these individual bits directly.
highlight: "Think of a variable as a row of light switches. Operators like Shift (<<, >>) slide the switches left or right, instantly scaling values."
image: circuit_board.jpg
---
layout: table
eyebrow: Part 05 · Operators
title: Bitwise Operations
headers:
  - Operator
  - Meaning
  - Example (a=5, b=3)
  - Result
rows:
  - [&, Bitwise AND, 5 & 3 (0101 & 0011), 0001 (1)]
  - [|, Bitwise OR, 5 | 3 (0101 | 0011), 0111 (7)]
  - [^, Bitwise XOR, 5 ^ 3 (0101 ^ 0011), 0110 (6)]
  - [<<, Left Shift, 5 << 1 (0101 << 1), 1010 (10)]
  - [>>, Right Shift, 5 >> 1 (0101 >> 1), 0010 (2)]
---
layout: title
eyebrow: Course Section 6
title: Part 06
subtitle: Talking to the User
---
layout: bullets
eyebrow: Part 06 · Terminal I/O
title: Formatted vs. Unformatted I/O
bullets:
  - bold: Formatted I/O:
    text: Uses format specifiers to read/write specific data types (`printf`, `scanf`).
  - bold: Unformatted I/O:
    text: Reads/writes raw character characters directly without format conversion (`getchar`, `putchar`, `gets`, `puts`).
---
layout: study
eyebrow: Part 06 · Output
title: printf() : Formatted Output
Prints text and variables to the screen using format specifiers:
- `%d` / `%i`: Integer values
- `%f`: Float/Decimal values
- `%c`: Single character values
- `%s`: Character array strings
- `\n`: Escape sequence to start a new line
```c
int age = 20;
printf("I am %d years old.\n", age);
```
---
layout: study
eyebrow: Part 06 · Input
title: scanf() : Formatted Input
Reads data input from the user keyboard.
- **Address operator (&)**: You must prepend the variable name with `&` to tell scanf the hardware memory address where the typed value should be stored!
```c
int age;
printf("Enter age: ");
scanf("%d", &age); // Stores input in RAM address of variable 'age'
```
---
layout: study
eyebrow: Part 06 · Unformatted I/O
title: gets() & puts() : String Helpers
Specialized functions to read and write whole sentences of text.
* **gets() (Sentence Input)**: Reads line inputs containing white spaces (unlike `scanf` which stops at the first space).
  ```c
  char name[50];
  gets(name);
  ```
* **puts() (Sentence Output)**: Prints a string array to the screen and automatically appends a new line.
  ```c
  char msg[] = "Welcome to C";
  puts(msg);
  ```

> [!WARNING]
> `gets()` has no array bounds check, causing dangerous **Buffer Overflows**. Modern C compilers throw build warnings for it. Prefer `fgets(name, 50, stdin)` in secure code!
---
layout: trace
type: accumulator
eyebrow: Extra Practice · Sum
title: Sum Accumulator Simulator
lede: Observe how a single variable tallies values step-by-step, mimicking a piggy bank.
code: |
  int sum = 0;
  sum = sum + 10;
  sum = sum + 20;
  sum = sum + 15;
---
layout: quiz
eyebrow: Quiz Time
question: What is the output of the C expression 14 % 5?
options:
  - text: 2.8
    correct: false
    feedback: Modulo only returns integer remainders.
  - text: 2
    correct: false
    feedback: 2 is the quotient (14 / 5), not the remainder.
  - text: 4
    correct: true
    feedback: Correct! 5 * 2 = 10, remainder is 4.
  - text: 0
    correct: false
    feedback: 14 is not perfectly divisible by 5.
---
layout: blank
eyebrow: Syntax Exercise
title: Semicolon Syntax
lede: Click the blank space in the code below to insert the correct statement terminator.
code: |
  #include <stdio.h>
  int main() 
  {
      int salary = 50000______
      printf("Salary is %d", salary);
      return 0;
  }
blankVal: ";"
---
layout: todo
eyebrow: Practice Exercise
title: Write your first C program
desc: Write a program that declares an integer variable, assigns it the value 42, and displays it on the screen.
hint: Use `int score = 42;` and print it using `printf("Score: %d", score);` inside main().

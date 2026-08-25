---
layout: title
eyebrow: Course GEE 1101
title: Introduction to C
subtitle: Programming for Problem Solving
lede: Master the logic of computing, compilation cycles, variables, memory, and C syntax using visual simulators.
---
layout: agenda
eyebrow: Part 01 · Overview
title: Agenda & Syllabus
facts:
  - num: 01
    title: Origins of C
    desc: History, legacy, and Dennis Ritchie's Unix blueprint.
  - num: 02
    title: Compilation Cycle
    desc: How compilers and interpreters translate source to machine binary.
  - num: 03
    title: Anatomy of a C Program
    desc: Header imports, main function, comments, and structure.
  - num: 04
    title: Variables & Constants
    desc: Data types, storage boxes in RAM, and memory addresses.
---
layout: hero
eyebrow: Part 01 · History
title: Dennis Ritchie & C
lede: In 1972, Dennis Ritchie at Bell Labs created C to build the Unix operating system. Today, C powers almost all modern operating systems, hardware drivers, and databases.
highlight: "Dennis Ritchie's quote: 'C is quirky, flawed, and an enormous success.'"
image: samayal_chef.jpg
---
layout: bullets
eyebrow: Part 01 · Legacy
title: Why Learn C?
bullets:
  - bold: Mother of Languages:
    text: C forms the syntax foundation for C++, Java, C#, and JavaScript.
  - bold: Hardware Control:
    text: Direct RAM memory access via pointers and system registers.
  - bold: High Performance:
    text: Runs close to assembly speed with zero interpreter overhead.
---
layout: hero
eyebrow: Part 02 · Source → Machine
title: The Catering Analogy
lede: A Compiler translates the entire source code (.c) into machine binary (.exe) all at once before running it.
highlight: "Analogy: Like hiring a Catering Service. You order the full menu beforehand. They cook the entire feast and deliver it all at once."
image: samayal_chef.jpg
---
layout: bullets
eyebrow: Part 02 · Source → Machine
title: How Compilers Work
bullets:
  - bold: One-Pass Translation:
    text: Reads the entire source code file (.c) from top to bottom.
  - bold: Output File:
    text: Generates an independent machine binary executable file (.exe / .out).
  - bold: Execution Speed:
    text: Pre-compiled code runs blazing fast directly on the CPU.
  - bold: Error Reporting:
    text: Reports all errors at once at the very end.
---
layout: hero
eyebrow: Part 02 · Source → Machine
title: The Dosa Master Analogy
lede: An Interpreter reads and executes code line-by-line on the fly during runtime.
highlight: "Analogy: Like a Live Dosa Master. He pours batter, cooks one dosa, serves it, then immediately starts the next one."
image: dosa_master.jpg
---
layout: bullets
eyebrow: Part 02 · Source → Machine
title: How Interpreters Work
bullets:
  - bold: On-Demand Execution:
    text: Translates and runs scripting code one line at a time.
  - bold: No Binary File:
    text: Does not output an executable file; requires source code to run.
  - bold: Runtime Overhead:
    text: Slower execution because translation happens dynamically during run.
  - bold: Instant Termination:
    text: Stops execution immediately on the first line containing a bug.
---
layout: table
eyebrow: Part 02 · Comparison
title: Compiler vs Interpreter
headers:
  - Feature
  - Compiler
  - Interpreter
rows:
  - [Output File, Generates executable (.exe), No executable created]
  - [Speed, Blazing Fast (Pre-cooked), Slower (Cook-on-demand)]
  - [Errors, Shows all errors at the end, Stops at the first error line]
---
layout: structure
eyebrow: Part 03 · Anatomy
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
  - Documentation (Comments describing project)
  - Preprocessor Link (Importing headers like stdio.h)
  - Definitions (Constants defined via #define)
  - Global Declarations (Variables visible to all functions)
  - Main Function Entry (Where CPU execution starts)
  - Subprograms (User defined helper functions)
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
  - bold: #include directive:
    text: Imports ready-made library definitions (like stdio.h).
  - bold: stdio.h:
    text: Standard Input Output header containing printf() and scanf() commands.
  - bold: Linker Phase:
    text: Merges imported helper libraries with your compiled code to make an executable.
---
layout: hero
eyebrow: Part 04 · Variables
title: The Spice Box Analogy
lede: A Variable is a named storage container in computer memory (RAM).
highlight: "Analogy: Like an Anjarai Petti (South Indian spice box). Dedicated compartments for mustard, cumin, and cardamom. You store specific items in specific cups."
image: anjarai_petti.jpg
---
layout: trace
type: swapping
eyebrow: Part 04 · Swapping
title: Swapping Values Simulator
lede: Click Step to trace how variables swap values in RAM using a temporary helper storage container (Temp).
---
layout: trace
type: accumulator
eyebrow: Part 04 · Accumulator
title: Sum Accumulator Simulator
lede: Observe how a single variable tallies values step-by-step, mimicking a piggy bank.
code: |
  int sum = 0;
  sum = sum + 10;
  sum = sum + 20;
  sum = sum + 15;
---
layout: hero
eyebrow: Part 05 · Operators
title: The Change Analogy
lede: The Modulo operator (%) calculates the remainder of an integer division.
highlight: "Analogy: Leftover tea change. You buy tea for Rs. 15. You hand over a Rs. 50 note. Modulo calculates the leftover change (Rs. 5) you get back."
image: tea_shop_change.jpg
---
layout: quiz
eyebrow: Part 05 · Operators Quiz
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
eyebrow: Part 05 · Syntax Exercise
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
eyebrow: Part 06 · Exercise
title: Write your first C program
desc: Write a program that declares an integer variable, assigns it the value 42, and displays it on the screen.
hint: Use `int score = 42;` and print it using `printf("Score: %d", score);` inside main().

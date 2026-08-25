---
layout: title
eyebrow: Course GEE 1101
title: Control Structures & Arrays
subtitle: Module 3 Slide Deck
lede: Master conditional gates, loops, multi-value arrays, and character garland string structures.
---
layout: agenda
eyebrow: Part 01 · Overview
title: Agenda
facts:
  - num: 01
    title: Decision Gates
    desc: if-else conditions and ternary gates.
  - num: 02
    title: Loop Structures
    desc: while loops and iterative calculations.
  - num: 03
    title: Array Storage
    desc: Storing multiple values under a single name in RAM.
  - num: 04
    title: Character Strings
    desc: Char arrays and null-terminator string garlands.
---
layout: trace
type: ternary
eyebrow: Part 01 · Decision Gates
title: Ternary Voting Gate Simulator
lede: Adjust the age slider to trace how the ternary operator (? :) routes values.
---
layout: hero
eyebrow: Part 02 · Loops
title: The Wet Grinder Analogy
lede: A while loop repeats instructions as long as a test condition remains True.
highlight: "Analogy: Like grinding batter in a wet grinder. You dump rice inside. As long as it is still coarse (condition is True), the grinder stone keeps rotating (loops repeats)."
image: wet_grinder.jpg
---
layout: trace
type: loopTracer
eyebrow: Part 02 · Loops
title: Loop Iteration Console Trace
lede: Trace loop cycle variables in real-time as the computer executes a for-loop.
---
layout: bullets
eyebrow: Part 03 · Arrays
title: What is an Array?
bullets:
  - bold: Continuous Memory:
    text: A sequence of items of the same data type stored side-by-side in RAM.
  - bold: Index Address:
    text: Access elements using zero-indexed positions (e.g. arr[0] is the first item).
  - bold: Fixed Size:
    text: Array size must be declared beforehand and cannot grow dynamically.
---
layout: trace
type: arrayMath
eyebrow: Part 03 · Arrays
title: Array Address Calculator
lede: Click different indexes in the array seat-row to calculate their exact hardware RAM memory addresses.
---
layout: hero
eyebrow: Part 04 · Strings
title: The Flower Garland Analogy
lede: A String in C is a sequence of characters terminated by a null character (\0).
highlight: "Analogy: Tying a flower garland. Each flower represents a character ('C', 'o', 'd', 'e'). The final knot represents the Null Terminator (\0) which stops the flowers from falling off."
image: flower_garland.jpg
---
layout: trace
type: stringTracer
eyebrow: Part 04 · Strings
title: Garland Null-Terminator trace
lede: Trace how a character loop traverses a string garland, exiting the moment it hits the null knot (\0).
---
layout: quiz
eyebrow: Part 04 · Strings Quiz
question: What is the size of the string "CRESCENT" in memory?
options:
  - text: 8 bytes
    correct: false
    feedback: "CRESCENT" has 8 letters, but it needs one extra byte for the null terminator.
  - text: 9 bytes
    correct: true
    feedback: Correct! 8 bytes for characters plus 1 byte for '\0'.
  - text: 10 bytes
    correct: false
    feedback: Only one null terminator byte is appended.
---
layout: blank
eyebrow: Part 04 · Strings Blank
title: Null Terminator Syntax
lede: Click the blank space to insert the null character that terminates C strings.
code: |
  char grade = 'A';
  char name[4] = "CSE"; // name contains 'C', 'S', 'E', '______'
blankVal: "\\0"
---
layout: todo
eyebrow: Part 05 · Practice
title: Find the maximum element in an array
desc: Write a loop to find the largest integer inside an array of 5 elements.
hint: Declare `int max = arr[0];` and loop from `i = 1` to `4`. If `arr[i] > max`, update `max = arr[i];`.

![CALSUCO Logo](https://calico.berkeley.edu/images/banner/blocks-suco.png)

# calsuco-22

## Quick Start
This repository contains all contest materials for CALSUCO '22, including solutions, editorials, tests, templates, and problem statements.

You can explore this repository using GitHub in your browser or download an [archive of all the files](https://github.com/calico-team/calsuco-22/archive/refs/heads/main.zip). If you'd like to see what files participants were given during the contest, you can download the [contest.zip](https://calico.berkeley.edu/files/calsuco-22/contest.zip)!

Although the contest is over, you can still submit solutions to the [judge platform](https://calicojudge.com) under the `calsuco-22-archive` contest. Sign in or register if you don't have an account already. Then change the selected contest to `calsuco-22-archive` on the right side of the navigation bar.

This is our first time publishing solutions and editorials in a contest repository! We highly encourage you to take a look as we're very happy how they turned out; we hope you find this to be a useful and interesting educational resource!

## Contest Overview
For the inaugural CALSUCO, we wanted to experiment with some more interesting problem types we've yet to explore in previous contests, those being open and interactive ones. We hope you had a fun time reading the problems and tackling some novel challenges. This contest was also a step up in difficulty as the highest score achieved was 66, although we believe that may partially be because it was an individual contest with less time and also due to technical issues on our end.

We recognize that a significant issue arose on our end regarding problem 2 during the contest, and we want to apologize to all contestants affected by it. A more detailed explanation of what went down and what we did can be found in [this document](https://docs.google.com/document/d/1KLo9JlxjuokYgyk-Ugq--Rdr3t6SrUCKa1Kte9DEFhs/edit?usp=sharing).

## Leaderboard

A huge congratulations to our awesome winning contestants:

1. **m177** (*Chongtian Ma*) from StuyCCC
2. **Eric Xue** (*Eric Xue*)
3. **plsdontflop** (*Daniel Qiu*)
4. **TheKingAleks** (*Aleksandar Yanev*) from HSM "D-r Petar Beron" Varna
5. **Vraj Patel** (*Vraj Patel*)
6. **hi** (*George Pong*)
7. **MeepMurp5** (*Vincent Wang*)
8. **solarlego** (*Casey Dow*) from Campolindo
9. **RHB** (*Dorothy Zheng*)
10. **lchi123** (*Leonardo T Chi*) from STEMnARTS

We also wanted to shout out some more contestants for their amazing achievements! Just 5 minutes into the contest, **solarlego** submitted a lightning-fast solve of 1A. Using some clever dynamic programming, **biximo** was the only contestant to crack 3B. Finally, the behemoth of 1C presenting gargantuan numbers was only solved by the trio of **Vraj Patel**, **m177**, and **hi** using Python’s arbitrary precision integer arithmetic.

## Repository Structure
The root of the repository has `calsuco-22.pdf`, which contains all problem statements, and `calsuco-22-editorial.pdf`, which contains all editorials. Subdirectories are named after each problem and contain their solutions, editorials, tests, templates, and problem statements.

### Solutions
Solutions are programs written by us that implement different approaches of varying efficiency in multiple programming languages to solve each problem. As a result, some solutions may pass more test sets than others. Solution files are named `[problem name]_[solution name].[extension]`, where `[solution_name]` is a keyword that describes the approach, and `[extension]` is the extension used by that language's source files (for example, `.cpp`, `.java`, or `.py`).

### Editorials
Editorials describe and thoroughly explain several approaches of varying efficiency to solve each problem. They are named `[problem_name]-editorial.pdf`.

### Tests
These are the inputs and outputs we use to test your program for correctness. Input files have the `.in` extension and corresponding output files have the `.ans` extension with the same file name. Test files are categorized as sample (usually named `sample.in` and `sample.ans` or similar) and hidden (everything else).

### Templates
Templates provide starter code that handle parsing input in multiple languages, so contestants can jump right into problem solving. They are named `[problem name]_template.[extension]`.

Note that these templates are only guaranteed to apply to the main test set of each problem; completing bonus test sets may require modifying the templates.

### Problem Statements
Problem statements describe the problem contestants need to solve, as well as their input and output format. They are named `[problem name].pdf`.

### Directory Tree
```
[contest name]
├── [contest name].pdf
├── [contest name]-editorial.pdf
├── [problem name]
│   ├── [problem name].pdf
│   ├── [problem name]-editorial.pdf
│   ├── solutions
│   │   ├── [problem name]_[solution name].[cpp | java | py]
│   │   └── ...
│   ├── templates
│   │   ├── [problem name]_template.[cpp | java | py]
│   │   └── ...
│   └── tests
│       ├── sample.in
│       ├── sample.ans
│       └── ...
├── [problem name]
│   └── ...
└── ...
```

## Feedback
If you can take some time to fill out [this feedback form](https://forms.gle/H4m2tERyjRKxPtiC6) and let us know how we did, that would be tremendously appreciated! We work hard to improve the contest experience for everyone, and any and all feedback is extremely helpful.

This is the same feedback form sent in the post-contest email. But if you have any new feedback for the editorials or solutions, feel free to submit another response!

# greek--compiler
Compiler for the greek++ language (Translators course project).

## Introduction
This project focuses on the design and implementation of a compiler for **greek++**, a simplified educational programming language.

The compiler performs lexical, syntactic, and semantic analysis, generates intermediate code (quadruples), and produces final assembly output.

---

## How It Works
The compiler follows a classic compilation pipeline:

### Lexical Analysis
The source program is scanned and converted into tokens such as identifiers, numbers, operators, and keywords.

### Syntactic Analysis
A recursive-descent parser is implemented based on the official greek++ grammar to validate program structure.

### Semantic Analysis
Semantic checks are performed using a symbol table with nested scopes, ensuring correct declarations, scope visibility, and parameter passing.

### Intermediate Code Generation
Intermediate code is generated in the form of quadruples, with backpatching used for control-flow statements.
The output is written to a `.int` file.

### Final Code Generation
The intermediate code is translated into assembly code and written to a `.asm` file.

---

## Features
- Structured programming constructs (if-else, loops)
- Procedures and functions
- Symbol table with scope and offset management
- Intermediate code and final assembly generation

---

## How to Use

### Requirements
- Python 3

### Run
```bash
python3 final_4838
.py test.greek

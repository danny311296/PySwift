# Swift Compiler

Implementation of the front-end of a compiler for the Swift Programming Language. 

## About The Project

This project is made using Python's PLY. It is done as part of Compiler Design Lab Project and currently supports two constructs 
of the Swift Programming Language 
* For Loops
* Functions


### Prerequisites

* Python2 

## Working
The compiler does the following tasks during various phases
### Phase 1: Lexical Analysis 
* Removal of single and multi line comments
* Conversion of the Swift source code into a stream of tokens
### Phase 2: Syntax Analysis 
* Parse the token stream generated from the lexical analyser and check if it is accepted as per the grammar defined by the language
* Creation of the Abstract Syntax Tree(AST) is done in this phase
### Phase 3: Semantic Analysis 
* For assignments of the form a = value , check if variable a was already declared else gives error
* For declarations like var a: Int , gives error if variable a was already declared
* Type Checking
* Function Parameters / Return Types
### Phase 4: TAC Generation 
* The AST generated is put into use in the generation of the TAC for the Swift Source program.
### Phase 5: TAC Optimisation
* Optimisations like Constant Folding, Constant Propagation, Loop Unrolling were performed to generate an optimised TAC.

## Running

    python swift_parser.py
    python tac.py
    python optimize.py

## Authors

* [Aviral Joshi](https://github.com/dataviral) 
* [Bhaarat Chetty](https://github.com/bhaaratchetty) 
* [Chirag Ramesh](https://github.com/chiggy97)
* [Daniel I](https://github.com/danny311296) 

## Acknowledgments

* We would like to thank our Compiler Design teacher Prof. C O Prakasha for guiding us in this project


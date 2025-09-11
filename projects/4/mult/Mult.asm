// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
// The algorithm is based on repetitive addition.

//Initialize R2 to zero
@2
M=0

//Jump to out if R0 or R1 are 0
@0
D=M
@END
D;JEQ
//
@1
D=M
@END
D;JEQ

(LOOP)
    //jump to OUT if R1<=0
    @1
    D=M
    @END
    D;JLE

    //if not, loop
    @ADD
    0;JMP

(ADD)
    //Add one copy of R0 to register R2
    @0
    D=M
    @2
    M=D+M

    //subtract one from R1
    @1
    M=M-1

    @LOOP
    0;JMP

(END)
    @END
    0;JMP

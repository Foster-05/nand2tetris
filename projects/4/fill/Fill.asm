// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, 
// the screen should be cleared.

//// Replace this comment with your code.

//KBD - SCREEN = a 512*256 = 131072/16=8192 which is the amount of registers to write to the screen 24576 - 16384 = 8192

(WAIT)
@KBD
D=M
@FILL
M=D;JGT
//When KBD is valued jump to fill
@WAIT
0;JMP
//While KBD=0 wait


(HOLD)
@KBD
D=M
@EMPTY
M=D;JEQ
//When KBD is empty jump to EMPTY

//************************************compare if at end
@HOLD
M=D;JGT
//While KBD=1 and at the end wait


(FILL)
//start the filling process
@SCREEN
//Fill a pixel (set to -1)

//Move 16 bits down

//Check if KBD is still valued AND we've reached the end
//If still valued and we're still working: come back to FILL

//If valued and we're at the end: jump to hold

//If empty: start emptying pixels


(EMPTY)
//Start the emptying process

//Empty a pixel

//Move a pixel up

//Check if KBD is still unvalued AND if we've reached the end
//If still unvalued and we're still working: come back to EMPTY

//If still unvalued and we're at the end: jump to WAIT
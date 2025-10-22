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
//initialize ADDY to the start of SCREEN
@SCREEN
D = A
@ADDY
M = D 

(WAIT) 
@KBD
D = A
@ADDY
D = D-M
@WAIT
D;JLE
// wait while screen is empty
//When KBD is valued jump to fill
@KBD
D=M
@FILL
D;JNE

@ADDY
D = M
@SCREEN
D = D-A
@CLEAR
D;JNE
@WAIT
D;JLE

//While KBD=0 wait
@WAIT
0;JMP
//*********************************************************
(FILL)
// if still valued and we're still working (KBD-SCREEN > 0): come back to FILL
//Not working: fills too much



//start the filling process
@ADDY
A = M
//Fill a pixel (set to -1)
M = -1
//Move to the next address, 16 bits down
D = A+1
@ADDY
M = D

@WAIT
0;JMP

//**********************************************************
(CLEAR)
//Start the clearing process
@ADDY
A=M
//Empty a pixel
M = 0
//Move a pixel up
D = A-1
@ADDY
M = D
//Check if KBD is still unvalued AND if we've reached the end
//If valued: jump to FILL
@KBD
D = M
@FILL
D;JNE
//If still unvalued and we're still working: come back to CLEAR
//Not working: jumping to WAIT instead of CLEAR
@ADDY
D = M
@SCREEN
D = D-A
@CLEAR
D;JNE
//If still unvalued and we're at the end: jump to WAIT
@WAIT
0;JMP
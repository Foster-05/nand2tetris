// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, 
// the screen should be cleared.

//// Replace this comment with your code.
//*******************************************************
//Initialize CUR_ADDRESS to the start of SCREEN
@SCREEN
D = A
@ADDY
M = D

//WAIT loop: hold screen while at top of screen
//*******************************************************
(WAIT)
//KBD - ADDY = 0 if at end of screen, valued if in the middle of screen

//If we're not at the end: jump to FILL
@KBD
D = A
@ADDY
D = D-M
@FILL
D;JNE
//Catch case; loop to WAIT if all else fails
@WAIT
0;JMP


//FILL loop: Add a pixel and move to next address
//******************************************************
(FILL)
//Jump to current address in screen
@ADDY
A = M
//Fill pixel
M = -1

//Increment through screen:
@ADDY
M = M+1

//Jump back to WAIT: it will check if we're at the end of screen or keyboard pressed
@WAIT
0;JMP


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


//HOLD loop: hold screen at the beginning of the screen
//******************************************************
(HOLD)

//Check if keyboard is pressed
//If keyboard pressed: jump to FILL
@KBD
D = M
@FILL
D;JNE
//Check screen position
@SCREEN
D=A 
@ADDY
D = M - D
//ADDY-SCREEN = 0 if at beginning of screen, valued if in the middle of screen
//Jump back to HOLD if we're at the beginning of screen (less than so we clear the last pixel)
@HOLD
D;JLT
//If keyboard not pressed and we're not at the start: Jump to EMPTY
@EMPTY
0;JMP

//WAIT loop: hold screen while at top of screen
//*******************************************************
(WAIT)
//Check screen position
@KBD
D = A
@ADDY
D = D-M
//KBD - ADDY = 0 if at end of screen, valued if in the middle of screen
//Loop to INT if at end of screen
@INT
D;JLE
//Check if keyboard is pressed
//If keyboard not pressed: jump to EMPTY
@KBD
D = M
@EMPTY
D;JEQ
//If keyboard is pressed and we're not at the end: jump to FILL
@KBD
D = A
@ADDY
D = D-M
@FILL
D;JNE
//Catch case; jump to WAIT if all else fails
@WAIT
0;JMP

//INT loop: check if keyboard pressed, intermediate step for when screen is full
//******************************************************************************
(INT)
//Decide to empty or go back to WAIT:
//Check if keyboard is pressed
//If keyboard not pressed: jump to EMPTY
@KBD
D = M
@EMPTY
D;JEQ
//Else jump back to WAIT
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

//EMPTY loop: Clear a pixel and move to next address
//*****************************************************
(EMPTY)
//Clear current pixel
@ADDY
A = M
M = 0

//Increment back through screen:
@ADDY
M = M-1

//Jump back to HOLD for all checks
@HOLD
0;JMP
//Rewrite in progress

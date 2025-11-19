<h1>nand2tetris</h1>
<h2> Project 9 </h2>
Project 9 was assigned as simply "make something in Jack"! Jack is the Java-like
language for the purposes of nand2tetris with a very simple syntax. Its syntax
is designed to be intentionally simple so that we may write a compiler for it 
during Project 10. 9 was intended to familiarize the class with Jack to deepen
our understanding in order to make 10 easier to understand. For Project 9,
my partner Gabriel Rottet and I decided to recreate the classic game Dig Dug in
Jack. We decided that this was sufficiently complicated to warrant a week or two of our time, among other classes and so on.

<img alt="image of Dig Dug gameplay" src="Screenshot from 2025-11-19 18-27-41.png">

Our version of Dig Dug implemented moving, digging in the ground, and
continuously updating tiles based on their surroundings: an air edge would have
a different texture than a dirt edge. We accomplished all this with a fairly
simple few classes, namely one each for controlling and drawing our character,
one to control the tilemap that stores and analyzes what's dirt and air, and
a few others to tie it together.
 
In the end, we ended up storing and using 32 unique sprites each made with an
online bitmap editor that changed certain values in memory to update exact
addresses on the screen. We could manipulate where these get drawn to change
the character's location, as well as load different dirt sprites to update the
tiles surrounding the character.

The full program is stored in the jack/digdug folder in this repository.
If you'd like to run the program for yourself, go to the [Online nand2tetris 
IDE](https://nand2tetris.github.io/web-ide/compiler) and upload the full contents
of the folder. Compile, run, and ensure it's run at the full speed available
and your keyboard is enabled. Have fun!


<p>My notes on how to use, syntax, and in-class examples.</p>

To run HardwareSimulator: navigate to nand2tetris root, run ./HardwareSimulator


---



<h3>Example: adding 16-bit integers in hdl</h3>

48 inputs, 16 outputs

```
CHIP Add3Way16{
	
	IN first[16], second[16], third[16]
	
	OUT out[16]

	PARTS:
		Add16(a=first, b=second, out = temp);
		Add16(a=temp, b=third, out=out);
}
```
---

<h3>Example: Anding 4 bits individually along an input.</h3>

```
CHIP And4Way{

	IN a[4];

	OUT out;

	
	PARTS:
		And(a=a[0], b=a[1], out= t01);
		And(a=t01, b=a[2], out= t02);
		And(a=t02, b=a[3], out= out);
}
```
---
<h3>Example: bit-wise And of two 4-bit inputs</h3>

```
CHIP And4{
	IN a[4], b[4];
	OUT out[4];

	PARTS:
		And(a=a[0], b=b[0], out=out[0]);
		And(a=a[1], b=b[1], out=out[1]);
		And(a=a[2], b=b[2], out=out[2]);
		And(a=a[3], b=b[3], out=out[3]);
}
```
---
<h3>To break up indexes:</h3>

```

Add16(a[0..7]=lsb, a[8..15]=msb, b=..., out=...);

```

Booleans can be used as buses of any width.


---

<h1>Hack Assembly</h1>
---
<h3> Screen syntax: to set pixel (row, col) on or off: </h3>
```
word = RAM[16384 + (32*row) + col/16]
set the (col % 16)th bit of word
RAM[i] = word
```
Credit Stewart Thomas

---



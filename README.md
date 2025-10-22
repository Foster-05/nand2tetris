<h1>nand2tetris</h1>
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



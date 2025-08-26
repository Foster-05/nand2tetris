<h1>nand2tetris</h1>
<p>My notes on how to use, syntax, and in-class examples.</p>

To run HardwareSimulator: navigate to nand2tetris root, run ./HardwareSimulator






<h2>Example: adding 16-bit integers in hdl</h2>

48 inputs, 16 outputs

---
CHIP Add3Way16{
	
	IN first[16], second[16], third[16]
	
	OUT out[16]

	PARTS:
		Add16(a=first, b=second, out = temp);
		Add16(a=temp, b=third, out=out);
}
---

<h2>Example: Anding 4 bits individually along an input.</h2>

---
CHIP And4Way{

	IN a[4];

	OUT out;

	
	PARTS:
		And(a=a[0], b=a[1], out= t01);
		And(a=t01, b=a[2], out= t02);
		And(a=t02, b=a[3], out= out);
}

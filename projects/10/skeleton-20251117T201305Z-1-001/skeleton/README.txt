This is a skeleton you are welcome to use to get started. It somewhat follows the book, but also veers off in a few ways.


--- OVERVIEW ---

First of all: Do not feel like you are required to use these files. If they are confusing, you can ignore them. However, they are meant to give you some help, especially in getting started with this project.

Specifically (more details in the next section)
:: The hjc.py file supplies the file input/output handling for you and lets you focus on the "Process" functions and the appropriate helper classes.
:: The hjcTokenWriter class mostly works as-is, BUT you will need to edit this file.
:: The hjcTokenizer needs quite a bit of work from you. You do not need to use all the functions defined in the file, so feel free to remove any extra or confusing ones.
:: A "compilationEngine" class is entirely missing from this folder and you will need to write one. That would be where you implement the recursive compiling routines that actually parse the expected grammar of the language.

Debugging is not too cumbersome. In general, you open the supplied, expected output XML file in one window, and then look at your program's output file in another window. You just need to go through the files and make sure they match exactly. It is surprisingly easier to debug this way than the previous projects.

I suggest making sure start out with making sure you can parse through a file and get/read the tokens. A CodePlan PDF (supplied by me in folder up one level) helps with making sense of this process. I tried to write in that my own thought processes for how I organized my code. Once you are able to break apart the tokens from a file, then get the xxxT.xml files working. For these, just emit the token type and the token itself. No need to include the code structure. Lastly, once these tasks are done, then you can focus on understanding the grammer part and producing the final xxx.xml files which include the individual tokens, what type of token they are, and the structure of the Jack code you are compiling.

This project takes some time to do and is not easy. You need to get a handle on the basics, and getting the more simple tokens emitted first. Once you have that, the compliationengine mostly just takes time debugging. It's fun and once you have done this you have really accomplished something!!! You are parsing a language according to a formal grammar!


--- FILE DETAILS ---

hjc.py
- This is the main python file to run. It handles all the file and directory items. It will pass execution to ProcessT and then Process functions, passing them a) a valid input jack file name and b) a file name to write to. Look at these functions for where to start writing your code.

ProcessT() :: Sets up a loop to go through the file, and is intended to write the xxxT.xml files. (first part of project 10)

Process() :: Similar to the ProcessT function, but writes the "full" XML file. This will be done by calling the CompilationEngine portion which would call a CompileClass function and that does most of the work. This function will know the grammar and then recursively call compile functions as necessary, until the file has been parsed.

---

HjcConstants.py
- Holds a list of constants that you can use to organize your code a bit. No need to repeat things.

---

hjcTokenWriter.py
- This has a series of helper functions that facilitate writing to an output XML file. It handles some of the opening/closing of the tags as well as replacing some characters with valid XML characters. I have also included the annoying XML characters that must escaped, like an Ampersand (&). You will probably want to extend this so that you can add indentation levels.

WriteXML() :: This function accepts a "tag" and a "value". It takes care of opening and closing the tags, and also escaping characters which are not allowed in XML.

---

hjcTokenizer.py
- This is mostly a skeleton file for you and doesn't do much besides set up functions that you may want to use. Importantly, I did include an "_eat()" function which eats a character from a current stream (in this case, a variable containing the current line. Eating means simply removing a character from the line.

You will need to edit this file quite a bit. And again:  You are not required to use all these functions. I am supplying this skeleton file so that you can get started with things.

---

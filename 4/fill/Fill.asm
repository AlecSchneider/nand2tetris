// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, 
// the screen should be cleared.

@R0
// 0 is white
M=0

(LOOP)
@KBD
D=M
@WHITE
D;JEQ
@BLACK
0;JMP

(WHITE)
@R0
D=M
@DONE
D;JEQ
@R0
M=0
@R1
M=0
@DRAW
0;JMP

(BLACK)
@R0
D=M
@DONE
D;JGT
@R0
M=1
@R1
M=-1
@DRAW
0;JMP

(DRAW)
@SCREEN
D=A
@n
M=D
@i
M=0
(DRAWLOOP)
  @8192
  D=A
  @i
  D=M-D
  @LOOP
  D;JEQ
  @R1
  D=M
  @n
  A=M
  M=D
  @n
  M=M+1
  @i
  M=M+1
  @DRAWLOOP
  0;JMP

(DONE)
@LOOP
0;JMP
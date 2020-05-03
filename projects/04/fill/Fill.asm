// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed.
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Pseudo Code
//  if (key != 0) {
//    color = BLACK;
//  } else {
//    color = WHITE;
//  }
//  for (int address = SCREEN; address < SCREEN + 8192; address++) {
//    RAM[address] = color;
//  }

(START)
  // set up loop variable
  @SCREEN
  D=A
  @address
  M=D  // address = SCREEN;

  @KBD
  D=M
  @BLACK
  D;JNE     // Goto BLACK if key = 0

  @color
  M=0       // color = 0; (white)

  @LOOP
  0;JMP     // Goto LOOP

(BLACK)
  @color
  M=-1       // color = -1; (black)

(LOOP)
  @8192
  D=A
  @SCREEN
  D=D+A
  @address
  D=M-D
  @START
  D;JEQ     // Goto START if address - (SCREEN + 8192) == 0

  @color
  D=M
  @address
  A=M
  M=D       // RAM[address] = color;

  @address
  M=M+1

  @LOOP
  0;JMP     // Goto LOOP

(STOP)
  @STOP
  0;JMP

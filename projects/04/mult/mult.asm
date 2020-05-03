// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Adapted simpler version of code so that it works with negatives

// Pseudo Code
//  product = 0;
//  negativeR1 = R1 < 0;
//  positiveR1 = if (R1 < 0) -R1; else R1;
//  for (int i = 0; i < positiveR1, i++) {
//    product += R0;
//  }
//  if (negativeR1) {
//    product = -product;
//  }
//  R2 = product;

  @product
  M=0       // product = 0;

  @i
  M=0       // i = 0;

  @R2
  M=0       // R2 = 0;

  @R1
  D=M
  @NEGATIVE
  D;JLT    // Goto NEGATIVE if R1 < 0

  @positiveR1
  M=D       // positiveR1 = R1
  @negativeR1
  M=0
  @LOOP
  0;JMP     // Goto LOOP

(NEGATIVE)
  @R1
  D=M
  @negativeR1
  M=1
  @positiveR1
  M=-D      // positiveR1 = -R1

(LOOP)
  @i
  D=M
  @positiveR1
  D=D-M     // i - positiveR1;
  @STOP
  D;JEQ     // Goto STOP if i - positiveR1 < 0

  @product
  D=M
  @R0
  D=D+M
  @product
  M=D       // product += R0;

  @i
  M=M+1     // i++;

  @LOOP
  0;JMP     // Goto LOOP

(STOP)
  @product
  D=M
  @R2
  M=D       // R2 = product;

  @negativeR1
  D=M
  @END
  D;JEQ     // Goto END if negativeR1 == 0 (or negativeR1 is false)

  @R2
  M=-M

(END)
  @END
  0;JMP

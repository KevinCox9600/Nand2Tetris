"""Converts the hack assembly language into binary hack machine code"""

import sys
import parser_asm

if __name__ == '__main__':
    if len(sys.argv) == 2:
        parser = parser_asm.Parser(sys.argv[1])
    # parser_asm.Parser('./add/Add.asm')
    # parser_asm.Parser('./max/Max.asm')
    # parser_asm.Parser('./max/MaxL.asm')
    # parser_asm.Parser('./pong/Pong.asm')
    # parser_asm.Parser('./pong/PongL.asm')
    # parser_asm.Parser('./rect/Rect.asm')
    # parser_asm.Parser('./rect/RectL.asm')

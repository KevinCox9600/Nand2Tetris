import re
from translator import Code


class Parser:
    def __init__(self, file: str):
        self.commands = []
        self.table = {
            'SP': 0, 'LCL': 1, 'ARG': 2, 'THIS': 3, 'THAT': 4,
            'R0': 0, 'R1': 1, 'R2': 2, 'R3': 3, 'R4': 4, 'R5': 5,
            'R6': 6, 'R7': 7, 'R8': 8, 'R9': 9, 'R10': 10, 'R11': 11,
            'R12': 12, 'R13': 13, 'R14': 14, 'R15': 15,
            'SCREEN': 16384, 'KBD': 24576
        }
        self.next_available_mem = 16
        self.line_number = 0
        with open(file) as f:
            line = f.readline()
            while line:
                clean_line = self.clean_line(line)

                command_type = self.command_type(clean_line)
                if command_type == 'A_COMMAND' or command_type == 'C_COMMAND':
                    self.commands.append(clean_line)
                    self.line_number += 1
                if command_type == 'L_COMMAND':
                    self.add_symbol(clean_line)
                line = f.readline()

        for index, command in enumerate(self.commands):
            command_type = self.command_type(command)
            if command_type == 'A_COMMAND':
                self.commands[index] = self.convert_a(command)
            elif command_type == 'C_COMMAND':
                self.commands[index] = self.convert_c(command)
        with open(file[:-3] + 'hack', 'w') as hack_file:
            for command in self.commands:
                hack_file.write(command + '\n')

    @staticmethod
    def clean_line(line: str) -> str:
        """Removes the comments and whitespace from a line"""
        return re.sub(r'//.*', '', line).strip()

    @staticmethod
    def command_type(command: str) -> str:
        """Determines the type of the given command"""
        if command:
            if command[0] == '@':
                return 'A_COMMAND'
            elif command[0] == '(':
                return 'L_COMMAND'
            else:
                return 'C_COMMAND'
        else:
            return ''

    def convert_a(self, command: str) -> str:
        """Converts an A instruction to binary"""
        address = command[1:]
        if address in self.table.keys():
            num = self.table[address]
        elif re.search(r'\D', address):
            num = self.next_available_mem
            self.next_available_mem += 1
            self.table[address] = num
        else:
            num = int(address)
        converted = f'0{num:015b}'
        return converted

    @staticmethod
    def convert_c(command: str) -> str:
        """Converts a C instruction to binary"""
        dest_s, comp_s, jump_s = '', '', ''
        if '=' in command and ';' in command:
            dest_s, after = command.split('=')
            comp_s, jump_s = after.split(';')
        elif '=' in command:
            dest_s, comp_s = command.split('=')
        elif ';' in command:
            comp_s, jump_s = command.split(';')
        else:
            print('hmm, expected "=" or ";" but found neither')
        comp = Code.comp(comp_s)
        dest = Code.dest(dest_s)
        jump = Code.jump(jump_s)
        converted = '111' + comp + dest + jump
        return converted

    def add_symbol(self, command: str) -> None:
        """Adds a symbol to the symbol dictionary if necessary"""
        if command[0] == '(':
            label = re.findall(r'\((.*?)\)', command)[0]
            if label not in self.table.keys():
                self.table[label] = self.line_number
        # else:
        #     address = command[1:]
        #     if address in self.table.keys():
        #         self.table[address] = self.next_available_mem

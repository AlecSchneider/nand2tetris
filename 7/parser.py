class Parser:
    def __init__(self, file):
        self.file = file
        self.line = None
        self.line_number = -1

    def get_line(self):
        return self.line

    def has_more_lines(self) -> bool:
        return self.line_number < len(self.file) - 1

    def advance(self):
        # skip whitespace / comments

        is_whitespace = True
        is_comment = True
        while self.has_more_lines and (is_whitespace or is_comment):
            self.line_number += 1
            is_whitespace = False
            is_comment = False
            self.line = self.file[self.line_number].strip()
            print(self.line)
            if self.line.startswith("//"):
                is_comment = True
            elif len(self.line) == 0:
                is_whitespace = True

    def command_type(self):
        command = self.line.split(" ")[0]
        # C_ARITHMETIC, C_PUSH, C_POP, C_LABEL, C_GOTO, C_IF, C_FUNCTION, C_RETURN, C_CALL
        if command == "push":
            return "C_PUSH"
        elif command == "pop":
            return "C_POP"
        elif command in ["add", "sub", "eq", "lt", "gt", "neg", "and", "or", "not"]:
            return "C_ARITHMETIC"

        raise Exception("not implemented")

    def arg1(self):
        line_split = self.line.split(" ")

        if self.command_type() == "C_ARITHMETIC":
            return line_split[0]

        if len(line_split) < 2:
            raise Exception("should not be called")

        return line_split[1]

    def arg2(self):
        line_split = self.line.split(" ")

        if len(line_split) < 3:
            raise Exception("should not be called")

        return line_split[2]

class Parser:
    def __init__(self, file):
        self.file = file
        self.line = None
        self.lineNumber = -1

    def getLine(self):
        return self.line

    def hasMoreLines(self) -> bool:
        return self.lineNumber < len(self.file) - 1

    def advance(self):
        # skip whitespace / comments

        isWhitespace = True
        isComment = True
        while self.hasMoreLines and (isWhitespace or isComment):
            self.lineNumber += 1
            isWhitespace = False
            isComment = False
            self.line = self.file[self.lineNumber].strip()
            print(self.line)
            if self.line.startswith("//"):
                isComment = True
            elif len(self.line) == 0:
                isWhitespace = True

    def instructionType(self):
        if self.line.startswith("@"):
            return "A_INSTRUCTION"
        elif self.line.startswith("("):
            return "L_INSTRUCTION"
        else:
            return "C_INSTRUCTION"

    def symbol(self):
        instructionType = self.instructionType()
        if instructionType == "L_INSTRUCTION":
            return self.line[1:-1]
        elif instructionType == "A_INSTRUCTION":
            return self.line[1:]

    def dest(self):
        if "=" in self.line:
            return self.line.split("=")[0]

        return None

    def comp(self):
        if "=" in self.line:
            if ";" in self.line:
                return self.line.split("=")[1].split(";")[0]
            return self.line.split("=")[1]
        if ";" in self.line:
            return self.line.split(";")[0]

        return None

    def jump(self):
        try:
            return self.line.split(";")[1]
        except:
            return None

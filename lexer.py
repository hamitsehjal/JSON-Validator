from token_1 import Token


class Lexer:
    def __init__(self, input_string: str):
        self.tokens = []
        self.data = input_string

    def getTokens(self):
        n = len(self.data)
        i = 0

        while i < n:
            ch = self.data[i]
            tkn = None
            if ch == "{":
                tkn = Token("LEFT_BRACE", "{")
                i += 1
            elif ch == "}":
                tkn = Token("RIGHT_BRACE", "}")
                i += 1
            elif ch == "[":
                tkn = Token("LEFT_BRACKET", "[")
                i += 1
            elif ch == "]":
                tkn = Token("RIGHT_BRACKET", "]")
                i += 1

            # handle String
            elif ch == '"':
                j = i + 1

                while j < n and self.data[j] != '"':
                    j += 1

                if j == n:
                    raise ValueError('Expect a "')
                elif self.data[j] != '"':
                    raise ValueError(f'Expected a ", instead got {self.data[j]}')
                else:
                    # self.data[i+1:j] -> string value
                    tkn = Token("STRING", self.data[i + 1 : j])
                    i = j + 1  # update the point

            # handle colon
            elif ch == ":":
                tkn = Token("COLON", ":")
                i += 1

            # handle comma
            elif ch == ",":
                tkn = Token("COMMA", ",")
                i += 1

            # handle null
            elif self.data[i : i + 4] == "null":
                tkn = Token("NULL", "null")
                i += 4

            # handle boolean(True)
            elif self.data[i : i + 4] == "true":
                tkn = Token("BOOLEAN", "true")
                i += 4

            # handle boolean(false)
            elif self.data[i : i + 5] == "false":
                tkn = Token("BOOLEAN", "false")
                i += 5

            # handle Numbers (5,-5, 5.2,-5.2)
            elif ch.isdigit() or ch == "-":
                j = i
                if ch == "-":
                    j += 1

                # Must have 1 digit after minus
                if j >= n or not self.data[j].isdigit():
                    raise ValueError("Expected a digit")

                # parse integer part
                while j < n and self.data[j].isdigit():
                    j += 1

                # Handle Decimal Part
                if j < n and self.data[j] == ".":
                    j += 1
                    if j >= n or not self.data[j].isdigit():
                        raise ValueError("Expected a digit")

                    while j < n and self.data[j].isdigit():
                        j += 1

                tkn = Token("NUMBER", self.data[i:j])
                i = j

            # handle empty spaces:
            elif ch.isspace():
                i += 1
            else:
                raise ValueError(f"Expected a Valid Value, got {ch}")

            # Add token if its valid
            if tkn is not None:
                self.tokens.append(tkn)

        return self.tokens

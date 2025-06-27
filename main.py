import sys
from lexer import Lexer
from parser import Parser

if __name__ == "__main__":
    filepath: str = "./tests/step4/valid2.json"
    with open(filepath, "r") as file:
        data = file.read()
        lexer = Lexer(input_string=data)
        try:
            tokens = lexer.getTokens()

            # Parse the tokens
            parser = Parser(tokens=tokens)
            if parser.isValid():
                print(f"File - {filepath} | Status: Valid")
                sys.exit(0)
            else:
                print(f"File - {filepath} | Status: Invalid")
                sys.exit(1)
        except FileNotFoundError as e:
            print(f"File Not Found - {e}")
            sys.exit(1)
        except Exception as e:
            print(f"Lexer Exception: File - {filepath} | Status: Invalid")
            sys.exit(1)

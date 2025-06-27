{"name": "hamit"}
"""
Json can be  - Object, Array, Number, Boolean, String, Null
Object is: `{` + key-val-pairs + `}`
key-val-pairs is: String + `:` + Value
Value is: Object, Array, Number, Boolean, String, Null

{"name":"hamit"}
['{','name',':','hamit','}']
"""
from typing import List, Tuple
from token_1 import Token


class Parser:
    def __init__(self, tokens: List[Token]) -> None:
        self.tokens: List[Token] = tokens
        self.total_count: int = len(tokens)

    def isValid(self) -> bool:
        return self._parseValue(0)[0]

    def _parseValue(self, idx: int) -> Tuple[bool, int]:
        token: Token = self.tokens[idx]

        if token.ttype == "LEFT_BRACE":
            return self._parseObject(idx)
        elif token.ttype == "LEFT_BRACKET":
            return self._parseArray(idx)
        elif token.ttype == "STRING":
            return (True, idx)
        elif token.ttype == "NUMBER":
            return (True, idx)
        elif token.ttype == "BOOLEAN":
            return (True, idx)
        elif token.ttype == "NULL":
            return (True, idx)
        else:
            # invalid
            return (False, idx)

    def _parseArray(self, idx: int) -> Tuple[bool, int]:
        i: int = idx

        if self.tokens[i].ttype != "LEFT_BRACKET":
            return (False, i)

        i += 1
        if not self._inBounds(i):
            return (False, i)

        res, i = self._parseValue(idx=i)
        if not res:
            return (False, i)

        i += 1
        if not self._inBounds(i):
            return (False, i)

        if self.tokens[i].ttype != "RIGHT_BRACKET":
            return (False, i)

        return (True, i)

    def _parseKeyValuePair(self, idx: int) -> Tuple[bool, int]:
        i: int = idx
        if self.tokens[i].ttype != "STRING":

            return (False, i)

        # Checking for colon
        i += 1
        if not self._inBounds(i):
            return (False, i)

        if self.tokens[i].ttype != "COLON":
            return (False, i)

        # Parse Value
        i += 1
        if not self._inBounds(i):
            return (False, i)

        res, i = self._parseValue(idx=i)
        if not res:
            return (False, i)

        return (True, i)

    def _parseObject(self, idx: int) -> Tuple[bool, int]:
        i: int = idx

        # Right Brace
        if self.tokens[i].ttype != "LEFT_BRACE":
            return (False, i)

        i += 1
        if not self._inBounds(i):
            return (False, i)

        if self.tokens[i].ttype in ("STRING", "RIGHT_BRACE"):
            if self.tokens[i].ttype == "STRING":
                # handling key-value pair
                res, i = self._parseKeyValuePair(i)
                if not res:
                    return (False, i)

                # handle comma (another key-val pair) if present
                i += 1
                if not self._inBounds(i):
                    return (False, i)

                while self.tokens[i].ttype == "COMMA":
                    i += 1
                    if not self._inBounds(i):
                        return (False, i)

                    res, i = self._parseKeyValuePair(i)

                    if not res:
                        return (False, i)

                    i += 1
                    if not self._inBounds(i):
                        return (False, i)

                if self.tokens[i].ttype != "RIGHT_BRACE":
                    return (False, i)

                return (True, i)

        else:
            return (False, i)

    def _inBounds(self, idx) -> bool:
        return 0 <= idx < self.total_count

class Token:
    def __init__(self, ttype, val):
        self.ttype = ttype
        self.val = val

    def __str__(self):
        return f"Token({self.ttype}, {self.val})"

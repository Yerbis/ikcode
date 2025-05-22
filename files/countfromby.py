class CountFromBy():
    def __init__(self, v: int, i: int) -> None:
        self.val = v
        self.incr = i
    
    def increase(self) -> None:
        self.val += self.incr # go to notes/pybook_notes/pybooknotes.txt for info

    def __repr__(self) -> str: # the "->" just lets users know it returns a str
        return str(self.val)
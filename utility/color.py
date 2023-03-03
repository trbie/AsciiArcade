class Color:
    R:int
    G:int
    B:int
    Start:str

    End = "\033[0m"

    def __init__(self, r, g, b):
        self.R = r
        self.G = g
        self.B = b

        self.Start = f"\033[38;2;{r};{g};{b}m"


    def __str__(self):
        return f"({self.R}, {self.G},  {self.B})"


class Colors:
    Red = Color(255, 0, 0)
    Green = Color(0, 255, 0)
    Blue = Color(0, 0, 255)
    White = Color(255, 255, 255)
    Black = Color(0, 0, 0)

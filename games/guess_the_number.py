import random
from utilities.console import Console

class GuessTheNumber:
    Answer:int
    Turns:int

    Win:bool
    End:bool

    Min: int
    Max: int


    def __init__(self, config={"min": 1, "max": 10}):
        self.Min = config["min"]
        self.Max = config["max"]


    def Reset(self):
        self.Answer = random.randint(self.Min, self.Max)
        self.Turns = 3
        self.Win = False
        self.End = False

        Console.Clear()


    def Play(self) -> None:
        self.Reset()

        print(f"I'm thinking of a number between {self.Min} and {self.Max}")

        while not self.End:
            guess = self.GetInput()
            self.ProcessInput(guess)

        self.ShowEndScreen()


    def GetInput(self, msg:str = "") -> int:
        print()

        msg = msg + "\n" if msg != "" else ""
        inpt = input(f"{msg}What number do you guess ({self.Turns})? ")

        if not inpt.isnumeric() or int(inpt) < self.Min or int(inpt) > self.Max:
            return self.GetInput(f"Invalid Input (Must be an number within the range of {self.Min}-{self.Max})")

        return int(inpt)


    def ProcessInput(self, inpt:int) -> None:
        self.Turns -= 1

        if inpt == self.Answer or self.Turns <= 0:
            self.End = True

            if inpt == self.Answer:
                self.Win = True
        
        else:
            hint = "higher" if inpt < self.Answer else "lower"
            print(f"My number is {hint} than {inpt}")


    def ShowEndScreen(self) -> None:
        print("=" * 30)

        if self.Win:
            print("You won, my number was", self.Answer)
        else:
            print("Nice try, but my number was", self.Answer)

        Console.Pause()



if __name__ == "__main__":
    game = GuessTheNumber()
    game.Play()

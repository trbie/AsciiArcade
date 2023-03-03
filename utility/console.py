import os
import platform

class Console:

    @staticmethod
    def Clear():
        plat = platform.system()
        if plat == "Windows":
            os.system("cls")
            
        elif plat == "Linux" or plat == "Darwin":
                os.system("clear")

        else:
            print("\n" * 500)

    
    @staticmethod
    def Pause():
        plat = platform.system()
        if plat == "Windows":
            os.system("pause")
            
        elif plat == "Linux" or plat == "Darwin":
                os.system("read -p 'Press Enter to continue . . . '")

        else:
            input("Press Enter to continue . . . ")


    @staticmethod
    def ColorPrint(message:str, colors):
        c = 0
        i = 0

        if len(colors) > 0:
            colored = message.replace("}", colors[0].End)

        for color in colors:
            i =  colored.find("{", i)
            colored = colored[:i] + colors[c].Start + colored[i+1:]
            c += 1

        print(colored)

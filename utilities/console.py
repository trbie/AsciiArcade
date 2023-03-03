import os
import platform

class Console:

    @staticmethod
    def Clear():
        match platform.system():
            case "Windows":
                os.system("cls")

            case "Linux":
                os.system("clear")

            case "Darwin":
                os.system("clear")

    
    @staticmethod
    def Pause():
        match platform.system():
            case "Windows":
                os.system("pause")
            
            case "Linux":
                os.system("read -p 'Press Enter to continue . . . '")

            case "Darwin":
                os.system("read -p 'Press Enter to continue . . . '")

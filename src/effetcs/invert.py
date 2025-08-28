
import cv2
from colorama import Fore, Style

class InvertEffect:
    def __init__(self, imagePath, resultPath):
        self.imagePath = imagePath
        self.resultPath = resultPath

    def apply(self):
        try:
            img = cv2.imread(self.imagePath)
            inverted = 255 - img
            cv2.imwrite(self.resultPath, inverted)
            print(Fore.GREEN + "Inverted image saved successfully." + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error occurred: {e}" + Style.RESET_ALL)


import cv2
from colorama import Fore, Style

class BlurEffect:
    def __init__(self, imagePath, resultPath):
        self.imagePath = imagePath
        self.resultPath = resultPath

    def apply(self):
        try:
            image = cv2.imread(self.imagePath)
            blurred = cv2.GaussianBlur(image, (15, 15), 0)
            cv2.imwrite(self.resultPath, blurred)
            print(Fore.GREEN + "Blurred image saved successfully." + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error occurred: {e}" + Style.RESET_ALL)


import cv2
from colorama import Fore, Style
import numpy as np

class SharpenEffect:
    def __init__(self, imagePath, resultPath):
        self.imagePath = imagePath
        self.resultPath = resultPath

    def apply(self):
        try:
            img = cv2.imread(self.imagePath)
            kernel = np.array([[0, -1, 0],
                               [-1, 5,-1],
                               [0, -1, 0]])
            sharpened = cv2.filter2D(img, -1, kernel)
            cv2.imwrite(self.resultPath, sharpened)
            print(Fore.GREEN + "Sharpened image saved successfully." + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error occurred: {e}" + Style.RESET_ALL)

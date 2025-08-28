import cv2
from colorama import Fore, Style

class BrightenEffect:
    def __init__(self, imagePath, resultPath, beta=50):
        self.imagePath = imagePath
        self.resultPath = resultPath
        self.beta = beta

    def apply(self):
        try:
            img = cv2.imread(self.imagePath)
            brightened = cv2.convertScaleAbs(img, beta=self.beta)
            cv2.imwrite(self.resultPath, brightened)
            print(Fore.GREEN + "Brightened image saved successfully." + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error occurred: {e}" + Style.RESET_ALL)

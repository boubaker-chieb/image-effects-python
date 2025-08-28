
import cv2
from colorama import Fore, Style

class PencilSketchEffect:
    def __init__(self, imagePath, resultPath):
        self.imagePath = imagePath
        self.resultPath = resultPath

    def apply(self):
        try:
            img = cv2.imread(self.imagePath)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            inv = 255 - gray
            blur = cv2.GaussianBlur(inv, (21,21), 0)
            sketch = cv2.divide(gray, 255 - blur, scale=256)

            cv2.imwrite(self.resultPath, sketch)

            print(Fore.GREEN + "Pencil sketch image saved successfully." + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error occurred: {e}" + Style.RESET_ALL)

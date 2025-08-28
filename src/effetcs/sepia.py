import cv2
import numpy as np

from colorama import Fore, Style

class SepiaEffect:
    def __init__(self, imagePath, resultPath):
        self.imagePath = imagePath
        self.resultPath = resultPath

    def apply(self):
        try:
          image = cv2.imread(self.imagePath)
          # Sepia filter matrix
          sepia_filter = np.array([[0.272, 0.534, 0.131],
                                    [0.349, 0.686, 0.168],
                                    [0.393, 0.769, 0.189]])
          sepia_image = cv2.transform(image, sepia_filter)
          sepia = np.clip(sepia_image, 0, 255)
          cv2.imwrite(self.resultPath, sepia)
        except Exception as e:
            print(Fore.RED + f"Error occurred: {e}" + Style.RESET_ALL)
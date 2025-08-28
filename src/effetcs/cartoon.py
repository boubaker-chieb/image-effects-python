
import cv2
from colorama import Fore, Style

class CartoonEffect:
    def __init__(self, imagePath, resultPath):
        self.imagePath = imagePath
        self.resultPath = resultPath

    def apply(self):
        try:
            img = cv2.imread(self.imagePath)
            # Convert to gray
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            gray = cv2.medianBlur(gray, 5)

            # Detect edges
            edges = cv2.adaptiveThreshold(gray, 255,
                                        cv2.ADAPTIVE_THRESH_MEAN_C,
                                        cv2.THRESH_BINARY, 9, 9)

            # Apply bilateral filter for smoothing
            color = cv2.bilateralFilter(img, 9, 300, 300)

            # Combine edges with color
            cartoon = cv2.bitwise_and(color, color, mask=edges)

            cv2.imwrite(self.resultPath, cartoon)

            print(Fore.GREEN + "Cartoon image saved successfully." + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error occurred: {e}" + Style.RESET_ALL)

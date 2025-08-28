import cv2
class GrayScaleEffect:
    def __init__(self, imagePath, resultPath):
        self.imagePath = imagePath
        self.resultPath = resultPath

    def apply(self):
        try:
            # Convert the image to grayscale
            image = cv2.imread(self.imagePath)
            # Convert to grayscale
            grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            # Save the grayscale image
            cv2.imwrite(self.resultPath, grayImage)
            print("Grayscale image saved successfully.")
        except Exception as e:
            print(f"Error occurred: {e}")

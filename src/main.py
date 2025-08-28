import os
from colorama import Fore, Style
from effetcs.grayscale import GrayScaleEffect
from effetcs.sepia import SepiaEffect
from effetcs.blur import BlurEffect
from effetcs.cartoon import CartoonEffect
from effetcs.pencil_sketch import PencilSketchEffect
from effetcs.invert import InvertEffect
from effetcs.brighten import BrightenEffect
from effetcs.sharpen import SharpenEffect

filePath = os.path.join(os.path.dirname(__file__), 'assets', 'input_image.jpg')
# Test Scale Effect
resultScalePath = os.path.join(os.path.dirname(__file__), 'assets', 'grayscale' , 'grayscale_image.jpg')
print(Fore.BLUE + f"Processing image at: {filePath}" + Style.RESET_ALL)
grayScaleEffect = GrayScaleEffect(filePath, resultScalePath)
grayScaleEffect.apply()

# Test Sepia Effect
resultSepiaPath = os.path.join(os.path.dirname(__file__), 'assets', 'sepia' , 'sepia_image.jpg')
print(Fore.GREEN + f"Processing image at: {filePath}" + Style.RESET_ALL)
sepiaEffect = SepiaEffect(filePath, resultSepiaPath)
sepiaEffect.apply()

# Test Blur Effect
resultBlurPath = os.path.join(os.path.dirname(__file__), 'assets', 'blur' , 'blur_image.jpg')
print(Fore.MAGENTA + f"Processing image at: {filePath}" + Style.RESET_ALL)
blurEffect = BlurEffect(filePath, resultBlurPath)
blurEffect.apply()

# Test Cartoon Effect
resultCartoonPath = os.path.join(os.path.dirname(__file__), 'assets', 'cartoon' , 'cartoon_image.jpg')
print(Fore.CYAN + f"Processing image at: {filePath}" + Style.RESET_ALL)
cartoonEffect = CartoonEffect(filePath, resultCartoonPath)
cartoonEffect.apply()

# Test Pencil Sketch Effect
resultPencilSketchPath = os.path.join(os.path.dirname(__file__), 'assets', 'pencil_sketch' , 'pencil_sketch_image.jpg')
print(Fore.YELLOW + f"Processing image at: {filePath}" + Style.RESET_ALL)
pencilSketchEffect = PencilSketchEffect(filePath, resultPencilSketchPath)
pencilSketchEffect.apply()

# Test Invert Effect
resultInvertPath = os.path.join(os.path.dirname(__file__), 'assets', 'invert' , 'invert_image.jpg')
print(Fore.MAGENTA + f"Processing image at: {filePath}" + Style.RESET_ALL)
invertEffect = InvertEffect(filePath, resultInvertPath)
invertEffect.apply()

# Test Brighten Effect
resultBrightenPath = os.path.join(os.path.dirname(__file__), 'assets', 'brighten' , 'brighten_image.jpg')
print(Fore.YELLOW + f"Processing image at: {filePath}" + Style.RESET_ALL)
brightenEffect = BrightenEffect(filePath, resultBrightenPath)
brightenEffect.apply()

# Test Sharpen Effect
resultSharpenPath = os.path.join(os.path.dirname(__file__), 'assets', 'sharpen' , 'sharpen_image.jpg')
print(Fore.CYAN + f"Processing image at: {filePath}" + Style.RESET_ALL)
sharpenEffect = SharpenEffect(filePath, resultSharpenPath)
sharpenEffect.apply()

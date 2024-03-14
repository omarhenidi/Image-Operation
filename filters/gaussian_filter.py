from scipy.ndimage import convolve
from PIL import Image
import numpy as np

class GaussianFilter:
    
    def __init__(self, path):
        self.image = path

    def apply_filter(self):
        # Load the image and convert it to grayscale
        self.img = np.array(Image.open(self.image).convert("L"))

        # Define the Gaussian filter kernel
        gaussian_kernel = np.array([[1, 4, 6, 4, 1],
                                    [4, 16, 24, 16, 4],
                                    [6, 24, 36, 24, 6],
                                    [4, 16, 24, 16, 4],
                                    [1, 4, 6, 4, 1]]) / 256

        # Apply Gaussian filter
        gaussian_filtered = convolve(self.img, gaussian_kernel, mode="reflect")

        # show result images
        self.img1 = Image.fromarray(gaussian_filtered)
        # Save image
        self.save = input("Do You Need To Save the New Image (Y/N): ")
        if self.save.lower() == 'y':
            if self.img1.mode != 'RGB':
                self.img_name = input("Enter Image Name: ")
                self.new_img =self.img1.convert('RGB')
                self.new_img.save(f'{self.img_name}.jpg')
        # Show the new image
        self.img1.show()


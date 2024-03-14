from PIL import Image
import numpy as np
from scipy.ndimage import convolve


class MeanFilter:

    def __init__(self, path):
        self.image = path

    def apply_filter(self):
        # Read the image
        self.img = np.array(Image.open(self.image).convert('L'))
        # Define the mean filter kernel
        mean_kernel = np.ones((5, 5)) / 25
        # Apply mean filter
        mean_filtered = convolve(self.img, mean_kernel, mode="reflect")
        # Convert matrix to image
        self.img = Image.fromarray(mean_filtered)
        # Save image
        self.save = input("Do You Need To Save the New Image (Y/N): ")
        if self.save.lower() == 'y':
            if self.img.mode != 'RGB':
                self.img_name = input("Enter Image Name: ")
                self.new_img =self.img.convert('RGB')
                self.new_img.save(f'{self.img_name}.jpg')
        # Show the new image
        self.img.show()

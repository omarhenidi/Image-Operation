import numpy as np
from PIL import Image
from scipy.ndimage import convolve


class LaplacianFilter:
        
    def __init__(self, path):
        self.image = path

    def apply_filter(self):
        # Load The Image
        self.img = np.array(Image.open(self.image).convert('L'))
        # Define the Laplacian filter kernel
        self.laplacian_kernel = np.array([[0, 1, 0],
                                    [1, -4, 1],
                                    [0, 1, 0]])
        # Apply Laplacian filter
        self.laplacian_filtered = convolve(self.img, self.laplacian_kernel, mode="reflect")
        # Convert Array To An Image
        self.img = Image.fromarray(self.laplacian_filtered)
        # Save image
        self.save = input("Do You Need To Save the New Image (Y/N): ")
        if self.save.lower() == 'y':
            if self.img.mode != 'RGB':
                self.img_name = input("Enter Image Name: ")
                self.new_img =self.img.convert('RGB')
                self.new_img.save(f'{self.img_name}.jpg')
        # Show the new image
        self.img.show()

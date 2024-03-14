from PIL import Image
import numpy as np


class MedianFilter:

    def __init__(self, path):
        self.image = path

    def apply_filter(self):
        # Read the image
        self.img = np.array(Image.open(self.image).convert('L'))
        # Apply median filter
        median_filtered = np.empty_like(self.img)
        for i in range(self.img.shape[0]):
            for j in range(self.img.shape[1]):
                median_filtered[i, j] = np.median(self.img[max(i-2,0):i+3, max(j-2,0):j+3])


        # Convert matrix to image
        self.img = Image.fromarray(median_filtered)
        # Save image
        self.save = input("Do You Need To Save the New Image (Y/N): ")
        if self.save.lower() == 'y':
            if self.img.mode != 'RGB':
                self.img_name = input("Enter Image Name: ")
                self.new_img =self.img.convert('RGB')
                self.new_img.save(f'{self.img_name}.jpg')
        # Show Image
        self.img.show()

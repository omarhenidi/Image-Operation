import numpy as np
from PIL import Image

class ImageOperations:

    def __init__(self):
        self.operation = ''
        self.option = ''
        self.img1 = ''
        self.img2 = ''
        self.number = 0

    def choose_operation(self):
        while (True):
            try:
                self.operation = int(input('''Choose The Operation: 
        1- AND
        2- NAND
        3- OR
        4- NOR
        5- XOR
        6- XNOR
                '''))
                if self.operation > 0 and self.operation <= 6:
                    break
                else:
                    print('''
                    Your Input Out Of The Range!
                    Enter Number Between 1 and 6
                    ''')
            except:
                print('Your Input Not Valid Number Please Try Again!')
        return self.operation

    def choose_option(self):
        while (True):
            try:
                self.option = int(input('''Choose Option: 
        1- Image With Image 
        2- Image With Number
            '''))
                if self.option > 0 and self.option <= 2:
                    break
                else:
                    print('''
                    Your Input Out Of The Range!
                    Enter 1 OR 2
                    ''')
            except:
                print('Your Input Not Valid Number Please Try Agine!')

    def input_operand(self):
        while(True):
            if self.option == 1:
                self.img1 = input("Enter First Image Path: ")
                self.img2 = input("Enter Second Image Path: ")
                break
            elif self.option == 2:
                try:
                    self.img1 = input("Enter First Image Path: ")
                    self.number = int(input("Enter An Intger: "))
                    break
                except:
                    print('Your Input Not Valid Please Try Again!')  
            else:
                print('Option Not Recoginized')
        
    def preprocessing(self):
        self.img1 = Image.open(self.img1)
        self.img1 = np.array(self.img1.resize((800,600)))
        if self.option == 1:
            self.img2 = Image.open(self.img2)
            self.img2 = np.array(self.img2.resize((800,600)))
        else:
            self.img2 = self.number
        
    def bitwis_and(self):
        try:
            self.preprocessing()
            im = np.bitwise_and(self.img1, self.img2)
            img = Image.fromarray(im)
            self.save = input("Do You Need To Save the New Image (Y/N): ")
            if self.save.lower() == 'y':
                self.img_name = input("Enter Image Name: ")
                img.save(f'{self.img_name}.jpg')
            img.show()
        except:
            print("Something Went Wrong, Please Try Agine!")
    
    def bitwis_nand(self):
        try:
            self.preprocessing()
            im = np.bitwise_not(np.bitwise_and(self.img1, self.img2))
            img = Image.fromarray(im)
            self.save = input("Do You Need To Save the New Image (Y/N): ")
            if self.save.lower() == 'y':
                self.img_name = input("Enter Image Name: ")
                img.save(f'{self.img_name}.jpg')
            img.show()
        except:
            print("Something Went Wrong, Please Try Agine!")

    def bitwis_or(self):
        try:
            self.preprocessing()
            im = np.bitwise_or(self.img1, self.img2)
            img = Image.fromarray(im)
            self.save = input("Do You Need To Save the New Image (Y/N): ")
            if self.save.lower() == 'y':
                self.img_name = input("Enter Image Name: ")
                img.save(f'{self.img_name}.jpg')
            img.show()
        except:
            print("Something Went Wrong, Please Try Agine!")

    def bitwis_nor(self):
        try:
            self.preprocessing()
            im = np.bitwise_not(np.bitwise_or(self.img1, self.img2))
            img = Image.fromarray(im)
            self.save = input("Do You Need To Save the New Image (Y/N): ")
            if self.save.lower() == 'y':
                self.img_name = input("Enter Image Name: ")
                img.save(f'{self.img_name}.jpg')
            img.show()
        except:
            print("Something Went Wrong, Please Try Agine!")

    def bitwis_xor(self):
        try:
            self.preprocessing()
            im = np.bitwise_xor(self.img1, self.img2)
            img = Image.fromarray(im)
            self.save = input("Do You Need To Save the New Image (Y/N): ")
            if self.save.lower() == 'y':
                self.img_name = input("Enter Image Name: ")
                img.save(f'{self.img_name}.jpg')
            img.show()
        except:
            print("Something Went Wrong, Please Try Agine!")

    def bitwis_xnor(self):
        try:
            self.preprocessing()
            im = np.bitwise_not(np.bitwise_xor(self.img1, self.img2))
            img = Image.fromarray(im)
            self.save = input("Do You Need To Save the New Image (Y/N): ")
            if self.save.lower() == 'y':
                self.img_name = input("Enter Image Name: ")
                img.save(f'{self.img_name}.jpg')
            img.show()
        except:
            print("Something Went Wrong, Please Try Agine!")

    def main(self):
        self.choose_operation()
        self.choose_option()
        self.input_operand()
        if self.operation == 1:
            self.bitwis_and()
        elif self.operation == 2:
            self.bitwis_nand()
        elif self.operation == 3:
            self.bitwis_or()
        elif self.operation == 4:
            self.bitwis_nor()
        elif self.operation == 5:
            self.bitwis_xor()
        elif self.operation == 6:
            self.bitwis_xnor()
        else:
            print("Something Went Wrong, Please Try Agine!")

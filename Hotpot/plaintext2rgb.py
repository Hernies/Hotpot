#first contact
from ctypes import sizeof
from tkinter import Image
import PIL


def test():
    f='test.txt'
    file = open(f)
    text = file.read()
    text = list(text)
    print(text)
    size = len(text)/3
    #img = Image.(('RGB'), size, size) #create 
    file.close()
    #return img.show()

test()
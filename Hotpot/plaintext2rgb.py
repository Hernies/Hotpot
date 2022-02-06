#first contact
from ctypes import sizeof
from PIL import Image
import numpy as n


def test():
    f='test4.txt'
    file = open(f)
    text = file.read()  
    file.close()            # this is dumb, should just read from file instead of dumping it into a 
    text = list(text)       #rudimentary fix, turn text into list so we can manage the characters
    size = n.floor(n.sqrt(len(text)//3))     #will only work for 5px images for now
    print(size)
    img =  Image.new('RGB', (size,size), 'white')
    pixels = img.load() # create the pixel map
    c = 0
    for i in range(img.size[0]):    # for every col:
        for j in range(img.size[1]):    # For every row
            pixels[i,j] = (ord(text[c]),ord(text[c+1]) ,ord(text[c+2]) ) # set the colour accordingly
            c+=1
        c+=1    
    img.show()
        

test()
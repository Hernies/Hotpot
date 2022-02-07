#first contact
from ctypes import sizeof
from PIL import Image
import math as m

#TODO crear el concepto en una funcion tweakeable
#TODO no usar una lista si no leer directamente del archivo
#TODO leer de carpeta de tests y escupir pngs de mismo nombre

def test():
    f='test2.txt'
    file = open(f)
    text = file.read()  
    file.close()            # this is dumb, should just read from file instead of dumping it into a 
    text = list(text)       #rudimentary fix, turn text into list so we can manage the characters
    size = m.floor(m.sqrt(len(text)//3))     #will only work for square images for now
    print(size)
    # for elem in text:
    #     print(ord(elem))

    img =  Image.new('RGB', (size,size))
    pixels = img.load() # create the pixel map
    c = 0
    for i in range(img.size[0]):    # for every col:
        for j in range(img.size[1]):    # For every row
            pixels[i,j] = (ord(text[c]), ord(text[c+1]), ord(text[c+2])) # set the colour accordingly
            c+=1
        c+=1    
    img.show()
    img.save('test2.png')
    
test()        
#stackoverflow random palette example
def palette_tests(textname):
    # Load document as bytes
    qran = pathlib.Path(textname + 'txt').read_bytes()
    size = m.floor(m.sqrt(len(qran)))     #round the value for a square image

    # Make palette image from bytes
    img = Image.frombuffer('P', (size,size), qran, "raw", 'P', 0, 1)

    # Add random palette of 256 RGB triplets to image
    palette = np.random.randint(0,256, 768, np.uint8)
    img.putpalette(palette)

    img.save(textname + 'png')
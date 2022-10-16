import cv2
import random
import os

random.seed(10)

# путь до пикчи абсолютный, относительный не работает
path = "C:\\Users\\User\\Documents\\Python\\Steganography-project\\resources\\apple.bmp"
new_path = "C:\\Users\\User\\Documents\\Python\\Steganography-project\\resources\\apple_new.bmp"
msg = "Hello world\0"

# load image for work
def load_image(path):
    image = cv2.imread(path)
    return image

# https://habr.com/ru/post/304210/
def get_luminosity(image, x, y):
    return image.item(x, y, 0) * 0.0722 + image.item(x, y, 1) * 0.7152 + image.item(x, y, 2) * 0.2126 #BGR

def get_luminosity_old(image, x, y):
    return image.item(x, y, 0) * 0.11448 + image.item(x, y, 1) * 0.58662 + image.item(x, y, 2) * 0.29890 #BGR

# get blue component luminosity value
def get_blue(image, x, y):
    return image.item(x, y, 0)

# decrease blue value
def set_blue_last_0(image, x, y):
    current = get_blue(image, x, y)
    current -= 0.5 * get_luminosity_old(image, x, y)
    if current < 0: current = 0
    #current = 0
    return image.itemset((x, y, 0), current)

# set blue to zero
def set0(image,x,y):
    return image.itemset((x,y,0), 0)

# encrease blue value
def set_blue_last_1(image, x, y):
    current = get_blue(image, x, y)
    current += 0.5 * get_luminosity_old(image, x, y)
    if current > 255: current = 255
    current = 255
    return image.itemset((x, y, 0), current)

# set blue value to 255
def set1(image,x,y):
    return image.itemset((x,y,0), 255)

# some stolen functions for converting string into binary view
def str2bin(text: str, encoding='utf-8') -> str:
    return ''.join(
        bin(c)[2:].rjust(8, '0') for c in text.encode(encoding)
    )

def msgencoder(msg):
    return format(int(bytes(msg, 'utf-8').hex(), base=16), 'b')

def msgdecoder(msg):
    return bytes.fromhex(format(int(msg, base=2), 'x')).decode('utf-8')

def decode_binary_string(s, encoding='UTF-8'):
    byte_string = ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))
    return byte_string.decode(encoding)
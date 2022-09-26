import cv2
import random

random.seed(10)

path = "C:/Users/User/Documents/Python/Steganography-project/resources/kotiki.bmp"
msg = "Hello world"

def load_image(path):
    image = cv2.imread(path)
    return image

# https://habr.com/ru/post/304210/
def get_luminosity(image, x, y):
    return image.item(x, y, 0) * 0.0722 + image.item(x, y, 1) * 0.7152 + image.item(x, y, 2) * 0.2126 #BGR

def get_luminosity_old(image, x, y):
    return image.item(x, y, 0) * 0.114 + image.item(x, y, 1) * 0.587 + image.item(x, y, 2) * 0.299 #BGR

def get_blue(image, x, y):
    return image.item(x, y, 0)

def set_blue_last_0(image, x, y):
    current = get_blue(image, x, y)
    current -= 0.1 * get_luminosity(image, x, y)
    return image.itemset((x, y, 0), current)

def set_blue_last_1(image, x, y):
    current = get_blue(image, x, y)
    current += 0.1 * get_luminosity(image, x, y)
    return image.itemset((x, y, 0), current)

def str2bin(text: str, encoding='utf-8') -> str:
    return ''.join(
        bin(c)[2:].rjust(8, '0') for c in text.encode(encoding)
    )

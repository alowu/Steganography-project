import cv2

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
    current = current >> 1
    current = current << 1
    return image.itemset((x, y, 0), current)

def set_blue_last_1(image, x, y):
    current = get_blue(image, x, y)
    current += 1
    return image.itemset((x, y, 0), current)

# reading the image location through args
# and reading the image using cv2.imread
image = load_image(path)
# printing out the various dimensions of the image
print("width : ", image.shape[1])
print("height : ", image.shape[0])
print("channels : ", image.shape[2])

print("lumi: ", get_luminosity(image, 10, 500)) 
print("lumi old: ", get_luminosity(image, 10, 500))
print("blue", get_blue(image, 10, 10))
set_blue_last_1(image, 10, 10)
print("blue after zero last", get_blue(image, 10, 10))
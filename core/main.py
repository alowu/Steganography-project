# rewrite logic into one file without using functions
import stegano_lib_def as sl
import numpy as np
import cv2

my = 10

msg = "Hello world\0"
msg_str_len = len(msg)
msg_bin = sl.msgencoder(msg)
msg_bin_len = len(msg_bin)
if msg_bin_len % 2 != 0: msg_bin = '0' + msg_bin

image = sl.load_image("C:\\Users\\User\\Documents\\Python\\Steganography-project\\resources\\kotiki.bmp")
new_path = "C:\\Users\\User\\Documents\\Python\\Steganography-project\\resources\\apple_new.bmp"
img_width = image.shape[1]
img_height = image.shape[0]

ind_x = np.random.randint(my + 1, img_height - my, msg_bin_len)
ind_y = np.random.randint(my + 1, img_width - my, msg_bin_len)
rep = 0

for i in range(msg_bin_len):
    if msg_bin[i] == '0':
        print("iteration before zero", i, sl.get_luminosity_old(image, ind_x.item(i), ind_y.item(i)))
        sl.set_blue_last_0(image, ind_x.item(i), ind_y.item(i))
        print("iteration after zero", i, sl.get_luminosity_old(image, ind_x.item(i), ind_y.item(i)))
    else:
        print("iteration before one", i, sl.get_luminosity_old(image, ind_x.item(i), ind_y.item(i)))
        sl.set_blue_last_1(image, ind_x.item(i), ind_y.item(i))
        print("iteration after one", i, sl.get_luminosity_old(image, ind_x.item(i), ind_y.item(i)))

cv2.imwrite(sl.new_path, image)
new_image = sl.load_image(new_path)

#cv2.imshow('img', new_image)
#cv2.waitKey(0)

def get_avg_lum(image, x, y, my):
    sum = 0
    for i in range(1, my + 1):
        sum += sl.get_blue(image, x, y + i)
        sum += sl.get_blue(image, x, y - i)
        sum += sl.get_blue(image, x + i, y)
        sum += sl.get_blue(image, x - i, y)
    return sum/4/my

buffer = ''
msg = ''
for i in range(img_width * img_height):
    #if get_avg_lum(new_image, ind_x.item(i), ind_y.item(i), my) < sl.get_luminosity_old(new_image, ind_x.item(i), ind_y.item(i)):
    #if get_avg_lum(image, ind_x.item(i), ind_y.item(i), my) > sl.get_luminosity(image, ind_x.item(i), ind_y.item(i)):
    if sl.get_blue(new_image, ind_x.item(i), ind_y.item(i)) == 255:
        buffer += "1"
    else:
        buffer += "0"
    if len(buffer) == 8:
        #symbol = sl.msgdecoder(buffer)
        #print(buffer)
        symbol = int(buffer, 2)
        msg += chr(symbol)
        buffer = ''
        print(msg)
        if symbol == '\0':
            break
import stegano_lib_def as sl
import numpy as np

my = 2

seed_ = int(input("enter seed: "))

image = sl.load_image(sl.new_path)
img_width = image.shape[1]
img_height = image.shape[0]

#ind_width = list(range(4,92))
#ind_height = list(range(4, 92))
np.random.seed(seed_)
ind_width = np.random.randint(my + 1, img_width - my, img_width * img_height)
np.random.seed(seed_)
ind_height = np.random.randint(my + 1, img_height - my, img_width * img_height)
print(ind_height)
print(ind_width)

# calculate avg lumi value of near pixels
def get_avg_lum(image, x, y, my):
    sum = 0
    for i in range(1, my + 1):
        sum += sl.get_luminosity_old(image, x - i, y)
        sum += sl.get_luminosity_old(image, x + i, y)
        sum += sl.get_luminosity_old(image, x, y - i)
        sum += sl.get_luminosity_old(image, x, y + i)
    return sum/4/my

buffer = ''
msg = ''
for i in range(img_width * img_height):
    # if avg lum > than current pixel lumi value write 1 to buffer
    if get_avg_lum(image, ind_height.item(i), ind_width.item(i), my) > sl.get_luminosity_old(image, ind_height.item(i), ind_width.item(i)):
        buffer += "1"
    else:
        buffer += "0"
    if len(buffer) == 8: # when buffer get 8 bits convert this buffer to symbol and concatenate to extract message
        #symbol = sl.msgdecoder(buffer)
        symbol = int(buffer, 2)
        msg += chr(symbol)
        buffer = ''
        print(msg)
        if symbol == '\0':
            break

print(msg)

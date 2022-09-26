import stegano_lib_def as sl
import numpy as np

my = 2

image = sl.load_image(sl.path)
img_width = image.shape[1]
img_height = image.shape[0]

msg_bin = sl.str2bin(sl.msg)
msg_len = len(msg_bin)

np.random.seed(10)
ind_width = np.random.randint(my + 1, img_width - my, (2, msg_len))
ind_height = np.random.randint(my + 1, img_height - my, (2, msg_len))
print(ind_height)
print(ind_width)

def encrypt():
    for i in range(msg_len):
        if msg_bin[i] == 0:
            sl.set_blue_last_0(image, ind_height.item(i), ind_width.item(i))
        else:
            sl.set_blue_last_1(image, ind_height.item(i), ind_width.item(i))
    sl.cv2.imshow('img', image)
    sl.cv2.waitKey(0)
    
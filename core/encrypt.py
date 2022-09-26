import stegano_lib_def as sl
import numpy as np

my = 2

seed_ = int(input("enter seed: "))

image = sl.load_image(sl.path)
img_width = image.shape[1]
img_height = image.shape[0]

msg_bin = sl.msgencoder(sl.msg)
msg_len = len(msg_bin)

np.random.seed(seed_)
ind_width = np.random.randint(my + 1, img_width - my, msg_len)
#ind_width = list(range(4, msg_len+ 4))
np.random.seed(seed_)
ind_height = np.random.randint(my + 1, img_height - my, msg_len)
#ind_height = list(range(4, msg_len+ 4))
print(ind_height)
print(ind_width)

def encrypt():
    for i in range(msg_len):
        if msg_bin[i] == 0:
            sl.set_blue_last_0(image, ind_height.item(i), ind_width.item(i))
            #sl.set_blue_last_0(image, ind_height[i], ind_width[i])
        else:
            sl.set_blue_last_1(image, ind_height.item(i), ind_width.item(i))
            #sl.set_blue_last_1(image, ind_height[i], ind_width[i])
    #sl.cv2.imshow('img', image)
    #sl.cv2.waitKey(0)
    sl.cv2.imwrite(sl.new_path, image)

encrypt()
import cv2
import random


def lumi(image, x, y):
    return image.item(x, y, 0) * 0.11448 + image.item(x, y, 1) * 0.58662 + image.item(x, y, 2) * 0.29890  # BGR


def writepixel(image, x, y, bit, q):
    blue = image.item(x, y, 0)

    if bit == 1:
        blue_new = blue + q * lumi(image, x, y)
    else:
        blue_new = blue - q * lumi(image, x, y)

    if blue_new > 255:
        blue_new = 255

    if blue_new < 0:
        blue_new = 0

    image.itemset((x, y, 0), blue_new)
    return 0


def writebit(image, bit, p_x, p_y, q, num_rep):
    for i in range(0, num_rep):
        writepixel(image, p_x, p_y, bit, q)


def writebyte(image, byte, p_x, p_y, q, num_rep):
    ran = len(p_x)
    if ran != 8:
        for i in range(8 - ran):
            bit = 0
            writebit(image, int(bit), p_x[i], p_y[i], q, num_rep)
    for i in reversed(range(0, ran)):
        bit = int(byte) % 10
        writebit(image, int(bit), p_x[i], p_y[i], q, num_rep)
        byte //= 10


def tobinary(a):
    l, m = [], []
    for i in a:
        l.append(ord(i))
    for i in l:
        m.append(int(bin(i)[2:]))
    summ = 8 * len(m)
    yield summ
    yield m


def encode(image, msg, img_path, p_x, p_y, q, num_rep=1):
    img_w = image.shape[1]
    img_h = image.shape[0]
    if len(msg) * 8 * num_rep > (int(img_h) / 4 - 1) * (int(img_w) / 4 - 1):
        print("Picture is small. Please restart program and try again")
        return None
    limit = len(msg)
    for i in range(0, limit):
        bit = msg[i]
        writebyte(image, bit, p_x[i * 8:(i + 1) * 8], p_y[i * 8:(i + 1) * 8], q, num_rep)
    img_path_new = img_path.split('.')[0] + '_encrypted.bmp'
    cv2.imwrite(img_path_new, image)
    return img_path_new


def createlists(amount, max_x, max_y, key='123'):
    random.seed(key)
    a = []
    for i in range(amount):
        a.append(random.randint(4, max_x - 4))
    yield a
    random.seed(key[::-1])
    b = []
    for i in range(amount):
        b.append(random.randint(4, max_y - 4))
    yield b

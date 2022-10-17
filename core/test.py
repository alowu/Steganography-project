import cv2
import numpy as np
import math
import re

q = 0.3
q = input("энергия встраиваемого сигнала: ")
q = float(q)
c = 3
c = input("размер области: ")
c = int(c)
text = "its finnaly works with any string length"
text = input("введите текст: ")

x_pos = c
y_pos = c
num_rep = 1
#num_rep = input("количество повторений: ")
#num_rep = int(num_rep)


kotiki = "C:\\Users\\User\\Documents\\Python\\Steganography-project\\resources\\kotiki.bmp"
apple = "C:\\Users\\User\\Documents\\Python\\Steganography-project\\resources\\apple.bmp"
img = cv2.imread(kotiki)
img_new = "C:\\Users\\User\\Documents\\Python\\Steganography-project\\resources\\apple_new.bmp"
img_w = img.shape[1]
img_h = img.shape[0]

def l(image, x, y):
    return image.item(x, y, 0) * 0.11448 + image.item(x, y, 1) * 0.58662 + image.item(x, y, 2) * 0.29890 #BGR

def b(image, x, y):
    return image.item(x, y, 0)

def toBinary(msg):
    l, m = [],[]
    for i in msg:
        l.append(ord(i))
    for i in l:
        m.append(int(bin(i)[2:]))
    return l

def toBinary2(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(int(bin(i)[2:]))
  return m

def cutZero(s):
    for i in range(0,8):
        if s[i] == "0":
            continue
        if s[i] == "1":
            s_new = s[i:9]
            break
    return s_new

def toString(msg):
    l = []
    m = ""
    for i in msg:
        l.append(chr(i))
    for x in l:
        m += x
    m = m[4:]
    return m

def toString2(a):
  l=[]
  m=""
  for i in a:
    b=0
    c=0
    k=int(math.log10(i))+1
    for j in range(k):
      b=((i%10)*(2**j))   
      i=i//10
      c=c+b
    l.append(c)
  for x in l:
    m=m+chr(x)
  return m

def writePixel(image, x, y, bit, q):
    blue = image.item(x, y, 0)
    blue_new = 0

    if bit == 1:
        blue_new = blue + q * l(image, x, y)
    else:
        blue_new = blue - q * l(image, x, y)

    if blue_new > 255: 
        blue_new = 255

    if blue_new < 0:
        blue_new = 0
    
    image.itemset((x, y, 0), blue_new)
    return 0

def writeBit(image, bit):
    global x_pos; global y_pos
    for i in range(0, num_rep):
        if x_pos + c + 1 >= img_h:
            x_pos = c
            y_pos += c + 1
        writePixel(image, x_pos, y_pos, bit, q)
        x_pos += c + 1

def writeByte(image, byte):
    for i in reversed(range(0, 8)):
        bit = int(byte) % 10
        writeBit(image, int(bit))
        byte /= 10

def readPixel(image, x, y):
    sum = 0
    for i in range(1, c + 1):
        sum += b(image, x + i, y)
        sum += b(image, x - i, y)
        sum += b(image, x, y + i)
        sum += b(image, x, y - i)
    avg = sum/4/c
    blue = b(image, x, y)
    if blue > avg:
        return 1
    else:
        return 0

def readBit(image):
    sum = 0
    global x_pos; global y_pos
    for i in range(0, num_rep):
        if x_pos + c + 1 > img_h:
            x_pos = c
            y_pos += c + 1
        sum += readPixel(image, x_pos, y_pos)
        x_pos += c + 1
    avg = sum#/c/4

    if avg > 0.5:
        return 1
    else:
        return 0

def readByte(image):
    val = ""
    for i in range(0, 8):
        tmp = readBit(image)
        val += str(tmp)
    return val[::-1]

def encode(image, msg):
    global x_pos; x_pos = c
    global y_pos; y_pos = c
    if len(msg) * 8 * num_rep > (int(img_h) / 4 - 1) * (int(img_w) / 4 - 1):
        print("picture is small")
        exit()
    limit = len(msg)
    for i in range(0, limit):
        bit = msg[i]
        writeByte(image, bit)
    cv2.imwrite(kotiki, image)

def decode(image):
    global x_pos; x_pos = c
    global y_pos; y_pos = c
    ll = []
    for i in range(0, 8):
        ll.insert(i,readByte(image))

    len1 = ""
    for i in range(0, 8):
        len1 += str(ll[i])
    #print(len1)

    msg_len = ""

    for i in range(0, 4):
        t = len1[i*8:(i+1)*8]
        n = toString2([int(t)])
        #print(n)
        msg_len += n
    #print(msg_len)
    msg_len = int(msg_len)

    result = ""
    for i in range(0, msg_len):
        t = readByte(image)
        result += toString2([int(t)])

    print(result)
    return result


def addLenMsg(msg):
    leng = len(msg)
    len_m = ""
    if leng > 9999:
        print("message is too big"); exit()
    else:
        tmp = list("00000000")
        i = 3
        while leng >= 1:
            n = int(leng) % 10
            tmp[i] = str(n)
            leng /= 10
            i -= 1
        tmp = "".join(tmp)
        len_m = tmp + msg
        return len_m

#len_m = addLenMsg("")
#print(len_m)
#enc = toBinary(len_m)
#print(enc)
#print(toString(enc))
#print(len(enc))
#fullMsg = []
#ind = 0
#for j in range(0, len(enc)):
#    byte = enc[j]
#    for i in reversed(range(0, 8)):
#        fullMsg.insert(ind, (byte >> i) & 1)
#        ind += 1
        #print(bit)
#print(fullMsg)
#print(len(fullMsg))

#s = "00110000"
#s_new = cutZero(s)
#print(s_new)
#print(toString2([int(s_new)]))



text = addLenMsg(text)
text = toBinary2(text)
encode(img, text)
decode(img)
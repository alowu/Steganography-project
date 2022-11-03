import math


def blue(image, x, y):
    return image.item(x, y, 0)


def tostring(a):
    l = []
    m = ""
    for i in a:
        p = 0
        c = 0
        k = int(math.log10(i)) + 1
        for j in range(k):
            p = ((i % 10) * (2 ** j))
            i = i // 10
            c = c + p
        l.append(c)
    for x in l:
        m = m + chr(x)
    return m


def readpixel(image, x, y, c):
    summ = 0
    for i in range(1, c + 1):
        summ += blue(image, x + i, y)
        summ += blue(image, x - i, y)
        summ += blue(image, x, y + i)
        summ += blue(image, x, y - i)
    avg = summ / 4 / c
    blue_ = blue(image, x, y)
    if blue_ > avg:
        return 1
    else:
        return 0


def readbit(image, num_rep, c, p_x, p_y):
    summ = 0
    for i in range(0, num_rep):
        summ += readpixel(image, p_x, p_y, c)

    if summ > 0.5:
        return 1
    else:
        return 0


def readbyte(image, num_rep, c, p_x, p_y):
    val = ""
    ran = len(p_x)
    for i in range(0, ran):
        tmp = readbit(image, num_rep, c, p_x[i], p_y[i])
        val += str(tmp)
    return val


def decode(image, p_x, p_y, amount_chars, num_rep=1, c=3):
    result = ""
    for i in range(amount_chars):
        x = p_x[i * 8:(i + 1) * 8]
        y = p_y[i * 8:(i + 1) * 8]
        t = readbyte(image, num_rep, c, x, y)
        result += tostring([int(t)])

    print(result)
    return result

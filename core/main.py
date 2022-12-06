import base64
import core.decrypt
import core.encrypt


def texttoimg(text, path, key, q=0.5):
    img = core.encrypt.cv2.imread(path)
    img_w = img.shape[1]
    img_h = img.shape[0]

    amount_bits, text = core.encrypt.tobinary(text)

    key = str(len(text)) + "@" + str(amount_bits) + "@" + key

    key_b = key.encode('ascii')
    base64_bytes = base64.b64encode(key_b)
    key_base64 = base64_bytes.decode('ascii')


    points_x, points_y = core.encrypt.createlists(amount_bits, img_h, img_w, key_base64)
    new = core.encrypt.encode(img, text, path, points_x, points_y, q)
    return new, key_base64


def imgtotext(path, key_base64):
    base64_bytes = key_base64.encode('ascii')
    key_bytes = base64.b64decode(base64_bytes)
    key = key_bytes.decode('ascii')

    amount_chars, amount_bits, key_decode = key.split('@')

    img_decode = core.encrypt.cv2.imread(path)
    img_w_decode = img_decode.shape[1]
    img_h_decode = img_decode.shape[0]
    points_x_decode, points_y_decode = core.encrypt.createlists(int(amount_bits), img_h_decode, img_w_decode, key_base64)
    result = core.decrypt.decode(img_decode, points_x_decode, points_y_decode, int(amount_chars))
    return result


def main(t, k, q, pi, choose):

    if choose == 1:
        if q:
            return texttoimg(t, pi, k, float(q))
        else:
            return texttoimg(t, pi, k)

    elif choose == 2:
        return imgtotext(pi, k)


if __name__ == "__main__":
    main()

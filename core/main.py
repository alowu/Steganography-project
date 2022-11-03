import base64
import decrypt
import encrypt


def texttoimg(text, path, key, q=0.5):
    img = encrypt.cv2.imread(path)
    img_w = img.shape[1]
    img_h = img.shape[0]

    amount_bits, text = encrypt.tobinary(text)

    key = str(len(text)) + "@" + str(amount_bits) + "@" + key

    key_b = key.encode('ascii')
    base64_bytes = base64.b64encode(key_b)
    key_base64 = base64_bytes.decode('ascii')

    print(f'''use this key to decode:
    --->   {key_base64}   <---''')

    points_x, points_y = encrypt.createlists(amount_bits, img_h, img_w, key_base64)
    new = encrypt.encode(img, text, path, points_x, points_y, q)
    if new:
        print(f'Text is saved in image. Path to it is:'
              f'{new}')
    input("Press any key to exit")


def imgtotext(path, key_base64):
    base64_bytes = key_base64.encode('ascii')
    key_bytes = base64.b64decode(base64_bytes)
    key = key_bytes.decode('ascii')

    amount_chars, amount_bits, key_decode = key.split('@')

    img_decode = encrypt.cv2.imread(path)
    img_w_decode = img_decode.shape[1]
    img_h_decode = img_decode.shape[0]
    points_x_decode, points_y_decode = encrypt.createlists(int(amount_bits), img_h_decode, img_w_decode, key_base64)
    result = decrypt.decode(img_decode, points_x_decode, points_y_decode, int(amount_chars))
    print(f'Decrypted text is:'
          f'{result}')
    input("Press any key to exit")


def main():
    choose = int(input('CHOOSE OPTION\n'
                       '1 for encrypt text\n'
                       '2 for decrypt text\n'))

    if choose == 1:
        t = k = pi = ''
        while t == '':
            t = input("Enter text to encrypt: ")
        while k == '':
            k = input("Enter key for encryption: ")
        while pi == '':
            pi = input("Copy path to image: ")
            pi = pi.replace('\\', '\\\\')
        q = input("Enter energy of encryption in range 0.05 to 1 (or click enter, default 0.5): ")
        if q:
            texttoimg(t, pi, k, float(q))
        else:
            texttoimg(t, pi, k)

    elif choose == 2:
        pi = k = ''
        while k == '':
            k = input("Enter key for decryption: ")
        while pi == '':
            pi = input("Copy path to image: ")
            pi = pi.replace('\\', '\\\\')
        imgtotext(pi, k)


if __name__ == "__main__":
    main()

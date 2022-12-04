import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QFileDialog, QLabel, QTextEdit
from PyQt5.QtGui import QPixmap
from PIL import ImageQt



class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.setWindowTitle('Steganography-project')
        self.window_width, self.window_height = 800, 700
        self.setFixedSize(self.window_width, self.window_height)

        uic.loadUi('image.ui', self)

        self.OpenFileButton = self.findChild(QPushButton, 'OpenFileButton')
        self.SaveFileButton = self.findChild(QPushButton, 'SaveFileButton')
        self.EncryptButton = self.findChild(QPushButton, 'EncryptButton')
        self.DecryptButton = self.findChild(QPushButton, 'DecryptButton')
        self.EEButton = self.findChild(QPushButton, 'EEButton')
        self.KEButton = self.findChild(QPushButton, 'KEButton')
        self.labelLeft = self.findChild(QLabel, 'labelLeft')
        self.labelRight = self.findChild(QLabel, 'labelRight')
        self.textToEncrypt = self.findChild(QTextEdit, 'textToEncrypt')
        self.textKeyForEncryption = self.findChild(QTextEdit, 'textKeyForEncryption')
        self.textEnergy = self.findChild(QTextEdit, 'textEnergy')
        self.textKeyForDecryption = self.findChild(QTextEdit, 'textKeyForDecryption')
        self.textDecrypt = self.findChild(QTextEdit, 'textDecrypt')

        self.OpenFileButton.clicked.connect(self.open_image)
        self.SaveFileButton.clicked.connect(self.save_image)
        self.EncryptButton.clicked.connect(self.clicker_encrypt_button)

        self.show()

    def open_image(self):
        iname = QFileDialog.getOpenFileName(self, 'Open Image', 'D:\\Steganography-project\\resources', 'Image (*.bmp)')
        self.pixmapLeft = QPixmap(iname[0])
        self.labelLeft.setPixmap(self.pixmapLeft)

    def save_image(self):
        image = ImageQt.fromqpixmap(self.labelRight.pixmap())
        image.save('test.jpg')

    def clicker_encrypt_button(self):
        text = self.textToEncrypt.toPlainText()
        with open('text.txt', 'w') as f:
            f.write(text)

        flag = 1



if __name__ == '__main__':
    app = QApplication(sys.argv)
    MyApp = MyApp()
    sys.exit(app.exec_())

# coding: utf-8

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QFileDialog, QLabel, QTextEdit, QTextBrowser, QMessageBox
from PyQt5.QtGui import QPixmap
from PIL import ImageQt
from core.main import main

fnamer = ''    #глобальная переменная для хранения пути к правому изображению
fnamel = ''    #глобальная переменная для хранения пути к левому изображению


class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.window_width, self.window_height = 800, 700
        self.setFixedSize(self.window_width, self.window_height)

        uic.loadUi('project.ui', self)

        self.LeftOpenFileButton = self.findChild(QPushButton, 'LeftOpenFileButton')
        self.RightOpenFileButton = self.findChild(QPushButton, 'RightOpenFileButton')
        self.SaveFileButton = self.findChild(QPushButton, 'SaveFileButton')
        self.EncryptButton = self.findChild(QPushButton, 'EncryptButton')
        self.DecryptButton = self.findChild(QPushButton, 'DecryptButton')
        self.labelLeft = self.findChild(QLabel, 'labelLeft')
        self.labelRight = self.findChild(QLabel, 'labelRight')
        self.textToEncrypt = self.findChild(QTextEdit, 'textToEncrypt')
        self.textEncryptionKey = self.findChild(QTextEdit, 'textEncryptionKey')
        self.textEnergy = self.findChild(QTextEdit, 'textEnergy')
        self.textDecryptionKey = self.findChild(QTextEdit, 'textDecryptionKey')
        self.textKeyBrowser = self.findChild(QTextBrowser, 'textKeyBrowser')
        self.textDecryptionMessageBrowser = self.findChild(QTextBrowser, 'textDecryptionMessageBrowser')
        self.AboutAppButton = self.findChild(QPushButton, 'AboutAppButton')


        self.LeftOpenFileButton.clicked.connect(self.open_left_image)
        self.RightOpenFileButton.clicked.connect(self.open_right_image)
        self.SaveFileButton.clicked.connect(self.save_image)
        self.EncryptButton.clicked.connect(self.clicker_encrypt_button)
        self.DecryptButton.clicked.connect(self.clicker_decrypt_button)
        self.AboutAppButton.clicked.connect(self.show_dialog)

        self.show()

    def open_left_image(self):
        global fnamel
        fnamel = QFileDialog.getOpenFileName(self, 'Open Image', '', 'Image (*.bmp)')[0]    #функция getOpenFileName() возвращает список из двух значений: путь к файлу и расширение; поэтому мы берём только перую переменную (путь к файлу) из возвращаемого списка
        self.pixmapLeft = QPixmap(fnamel)
        self.labelLeft.setPixmap(self.pixmapLeft)

    def open_right_image(self):
        global fnamer
        fnamer = QFileDialog.getOpenFileName(self, 'Open Image', '', 'Image (*.bmp)')[0]    #функция getOpenFileName() возвращает список из двух значений: путь к файлу и расширение; поэтому мы берём только перую переменную (путь к файлу) из возвращаемого списка
        self.pixmapRight = QPixmap(fnamer)
        self.labelRight.setPixmap(self.pixmapRight)

    def save_image(self):
        image = ImageQt.fromqpixmap(self.labelRight.pixmap())
        name, _ = QFileDialog.getSaveFileName(self, 'Save Image With Decryption Message', '', 'Image (*.bmp)')
        image.save(name)


    def clicker_encrypt_button(self):
        flag = 1
        Message = self.textToEncrypt.toPlainText()
        Key = self.textEncryptionKey.toPlainText()
        Energy = self.textEnergy.toPlainText()

        path_and_key = main(Message, Key, Energy, fnamel, flag)
        global fnamer
        fnamer = path_and_key[0]
        DecryptionKey = path_and_key[1]

        self.pixmapRight = QPixmap(fnamer)
        self.labelRight.setPixmap(self.pixmapRight)

        self.textKeyBrowser.setText(DecryptionKey)

    def clicker_decrypt_button(self):
        flag = 2
        Key = self.textDecryptionKey.toPlainText()
        global fnamer
        print(fnamer, Key)

        DecryptionMessage = main('', Key, '', fnamer, flag)
        print(DecryptionMessage)
        self.textDecryptionMessageBrowser.setText(DecryptionMessage)

    def show_dialog(self):
        MsgBox = QMessageBox()
        MsgBox.setIcon(QMessageBox.Information)
        file = open('README.txt',  'r', encoding='utf-8')
        AboutText = file.read()
        file.close()
        MsgBox.setText(AboutText)
        MsgBox.setWindowTitle("About App")
        MsgBox.setStandardButtons(QMessageBox.Ok)
        retval = MsgBox.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MyApp = MyApp()
    sys.exit(app.exec_())

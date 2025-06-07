import sys
from PyQt5.QtWidgets import QApplication, QTextBrowser, QMainWindow,QPushButton
from PyQt5.QtGui import QColor, QPalette, QFont
from PyQt5.QtCore import QFile, QTextStream, Qt, QPropertyAnimation, QRect


class TextBrowserDemo(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建 QTextBrowser 控件
        self.textbrowser = QTextBrowser(self)
        self.setCentralWidget(self.textbrowser)
        self.setFixedSize(1000, 2000)

        # # 设置背景色为黑色
        # palette = self.textbrowser.palette()
        # palette.setColor(QPalette.Base, QColor('black'))
        # self.textbrowser.setPalette(palette)
        # 设置窗口属性以允许背景透明
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 无边框窗口

        # 设置窗口背景为半透明黑色
        self.setStyleSheet("background-color: rgba(0, 0, 0, 128);")  # RGBA中的128表示50%的透明度

        # 设置中文字体
        self.textbrowser.setStyleSheet("color: white;")  # 设置文本颜色为白色
        self.textbrowser.setFont(QFont("宋体", 12))  # 设置字体和大小，根据需要选择合适的字体
        self.textbrowser.setAlignment(Qt.AlignLeft | Qt.AlignTop)  # 设置文本对齐方式
        # font = QFont("Microsoft YaHei")
        # self.textbrowser.setFont(font)
        # 添加关闭按钮
        self.close_button = QPushButton('x', self)
        self.close_button.setFont(QFont("黑体", 12))  # 设置按钮字体
        self.close_button.setStyleSheet("background-color: rgba(0, 0, 0, 128); color: white; border-radius: 5px;")  # 设置按钮样式
        self.close_button.setGeometry(958, 0, 40, 30)  # 设置按钮的位置和大小
        self.close_button.clicked.connect(self.close)  # 点击按钮时关闭窗口

    def displaytextfile(self, filepath):
        # 打开文件并指定UTF-8编码
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            self.textbrowser.setText(content)

        # 调整窗口大小以适应内容
        self.adjustSize()

        # 设置动画
        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(500)
        initial_x = -self.width()
        self.animation.setStartValue(QRect(initial_x, 0, self.width(), self.height()))
        self.animation.setEndValue(QRect(0, 0, self.width(), self.height()))
        self.animation.start()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    demo = TextBrowserDemo()
    demo.displaytextfile('./output.txt')
    demo.show()
    sys.exit(app.exec())

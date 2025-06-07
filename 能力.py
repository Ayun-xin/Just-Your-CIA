# -*- coding: utf-8 -*-
import sys

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox
)
from PyQt5.QtCore import QFile, QTextStream, Qt, QPropertyAnimation, QRect
from PyQt5.QtWidgets import QApplication, QTextBrowser, QMainWindow,QPushButton
class AbilityInputWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('能力')

        self.setGeometry(1000, 500, 400, 300)

        layout = QVBoxLayout()

        # 创建五个能力输入框
        self.ability_inputs = []
        for i in range(1, 7):
            hbox = QHBoxLayout()
            label = QLabel(f'能力{i}:')
            hbox.addWidget(label)
            input_box = QLineEdit()
            hbox.addWidget(input_box)
            self.ability_inputs.append(input_box)
            layout.addLayout(hbox)

        # 创建保存按钮
        save_button = QPushButton('保存')
        save_button.clicked.connect(self.save_abilities)
        layout.addWidget(save_button)

        self.setLayout(layout)

    def save_abilities(self):
        abilities = [input_box.text() for input_box in self.ability_inputs]
        with open('abilities.txt', 'w',encoding='utf-8') as file:
            for ability in abilities:
                file.write(ability + '\n')
        QMessageBox.information(self, '提示', '能力已保存到abilities.txt文件中')
        with open('abilities_tool.txt', 'w',encoding='utf-8') as file:
            for ability in abilities:
                file.write(ability+'工具'+ '\n')
        QMessageBox.information(self, '提示', '工具已保存到abilities_tool.txt文件中')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AbilityInputWindow()
    window.show()
    sys.exit(app.exec_())

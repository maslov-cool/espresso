import io
import sys

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt6.QtGui import QColor
import sqlite3

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1000</width>
    <height>600</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>1000</width>
    <height>600</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>1000</width>
    <height>600</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QTableWidget" name="table">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>1000</width>
      <height>600</height>
     </rect>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>1000</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)  # Загружаем дизайн

        connection = sqlite3.connect('coffee.sqlite')
        cursor = connection.cursor()

        query = '''SELECT * FROM table_for_coffee'''
        result = cursor.execute(query).fetchall()[::-1]

        self.table.setRowCount(len(result))
        self.table.setColumnCount(7)

        # Закрашиваем шапку таблицы (горизонтальные заголовки)
        self.table.horizontalHeader().setStyleSheet(
            "QHeaderView::section { background-color: rgb(255, 170, 127);}")

        # Закрашиваем боковую шапку таблицы (вертикальные заголовки)
        self.table.verticalHeader().setStyleSheet(
            "QHeaderView::section { background-color: rgb(255, 170, 127);}")

        # Устанавливаем заголовки столбцов
        header_labels = ['ID', 'Название_сорта', 'Степень_обжарки', 'Молотый/в_зернах', 'Описание_вкуса', 'Цена',
        'Объём_упаковки']
        self.table.setHorizontalHeaderLabels(header_labels)

        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                item = QTableWidgetItem(str(val))
                item.setBackground(QColor(85, 255, 255))
                self.table.setItem(i, j, item)

        connection.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())

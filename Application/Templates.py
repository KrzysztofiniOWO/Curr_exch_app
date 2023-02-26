from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore



class My_widgets(QWidget):
    """Class specified to create table to store our currencies data"""

    def __init__(self):
        """We initialize our table class"""

    def create_currency_table(self, names, prices_buy, prices_sell):
        """We create table to store our data"""

        #We create table and set it's size
        table = QTableWidget()
        table.setRowCount(len(names)+1)
        table.setColumnCount(3)

        #We make headers invisible, because we don't need them
        table.verticalHeader().setVisible(False)
        table.horizontalHeader().setVisible(False)

        #We set sizes of out table, columns and rows
        table.resizeRowsToContents()
        table.setFixedWidth(510)
        table.setFixedHeight(640)
        table.verticalHeader().setMinimumSectionSize(30)
        table.setColumnWidth(0, 300)
        table.setColumnWidth(1, 100)
        table.setColumnWidth(2, 98)
        table.resizeRowsToContents()

        #We make stylesheet for our table
        table.setStyleSheet(
            "font-size: 20px;" +
            "background: #8bd6ff;" +
            "border: 5px solid '#00c4ff';" +
            "QHeaderView::section { color:white; background-color:#232326; }"
        )

        #We set our data inside table

        #We set our header names
        names.insert(0, "Names")
        prices_buy.insert(0, "Buy")
        prices_sell.insert(0, "Sell")

        #We fill other cells in our table
        for row in range(0, len(names)):
            table.setItem(row, 0, QTableWidgetItem(names[row]))
            table.setItem(row, 1, QTableWidgetItem(prices_buy[row]))
            table.setItem(row, 2, QTableWidgetItem(prices_sell[row]))

        return table

    def create_button(self, text, connection, margin):
        """Function to make creating new buttons easier in our app"""

        #We create button and make it interactive
        button = QPushButton(text)
        button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        #We connect our button to class it's supposed to work with
        button.clicked.connect(connection)

        #We set max widthh for our button
        button.setMaximumWidth(800)

        #We make stylesheet for our button with padding
        button.setStyleSheet(
            "*{font-size: 35px;" +
            "color: '#121b27';" +
            "padding: 25px 20px;" +
            "margin: 30px 100px;" +
            "background: '#8bd6ff';" +
            "border: 5px solid '#00c4ff';" +
            "border-radius: 30px;" +
            "text-align: center;}" +
            "*:hover{background: '#a8fff7';}"
        )

        if not margin:
            button.setStyleSheet(
                "*{font-size: 35px;" +
                "color: '#121b27';" +
                "padding: 25px 20px;" +
                "background: '#8bd6ff';" +
                "border: 5px solid '#00c4ff';" +
                "border-radius: 30px;" +
                "text-align: center;}" +
                "*:hover{background: '#a8fff7';}"
            )

        return button

    def create_logo(self, path):
        """Function to make creating new images easier in our app"""

        #We import our image
        image = QPixmap(path)

        #We set our image on logo and style it a bit
        logo = QLabel()
        logo.setPixmap(image)
        logo.setAlignment(QtCore.Qt.AlignCenter)
        logo.setStyleSheet("margin-top: 30px;")

        return logo

    def create_combo_box(self, items, width, height):
        """Function to make creating combo boxes easier in our app"""

        #We create_combo box and fill it with items
        combo_box = QComboBox()
        combo_box.addItems(items)
        combo_box.setFixedWidth(width)
        combo_box.setFixedHeight(height)

        # We make stylesheet for our button
        combo_box.setStyleSheet(
            "QComboBox" +
            "{" +
            "background: '#8bd6ff';" + "border: 5px solid '#00c4ff';" +
            "padding: 8px;" + "font-size: 18px;" + "margin: 0px 50px;"
            "}" +
            "QComboBox QListView" +
            "{" +
            "background: '#8bd6ff';" + "padding: 10px;" + "border: 5px solid '#00c4ff';"
            "}" +
            "QComboBox::drop-down" +
            "{" +
            "border: 0px;" + "padding-right: 10px;"
            "}" +
            "QComboBox::down-arrow" +
            "{" +
            "image: url(down_arrow.png);" +
            "border-width: 0px;" +
            "float: right;" +
            "}"
        )

        return combo_box

    def create_qlineedit(self, text):
        """Function to make creating user input fields easier in our app"""

        # We create input box and set text in it
        input_box = QLineEdit(text)

        #We align text to the center of input box
        input_box.setAlignment(QtCore.Qt.AlignCenter)

        # We make stylesheet for our input box
        input_box.setStyleSheet(
            "*{font-size: 35px;" +
            "color: '#121b27';" +
            "padding: 25px 20px;" +
            "margin: 30px 100px;" +
            "background: '#ffe79a';" +
            "border: 5px solid '#ffa952';" +
            "border-radius: 30px;}"
        )

        return input_box

    def create_label(self, text):
        """Function to make creating labels easier in our app"""

        #We create label and fill it with given text
        label = QLabel(text)

        #We set sizes and alignment for our labels
        label.setAlignment(Qt.AlignCenter)
        label.adjustSize()
        label.setFixedHeight(60)

        # We make stylesheet for our label
        label.setStyleSheet(
            "font-size: 30px;"
        )

        return label



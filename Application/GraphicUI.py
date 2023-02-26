import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QMessageBox
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtGui, QtCore
from Application import Scrapper, Templates



widgets = {
    "button": [],
    "logo": [],
    "label": [],
    "table": [],
    "combo_box": [],
    "group_box": [],
    "q_line": []
}


class Window(QWidget):
    """Main window for application"""

    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 1200, 800)
        self.setStyleSheet("background-color: #2072d8;")
        self.setWindowTitle("Currencies")
        self.setWindowIcon(QtGui.QIcon('dolar.png'))
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.home()

    def home(self):

        #We clear our grid (when changing frame in application)
        self.clear_grid()

        #We create logo for our main menu
        logo_main_menu = Templates.My_widgets.create_logo(self, "exchange.png")
        widgets["logo"].append(logo_main_menu)

        # We create button to check buy/sell price of currencies
        curr_tab_butt = Templates.My_widgets.create_button(self, "Check buy/sell prices", self.currencies_buy_sell, True)
        widgets["button"].append(curr_tab_butt)

        #We create button leading to our exchange calculator
        exch_tab_butt = Templates.My_widgets.create_button(self, "Calculate currencies", self.exchange_calculator, True)
        widgets["button"].append(exch_tab_butt)

        # We create exit button
        exit_butt = Templates.My_widgets.create_button(self, "Quit", QCoreApplication.instance().quit, True)
        widgets["button"].append(exit_butt)

        #Add our elements to grid
        self.grid.addWidget(widgets["logo"][-1], 0, 0)
        self.grid.addWidget(widgets["button"][-3], 1, 0)
        self.grid.addWidget(widgets["button"][-2], 2, 0)
        self.grid.addWidget(widgets["button"][-1], 3, 0)

        self.show()

    def currencies_buy_sell(self):
        """Frame to show user prices of currencies"""

        # We clear our grid (when changing frame in application)
        self.clear_grid()

        #We reach for data we scrapped in Scrapper.py
        currency_names = Scrapper.get_currency_names()
        currency_buy_prices = Scrapper.get_currency_buy()
        currency_sell_prices = Scrapper.get_currency_sell()

        #Table showing currencies prices
        table = Templates.My_widgets.create_currency_table(self, currency_names, currency_buy_prices, currency_sell_prices)
        widgets["table"].append(table)

        #Button to go back to main menu
        go_back_button = Templates.My_widgets.create_button(self, "Go back", self.home, True)
        widgets["button"].append(go_back_button)

        # Add our elements to grid
        self.grid.addWidget(widgets["table"][-1], 0, 0)
        self.grid.addWidget(widgets["button"][-1], 1, 0)

        self.show()

    def exchange_calculator(self):
        """Frame to calculate currencies"""

        # We clear our grid (when changing frame in application)
        self.clear_grid()

        # We reach for data we scrapped in Scrapper.py
        currency_names = Scrapper.get_currency_names()
        currency_buy_prices = Scrapper.get_currency_buy()
        currency_sell_prices = Scrapper.get_currency_sell()

        # We create label on top of the screen
        top_label = Templates.My_widgets.create_label(self, "Enter amount you want to exchange")
        widgets["label"].append(top_label)

        # We create label on top of the combo box
        from_label = Templates.My_widgets.create_label(self, "From")
        widgets["label"].append(from_label)

        # We create label on top of the combo box
        to_label = Templates.My_widgets.create_label(self, "To")
        widgets["label"].append(to_label)

        # We create input box for user to write amount he wants to exchange
        input_amount = Templates.My_widgets.create_qlineedit(self, "0")
        widgets["q_line"].append(input_amount)

        #We create combo box to select which currency we exchange
        from_sell_exch = Templates.My_widgets.create_combo_box(self, currency_names, 300, 50)
        widgets["combo_box"].append(from_sell_exch)

        #We create combo box to select currency which we exchange to
        to_sell_exch = Templates.My_widgets.create_combo_box(self, currency_names, 300, 50)
        widgets["combo_box"].append(to_sell_exch)

        #Button to go back to main menu
        go_back_butt = Templates.My_widgets.create_button(self, "Go back", self.home, False)
        widgets["button"].append(go_back_butt)

        #We create arrow pointing right between currencies to exchange
        right_arrow = Templates.My_widgets.create_logo(self, "arrow-right.png")
        widgets["logo"].append(right_arrow)

        # We add button to calculate currencies
        calculate_button = Templates.My_widgets.create_button(self, "Calculate", self.calculate_currencies, True)
        widgets["button"].append(calculate_button)

        # Add our elements to grid
        self.grid.addWidget(widgets["label"][-3], 0, 1)
        self.grid.addWidget(widgets["label"][-2], 2, 0)
        self.grid.addWidget(widgets["label"][-1], 2, 2)
        self.grid.addWidget(widgets["q_line"][-1], 1, 1)
        self.grid.addWidget(widgets["combo_box"][-2], 3, 0)
        self.grid.addWidget(widgets["logo"][-1], 2, 1, 2, 1)
        self.grid.addWidget(widgets["combo_box"][-1], 3, 2)
        self.grid.addWidget(widgets["button"][-1], 4, 1)
        self.grid.addWidget(widgets["button"][-2], 5, 1)

        self.show()

    def calculate_currencies(self):
        """Function used to calculate currencies"""

        #We get current values of combo boxes and input boxes
        name_from = widgets["combo_box"][-2].currentText()
        name_to = widgets["combo_box"][-1].currentText()
        amount = widgets["q_line"][-1].text()

        # We change our amount to int
        amount = int(amount)

        # We reach for data we scrapped in Scrapper.py
        currency_names = Scrapper.get_currency_names()
        currency_buy_prices = Scrapper.get_currency_buy()
        currency_sell_prices = Scrapper.get_currency_sell()

        #We get indexes of currencies we want to work with
        index_from = currency_names.index(name_from)
        index_to = currency_names.index(name_to)

        #We calculate middle buy/sell prices of currencies we use
        mid_from_price = ((float(currency_sell_prices[index_from].replace(",", ".")) + float(currency_buy_prices[index_from].replace(",", "."))) / 2)
        mid_to_price = ((float(currency_sell_prices[index_to].replace(",", ".")) + float(currency_buy_prices[index_to].replace(",", "."))) / 2)
        amount_in_new_currency = round(((mid_from_price / mid_to_price) * amount), 2)

        #We create pop up window with new amount
        ans = QMessageBox()
        ans.setWindowTitle("Your new amount")
        ans.setText(f"For {amount} {currency_names[index_from]} you can get"
                    f" {amount_in_new_currency} {currency_names[index_to]}")
        ans.exec()

    def clear_grid(self):
        """Clear all items from grid when visiting new page in app"""

        for i in reversed(range(self.grid.count())):
            self.grid.itemAt(i).widget().setParent(None)




def main():
    app = QApplication(sys.argv)
    gui = Window()
    sys.exit(app.exec_())


main()

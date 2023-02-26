from bs4 import BeautifulSoup as bs
import requests

#Webpage with currencies buy/sell prices
page = requests.get("https://internetowykantor.pl/kursy-walut/")

#We read html code
soup = bs(page.content, features="html.parser")


def get_currency_names():
    """Get names of currencies"""

    #Get lines that interest us
    currency_names_scrap = soup.find_all(class_='nameplate__long-name')

    #Create empty list to store names
    currency_names = []

    #Find names
    for currency_name in currency_names_scrap:
        currency_name = str(currency_name)
        start_idx = currency_name.index(">")
        end_idx = currency_name.index("/") - 1
        currency_names.append(currency_name[start_idx + 1:end_idx])

    # Return names of currencies
    return currency_names


def get_currency_buy():
    """Get buy price of currencies"""

    # Get lines that interest us
    currency_buy_sell_scrap = soup.find_all(class_='bem-rate-table__rate')

    # Create empty list to store buy prices of currencies
    currency_buy = []

    #Find buy prices of currencies
    for line in currency_buy_sell_scrap:
        line = str(line)

        if "buy" in line:
            start_idx = line.index('"buy">')
            end_idx = line.index("/") - 1
            currency_buy.append(line[start_idx+6:end_idx])

    #Return buy prices of currencies
    return currency_buy


def get_currency_sell():
    """Get sell price of currencies"""

    # Get lines that interest us
    currency_buy_sell_scrap = soup.find_all(class_='bem-rate-table__rate')

    # Create empty list to store sell prices of currencies
    currency_sell = []

    # Find sell prices of currencies
    for line in currency_buy_sell_scrap:
        line = str(line)

        if "sell" in line:
            start_idx = line.index('"sell">')
            end_idx = line.index("/") - 1
            currency_sell.append(line[start_idx+7:end_idx])

    # Return sell prices of currencies
    return currency_sell

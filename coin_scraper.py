# Import libraries
import requests
from bs4 import BeautifulSoup
import warnings

# Supress warning messages
warnings.filterwarnings("ignore")

# Initialize the class
class Coin_Crawl:

    def __init__(self, url = "https://coinmarketcap.com/exchanges/binance/"):
        '''
		Function that establishes connection wit the url and obtains
        table with coin price values
		   
		Input: url stored as string from specific market of coinmarketcap.
		Output: None
		'''
        conn = requests.get(url) # Establish connection (instance variable)
        soup = BeautifulSoup(conn.content) # Obtain content (instance variable)
        # Get table with data (class variable)
        self.table = soup.find_all("table",
                     {"class":"table no-border table-condensed"})
    
    def calc_val(self, coin_name, num_coins):
        '''
		Function that extracts the coin market value from the given url
		   
		Input: Name of coin stored as string, Number of coins
		Output: Current market value of coin
		        Print statements showing total value in USD
		'''
        counter = 0 # Set a counter to find the index of ripple
        for coin in self.table: # Loop through the table to find coin
            for name in coin.find_all("a",
                                      {"class":"market-name"}):
                # Check when coin_name is found
                if name.text == coin_name:
                    coin_value = coin.find_all("span",
                                               {"class":"price"})[counter].text
                # Adjust counter indice
                counter += 1
        # Convert the coin value format
        coin_value = float(coin_value.replace('$',"").strip())
        # Print value in USD
        print(str(coin_name) + ' price in USD: ' +\
              str(round(coin_value,4)) + '$\n')
        # Print my value in USD
        print('My value of ' + coin_name + ' in USD: ' +\
              str(round(coin_value*num_coins,2)) + '$\n')
        return coin_value

# Calculate the coin value using the above class
c_val = Coin_Crawl(url = "https://coinmarketcap.com/exchanges/binance/")
ripple_value = c_val.calc_val(coin_name = "Ripple", num_coins = 189.810)
tron_value = c_val.calc_val(coin_name = "TRON", num_coins = 3356.640)
print('Total value in USD: ' +\
      str(round(tron_value*3356.640+ripple_value*189.810,2)) + '$\n')
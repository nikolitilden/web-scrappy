import urllib
import json

#Stock Tickers will only run for the time the stocks are open!!

htmltext = urllib.urlopen("http://www.bloomberg.com/markets/watchlist/recent-ticker/GOOG:US")

data = json.load(htmltext)

print data

print "The price of the stock is: ", data['last_price']

#
# Btcoin prices using JSon data
# Author: Chiheb NeXus
# Blog: https://nexus-coding.blogspot.com
# Bitcoin Ticker: https://www.bitstamp.net/api/ticker
#
#!/usr/bin python3

from urllib.request import urlopen as UrlOpen
from urllib.error import HTTPError as HTTPError
from json import loads as Load
from datetime import datetime as Time

class BitcoinPrice:
	def __init__(self, url):
		"""
		Class constructor
		"""
		try:
			response = UrlOpen(url)
			content = response.read()
			data = Load(content.decode("UTF-8"))
			self.bitcoin_data(data)

		except HTTPError as error:
			print("Error Code: {}".format(error.code))

	def convert_timestamp(self,timestamp):
		""""
		Covert timestamp to a readable time
		"""
		return Time.fromtimestamp(int(timestamp)).strftime("%Y-%m-%d | %H:%M:%S")

	def bitcoin_data(self,data):
		"""
		print data
		*nix Bash colors:
		Black        0;30     Dark Gray     1;30
		Red          0;31     Light Red     1;31
		Green        0;32     Light Green   1;32
		Brown/Orange 0;33     Yellow        1;33
		Blue         0;34     Light Blue    1;34
		Purple       0;35     Light Purple  1;35
		Cyan         0;36     Light Cyan    1;36
		Light Gray   0;37     White         1;37

		Example: 
			Green: \x1B[32;40m {0} \x1B[0m 
			Red: \x1B[31;40m {0} \x1B[0m
		"""
		

		print("\n\
	High price[1]: \x1B[32;40m{0} $\x1B[0m\t\tLow price[2]: \x1B[32;40m{1} $\x1B[0m\tLast price[3]: \x1B[32;40m{2} $\x1B[0m\n\
	Ask price[4]: \x1B[32;40m{3} $\x1B[0m\t\tBid price[5]: \x1B[32;40m{4} $\x1B[0m\tOpen price: \x1B[32;40m{5} $\x1B[0m\n\
	Volume[6]: \x1B[32;40m{6} BTC\x1B[0m\tVWAP[7]: \x1B[32;40m{7} $\x1B[0m\n\
	\t\t\tDate|Time: \x1B[32;40m{8}\x1B[0m\n\n\
	[1]High price: Last 24 hours BTC price high\n\
	[2]Low price*: Last 24 hours BTC price low\n\
	[3]Last price*: Last BTC price\n\
	[4]Ask price*: Lowest sell order\n\
	[5]Bid price: highest buy order\n\
	[6]Volume*: Last 24 hours volume\n\
	[7]VWAP*: Last 24 hours Volume Weighted Average Price\n"
				.format(data["high"], data["low"], data["last"],
						data["ask"], data["bid"], data["open"],
						data["volume"], data["vwap"], self.convert_timestamp(data["timestamp"]))
			)

if __name__ == '__main__':
	url = "https://www.bitstamp.net/api/ticker/"
	price = BitcoinPrice(url)

	
		



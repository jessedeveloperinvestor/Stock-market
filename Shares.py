#RUN THE FOLLOWING LINES ON TERMINAL:
#pip install alpha_vantage
#pip install pandas
#pip install sqlite3
#pip install json
#pip install requests
#pip install time
#pip install datetime

#CREATE TABLE - Run the function createtable() to create the table
from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import datetime as dt
import requests
import sqlite3
import time
import datetime
import json

#SHARES:
a1='B3SA3'
a2='PETR4'
a3=''
a4=''
a5=''
a6=''
a7=''

#SHARES' ACTIVATOR:
b1=1
b2=1
b3=0
b4=0
b5=0
b6=0
b7=0

#SELECT TICKER:
symbol=a1
stock_ticker=symbol+'.SAO'
i=0

#RESULTS:

def results():
	#ALPHA VANTAGE API:
	def alpha_vantage_api():
		API_Key='KY74URGMWMKH6FJ8'
		ts = TimeSeries (key=API_Key, output_format = "pandas")
		data_daily, meta_data = ts.get_daily(symbol=stock_ticker, outputsize ='compact')
		        # data_daily['column name'][row number]
		daterow=meta_data['3. Last Refreshed'][i]
		data_daily_lastClosingPrice = data_daily['4. close'][i]

	#ACTIVATOR:
	if b1==1:
		alpha_vantage_api()
	else:
		print(symbol,' não está habilitado/ is not active')


	conn=sqlite3.connect('shares.db')
	c=conn.cursor()

	def createtable():
		c.execute("""CREATE TABLE shares (
					ticker text,
					date integer,
					price real
		)""")
		conn.commit()

	def insert():
		from alpha_vantage.timeseries import TimeSeries
		import pandas as pd
		API_Key='KY74URGMWMKH6FJ8'
		ts = TimeSeries (key=API_Key, output_format = "pandas")
		data_daily, meta_data = ts.get_daily(symbol=stock_ticker, outputsize ='compact')
		daterow=meta_data['3. Last Refreshed']
		data_daily_lastClosingPrice = data_daily['4. close'][i]
		date=daterow
		c.execute('''INSERT INTO  shares (ticker, date, price) VALUES (?, ?, ?) ''',(stock_ticker, date, data_daily_lastClosingPrice))
		conn.commit()

	def select():
		c.execute("SELECT * FROM shares WHERE ticker='B3SA3.SAO'")
		#print(c.fetchall())
		print(c.fetchone())

	def update():
		try:
			c.execute('SELECT * FROM shares')
			[print(row) for row in c.fetchall()]
			c.execute('''UPDATE shares (ticker, date, price) SET value = (?) WHERE value = (?)''',(data_daily_lastClosingPrice, data_daily_lastClosingPrice))
			conn.commit()
		except:
			c.execute('DELETE FROM shares')
			conn.commit()
			from alpha_vantage.timeseries import TimeSeries
			import pandas as pd
			API_Key='KY74URGMWMKH6FJ8'
			ts = TimeSeries (key=API_Key, output_format = "pandas")
			data_daily, meta_data = ts.get_daily(symbol=stock_ticker, outputsize ='compact')
			daterow=meta_data['3. Last Refreshed']
			data_daily_lastClosingPrice = data_daily['4. close'][i]
			date=daterow
			c.execute('''INSERT INTO  shares (ticker, date, price) VALUES (?, ?, ?) ''',(stock_ticker, date, data_daily_lastClosingPrice))
			conn.commit()

	def lead_to_insert_or_update():
		from alpha_vantage.timeseries import TimeSeries
		import pandas as pd
		API_Key='KY74URGMWMKH6FJ8'
		ts = TimeSeries (key=API_Key, output_format = "pandas")
		data_daily, meta_data = ts.get_daily(symbol=stock_ticker, outputsize ='compact')
		daterow=meta_data['3. Last Refreshed']
		data_daily_lastClosingPrice = data_daily['4. close'][i]
		c.execute("SELECT * FROM shares")
		k=list(c.fetchall())
		y=str(k)
		stk=str(stock_ticker)
		dt=str(daterow)
		if stk in y:
			if dt in y:
				print('updating')
				update()
		else:
			print('inserting')
			insert()

	def delete_ticker():
		try:
			c.execute("DELETE FROM shares WHERE ticker = 'B3SA3.SAO'")
		except:
			c.execute('DELETE FROM shares')
			conn.commit()

	def show_database():
		c.execute('SELECT * FROM shares')
		[print(row) for row in c.fetchall()]

	#createtable()
	lead_to_insert_or_update()
	#insert()
	#select()
	#show_database()
	#delete_ticker()

	conn.close()
results()
print('Please, wait 10 seconds, this is a test version anf there is a limit for API calls')
time.sleep(10)

#TICKERS' DESCRIPTOR:
def descriptor():
	ticker=share
	company=''
	if stock_ticker=='B3SA3.SAO':
		company='Brasil, Bolsa Balcão'
	if stock_ticker=='PETR4.SAO':
		company='Petrobras'
	else:
		company=stock_ticker
	print('O ticker '+stock_ticker+' é da empresa '+company)

#REPEAT RESULTS FUNCTION - LOOP OF DAYS OF THE WEEK - INSIDE LOOP OF TICKERS:


symbol=a1
stock_ticker=symbol+'.SAO'

def looping_different_tickers():
	message='Please, wait 10 seconds, this is a test version anf there is a limit for API calls'
	descriptor()
	i=1
	results()
	print(message)
	time.sleep(10)
	i=2
	results()
	print(message)
	time.sleep(10)
	i=3
	results()
	print(message)
	time.sleep(10)
	i=4
	results()
	print(message)
	time.sleep(10)
	i=5
	results()
	print(message)
	time.sleep(10)
	i=6
	results()
	print(message)
	time.sleep(10)
looping_different_tickers()
symbol=a2
stock_ticker=symbol+'.SAO'
looping_different_tickers()
# symbol=a3
#stock_ticker=symbol+'.SAO'
# looping_different_tickers()
# symbol=a4
#stock_ticker=symbol+'.SAO'
# looping_different_tickers()
# symbol=a5
#stock_ticker=symbol+'.SAO'
# looping_different_tickers()
# symbol=a6
#stock_ticker=symbol+'.SAO'
# looping_different_tickers()
# symbol=a7
#stock_ticker=symbol+'.SAO'
# looping_different_tickers()

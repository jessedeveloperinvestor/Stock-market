#Run the function createtable() to create the table
from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import time
import datetime as dt
import requests
import sqlite3
import time
import datetime
import json

#SHARES:
a1='B3SA3'
a2='PETR4'

#SHARES' ACTIVATOR:
b1=1


#SELECT TICKER:
symbol=a1
stock_ticker=symbol+'.SAO'

#ALPHA VANTAGE API:
def alpha_vantage_api():
	API_Key='KY74URGMWMKH6FJ8'
	ts = TimeSeries (key=API_Key, output_format = "pandas")
	data_daily, meta_data = ts.get_daily(symbol=stock_ticker, outputsize ='compact')
	        # data_daily['column name'][row number]
	daterow=meta_data['3. Last Refreshed']

	data_daily_lastOpenPrice = data_daily['1. open'][0]
	data_daily_lastHighPrice = data_daily['2. high'][0]
	data_daily_lastLowPrice = data_daily['3. low'][0]
	data_daily_lastClosingPrice = data_daily['4. close'][0]
	data_daily_lastTradingVolume = data_daily['5. volume'][0]

#ACTIVATOR:
if b1==1:
	alpha_vantage_api()
else:
	print(symbol,' não está habilitado/ is not active')


conn=sqlite3.connect('shares.db')# or (':memory:')
c=conn.cursor()

def createtable():
	c.execute("""CREATE TABLE shares (
				ticker text,
				date integer,
				price real
	)""")
	conn.commit()

def insert():
	p=data_daily_lastClosingPrice
	date=daterow
	c.execute("INSERT INTO  shares (ticker, date, price) VALUES (?, ?, ?) ",
				(stock_ticker, date, p))
	conn.commit()

def select():
	c.execute("SELECT * FROM shares WHERE ticker='B3SA3.SAO'")
	#print(c.fetchall())
	print(c.fetchone())

def update():
	c.execute('SELECT * FROM shares')
	[print(row) for row in c.fetchall()]
	c.execute('UPDATE shares SET value = (?) WHERE (?) AND WHERE (?)',(data_daily_lastClosingPrice, data_daily_lastClosingPrice, daterow))
	conn.commit()

def lead_to_insert_or_update():
	from alpha_vantage.timeseries import TimeSeries
	import pandas as pd
	API_Key='KY74URGMWMKH6FJ8'
	ts = TimeSeries (key=API_Key, output_format = "pandas")
	data_daily, meta_data = ts.get_daily(symbol=stock_ticker, outputsize ='compact')
	daterow=meta_data['3. Last Refreshed']
	data_daily_lastClosingPrice = data_daily['4. close'][0]
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

def show_database():
	c.execute('SELECT * FROM shares')
	[print(row) for row in c.fetchall()]

#createtable()
lead_to_insert_or_update()
#insert()
#select()
#showdatabase()

conn.close()

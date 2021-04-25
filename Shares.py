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

stock_ticker='B3SA3.SAO'
API_Key='KY74URGMWMKH6FJ8'
ts = TimeSeries (key=API_Key, output_format = "pandas")

   ### STOCK TIME SERIES > DAILY ADJUSTED ###
        # Date / Open / High / Low / Close / Adjusted Close / Volume / Dividend / Split
data_daily, meta_data = ts.get_daily(symbol=stock_ticker, outputsize ='compact')
        # data_daily['column name'][row number]
daterow=meta_data['3. Last Refreshed']

data_daily_lastOpenPrice = data_daily['1. open'][0]
data_daily_lastHighPrice = data_daily['2. high'][0]
data_daily_lastLowPrice = data_daily['3. low'][0]
data_daily_lastClosingPrice = data_daily['4. close'][0]
data_daily_lastTradingVolume = data_daily['5. volume'][0]

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
	c.execute("SELECT * FROM shares")
	conn.commit()



print(data_daily_lastClosingPrice)
print(daterow)

#createtable()
#insert()
#select()

conn.close()

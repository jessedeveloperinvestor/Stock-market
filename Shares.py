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

#SHARES' ACTIVATOR:
b1=1
b2=1
b3=0
b4=0
b5=0

#SELECT TICKER:
symbol=a1
stock_ticker=symbol+'.SAO'

#TICKERS' DESCRIPTOR:
	company=''
	if stock_ticker=='B3SA3.SAO':
		company='Brasil, Bolsa Balcão'
	if stock_ticker=='PETR4.SAO':
		company='Petrobras'
	else:
		company=stock_ticker
	print('O ticker '+stock_ticker+' é da empresa '+company)

i=0

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
		c.execute('''UPDATE shares SET value = (?) WHERE value = (?)''',(data_daily_lastClosingPrice, data_daily_lastClosingPrice))
		conn.commit()
		print('Updated')
	except:
		print('Hi there, Python is got limitations.\nPlease, delete doubled and last seven days data of the target ticker throught a sqlite IDE,\nthen run this software again. Thank you.')
		print('Olá, Python tem limitações,\nfavor apague linhas de banco de dados repetidas e dos últimos 7 dias para o ticker de ação específico por editor de SQLite3,\nentão rode este software de novo. Obrigado.')

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

#USE THIS TO INSERT THE LAST WEEK DATA:

lead_to_insert_or_update()
message='Please, wait 10 seconds, this is a test version and there is a limit for API calls'
i=1
print(message)
time.sleep(100)
lead_to_insert_or_update()
i=2
print(message)
time.sleep(100)
lead_to_insert_or_update()
i=3
print(message)
time.sleep(100)
lead_to_insert_or_update()
i=4
print(message)
time.sleep(100)
lead_to_insert_or_update()



#CHOOSE SPECIFIC FUNTIONS:

#createtable()
#lead_to_insert_or_update()
#insert()
#select()
#show_database()
#delete_ticker()

conn.close()

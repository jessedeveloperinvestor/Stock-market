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


conn=sqlite3.connect('shares.db')
c=conn.cursor()
c.execute("""CREATE TABLE shares (
			ticker text,
			date integer,
			price real
)""")
conn.commit()
print('If there is an error message, so the database already exists in the same folder of the python scripts')
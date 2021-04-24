#SHARES

#RUN THE FOLLOWING LINES ON TERMINAL:
#pip install alpha_vantage
#pip install pandas
from alpha_vantage.timeseries import TimeSeries
from pprint import pprint

API_Key='KY74URGMWMKH6FJ8'
ts=TimeSeries(key=API_Key,output_format='pandas')

def getprices():
	ticket=share
	data, meta_data=ts.get_daily_adjusted(ticket)
	pprint(data.head(7))
#	pprint(data['0. date'].head(7))
	pprint(data['4. close'].head(7))

print('OLÁ, FAVOR INSERIR O TICKET DA AÇÃO E CLICAR EM ENTER')

share=''
try:
	ticket=input()
	n=0
	while n<1:
		share='B3SA3.SAO'
		getprices()
		n=n+1
	n=0
	while n<1:
		share='PETR4.SAO'
		getprices()
		n=n+1
except:
	ticket=share
	n=0
	while n<1:
		share='B3SA3.SAO'
		getprices()
		n=n+1
	n=0
	while n<1:
		share='PETR4.SAO'
		getprices()
		n=n+1

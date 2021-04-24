#SHARES

#RUN THE FOLLOWING LINES ON TERMINAL:
#pip install alpha_vantage
#pip install pandas
from alpha_vantage.timeseries import TimeSeries
from pprint import pprint

API_Key='(API KEY)'
ts=TimeSeries(key=API_Key,output_format='pandas')

def getcloseprice():
	ticker=share
	data, meta_data=ts.get_daily_adjusted(ticker)
	return(data['4. close'].head(7))

def descriptor():
	ticker=share
	company=''
	if ticker=='B3SA3.SAO':
		company='Brasil, Bolsa Balcão'
	if ticker=='PETR4.SAO':
		company='Petrobras'
	else:
		company=ticker
	print('O ticker '+ticker+' é da empresa '+company)

def share_on/off():
	

print('OLÁ, FAVOR INSERIR O TICKER DA AÇÃO E CLICAR EM ENTER')

share=''
try:
	ticker=input()+'.SAO'
	print(getcloseprice())
	descriptor()
except:
	ticket=share
	n=0
	while n<1:
		share='B3SA3.SAO'
		print(getcloseprice())
		descriptor()
		n=n+1
	n=0
	while n<1:
		share='PETR4.SAO'
		print(getcloseprice())
		descriptor()
		n=n+1

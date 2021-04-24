#SHARES

#RUN THE FOLLOWING LINES ON TERMINAL:
#pip install alpha_vantage
#pip install pandas
from alpha_vantage.timeseries import TimeSeries
from pprint import pprint

API_Key='(KEY)'
ts=TimeSeries(key=API_Key,output_format='pandas')

def getcloseprice():
	ticket=share
	data, meta_data=ts.get_daily_adjusted(ticket)
	return(data['4. close'].head(7))

print('OLÁ, FAVOR INSERIR O TICKET DA AÇÃO E CLICAR EM ENTER')

share=''
try:
	ticket=input()
	print(getcloseprice())
except:
	ticket=share
	n=0
	while n<1:
		share='B3SA3.SAO'
		print(getcloseprice())
		n=n+1
	n=0
	while n<1:
		share='PETR4.SAO'
		print(getcloseprice())
		n=n+1

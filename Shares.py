#SHARES
#The software requires an API Alpha Vantage key
#RUN THE FOLLOWING LINES ON TERMINAL:
#pip install alpha_vantage
#pip install pandas
from alpha_vantage.timeseries import TimeSeries
from pprint import pprint

API_Key='KY74URGMWMKH6FJ8'
ts=TimeSeries(key=API_Key,output_format='pandas')

#SHARES/AÇÕES:
a='B3SA3.SAO'
b='PETR4.SAO'

def getcloseprice():
	ticker=share
	data, meta_data=ts.get_daily_adjusted(ticker)
	return(data['4. close'].head(7))

def descriptor():
	ticker=share
	company=''
	if ticker==a:
		company='Brasil, Bolsa Balcão'
	if ticker==b:
		company='Petrobras'
	else:
		company=ticker
	if ticker.type==str:
		z='está habilitado'
	if ticker.type==float:
		z='não está habilitado'
	print('O ticker '+str(ticker)+z+' e é da empresa '+company)

def share_on_off():
	print("PARA HABILITAR ESTA AÇÃO, ESCREVA 'OK', DESABILITAR 'NÃO OK' OU PODE DEIXAR EM BRANCO")
	y=input()
	if y=='OK':
		ticker=str(ticker)
	if y='NÃO OK':
		ticker=float(ticker)

def list_builder():
	#getcloseprice()
	
	#filter data, postioned to ',' and build list
def database_manager():
	#list_builder()

	#if a==b: update
	#if a!=b: insert

print('OLÁ, FAVOR INSERIR O TICKER DA AÇÃO E CLICAR EM ENTER')

share=''
try:
	ticker=input()+'.SAO'
	print(getcloseprice())
	share_on_off()
	descriptor()
except:
	ticket=share
	n=0
	while n<1:
		share=a
		print(getcloseprice())
		share_on_off()
		descriptor()
		n=n+1
	n=0
	while n<1:
		share=b
		print(getcloseprice())
		share_on_off()
		descriptor()
		n=n+1

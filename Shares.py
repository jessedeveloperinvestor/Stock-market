#SHARES
#The software requires an API Alpha Vantage key
#RUN THE FOLLOWING LINES ON TERMINAL:
#pip install alpha_vantage
#pip install pandas
from alpha_vantage.timeseries import TimeSeries
from pprint import pprint

API_Key='KY74URGMWMKH6FJ8'
ts=TimeSeries(key=API_Key,output_format='json')

#SHARES/AÇÕES:
a='B3SA3.SAO'
b='PETR4.SAO'

def getcloseprice():
	ticker=share
	data=ts.get_daily_adjusted(ticker)
	#return(data['4. close'].head(7))
	return(data)

# def descriptor():
# 	ticker=share
# 	company=''
# 	if ticker==a:
# 		company='Brasil, Bolsa Balcão'
# 	if ticker==b:
# 		company='Petrobras'
# 	else:
# 		company=ticker
# 	if ticker.type==str:
# 		z='está habilitado'
# 	if ticker.type==float:
# 		z='não está habilitado'
# 	print('O ticker '+ticker+z+' e é da empresa '+company)

# def share_on_off():
# 	print("PARA HABILITAR ESTA AÇÃO, ESCREVA 'OK', DESABILITAR 'NÃO OK' OU PODE DEIXAR EM BRANCO")
# 	y=''
# 	y=input()
# 	try:
# 		if y=='OK':
# 			ticker=str(ticker)
# 		if y=='NÃO OK':
# 			ticker=float(ticker)
# 	except:
# 		 j=0

def list_builder():
	k=1
	#getcloseprice()
	
	#filter data, postioned to ',' and build list
def database_manager():
	k=2
	#list_builder()

	#if a==b: update
	#if a!=b: insert

def runner():
	pprint(getcloseprice())
	#share_on_off()
	#descriptor()

#OUTPUT ACTIONS:

print('OLÁ, FAVOR INSERIR O TICKER DA AÇÃO E CLICAR EM ENTER')

share=''
try:
	ticker=input()+'.SAO'
	runner()
except:
	ticker=share
	share=a
	runner()
	share=b
	runner()

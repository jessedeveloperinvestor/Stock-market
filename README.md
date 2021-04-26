#STock-market


~DESCRIÇÃO DO CÓDIGO FONTE:
  O código fonte inicia-se com o arquivo Shares_database_builder.py para criar um database em SQLite3, tal código gera um arquivo chamado Shares.db.
Então o arquivo Shares.py foi desenvolvido para ser customizável, possui várias funções criadas que podem ser chamadas individualmente e que, normalmente, algumas são chamadas.
Fiz diversos experimentos para desenvolver o Shares de maneira mais automatizada e que, natural e automaticamente importasse, inserisse e atualizasse todos os dados de todos os tickers automaticamente, mas aparentemente o Python não reconhece uma função dentro de outra função (ou várias).
  >>>>>O software cumpre todos os requisitos listados no arquivo projeto_alphavantage_abr21.pdf.

~ESPECIFICAÇÕES PARA CRIAÇÃO DO BANCO DE DADOS:
  É necessário instalar SQLite3, Python3, pip e as bibliotecas listadas no início do seguinte arquivo Shares_database_builder.py, através do terminal do OS (Windows, Linux ou MacOS) e executá-lo.
O database a ser criado terá o nome Shares.db e será armazenado na mesma pasta dos scripts em Python (que também devem estar juntos)

~DETALHES DE USO:
  O software principal é o Shares.py que começa com (e também o Shares_database_builder.py começa assim):
#RUN THE FOLLOWING LINES ON TERMINAL:
#pip install alpha_vantage
#pip install pandas
#pip install sqlite3
#pip install json
#pip install requests
#pip install time
#pip install datetime

  Ou seja, estas são bibliotecas do Python necessárias ao funcionamento do software.
Na seção #SHARES: pode-se cadastrar ativos/tickers diversos no software.
Na seção #SHARES' ACTIVATOR: pode-se habilitar um ticker definindo b1=1, desabilitar b1=0; o número depois da letra b corresponde ao número em a1, a2 etc que representa a ordem do ticker escolhido.
O #TICKERS' DESCRIPTOR: é um espaço para, inserindo mais:
	if stock_ticker=='B3SA3.SAO':
		company='Brasil, Bolsa Balcão'
...que se possa nomear os tickers, visto que o API da Alpha Vantage e diversos APIs financeiros não ofertam dados sobre os nomes das empresas correspondentes aos tickers.
  A seção #ALPHA VANTAGE API: inicia a importação de dados do API e armazenamento em listas/variáveis.
A seção #ACTIVATOR: é a lógica que apenas permite executar o funcionamento padrão do código principal (Shares.py, com função lead_to_insert_or_update() sendo prioritária) em ativos/tickers habilitados.
Em def createtable(): esta função está em ambos arquivos de Python para permitir a total operação por apenas o script principal, próximo ao final do código em:
#CHOOSE SPECIFIC FUNTIONS: a função pode ser acionada, desabilitando as outras funções como:
createtable()
lead_to_insert_or_update()
insert()
select()
show_database()
delete_ticker()
*Aliás, cada uma destas funções deve ser habilitada ou não independentemente, sendo que o código fonte original automaticamente utiliza a lead_to_insert_or_update() e nela decide-se se um ticker será atualizado (update(), outra função) ou inserido no database (insert()).
Por exmplo, para usar uma única função específica, pode-se deixar as últimas linhas do main script como:

#CHOOSE SPECIFIC FUNTIONS:

# createtable()
# lead_to_insert_or_update()
# insert()
# select()
show_database()
# delete_ticker()

conn.close()

  Desta forma, apenas a função especial show_database() que não possui # será executada e imprimirá no terminal/IDE uma espécie de lista em formato de tabela com o todo conteúdo do database/banco de dados.
A função insert() permite inserir dados manualmente no database, select() permite visualizar dados específicos/ou não (funcionando como SQL query) e, caso necesário - posteriormente adaptada, Python query/filtro também.

	Obrigado.

#STock-market


~DESCRIÇÃO DO CÓDIGO FONTE:
  O código fonte inicia-se com o arquivo Shares_database_builder.py para criar um database em SQLite3, tal código gera um arquivo chamado Shares.db.
Então o arquivo Shares.py foi desenvolvido para ser customizável, possui várias funções criadas que podem ser chamadas individualmente e que, normalmente, algumas são chamadas.
Fiz diversos experimentos para desenvolver o Shares de maneira mais automatizada e que, natural e automaticamente importasse, inserisse e atualizasse todos os dados de todos os tickers automaticamente, mas aparentemente o Python não reconhece uma função dentro de outra função (ou várias). O software cumpre todos os requisitos listados no arquivo projeto_alphavantage_abr21.pdf, exceto a função update que carece de melhoria, mas é desviada por um comando dado ao usuário que executa o código fonte.

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

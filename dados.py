import pandas as pd
import numpy as np
import folium
from matplotlib import pyplot as plt

data = pd.read_csv('/content/AB_NYC_2019.csv')
data.head()

colunas = ['price','neighbourhood_group']
colunaselec= ['neighbourhood_group']
data.loc[:,colunas].groupby(colunaselec).mean().reset_index()

colunas = ['price','neighbourhood','room_type']
colunaselec= ['neighbourhood','room_type']
data.loc[:,colunas].groupby(colunaselec).max().reset_index()

colunas = ['latitude','neighbourhood_group']
colunaselec= ['neighbourhood_group']
data.loc[:,colunas].groupby(colunaselec).min().reset_index()

colunas = ['host_id','calculated_host_listings_count']
linhas=data.loc[:,'calculated_host_listings_count']<=10
dados = data.loc[linhas, 'calculated_host_listings_count'].head()

plt.hist( dados, bins=10 );
plt.title( 'A distribuição de proprietário por imóveis cadastrados');
plt.xlabel( 'Quantidade de Imóveis Cadastrados' );
plt.ylabel( 'Quantidade de Proprietários' );

colunas = ['price','neighbourhood_group','longitude','latitude']
colunaselec=['neighbourhood_group']
dados= data.loc[:,colunas].groupby(colunaselec).min().reset_index()
dados

map = folium.Map()
for index, localizacao in dados.iterrows():
  folium.Marker([localizacao['latitude'],
                 localizacao ['longitude']],
                popup=localizacao[['neighbourhood_group', 'price']]
               ).add_to(map)
map


colunas = ['number_of_reviews','neighbourhood_group','longitude','latitude']
colunaselec=['neighbourhood_group']
dados= data.loc [:, colunas].groupby(colunaselec).max().reset_index()

mapa = folium.Map()

for index, localizacao in dados.iterrows():
  folium.Marker([localizacao['latitude'],
                localizacao ['longitude']],
                popup=localizacao ['neighbourhood_group']
              ).add_to(mapa)
mapa

colunas = ['room_type','latitude','longitude']
linhas = data.loc[:,'room_type']=='Private room'

dados = data.loc[linhas,colunas].sample(100)

mapa=folium.Map()

for index, localizacao in dados.iterrows():
  folium.Marker([localizacao['latitude'],
                 localizacao['longitude']],
                popup=localizacao['room_type']
                ).add_to(mapa)
mapa


colunas = ['room_type', 'latitude', 'longitude']
linhas = data.loc[:, 'room_type'] == 'Shared room'
dados = data.loc[linhas, colunas].sample( 100 )


mapa=folium.Map()

for index, localizacao in dados.iterrows():
  folium.Marker([localizacao['latitude'],
                 localizacao['longitude']],
                popup=localizacao['room_type']
                ).add_to(mapa)
mapa
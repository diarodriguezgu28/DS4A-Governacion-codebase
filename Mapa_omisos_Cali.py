!pip install folium
#Librerias
import pandas as pd
import folium  #needed for interactive map
from folium.plugins import HeatMap
from   collections           import Counter
from   sklearn               import preprocessing
from   datetime              import datetime
from   collections           import Counter
from geopy.geocoders import Nominatim
import numpy as np
#Cargar Base de Datos
Mapa = pd.read_csv(r"Merge_Municipios_Dian.csv")

#Variables de interes para generar la dirección y georeferenciación
Mapa=Mapa[['DIRECCION', 'BARRIO', 'MUNICIPIO', 'COD_MUNICIPIO', 'NoOmiso']]

#Arreglar la Columna(varaible) Barrio
Mapa['BARRIO'] = Mapa['BARRIO'].astype(str)
Mapa.BARRIO = list(map(lambda x: x.replace('\t\t\t','').replace('\t','').replace('\t\t','').replace('(Cabecera)','').replace('( Cabecera)','').replace('(A.San)','').replace('(El Carm)','').replace('(N Sn Vic.)','').replace('(ZARAGOZA)',''),Mapa.BARRIO))
Mapa[['complemento','BARRIO_1']] =  Mapa.BARRIO.str.split('- ', expand=True)
Mapa['BARRIO_1'] = np.where(Mapa['MUNICIPIO'] =='cali', Mapa['complemento'], Mapa['BARRIO_1'])
Mapa['BARRIO_1'] = np.where(Mapa['MUNICIPIO'] =='yumbo', Mapa['complemento'], Mapa['BARRIO_1'])
Mapa['BARRIO_1'] = np.where(Mapa['MUNICIPIO'] =='jamundi', Mapa['complemento'], Mapa['BARRIO_1'])
Mapa['BARRIO_1'] = np.where(Mapa['MUNICIPIO'] =='la cumbre', Mapa['complemento'], Mapa['BARRIO_1'])
Mapa['BARRIO_1'] = np.where(Mapa['MUNICIPIO'] =='dagua', Mapa['complemento'], Mapa['BARRIO_1'])
Mapa['BARRIO_1'] = np.where(Mapa['MUNICIPIO'] =='vijes', Mapa['complemento'], Mapa['BARRIO_1'])

#Arreglar la Columna(varaible) Municipio
Mapa[['complemento_1','MUNICIPIO_1']] =  Mapa.MUNICIPIO.str.split('- ', expand=True)
Mapa['MUNICIPIO_1'] = np.where(Mapa['MUNICIPIO'] =='cali', Mapa['MUNICIPIO'], Mapa['MUNICIPIO_1'])
Mapa['MUNICIPIO_1'] = np.where(Mapa['MUNICIPIO'] =='yumbo', Mapa['MUNICIPIO'], Mapa['MUNICIPIO_1'])
Mapa['MUNICIPIO_1'] = np.where(Mapa['MUNICIPIO'] =='jamundi', Mapa['MUNICIPIO'], Mapa['MUNICIPIO_1'])
Mapa['MUNICIPIO_1'] = np.where(Mapa['MUNICIPIO'] =='la cumbre', Mapa['MUNICIPIO'], Mapa['MUNICIPIO_1'])
Mapa['MUNICIPIO_1'] = np.where(Mapa['MUNICIPIO'] =='dagua', Mapa['MUNICIPIO'], Mapa['MUNICIPIO_1'])
Mapa['MUNICIPIO_1'] = np.where(Mapa['MUNICIPIO'] =='vijes', Mapa['MUNICIPIO'], Mapa['MUNICIPIO_1'])

#Unir Columnas(varaibles), Genera dirección a buscar
Mapa['direction'] = Mapa['BARRIO_1']+", "+Mapa['MUNICIPIO_1']
#Dejar Solo los Datos Para Cali
Mapa_Cali= Mapa[Mapa['MUNICIPIO_1']=='cali'].reset_index()
#Eliminar Viejo Indice
Mapa_Cali=Mapa_Cali.drop('index', axis=1)

#generar la laitud y Longitud
Mapa_Cali['latitude']='NaN'
Mapa_Cali['longitude']='NaN'

#Geocodoficar las direcciones para obtener la latitud y Longitud
for i in range(0,len(Mapa_Cali)):
    address=Mapa_Cali.loc[i,'direction']        
    try:
        search_location = geolocator.geocode(address, timeout=5)
        Mapa_Cali.loc[i,'latitude']=search_location.latitude 
        Mapa_Cali.loc[i,'longitude']=search_location.longitude
    except:
        continue

#eliminar las direcciones que no se pudieron geocodificar
Mapa_Cali['latitude'] = Mapa_Cali['latitude'].astype(float)
Mapa_Cali['longitude'] = Mapa_Cali['longitude'].astype(float)
Mapa_Cali=Mapa_Cali.dropna(subset=['latitude'])
Mapa_Cali=Mapa_Cali.dropna(subset=['direction'])
Mapa_Cali=Mapa_Cali.reset_index()

#generar dos bases de Datos (una para Omisos y otra para no omisios)
Mapa_Cali['NoOmiso'] = Mapa_Cali['NoOmiso'].astype(str)
Mapa_Cali['NoOmiso'] = np.where(Mapa_Cali['NoOmiso'] =='nan', 1, Mapa_Cali['NoOmiso'])
Mapa_Cali['NoOmiso'] = np.where(Mapa_Cali['NoOmiso'] =='True', 2, Mapa_Cali['NoOmiso'])
Mapa_Cali_1 = Mapa_Cali.loc[ Mapa_Cali['NoOmiso']=='1', ["latitude","longitude" ] ].reset_index()
Mapa_Cali_2 = Mapa_Cali.loc[ Mapa_Cali['NoOmiso']=='2', ["latitude","longitude" ] ].reset_index()
print(len(Mapa_Cali_1))
print(len(Mapa_Cali_2))

#Tipo de Mapa 1 (folium_map_1)
folium_map_1 = folium.Map(location=[3.43598, -76.5424],
                        zoom_start=12,
                        tiles="OpenStreetMap"
                        )
for i in range(0, 1008):
    marker = folium.CircleMarker(location=[Mapa_Cali_1["latitude"][i], Mapa_Cali_1["longitude"][i]],radius=3,color="red",fill=True)
    marker.add_to(folium_map_1)
for i in range(0, 694):
    marker = folium.CircleMarker(location=[Mapa_Cali_2["latitude"][i], Mapa_Cali_2["longitude"][i]],radius=3,color="blue",fill=True_1)
    marker.add_to(folium_map)
    
folium_map_1

#Tipo de Mapa 2 (folium_map_2)
folium_map_2 = folium.Map(location=[3.43598, -76.5424],
                        zoom_start=12,
                        tiles="Stamen Terrain"
                        )
for i in range(0, 1008):
    marker = folium.CircleMarker(location=[Mapa_Cali_1["latitude"][i], Mapa_Cali_1["longitude"][i]],radius=3,color="orange",fill=True)
    marker.add_to(folium_map_2)
for i in range(0, 694):
    marker = folium.CircleMarker(location=[Mapa_Cali_2["latitude"][i], Mapa_Cali_2["longitude"][i]],radius=3,color="lightblue",fill=True)
    marker.add_to(folium_map_2)
    
folium_map_2

#Tipo de Mapa 3 (folium_map_3)
folium_map_3 = folium.Map(location=[3.43598, -76.5424],
                        zoom_start=12,
                        tiles="Stamen Toner"
                        )
for i in range(0, 1008):
    marker = folium.CircleMarker(location=[Mapa_Cali_1["latitude"][i], Mapa_Cali_1["longitude"][i]],radius=3,color="gray",fill=True)
    marker.add_to(folium_map_3)
for i in range(0, 694):
    marker = folium.CircleMarker(location=[Mapa_Cali_2["latitude"][i], Mapa_Cali_2["longitude"][i]],radius=3,color="green",fill=True)
    marker.add_to(folium_map_3)
    
folium_map_3
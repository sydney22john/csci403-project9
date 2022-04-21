import json
import pandas as pd
import geopandas as gpd
import webbrowser

geo_file = 'data/denver_map.geojson'
gdf = gpd.read_file(geo_file)
gdf['nbhd_name'] = gdf['nbhd_name'].str.upper()

import folium

m = folium.Map(
    location=[39.73715, -104.989174],
    tiles='"http://{s}.tiles.mapbox.com/v4/wtgeographer.2fb7fc73/{z}/{x}/{y}.png?access_token=pk.xxx',
    attr='XXX Mapbox Attribution',
    zoom_start = 11
)

neighborhood_data = pd.read_csv('test/neighborhood_data_test.csv')
#neighborhood_data['ID_STR'] = neighborhood_data['NBHD_1'].astype(str)

folium.Choropleth(
    geo_data = gdf,
    data = neighborhood_data,
    columns = ['NBHD_1_CN', 'VALUE'],
    key_on = 'feature.properties.nbhd_name',
    fill_color = 'YlGn',
    fill_opacity = 0.7,
    line_opacity = .1,
    legend_name = 'value'
).add_to(m)

folium.LayerControl().add_to(m)

gdf['long'] = gdf.centroid.x
gdf['lat'] = gdf.centroid.y

for i, row in gdf.iterrows():
    folium.Marker(
        location = [row['lat'], row['long']],
        popup = folium.Popup('<b>'+row['nbhd_name']+ '</b>', show=False),
        icon = folium.Icon(color='red', icon='info_sign')
    ).add_to(m)

m.save("map.html")
webbrowser.open("map.html")


import json
import pandas as pd
import geopandas as gpd
import webbrowser

geo_file = 'Project9/data/denver_map.geojson'
gdf = gpd.read_file(geo_file)
gdf['nbhd_name'] = gdf['nbhd_name'].str.upper()
#print(gdf['nbhd_name'])

import folium


m = folium.Map(
    location=[39.73715, -104.989174],
    tiles='"http://{s}.tiles.mapbox.com/v4/wtgeographer.2fb7fc73/{z}/{x}/{y}.png?access_token=pk.xxx',
    attr='XXX Mapbox Attribution',
    zoom_start = 11
)
'''
folium.GeoJson(
     gdf,
     name='Denver'
 ).add_to(m)
'''


neighborhood_data = pd.read_csv('Project9/test/neighborhood_data_test.csv')
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



#folium.LayerControl().add_to(m)
m.save("map.html")
webbrowser.open("map.html")


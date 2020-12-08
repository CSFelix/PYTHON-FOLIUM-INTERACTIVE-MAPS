#!pip install folium
import folium

map_1 = folium.Map(location=[-22.951916, -43.210466], zoom_start=15)
folium.CircleMarker(location=[-22.951916, -43.210466], radius=15, popup="Christ the Redeemer").add_to(map_1)
folium.Marker(location=[-22.951916, -43.210466], popup="Christ the Redeemer").add_to(map_1)
map_1.save("map1.html")

import folium
from folium import plugins

stations_with_coords = {
    "Mall": [46.580, 26.915],
    "Autogara": [46.571, 26.920],
    "Cartier Sud": [46.550, 26.912]
}

route_map = folium.Map(location=[46.567, 26.909], zoom_start=13)

for station, coords in stations_with_coords.items():
    folium.Marker(location=coords, popup=station, icon=folium.Icon(color="blue", icon="car")).add_to(route_map)

optimized_routes = [
    (stations_with_coords["Mall"], stations_with_coords["Autogara"]),
    (stations_with_coords["Autogara"], stations_with_coords["Cartier Sud"]),
]

for start, end in optimized_routes:
    folium.PolyLine([start, end], color="green", weight=3, opacity=0.8).add_to(route_map)

legend_html = """
<div style="position: fixed; 
            bottom: 50px; left: 50px; width: 250px; height: 90px; 
            background-color: white; z-index:9999; font-size:14px;
            border:2px solid grey; border-radius:5px; padding: 10px;">
    <b>Legendă:</b><br>
    <i class="fa fa-car" style="color:blue"></i> Stații Car-Sharing<br>
    <span style="color:green;">▬</span> Traseu Optim Mall-Cartier Sud<br>
</div>
"""
route_map.get_root().html.add_child(folium.Element(legend_html))

optimized_route_output_path = "/home/rares/bacau_chosen_trip.html"
route_map.save(optimized_route_output_path)

optimized_route_output_path


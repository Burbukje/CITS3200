from django.shortcuts import render
from django.http import HttpResponse
import folium

# Create your views here.

def index(request):
        # Location of Perth
    perth = [-31.95249936453132, 115.86121640254342]

    # Styles for GeoJson Map
    border_styles = {
        'color': 'red',
        'weight': 2,
        'fillColor': 'blue',
        'fillOpacity': 0.1
    } 

    # Creating starting location and zoom of displayed map
    map1 = folium.Map(location=perth, zoom_start=12)
    
    # GeoJson data pack LGA of Perth
    folium.GeoJson("map/geoJSON/LGA_Boundaries_LGATE_233_WA_GDA2020_Public.geojson", 
                    name="LGA",
                    style_function=lambda x:border_styles).add_to(map1)

    # Adds layer control to Map
    folium.LayerControl().add_to(map1)

    # Format Map to display on webpage
    map1 = map1._repr_html_()
    context={
        'map1': map1
    }

    return render(request, "index.html", context)
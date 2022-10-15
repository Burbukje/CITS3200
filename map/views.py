from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import folium
import json
import geopandas as gpd


from django.http import JsonResponse
from webScraper.models import Local_Government
from django.core import serializers
from geojson import FeatureCollection
import geojson
# Create your views here.



def jsondata(request):
    data = Local_Government.objects.all()
    with open('map/geoJSON/LGAs_with_classified_data.geojson', 'w') as out:
        mast_point = serializers.serialize('geojson', data)
        out.write(mast_point)
    context = {'object': out}
    return HttpResponse(context, request)

def index(request):

    if not request.user.is_authenticated:
        return redirect("login")

    # Creating starting location and zoom of displayed map
    #map1 = create_lga_map()
    map1 = create_detailed_lga_map()
    # Format Map to display on webpage
    map1 = map1._repr_html_()
    context={
        'map1': map1
    }

    return render(request, "index.html", context)

def create_lga_map():
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
    
    geo_dict = read_classified_geojson()

    # GeoJson data pack LGA of Perth
    for shire in geo_dict:
        # GeoJson data pack LGA of Perth
        folium.GeoJson(geo_dict[shire], 
                        name=shire,
                        style_function=lambda x:border_styles).add_to(map1)

    # Adds layer control to Map
    folium.LayerControl().add_to(map1)

    return map1

def create_detailed_lga_map():
    lgas_count = Local_Government.objects.count()
    filename = "map/geoJSON/LGA_Boundaries_Metro_Area.geojson"
    classified_data = read_classified_geojson()
    the_final_file = open(filename)
    json_data = json.load(the_final_file)
    

    for ind in range(0, lgas_count):
        for val in json_data['features']:
            if 'name' in val['properties'].keys():
                lga_name = val['properties']['name']
            if classified_data[ind]['local_government_area'] == lga_name:
                val['properties']= classified_data[ind]

    with open("map/geoJSON/jsonfile.geojson", 'w') as json_file:
        json_file.seek(0)
        json.dump(json_data, json_file)

    file_geojson = "map/geoJSON/jsonfile.geojson"
    file = open(file_geojson)
    df = gpd.read_file(file)
    map2 = df.explore()
    

    folium.LayerControl().add_to(map2)
    return map2


def read_classified_geojson():
    lgas_count = Local_Government.objects.count()
    geo_file = "map/geoJSON/LGAs_with_classified_data.geojson"

    f = open(geo_file)
    json_file = json.load(f)
    all_lga = {}
    for index in range(0, lgas_count):
        classifications = json_file['features'][index]['properties']
        all_lga[index] = classifications
    return all_lga


from django.shortcuts import render
from django.http import HttpResponse
import folium
import json
import geopandas as gpd

from django.http import JsonResponse
from webScraper.models import Local_Government
from django.core import serializers


# Create your views here.

def jsondata(request):
    data = Local_Government.objects.all()
    with open(r'map/geoJSON/LGAs_with_classified_data.geojson', 'w') as out:
        mast_point = serializers.serialize('geojson', data)
        out.write(mast_point)
    context = {'object': out}
    return HttpResponse(context, request)

def index(request):
    # Creating starting location and zoom of displayed map
    #map1 = create_lga_map()
    map1 = create_detailed_lga_map()
    # Format Map to display on webpage
    map1 = map1._repr_html_()
    context={
        'map1': map1
    }

    return render(request, "index.html", context)

# def create_lga_map():
#     # Location of Perth
#     perth = [-31.95249936453132, 115.86121640254342]

#     # Styles for GeoJson Map
#     border_styles = {
#         'color': 'red',
#         'weight': 2,
#         'fillColor': 'blue',
#         'fillOpacity': 0.1
#     } 

#     # Creating starting location and zoom of displayed map
#     map1 = folium.Map(location=perth, zoom_start=12)
#     geo_dict = read_geojson()

#     # GeoJson data pack LGA of Perth
#     for shire in geo_dict:
#         # GeoJson data pack LGA of Perth
#         folium.GeoJson(geo_dict[shire], 
#                         name=shire,
#                         style_function=lambda x:border_styles).add_to(map1)
        

#     # Adds layer control to Map
#     folium.LayerControl().add_to(map1)

#     return map1

def create_detailed_lga_map():
    filename = "map/geoJSON/LGA_Boundaries_Metro_Area.geojson"
    classified_data = read_classified_geojson()
    all_lga={}
    datafile = json.load(filename)
    LGA_properties = datafile["features"]["properties"]
    if LGA_properties["name"] == classified_data["local_government_area"]:
        LGA_properties.append(classified_data)
        converted_data = json.dumps(LGA_properties)
        #df = gpd.read_file(converted_data, driver='GeoJSON')
        df = gpd.DataFrame(converted_data)
        # df = gpd.GeoDataFrame.from_features(converted_data)
        map2 = df.explore()

    folium.LayerControl().add_to(map2)
    return map2

def read_classified_geojson():
    geo_file = "map/geoJSON/LGAs_with_classified_data.geojson"
    # with open(geo_file, "r") as f:
    #     lga_dict = json.load(f) 
    classified_LGA = json.load(geo_file)
    #classifications is a dict
    classifications = classified_LGA["features"]["properties"]


    # all_lga = {}
    # for geocode in lga_dict["features"]:
    #     lga_name = geocode["properties"]["local_government_area"]
    #     all_lga[lga_name] = geocode
#change this to a geojson file
    return classifications
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import folium
import json
import geopandas as gpd
import pandas as pd



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
    map = create_detailed_lga_map()
    # Format Map to display on webpage

    map1 = create_heat_map()

    map1 = map1._repr_html_()
    map = map._repr_html_()
    context={
        'map1': map1,
        'map': map
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
    

    map1 = create_heat_map(map1)

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


def create_heat_map():
    # Load the geojson data
    geo_file = "map\geoJSON\LGA_Boundaries_Metro_Area.geojson"
    f = open(geo_file)
    lga_geo = json.load(f)

    # Location of Perth
    perth = [-31.95249936453132, 115.86121640254342]

    # Creating starting location and zoom of displayed map
    m = folium.Map(location=perth, zoom_start=12)

    # Read in the data in this case just the number of food retail in each LGA
    data_file = "map/geoJSON/food_retail.csv"

    food_retail_data = pd.read_csv(data_file)



    folium.Choropleth(
    geo_data=lga_geo,
    name="Food Retail",
    data=food_retail_data,
    columns=["State", "Food Retail"],
    key_on="feature.properties.name",
    fill_color="YlOrRd",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Food Retail",).add_to(m)


    data_file = "map/geoJSON/food_service.csv"

    food_service_data = pd.read_csv(data_file)

    folium.Choropleth(
    geo_data=lga_geo,
    name="Food Service",
    data=food_service_data,
    columns=["State", "Food Service"],
    key_on="feature.properties.name",
    fill_color="YlOrRd",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Food Service",).add_to(m)

    folium.LayerControl().add_to(m)

    return m
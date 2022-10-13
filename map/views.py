from django.shortcuts import render
from django.http import HttpResponse
import folium
import json
import geopandas as gpd
import pandas as pd

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


def create_detailed_lga_map():
    lgas_count = Local_Government.objects.count()
    filename = "map/geoJSON/LGA_Boundaries_Metro_Area.geojson"
    classified_data = read_classified_geojson()
    the_final_file = open(filename)
    json_data = json.load(the_final_file)
    

    for ind in range(0, lgas_count-1):
        #here is a key error
        print(type(json_data))
        for val in json_data['features']:
            if classified_data[ind]['local_government_area'] == val['properties']['name']:
                val['properties']= classified_data[ind]
                print(val['properties'])
            
            

    df = gpd.GeoDataFrame.from_features(json_data)
    # df = df.to_crs(epsg=4326)
    map2 = df.explore()
    #update the data to he original file
    # with open(filename, 'w') as outfile:
    #     outfile.seek(0)
    #     json.dump(json_data, outfile)

    folium.LayerControl().add_to(map2)
    return map2

def read_classified_geojson():
    lgas_count = Local_Government.objects.count()
    geo_file = "map/geoJSON/LGAs_with_classified_data.geojson"

    f = open(geo_file)
    #this is a weird format
    json_file = json.load(f)
    all_lga = {}
    for index in range(0, lgas_count):
        classifications = json_file['features'][index]['properties']
        all_lga[index] = classifications
    return all_lga


def overwrite_geojson():
    """Update the geojson file everytime there is a change made to the database"""
    print("blah")
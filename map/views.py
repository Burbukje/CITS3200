from django.shortcuts import render
from django.http import HttpResponse
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
    

    for ind in range(0, lgas_count):
        for val in json_data['features']:
            if 'name' in val['properties'].keys():
                lga_name = val['properties']['name']
            if classified_data[ind]['local_government_area'] == lga_name:
                val['properties']= classified_data[ind]

    with open("map/geoJSON/jsonfile.json", 'w') as json_file:
        json_file.seek(0)
        json.dump(json_data, json_file)

    #add it to a feature collection
    feature_collection = FeatureCollection(json_data)

                
    df = gpd.GeoDataFrame.from_features(feature_collection)

    # gdf = gpd.GeoDataFrame(df).set_geometry(json_data)
    # df = df.to_crs(epsg=4326)
    map2 = df.explore()
    #update the data to the original file
    #the problem is that the json_data is a string not a file
    #instead of creating that 
    new_geojson = create_updated_geojson()
    

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
        if classifications != "0" or classifications != None:
            all_lga[index] = classifications
    return all_lga


def create_updated_geojson():
    """Update the geojson file everytime there is a change made to the database"""
    input_file = json.load(open("map/geoJSON/jsonfile.json", "r", encoding="utf-8"))
    #create the geojson format
    # geojs={
    #     "type": "FeatureCollection",
    #     "features":[
    #         {
    #                 "type":"Feature",
    #                 "geometry": {
    #                 "type":"LineString",
    #                 "coordinates":d["geojson"]["coordinates"],
    #             },
    #                 "properties":d,
            
    #             } for d in input_file
    #         ]  
    #     }
    geojs = FeatureCollection(input_file)
    output_file = open("map/geoJSON/updated_geojson.geojson", "w")
    output_file.seek(0)
    #add the json data
    geojson.dump(geojs, output_file)



        
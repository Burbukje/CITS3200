from django.test import TestCase
import folium
from folium.features import GeoJson, Choropleth

import jinja2
from jinja2 import Environment, PackageLoader


class TestFolium(object):
    """"""
    def setup(self):
        """
        set map
        """
        #set up the folium map
        attr = 'http://127.0.0.1:8000/'
        self.m = folium.Map(
            location=[-31.95249936453132, 115.86121640254342],
            width=900,
            height=400,
            max_zoom=20,
            zoom_start=4,
            max_bounds=True,
            attr=attr
        )
        self.env = Environment(loader=PackageLoader('folium', 'templates'))

    def test_init(self):
        """
        test map
        """
        assert self.m.get_name().startswith('map_')
        assert self.m.get_root() == self.m._parent
        assert self.m.location == [-31.95249936453132, 115.86121640254342]
        assert self.m.options['zoom'] == 4
        assert self.m.options['maxBounds'] == [[-90, -180], [90, 180]]
        assert self.m.position == 'relative'
        assert self.m.height == (400, 'px')
        assert self.m.width == (900, 'px')
        assert self.m.left == (0, '%')
        assert self.m.top == (0, '%')
    
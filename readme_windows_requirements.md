For windows users:

**Backport Errors**

For python3.9 and greater avoid using backports.

If using python3.8 or lower:

Edit your requirements.txt file to inlcude the following

`backports.zoneinfo==0.2.1;python_version<"3.9"`

**Installing geopandas**

For more information
https://stackoverflow.com/questions/54734667/error-installing-geopandas-a-gdal-api-version-must-be-specified-in-anaconda

``` python
pip install pipwin
pipwin install gdal
pipwin install fiona
pip install geopandas
```
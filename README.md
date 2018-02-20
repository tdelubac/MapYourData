# Map Your Data

Plot your data on a geographic map. 

This is a python code showing how to plot data on a geographic map using the folium package. In this example code, we plot a number of counts per French departments. The shape of the departments are provided as a [geojson file](http://geojson.org/). The geojson file used for this code was obtained from [Geofla](https://public.opendatasoft.com/explore/dataset/geoflar-departements/). The counts are provided in a separate file. You can modify those two data files to plot your own data on your own maps.  

## Runing the code
You can install the required libraries by typing the following in your terminal:
'''
pip install -r requirements.txt
'''
To run the code simply type:
'''
python mapyourdata.py
'''
Then open the resulting departments.html file in your favorite browser. 

## License 
This code is under the FreeBSD license (see LICENSE.txt).
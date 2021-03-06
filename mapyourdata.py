import pandas as pd
import folium

# Loading the data with the number of counts per departments
# We load the department column as string because it is a str
# in the geojson file. 
df_counts = pd.read_csv('data/counts_per_department.csv', dtype={'department':object})

# Creating the initial map
m = folium.Map(location=[46.5,2], zoom_start=5.49)

# Creating the choropleth to add the coloured departments
# on top of the map
m.choropleth(
    geo_data     = 'data/departements.geojson',
    name         = 'French departments',
    data         = df_counts,
    columns      = ['department','counts'],
    key_on       = 'feature.properties.code',
    fill_color   = 'YlGn',
    fill_opacity = 0.7,
    line_opacity = 0.2,
    legend_name  = 'Number of answers per department' 
)

# Save to html and open it in your favorite browser
m.save('departments.html')
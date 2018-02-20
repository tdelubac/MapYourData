import pandas as pd
import folium

# specifying the path to the geojson data 
departments = 'data/departements.geojson'

# Loading the data with the number of counts per departments
# We load the department column as string because it is a str
# in the geojson file. 
df_counts = pd.read_csv('data/counts_per_department.csv', dtype={'department':object})
df_counts['department'] = df_counts['department'].astype(str)

# Creating the initial map
m = folium.Map(location=[46.5,2], zoom_start=5.49)

# Creating the choropleth to add the coloured departments
# on top of the map
m.choropleth(
    geo_data     = departments,
    name         = 'French departments',
    data         = df_counts,
    columns      = ['department','counts'],
    key_on       = 'feature.properties.code',
    fill_color   = 'YlGn',
    fill_opacity = 0.7,
    line_opacity = 0.2,
    legend_name  = 'Number of answers per department' 
)
folium.LayerControl().add_to(m)

# Save to html and open it in your favorite browser
m.save('departments.html')
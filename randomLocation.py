"""
Getting a random point inside a country based on its name.
In this solution, the shapefile with countries was used.
"""

# imports
import re
import random
import shapefile
from shapely.geometry import shape, Point

# function that takes a shapefile location and a country name as inputs
def random_point_in_state(shp_location, state_name):
    shapes = shapefile.Reader(shp_location, encoding = 'latin1') # reading shapefile with pyshp library
    state = [s for s in shapes.records() if state_name in s][0] #getting features of the select state
    state_id = int(re.findall(r'\d+', str(state))[0]) # getting feature(s)'s id of that match
    shapeRecs = shapes.shapeRecords() #return the geometry and attributes for all shapes as a list

    feature = shapeRecs[state_id].shape.__geo_interface__ #geo_interface object
    shp_geom = shape(feature) #read a single shape by calling its index

    minx, miny, maxx, maxy = shp_geom.bounds #definir los limites
    while True:
        p = Point(random.uniform(minx, maxx), random.uniform(miny, maxy)) #punto aleatorio
        if shp_geom.contains(p): #el estado debe de contener el punto geografico
            return p.x, p.y
    
x,y = random_point_in_state(
    "/mnt/f/Telematica/UndecimoSemestre/ProyectoTerminal_2/fill_db/mapas/Mexico_States.shp",
     "México"
)
print('longitud: '+ str(x))
print('latitud: ' + str(y))
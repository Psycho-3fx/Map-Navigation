# Import Geopy And Gmplot Module For Find Coordinates And Path
from geopy.geocoders import Nominatim
from geopy import distance
import gmplot

# Input The Current and Destination Place Name
geocoder=Nominatim(user_agent="I Know Python")
location1=input("Enter The Current Location:")
location2=input("Enter The Destination:")
# .geocoder Function To find The Coordinates For The Entered Locations
coordinates1=geocoder.geocode(location1)
coordinates2=geocoder.geocode(location2)

# Print the Two Coordinates
lat1,long1=(coordinates1.latitude),(coordinates1.longitude)
lat2,long2=(coordinates2.latitude),(coordinates2.longitude)
place1=(lat1,long1)
place2=(lat2,long2)
# Print The Location
print("From=",location1)
print("To=",location2)
print("Air distance between",location1,"and",location2,"is",distance.distance(place1,place2))

#Decalare The Latitude And Longitude
latitude_list = [lat1,lat2]
longitude_list = [long1,long2]
# Display The Way You Travelling
gmap = gmplot.GoogleMapPlotter(20.593684 ,78.96288, 5)
gmap.scatter( latitude_list, longitude_list, '#ff0000', size =40, marker = False)
# polygon method Draw a polygon with
# the help of coordinates
gmap.polygon(latitude_list, longitude_list, color = 'darkblue',edge_width=2.5)
#gmap.apikey = "Your_API_KEY"
gmap.apikey = "AIzaSyDeRNMnZ__VnQDiATiuz4kPjF_c9r1kWe8"
#Location Where You Want To Save Ypur File
gmap.draw( "Direction For Your Destination.html" )



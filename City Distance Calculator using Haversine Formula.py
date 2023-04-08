from pygeocoder import Geocoder
from math import radians, sin, cos, sqrt, atan2

def get_distance(locA, locB):
    # Calculate distance between two points on the earth
    earth_rad = 6371.0  # Earth radius in kilometers
    lat1, lon1 = locA
    lat2, lon2 = locB
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat/2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    return earth_rad * c

def get_latlongs(location):
    # Get the latitude and longitude of a location
    return Geocoder.geocode(location)[0].coordinates

def convert_km_to_miles(km):
    # Convert kilometers to miles
    miles_per_km = 0.621371192
    return km * miles_per_km

def main():
    # Get the names of two cities
    cityA = input('Type the first city: ')
    cityB = input('Type the second city: ')

    # Get the desired distance units from the user
    while True:
        units = input('Type distance units (miles or kilometers): ').lower()
        if units in ['km', 'kilometers', 'kilometer']:
            units = 'km'
            break
        elif units in ['m', 'mile', 'miles']:
            units = 'm'
            break
        else:
            print('Units not recognised, please try again')

    # Find the distance between the two cities
    try:
        distance = get_distance(get_latlongs(cityA), get_latlongs(cityB))

        # Display the distance
        if units == 'km':
            print(f'{distance:.2f} km')
        else:
            distance = convert_km_to_miles(distance)
            print(f'{distance:.2f} miles')

    except:
        print('Error: Are the input cities correct?')

if __name__ == '__main__':
    main()

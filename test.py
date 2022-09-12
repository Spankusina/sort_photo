# from exif import Image
import reverse_geocoder as rg
# import pycountry

# def format_dms_coordinates(coordinates):
#     return f"{coordinates[0]}° {coordinates[1]}\' {coordinates[2]}\""    

# def dms_coordinates_to_dd_coordinates(coordinates, coordinates_ref):
#     decimal_degrees = coordinates[0] + \
#                       coordinates[1] / 60 + \
#                       coordinates[2] / 3600
    
#     if coordinates_ref == "S" or coordinates_ref == "W":
#         decimal_degrees = -decimal_degrees
    
#     return decimal_degrees

# with open(r'E:\prog\!\s\2022\09\09\IMG_20220909_142510.jpg', 'rb') as palm_file:
#     images = Image(palm_file)

# decimal_latitude = dms_coordinates_to_dd_coordinates(images.gps_latitude, images.gps_latitude_ref)
# decimal_longitude = dms_coordinates_to_dd_coordinates(images.gps_longitude, images.gps_longitude_ref)
coordinates = (51.5214588,-0.1729636),(9.936033, 76.259952),(37.38605,-122.08385)
rg.search(coordinates)
# location_info['country'] = pycountry.countries.get(alpha_2=location_info['cc'])
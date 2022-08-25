import os
import datetime
from exif import Image

def md(path):
    if os.path.exists(path) == False:
        os.makedirs(path)

path_in_dir = ''

while os.path.exists(path_in_dir) == False:
    path_in_dir = input('Введите адрес папки, откуда взять фотографии: ')
    if os.path.exists(path_in_dir) == False:
        print('Адрес не верный')

path_out_dir = input('Введите адрес папки, куда сложить фотографии: ')
md(path_out_dir)

count = 0

for adress, dirs, files in os.walk(path_in_dir):
    for photo in files:
        if '.jpg' in photo or '.jpeg' in photo:
            full_path_photo = os.path.join(adress, photo)
            print(full_path_photo)
            
            with open(full_path_photo, "rb") as palm_file:
                images = Image(palm_file)

            if images.has_exif:
                data_photo = images.datetime_original
                year_photo = data_photo[0:4]
                month_photo = data_photo[5:7]
            else:
                data_photo = datetime.datetime.fromtimestamp(os.path.getmtime(full_path_photo))
                year_photo = str(data_photo.year)
                if data_photo.month < 10:
                    month_photo = '0' + str(data_photo.month)
                else:
                    month_photo = str(data_photo.month)
            
            palm_file.close

            new_path_dir = os.path.join(path_out_dir, year_photo, month_photo)
            print(new_path_dir)

            md(new_path_dir)

            


            # print(full_path_photo, full_date_photo)
        # if '_compressed' in file:
        #     full = os.path.join(adress, file)
        #     new_file = file.replace('_compressed', '')
        #     new_full = os.path.join(adress, new_file)
        #     os.rename(full, new_full)
            count += 1
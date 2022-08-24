import os
from exif import Image

path_in_dir = ''

while os.path.exists(path_in_dir) == False:
    path_in_dir = input('Введите адрес папки, откуда взять фотографии: ')
    if os.path.exists(path_in_dir) == False:
        print('Адрес не верный')

path_out_dir = input('Введите адрес папки, куда сложить фотографии: ')
if os.path.exists(path_out_dir) == False:
    os.makedirs(path_out_dir)
count = 0

for adress, dirs, files in os.walk(path_in_dir):
    for photo in files:
        if '.jpg' in photo or '.jpeg' in photo:
            full_path_photo = os.path.join(adress, photo)
            with open(full_path_photo, "rb") as palm_file:
                images = Image(palm_file)
            data_photo = images.datetime_original
            year_photo = data_photo[0:4]
            month_photo = data_photo[5:7]
            print(year_photo, month_photo)
            


            # print(full_path_photo, full_date_photo)
        # if '_compressed' in file:
        #     full = os.path.join(adress, file)
        #     new_file = file.replace('_compressed', '')
        #     new_full = os.path.join(adress, new_file)
        #     os.rename(full, new_full)
            count += 1
import os
import datetime

path_in_dir = ''

while os.path.exists(path_in_dir) == False:
    path_in_dir = input('Введите адрес папки, откуда взять фотографии: ')
    if os.path.exists(path_in_dir) == False:
        print('Адрес не верный')

path_out_dir = input('Введите адрес папки, куда сложить фотографии: ')
if os.path.exists(path_out_dir) == False:
    os.mkdir(path_out_dir)
count = 0

for adress, dirs, files in os.walk(path_in_dir):
    for photo in files:
        if '.jpg' in photo or '.jpeg' in photo:
            full_path_photo = os.path.join(adress, photo)
            full_date_photo = datetime.datetime.fromtimestamp(os.path.getctime(full_path_photo))
            print(full_date_photo)
        # if '_compressed' in file:
        #     full = os.path.join(adress, file)
        #     new_file = file.replace('_compressed', '')
        #     new_full = os.path.join(adress, new_file)
        #     os.rename(full, new_full)
            count += 1
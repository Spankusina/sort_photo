import os
import datetime
import hashlib 
import shutil
from exif import Image

def md(path):
    if os.path.exists(path) == False:
        os.makedirs(path)

def no_exif(photo):
    data_photo = datetime.datetime.fromtimestamp(os.path.getmtime(full_path_photo))
    year = str(data_photo.year)
    if data_photo.month < 10:
        month = '0' + str(data_photo.month)
    else:
        month = str(data_photo.month)
    photo = photo.replace(extension, ' (no exif)' + extension)
    new_name_photo = os.path.join(adress, photo)
    os.rename(full_path_photo, new_name_photo)
    log.write(full_path_photo + ' renamed in ' + new_name_photo + '\n')
    return year, month, new_name_photo, photo

path_in_dir = ''
hash_list = []
count_move = 0

while os.path.exists(path_in_dir) == False:
    path_in_dir = input('Введите адрес папки, откуда взять фотографии: ')
    if os.path.exists(path_in_dir) == False:
        print('Адрес не верный')

path_out_dir = input('Введите адрес папки, куда сложить фотографии: ')
md(path_out_dir)

log_full_path = os.path.join(path_out_dir, 'log.txt')
log = open (log_full_path, 'a')
log.write('------- Start in ' + str(datetime.datetime.now()) + '\n')


#заносим хеш всех фотографий в конечной папке
for adress, dirs, files in os.walk(path_out_dir):
    for photo in files:
        if '.jpg' in photo or '.jpeg' in photo or '.JPG' in photo or '.JPEG' in photo:
            full_path_photo = os.path.join(adress, photo)
            with open(full_path_photo, 'rb') as palm_file:
                data = palm_file.read()
            
            file_hash = hashlib.md5()
            file_hash.update(data)
            if file_hash.hexdigest() not in hash_list:
                hash_list.append(file_hash.hexdigest())


for adress, dirs, files in os.walk(path_in_dir):
    if path_out_dir not in adress:
        for photo in files:       
            if '.jpg' in photo or '.jpeg' in photo or '.JPG' in photo or '.JPEG' in photo:
                if '.jpg' in photo:
                    extension = '.jpg'
                elif '.JPG' in photo:
                    extension = '.JPG'
                elif '.jpeg' in photo:
                    extension = '.jpeg'
                elif '.JPEG' in photo:
                    extension = '.JPEG'

                full_path_photo = os.path.join(adress, photo)
                
                with open(full_path_photo, 'rb') as palm_file:
                    data = palm_file.read()

                    file_hash = hashlib.md5()
                    file_hash.update(data)

                    palm_file.seek(0,0)
                    images = Image(palm_file)


                if images.has_exif:
                    if images.get('datetime_original', default='none') != 'none':
                        data_photo = images.datetime_original
                        year_photo = data_photo[0:4]
                        month_photo = data_photo[5:7]
                    else:
                        year_photo, month_photo, full_path_photo, photo = no_exif(photo)        
                else:
                    year_photo, month_photo, full_path_photo, photo = no_exif(photo)

                new_adress = os.path.join(path_out_dir, year_photo, month_photo)
                md(new_adress)

                #Если есть хеш фотографии в списке, тогда меняем название
                if file_hash.hexdigest() in hash_list:
                    replica = 1    
                    photo = photo.replace(extension, ' (copy ' + str(replica) + ')' + extension)
                    check_new_name_photo = os.path.join(new_adress, photo)
                    while os.path.exists(check_new_name_photo):
                        replica += 1
                        photo = photo.replace('copy ' + str(replica-1), 'copy ' + str(replica))
                        check_new_name_photo = os.path.join(new_adress, photo)

                    new_name_photo = os.path.join(adress, photo)
                    os.rename(full_path_photo, new_name_photo)
                    log.write(full_path_photo + ' renamed in ' + new_name_photo + '\n')
                    full_path_photo = new_name_photo
                else:
                    hash_list.append(file_hash.hexdigest())

                shutil.move(full_path_photo, new_adress)
                count_move +=1
                log.write(full_path_photo + ' moved in ' + new_adress + '\n')

log.write('Количество перенесенных файлов: ' + str(count_move) + '\n' + '------- Finish in ' + str(datetime.datetime.now()) + '\n')
log.close()
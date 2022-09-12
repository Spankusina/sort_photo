import os
import datetime
import hashlib 
import shutil
from exif import Image

def md(path):
    if os.path.exists(path) == False:
        os.makedirs(path)

def calend(data_photo):
    hour = data_photo.strftime("%H")
    if int(hour) < 7:
        data_photo = data_photo - datetime.timedelta(days=1)
    day = data_photo.strftime(r"%d")
    month = data_photo.strftime("%m")
    year = data_photo.strftime("%Y")
    return year, month, day

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


                if images.has_exif and images.get('datetime_original', default='none') != 'none':
                    data_photo = datetime.datetime.strptime(images.datetime_original, r'%Y:%m:%d %H:%M:%S')
                    year_photo, month_photo, day_photo = calend(data_photo)

                else:
                    data_photo = datetime.datetime.fromtimestamp(os.path.getmtime(full_path_photo))
                    year_photo, month_photo, day_photo = calend(data_photo) 
                    photo = photo.replace(extension, ' (no exif)' + extension)
                    new_name_photo = os.path.join(adress, photo)
                    os.rename(full_path_photo, new_name_photo)
                    log.write(full_path_photo + ' renamed in ' + new_name_photo + '\n')
                    full_path_photo = new_name_photo


                new_adress = os.path.join(path_out_dir, year_photo, month_photo, day_photo)
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
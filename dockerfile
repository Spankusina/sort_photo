FROM python

WORKDIR /app

COPY . .

RUN pip install exif

CMD [ "python", "photo_sorting.py"]
# Cleaning airbnb data

import csv

cleaned_data = []

with open ('data/listings.csv', 'r', encoding='utf-8') as f:
    csv_reader = csv.reader(f)
    _lat = 0
    _long = 0
    _id = 0
    _neighborhood = 0
    _price = 0
    for i, row in enumerate(csv_reader):
        if i == 0:
            _lat = row.index('latitude')
            _long = row.index('longitude')
            _id = row.index('id')
            _neighborhood = row.index('neighbourhood_cleansed')
            _price = row.index('price')
        cleaned_data.append([row[_id], row[_neighborhood], row[_price], row[_lat], row[_long]])

with open('data/airbnb_data.csv', 'w', newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerows(cleaned_data)
import csv

data_property = []
data_neighborhoods = []
data_class_types = []

with open("real_property_sales_and_transfers.csv", 'r') as f:
    csv_reader = csv.reader(f)
    for i, row in enumerate(csv_reader):
        if row[12][0:11] == 'RESIDENTIAL' or row[12][0:10] == 'COMMERCIAL':
            data_property.append([i]+row[5:12]+ [row[13]])
        if i == 0:
            data_property.append(['transaction_num']+row[5:12] + [row[13]])
        data_neighborhood = [row[13], row[14]]
        if data_neighborhood not in data_neighborhoods:
            data_neighborhoods.append(data_neighborhood)
        data_class_type = [row[11], row[12]]
        if  data_class_type not in data_class_types:
            data_class_types.append(data_class_type)

with open("property_data.csv", 'w', newline = '') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerows(data_property)


with open("neighborhood_data.csv", 'w', newline = '') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerows(data_neighborhoods)

with open("d_class_data.csv", 'w', newline = '') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerows(data_class_types)

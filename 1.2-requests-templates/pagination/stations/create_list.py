import csv
import os


def create_list(filename):
    path = os.path.join(os.getcwd(), filename)
    with open(path, encoding='utf-8', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        address_list = []
        for row in reader:
            dict_temp = {'Name': row['Name'], 'Street': row['Street'], 'District': row['District']}
            address_list.append(dict_temp)
    return address_list

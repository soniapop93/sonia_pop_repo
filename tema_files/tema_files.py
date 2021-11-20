# Specific ca eu din cerinta temei am inteles ca trebuie sa fac un dictionar cu acele masini,
# iar acestea le scriu intr-un fisier numit "input.csv"
# Dupa ce am generat fisierul le citesc din .csv, le salvez din nou intr-un dictionar, iar pe urma toate datele
# necesare le scriu in functie de conditii in fisierele de tip .json


import json
import os
import csv
import shutil

list_cars = [{"brand": "Volkswagen", "model": "Polo", "hp": "50", "price": "1000"},
             {"brand": "Audi", "model": "A3", "hp": "100", "price": "15000"},
             {"brand": "Opel", "model": "Meriva", "hp": "70", "price": "4000"},
             {"brand": "Volkswagen", "model": "Golf", "hp": "200", "price": "20000"},
             {"brand": "Tesla", "model": "S", "hp": "750", "price": "90000"},
             {"brand": "Mazda", "model": "CX-5", "hp": "175", "price": "11000"},
             {"brand": "Dodge", "model": "Challanger", "hp": "707", "price": "150000"},
             {"brand": "Mazda", "model": "RX-8", "hp": "240", "price": "12000"},
             {"brand": "Cupra", "model": "Leon", "hp": "200", "price": "35000"},
             {"brand": "Volkswagen", "model": "Arteon", "hp": "270", "price": "40000"},
             {"brand": "Ford", "model": "Mustang", "hp": "450", "price": "100000"},
             {"brand": "Toyota", "model": "Hilux 4x4", "hp": "200", "price": "52000"},
             {"brand": "Volkswagen", "model": "Passat", "hp": "150", "price": "15000"},
             {"brand": "Ford", "model": "Focus", "hp": "150", "price": "20000"}]

def generate_id(list_cars):
    for car, id in zip(list_cars, range(1, 1000)):
        car["id"] = id
    return list_cars


def write_input_csv(list_cars, file_name):
    with open(file_name, mode="w") as cars_file:
        columns_name = ["brand", "model", "hp", "price", "id"]
        cars_writer = csv.DictWriter(cars_file, delimiter=',', fieldnames=columns_name)
        cars_writer.writeheader()
        for car in list_cars:
            cars_writer.writerow(car)


def read_input_csv(file_name):
    list_cars = []

    with open(file_name, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0

        for row in csv_reader:
            if line_count > 0:
                list_cars.append(row)
            line_count += 1
    return list_cars


def f_json_obj(list_car, file_name):
    json_obj = json.dumps(list_car, indent=4)
    f = open("output_data/" + file_name, "a+")
    f.write(json_obj)
    f.close()


def hp_cars(list_cars):
    list_slow_cars = []
    list_fast_cars = []
    list_sport_cars = []

    for car in list_cars:
        if int(car["hp"]) < 120:
            list_slow_cars.append(car)
        elif int(car["hp"]) >= 120 and int(car["hp"]) < 180:
            list_fast_cars.append(car)
        elif int(car["hp"]) >= 180:
            list_sport_cars.append(car)

    f_json_obj(list_slow_cars, "slow_cars.json")
    f_json_obj(list_fast_cars, "fast_cars.json")
    f_json_obj(list_sport_cars, "sport_cars.json")


def price_cars(list_cars):
    list_cheap_cars = []
    list_medium_cars = []
    list_expensive_cars = []

    for car in list_cars:
        if int(car["price"]) < 1000:
            list_cheap_cars.append(car)
        elif int(car["price"]) >= 1000 and int(car["price"]) < 5000:
            list_medium_cars.append(car)
        elif int(car["price"]) >= 5000:
            list_expensive_cars.append(car)

    f_json_obj(list_cheap_cars, "cheap_cars.json")
    f_json_obj(list_medium_cars, "medium_cars.json")
    f_json_obj(list_expensive_cars, "expensive_cars.json")


def brand_cars(list_cars):
    brand_set = {car["brand"] for car in list_cars}
    obj = {}

    for i in brand_set:
        obj[i] = []

    for car in list_cars:
        if car["brand"] in brand_set:
            obj[str(car["brand"])].append(car)

    for item in obj.keys():

        f_json_obj(obj[item], str(item) + ".json")s

def delete_old_json_files():
    current_file_path = os.path.abspath(os.getcwd())

    if os.path.isdir("output_data") == True:
        with os.scandir(current_file_path + "/output_data") as entries:
            for f_entry in entries:
                if f_entry.is_file() and ".json" in f_entry.name:
                    os.remove(f_entry)

        os.rmdir(current_file_path + "/output_data")




def create_folder():
    current_file_path = os.path.abspath(os.getcwd())
    folder_name = "output_data"
    path_folder = os.path.join(current_file_path, folder_name)

    if folder_name not in os.listdir(current_file_path):
        os.makedirs(path_folder)


delete_old_json_files()
create_folder()
generate_id(list_cars)
write_input_csv(list_cars, "input.csv")
read_list_cars = read_input_csv("input.csv")
hp_cars(read_list_cars)
price_cars(read_list_cars)
brand_cars(read_list_cars)

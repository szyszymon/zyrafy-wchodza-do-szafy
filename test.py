import csv
import json
from pathlib import Path
from typing import Dict, List

file_path = "./upskill/recipients"

def read_json(file_path):
   json_file = open(file_path, "r")
      # data = json.load(json_file)
      # print("Type:", type(data))
   print(json.load(json_file))

# def load_csv(file_path):
#    with open(file_path, 'r') as csv_file:
#       reader = csv.DictReader(csv_file, skipinitialspace=True)
#       return row in csv.DictReader

#ma jedynie używać metodę load_csv/json
# rozbij stringa na części i sprawdź rozszerzenie pliku
def load_file(file_path):
   extension = file_path.suffix.lower()
   # if extension == ".csv":
   #    return read_csv(file_path)
   if extension == ".json":
      return read_json(file_path)
   else:
      print("Invalid file type. Please provide csv or json.")
pass


# przekaż bajty (mają się nazywać się file_content) i przekaż do metody load_csv/load_json

# load_file("participiants\participiants1.csv")

# jak zamiana pliku .csv w dicta ma finalnie wyglądać:
# loaded_participants = [
#    dict(id = 1, firstname = "Tanny", last_name = "Bransgrove")
# ]
# pass
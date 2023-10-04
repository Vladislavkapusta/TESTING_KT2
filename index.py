import json
import csv
from csv import DictReader
import os.path
import math

FILES_DIR = os.path.dirname(__file__)

def get_path(filename: str):
    return os.path.join(FILES_DIR, filename)

JSON_FILE_PATH = get_path(filename="users.json")
CSV_FILE_PATH = get_path(filename="books.csv")

with open(CSV_FILE_PATH, newline="") as csv_file:
    reader = csv.reader(csv_file)
    header = next(reader)
    books_list = []
    for row in reader:
        books_list.append(dict(zip(header, row)))

with open(JSON_FILE_PATH, "r") as json_file:
    users_list = json.loads(json_file.read())
num_users = len(users_list)
num_books = len(books_list)
difference = math.floor(num_books / num_users)

user_index = 0
for i in range(0, num_books + difference - 1, difference):
    print("ind: ", i, "user: ", user_index)
    if user_index == num_users:
        break
    users_list[user_index]["BOOKS"] = []
    for book_index in range(i, i + difference):
        users_list[user_index]["BOOKS"].append(books_list[book_index])
    user_index += 1

for i in range(0, num_users):
    if user_index * difference + i < num_books:
        users_list[i]["BOOKS"].append(books_list[user_index * difference + i])

with open("result.json", "w") as result_file:
    s = json.dumps(users_list, indent=4)
    result_file.write(s)
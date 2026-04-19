import time
import json

print("Loading data.")

with open("database.json", "r")as d:
    data = json.load(d)

def save_data():
    with open("database.json", "w")as d:
        json.dump(data, d, indent=4 )

time.sleep(2)
print("loadded")
time.sleep(2)

if data['login'] == "":
    print("You need register.")
    time.sleep(2.1)
    create_login = input("Write a login here : ")
    data['login'] =  create_login
    save_data()
    print(f"Your login : {data['login']} ")
import time
import json
import os
from colorama import Fore, Style

print("Loading data.")

with open("database.json", "r")as d:
    data = json.load(d)

def save_data():
    with open("database.json", "w")as d:
        json.dump(data, d, indent=4 )

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

time.sleep(2)
print("loadded")
time.sleep(2)
while True:
    if data['login'] == "":
        clear_console()
        print("You need register.")
        time.sleep(2.1)
        create_login = input("Write a login here : ")
        data['login'] =  create_login
        save_data()
        print(f"Your login : {data['login']} ")

    if data['password']  == "":
        clear_console()
        print(Fore.GREEN + "Time a create password!" + Style.RESET_ALL)
        create_password = input("Write your password : ")
        data['password'] = create_password
        save_data()
        time.sleep(1)
        print("Success")

    if data['description'] == "":
        clear_console()
        print(Fore.GREEN + "Tell  about your self " + Style.RESET_ALL)
        create_description = input("")
        data['description'] = create_description
        save_data()

    clear_console()
    print("Is information correct?")
    print("##########")
    print(f" Your login : {data['login']}")
    print(f" Description : {data['description']}")
    print(Fore.RED + f" Your password : {data['password']}" + Style.RESET_ALL)
    print("###########")
    print(Fore.RED + "DONT SHOW YOUR PASSWORD TO ANYONE" + Style.RESET_ALL)
    time.sleep(3)

    choice = input("yes or no  : ").strip().lower()

    if choice == "yes":
        break

    elif choice == "no":

        data['login'] = ""
        data['password'] = ""
        save_data()
        continue


while True:
    print(f"Welcome {data['login']}")
    break # === delete this if you dont need.


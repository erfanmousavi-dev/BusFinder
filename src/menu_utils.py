import jdatetime
from src import models

origins = [
    models.City(0, "Isfahan", "اصفهان"),
    models.City(1, "Tehran", "تهران"),
    models.City(2, "Kashan", "کاشان")
]

destinations = [
    models.City(0, "Isfahan", "اصفهان"),
    models.City(1, "Tehran", "تهران"),
    models.City(2, "Kashan", "کاشان")
]

def set_origin_destination():
    origin_destination = []
    for city in origins:
        print(f"{city.id} : {city.english_name}")
    print("\n")
    origin_id = int(input("Please enter an city id for origin : "))
    print("\n")
    origin_destination.append(find_city_by_id(origin_id,origins))
    for city in destinations:
        print(f"{city.id} : {city.english_name}")
    print("\n")
    destination_id = int(input("Please enter an city id for destination : "))
    origin_destination.append(find_city_by_id(destination_id,destinations))
    return origin_destination

def find_city_by_id(id, list):
    for city in list:
        if (id == city.id):
            return city.farsi_name

def set_date():
    today = jdatetime.date.today()
    year = today.year
    month = today.month
    day = today.day
    today_jalali = f"{year}/{month:02}/{day:02}"
    print(f"Today is : {today_jalali}")
    print("\n")
    result = input("Please enter the date in the above format (t for today) : ")
    print ("\n")
    if (result == "t"):
        print (f"Date set to : {today_jalali}")
        return today_jalali
    else:
        print (f"Date set to : {result}")
        return result
    
if (__name__ == "__main__"):
    print ("Please run the main program using main.py !")

class City:
    def __init__(
        self,
        id,
        english_name,
        farsi_name
    ):
        self.id = id
        self.english_name = english_name
        self.farsi_name = farsi_name 

    def __str__(self):
        return f"id : {self.id} english_name : {self.english_name} farsi_name : {self.farsi_name} "

class BusTicket:
    def __init__(
        self,
        provider,
        terminal,
        bus_type,
        date,
        time,
        empty_slot,
        price,
        id
    ):
        self.provider = provider
        self.terminal = terminal
        self.bus_type = bus_type
        self.date = date
        self.time = time
        self.empty_slot = empty_slot
        self.price = price
        self.id = id

    def __str__(self):
        return f"provider : {self.provider} terminal : {self.terminal} bus_type : {self.bus_type} date : {self.date} time : {self.time} empty_slot : {self.empty_slot} price : {self.price} id : {self.id}"

class Seat:
    def __init__(
        self,
        row,
        column,
        number,
        status
    ):
        self.row = row
        self.column = column
        self.number = number
        self.status = status

    def __str__(self):
        return f"Seat {self.number} - Row:{self.row} Col:{self.column} Status:{self.status}"
     
if (__name__ == "__main__"):
    print ("Please run the main program using main.py !")

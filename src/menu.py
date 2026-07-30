from src import ticket_analyzer
from src import seat_analyzer
from src import menu_utils

def show_menu():
    
    origin = None
    destination = None
    date = None

    while (True):
        print ("\n")
        print ("0 : Exit")
        print ("1 : Set Origin & Destination")
        print ("2 : Set Date")
        print ("3 : Find !")
        print ("\n")

        user_choise = int(input("Enter a number >> "))

        if(user_choise == 0):
            break

        elif (user_choise == 1):
            print ("\n")
            origin_destination = menu_utils.set_origin_destination()
            origin = origin_destination[0]
            destination = origin_destination[1]

        elif (user_choise == 2):
            print ("\n")
            date = menu_utils.set_date()
            
        elif (user_choise == 3):
            tickets = ticket_analyzer.get_tickets(origin, destination, date)

            for ticket in tickets:
                print ("\n")
                ticket_analyzer.show_ticket(ticket)
                print ("\n")
                print ("\n")
                seats = seat_analyzer.get_seats(ticket.id)
                seat_analyzer.show_seats(seats)

        else:
            print ("\n")
            print ("Wrong Selection !")
            continue


if (__name__ == "__main__"):
    print ("Please run the main program using main.py !")
import requests
import json
import re
from src import models

def get_seats(service_id):

    url = f"https://www.payaneha.com/busticket/Ajaxdisplayseat?value={service_id}"

    headers = {
    "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    html = response.text

    match = re.search(
        r'var model = (\[.*?\]);',
        html,
        re.DOTALL
    )

    if not match:
        return []

    json_data = match.group(1)

    seats_data = json.loads(json_data)

    seats = []

    for seat in seats_data:

        seat_obj = models.Seat(
            row=seat["Row"],
            column=seat["Column"],
            number=seat["ChairNumber"],
            status=seat["Status"]
        )

        seats.append(seat_obj)

    return seats

def show_seats(seats):
    seat_map = {}

    for seat in seats:
        if seat.row not in seat_map:
            seat_map[seat.row] = []

        seat_map[seat.row].append(seat)

    print("----------------------")
    print("       راننده")
    print("----------------------")

    for row in sorted(seat_map.keys()):

        line = ""

        for seat in sorted(seat_map[row], key=lambda x: x.column):

            if seat.status == "e":
                symbol = f"[{seat.number}]"

            elif seat.status == "m":
                symbol = "[M]"

            elif seat.status == "f":
                symbol = "[F]"

            else:
                symbol = "   "

            line += symbol + " "

        print(line)

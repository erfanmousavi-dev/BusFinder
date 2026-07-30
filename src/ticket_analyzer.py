from src import models
from bs4 import BeautifulSoup
import requests

site_url = "https://www.payaneha.com/busticket/ajaxsearch"

def get_html(origin, destination, datemove):
    try:
        response = requests.get(f"{site_url}?origin={origin}&dest={destination}&datemove={datemove}")
        return response
    except Exception as e:
        print (f"Error in get request to the url with {e}")

def get_tickets(origin, destination, date):
    raw_html = get_html(origin, destination, date)

    soup = BeautifulSoup(raw_html.text, 'html.parser')

    tickets = []

    services = soup.find_all("div", class_="wecan_services")

    for service in services:

        provider_tag = service.find("a", class_="co-brand")
        provider = provider_tag.text.strip() if provider_tag else None

        terminal = None

        terminal_tag = service.find(
            "a",
            href=lambda x: x and "/busticket/terminal/" in x
        )

        if terminal_tag:
            span = terminal_tag.find("span")
            terminal = span.text.strip() if span else terminal_tag.text.strip()

        bus_type_tag = service.find("div", class_="bus-type")
        bus_type = bus_type_tag.text.strip() if bus_type_tag else None

        date_tag = service.find("span", class_="date")
        ticket_date = date_tag.text.strip() if date_tag else None

        time = None

        time_tag = service.find("div", class_="time-move")

        if time_tag:
            strong = time_tag.find("strong")

            if strong:
                time = strong.text.strip()

        empty_slot = None

        capacity_tag = service.find("span", class_="capacity")

        if capacity_tag:
            capacity_text = capacity_tag.text.strip()

            empty_slot = (
                capacity_text
                .replace("ظرفیت باقیمانده :", "")
                .replace("صندلی", "")
                .strip()
            )

        price = None

        price_tag = service.find("span", class_="price-pay")

        if price_tag:

            price_span = price_tag.find("span")

            if price_span:
                price = price_span.text.strip()

        seat_button = service.find(
            "a",
            class_="display-seat-btn"
        )

        if seat_button:

            service_id = seat_button.get(
                "data-servicecode"
            )

        else:

            service_id = None

        ticket = models.BusTicket(
            provider=provider,
            terminal=terminal,
            bus_type=bus_type,
            date=ticket_date,
            time=time,
            empty_slot=empty_slot,
            price=price,
            id=service_id
        )

        tickets.append(ticket)

    return tickets

def show_ticket(ticket):

    print("شرکت:", ticket.provider)
    print("ترمینال:", ticket.terminal)
    print("نوع:", ticket.bus_type)
    print("تاریخ:", ticket.date)
    print("ساعت:", ticket.time)
    print("ظرفیت:", ticket.empty_slot)
    print("قیمت:", ticket.price)
    print("ID:", ticket.id)
    
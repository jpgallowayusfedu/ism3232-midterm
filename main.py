"""Run the Harvest Table Catering event report."""

from business_rules import (
    calculate_event_total,
    format_event_line,
    largest_event,
    needs_second_chef,
    needs_signoff,
    total_booked,
)

events = [
    {"client": "Finch Law", "guest_price": 18.00, "guests": 20, "nonprofit": False},
    {"client": "Garden Club", "guest_price": 22.00, "guests": 40, "nonprofit": True},
    {"client": "Hilltop Gym", "guest_price": 30.00, "guests": 120, "nonprofit": False},
    {"client": "Island Pantry", "guest_price": 25.00, "guests": 150, "nonprofit": True},
    {"client": "Juniper Spa", "guest_price": 16.00, "guests": 30, "nonprofit": False},
    {"client": "Kettle Works", "guest_price": 20.00, "guests": 80, "nonprofit": False},
    {"client": "Lumen Labs", "guest_price": 15.00, "guests": 81, "nonprofit": False},
    {"client": "Marlow Gala", "guest_price": 70.00, "guests": 50, "nonprofit": True},
]

print("Harvest Table Catering - Event Report")

for event in events:
    event_total = calculate_event_total(
        event["guest_price"],
        event["guests"],
        event["nonprofit"],
    )
    signoff = needs_signoff(event_total)
    second_chef = needs_second_chef(event["guests"], event_total)

    print(
        format_event_line(
            event["client"],
            event_total,
            signoff,
            second_chef,
        )
    )

booked_total = total_booked(events)
average_total = booked_total / len(events)
largest_client = largest_event(events)

signoffs_needed = 0
second_chefs_needed = 0

for event in events:
    event_total = calculate_event_total(
        event["guest_price"],
        event["guests"],
        event["nonprofit"],
    )

    if needs_signoff(event_total):
        signoffs_needed += 1
    if needs_second_chef(event["guests"], event_total):
        second_chefs_needed += 1

print(f"Events: {len(events)}")
print(f"Total booked: ${booked_total:.2f}")
print(f"Average event total: ${average_total:.2f}")
print(f"Largest event total: {largest_client}")
print(f"Sign-offs needed: {signoffs_needed}")
print(f"Second chefs needed: {second_chefs_needed}")

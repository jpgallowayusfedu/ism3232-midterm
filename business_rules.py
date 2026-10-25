# business_rules.py
# Author: Jaden Galloway

MIN_DISCOUNT_GUESTS = 25
LARGE_EVENT_GUESTS = 100
SMALL_DISCOUNT = 0.05
LARGE_DISCOUNT = 0.12
SERVICE_FEE_LIMIT = 500.00
SERVICE_FEE = 75.00
SIGNOFF_LIMIT = 2500.00
SECOND_CHEF_GUEST_LIMIT = 80
SECOND_CHEF_TOTAL_LIMIT = 3000.00


def calculate_food_cost(guest_price: float, guests: int) -> float:
    """Calculate the food cost before discounts."""
    return guest_price * guests


def get_event_discount(guests: int, nonprofit: bool = False) -> float:
    """Return the discount rate for an event."""
    if guests < MIN_DISCOUNT_GUESTS:
        return 0.0
    elif guests < LARGE_EVENT_GUESTS:
        return SMALL_DISCOUNT
    elif nonprofit:
        return LARGE_DISCOUNT
    else:
        return SMALL_DISCOUNT


def calculate_event_total(
    guest_price: float, guests: int, nonprofit: bool = False
) -> float:
    """Calculate the final event total after discounts and fees."""
    food_cost = calculate_food_cost(guest_price, guests)
    discount_rate = get_event_discount(guests, nonprofit)
    discounted_cost = food_cost * (1 - discount_rate)

    if discounted_cost <= SERVICE_FEE_LIMIT:
        discounted_cost += SERVICE_FEE

    return discounted_cost


def needs_signoff(total: float) -> bool:
    """Determine whether an event requires manager sign-off."""
    return total > SIGNOFF_LIMIT


def needs_second_chef(guests: int, total: float) -> bool:
    """Determine whether an event requires a second chef."""
    return guests > SECOND_CHEF_GUEST_LIMIT or total >= SECOND_CHEF_TOTAL_LIMIT


def total_booked(events: list) -> float:
    """Calculate the combined total for all events."""
    total = 0.0

    for event in events:
        total += calculate_event_total(
            event["guest_price"],
            event["guests"],
            event["nonprofit"],
        )
    return total


def largest_event(events: list) -> str:
    """Return the client name of the event with the highest total."""
    if not events:
        return ""

    largest_client = events[0]["client"]
    largest_total = calculate_event_total(
        events[0]["guest_price"],
        events[0]["guests"],
        events[0]["nonprofit"],
    )

    for event in events[1:]:
        event_total = calculate_event_total(
            event["guest_price"],
            event["guests"],
            event["nonprofit"],
        )

        if event_total > largest_total:
            largest_total = event_total
            largest_client = event["client"]

    return largest_client


def format_event_line(
    client: str, total: float, signoff: bool, second_chef: bool
) -> str:
    """Format an event's information as one report line."""
    signoff_text = "yes" if signoff else "no"
    chef_text = "yes" if second_chef else "no"

    return (
        f"{client}: ${total:.2f} | sign-off: {signoff_text} | second chef: {chef_text}"
    )

from business_rules import (
    calculate_event_total,
    calculate_food_cost,
    format_event_line,
    get_event_discount,
    largest_event,
    needs_second_chef,
    needs_signoff,
    total_booked,
)


def test_calculate_food_cost_multiplies_price_by_guests():
    assert round(calculate_food_cost(18.00, 20), 2) == 360.00


def test_calculate_food_cost_with_zero_guests():
    assert round(calculate_food_cost(18.00, 0), 2) == 0.00


def test_discount_is_zero_below_25_guests():
    assert get_event_discount(24) == 0.0


def test_discount_starts_at_25_guests():
    assert get_event_discount(25) == 0.05


def test_small_discount_applies_at_99_guests():
    assert get_event_discount(99) == 0.05


def test_large_event_discount_tier_starts_at_100_guests():
    assert get_event_discount(100) == 0.05


def test_nonprofit_gets_larger_discount_at_100_guests():
    assert get_event_discount(100, nonprofit=True) == 0.12


def test_nonprofit_changes_event_total():
    regular_total = calculate_event_total(10.00, 100)
    nonprofit_total = calculate_event_total(10.00, 100, nonprofit=True)
    assert regular_total != nonprofit_total


def test_service_fee_applies_when_discounted_cost_is_500():
    assert round(calculate_event_total(25.00, 20), 2) == 575.00


def test_service_fee_applies_below_500():
    assert round(calculate_event_total(24.99, 20), 2) == 574.80


def test_service_fee_does_not_apply_above_500():
    assert round(calculate_event_total(25.01, 20), 2) == 500.20


def test_signoff_not_needed_below_2500():
    assert needs_signoff(2499.99) is False


def test_signoff_not_needed_at_exactly_2500():
    assert needs_signoff(2500.00) is False


def test_signoff_needed_above_2500():
    assert needs_signoff(2500.01) is True


def test_second_chef_not_needed_at_80_guests_with_low_total():
    assert needs_second_chef(80, 100.00) is False


def test_second_chef_needed_at_81_guests_with_low_total():
    assert needs_second_chef(81, 1000.00) is True


def test_second_chef_not_needed_below_3000_with_80_guests():
    assert needs_second_chef(80, 2999.99) is False


def test_second_chef_needed_at_3000_with_80_guests():
    assert needs_second_chef(80, 3000.00) is True


def test_total_booked_adds_two_event_totals():
    events = [
        {"client": "Finch Law", "guest_price": 10.00, "guests": 10, "nonprofit": False},
        {
            "client": "Garden Club",
            "guest_price": 20.00,
            "guests": 10,
            "nonprofit": False,
        },
    ]
    assert round(total_booked(events), 2) == 450.00


def test_total_booked_with_empty_list():
    assert round(total_booked([]), 2) == 0.00


def test_largest_event_returns_highest_total_client():
    events = [
        {"client": "Finch Law", "guest_price": 10.00, "guests": 10, "nonprofit": False},
        {
            "client": "Garden Club",
            "guest_price": 20.00,
            "guests": 10,
            "nonprofit": False,
        },
    ]
    assert largest_event(events) == "Garden Club"


def test_largest_event_returns_first_client_when_totals_tie():
    events = [
        {"client": "Finch Law", "guest_price": 10.00, "guests": 10, "nonprofit": False},
        {
            "client": "Garden Club",
            "guest_price": 10.00,
            "guests": 10,
            "nonprofit": False,
        },
    ]
    assert largest_event(events) == "Finch Law"


def test_largest_event_with_empty_list():
    assert largest_event([]) == ""


def test_format_event_line_returns_expected_text():
    result = format_event_line("Finch Law", 435.00, False, False)
    assert result == "Finch Law: $435.00 | sign-off: no | second chef: no"

# Terminal Record: Harvest Table Catering

## 1. Building the project

mkdir ism3232-midterm
cd ism3232-midterm
git init
git branch -M main
mkdir tests
touch business_rules.py main.py commands.md requirements.txt .gitignore tests/__init__.py tests/test_business_rules.py
printf ".venv/\n__pycache__/\n" > .gitignore
python3 -m venv .venv
source .venv/bin/activate
python3 -m venv .venv
source .venv/bin/activate
python -m pip install pytest ruff
pip freeze > requirements.txt
git remote add origin https://github.com/jpgallowayusfedu/ism3232-midterm.git

## 2. The virtual environment

Command:
which python3

Output:
/home/jadenpearlg/ism3232-midterm/.venv/bin/python3

This output shows us that the virtual environment is active as the Python executable path points to the project's '.venv' directory.

## 3. The project structure

Command:
tree -L 2

Output:
.
├── README.md
├── __pycache__
│   └── business_rules.cpython-314.pyc
├── business_rules.py
├── commands.md
├── main.py
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py

4 directories, 8 files

The '.venv' folder is on my computer but not in my GitHub repository because '.gitignore' excludes it but contains the project's local Python environment and dependencies. 

## 4. Every function and test

Command:
rg 'def '

Output:
business_rules.py
15:def calculate_food_cost(guest_price: float, guests: int) -> float:
20:def get_event_discount(guests: int, nonprofit: bool = False) -> float:
32:def calculate_event_total(
46:def needs_signoff(total: float) -> bool:
51:def needs_second_chef(guests: int, total: float) -> bool:
56:def total_booked(events: list) -> float:
69:def largest_event(events: list) -> str:
95:def format_event_line(

commands.md
60:13:def test_calculate_food_cost_multiplies_price_by_guests():
61:17:def test_calculate_food_cost_with_zero_guests():
62:21:def test_discount_is_zero_below_25_guests():
63:25:def test_discount_starts_at_25_guests():
64:29:def test_small_discount_applies_at_99_guests():
65:33:def test_large_event_discount_tier_starts_at_100_guests():
66:37:def test_nonprofit_gets_larger_discount_at_100_guests():
67:41:def test_nonprofit_changes_event_total():
68:47:def test_service_fee_applies_when_discounted_cost_is_500():
69:51:def test_service_fee_applies_below_500():
70:55:def test_service_fee_does_not_apply_above_500():
71:59:def test_signoff_not_needed_below_2500():
72:63:def test_signoff_not_needed_at_exactly_2500():
73:67:def test_signoff_needed_above_2500():
74:71:def test_second_chef_not_needed_at_80_guests_with_low_total():
75:75:def test_second_chef_needed_at_81_guests_with_low_total():
76:79:def test_second_chef_not_needed_below_3000_with_80_guests():
77:83:def test_second_chef_needed_at_3000_with_80_guests():
78:87:def test_total_booked_adds_two_event_totals():
79:100:def test_total_booked_with_empty_list():
80:104:def test_largest_event_returns_highest_total_client():
81:117:def test_largest_event_returns_first_client_when_totals_tie():
82:130:def test_largest_event_with_empty_list():
83:134:def test_format_event_line_returns_expected_text():
86:15:def calculate_food_cost(guest_price: float, guests: int) -> float:
87:20:def get_event_discount(guests: int, nonprofit: bool = False) -> float:
88:32:def calculate_event_total(
89:46:def needs_signoff(total: float) -> bool:
90:51:def needs_second_chef(guests: int, total: float) -> bool:
91:56:def total_booked(events: list) -> float:
92:69:def largest_event(events: list) -> str:
93:95:def format_event_line(

tests/test_business_rules.py
13:def test_calculate_food_cost_multiplies_price_by_guests():
17:def test_calculate_food_cost_with_zero_guests():
21:def test_discount_is_zero_below_25_guests():
25:def test_discount_starts_at_25_guests():
29:def test_small_discount_applies_at_99_guests():
33:def test_large_event_discount_tier_starts_at_100_guests():
37:def test_nonprofit_gets_larger_discount_at_100_guests():
41:def test_nonprofit_changes_event_total():
47:def test_service_fee_applies_when_discounted_cost_is_500():
51:def test_service_fee_applies_below_500():
55:def test_service_fee_does_not_apply_above_500():
59:def test_signoff_not_needed_below_2500():
63:def test_signoff_not_needed_at_exactly_2500():
67:def test_signoff_needed_above_2500():
71:def test_second_chef_not_needed_at_80_guests_with_low_total():
75:def test_second_chef_needed_at_81_guests_with_low_total():
79:def test_second_chef_not_needed_below_3000_with_80_guests():
83:def test_second_chef_needed_at_3000_with_80_guests():
87:def test_total_booked_adds_two_event_totals():
100:def test_total_booked_with_empty_list():
104:def test_largest_event_returns_highest_total_client():
117:def test_largest_event_returns_first_client_when_totals_tie():
130:def test_largest_event_with_empty_list():
134:def test_format_event_line_returns_expected_text():

The file 'business_rules.py' defines 8 functions, and 'tests/test_business_rules.py' defines 24 test functions.

## 5. Which files print

Command:
rg -l 'print'

Output:
commands.md
main.py

'main.py' prints the event report and summary and 'business_rules.py' is not in the list because it contains calculation and decision-making functions and not report output.

## 6. The commit history

Command:
git log --oneline

Output:

0b89759 (HEAD -> main, origin/main) Add The virtual environment, The project structure, and Every function and test to commands.md
a2a951f Add Building the project to commands.md
0865f83 Add event report and business rule tests
45f2264 Add event report and summary calculations
cde75fd Added functions to business_rules.py
9dbb4ad Set up midterm project structure

There are 6 commits at this point.
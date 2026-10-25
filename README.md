# ISM3232 Midterm: Harvest Table Catering

- **Name:** Jaden Galloway
- **Version:** 1.0
- **Date:** October 25, 2026

## What This Program Does

This program calculates event costs for Harvest Table Catering. The rules are based on guest count, price per guest, nonprofit status, and the business's pricing rules. It generates an event report that shows each client's total, whether or not the manager sign-off is required, and whether a second chef is needed. This program also summarizes the total amount booked, average event total, largest event, and staffing requirments.

Business Rules
1. The food cost is the price per guest times the number of guests
2. The discount depends on the number of guests. Events with fewer than 25 guests reveive no discount. Events with 25-99 guests receive a 5% discount, but registered nonprofits receive a 12% discount.
3. The 12% discount is only for registered nonprofits. Any other event of 100 guests or more gets the 5% discount.
4. A $75 service fee is added when the discounted cost is $500 or less.
5. An event total of more than $2,500 needs a manager's sign-off.
6. An event needs a second chef when it has more than 80 guests or its event total is $3,000 or more. 

## How to Run

Create and activate a virtual environment, install the project requirements, and run the report from the project folder.

python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirments.txt
python main.py

## How to Test
Be sure to run Ruff to format and check the code, then run pytest to execute the automated tests.

ruff format .
ruff check .
pytest -v

This project contains 24 pytest tests covering the business-rull functions, boundary values, event totals, and report formatting.

## Files in This Repository

business_rules.py - Contains the eight functions that calculate event costs, discounts, staffing requirements, and report lines.
main.py - Runs the event report and prints the summary statistics.
commands.md - Records the terminal commands and their outputs used to build and inspect the project.
README.md - Explains the program, business rules, setup, testing, and repository files.
requirements.txt - Lists the Python packages required by the project.
.gitignore - Excludes local files and folders, including .venv/ and __pycache__/, from Git tracking.
tests/__init__.py - Contains the automated pytest tests for the business-rule functions.
tests/test_business_rules.py - Contains the automated pytest tests for the business-rule functions.

## AI Use Statement

I have not used AI tools in the creation of this project.

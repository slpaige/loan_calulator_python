import argparse
import math
import sys


def calculate_nominal_interest():
    nominal = interest / (12 * 100)
    return nominal


def calculate_annuity():
    nominal_int = calculate_nominal_interest()
    raised_by = math.pow(1 + nominal_int, periods)
    monthly_total = math.ceil(principal * ((nominal_int * raised_by) / (raised_by - 1)))
    over_payment = (monthly_total * periods) - principal
    print(f"Your annuity payment = {monthly_total}!")
    print(f"Overpayment = {over_payment}")


def calculate_principal():
    nominal_int = calculate_nominal_interest()
    raised_by = math.pow(1 + nominal_int, periods)
    loan_amount = math.floor(payment / ((nominal_int * raised_by) / (raised_by - 1)))
    over_payment = (payment * periods) - loan_amount
    print(f"Your loan principal = {loan_amount}!")
    print(f"Overpayment = {over_payment}")


def calculate_periods():
    nominal_int = calculate_nominal_interest()
    log_value = math.log(payment / (payment - nominal_int * principal), 1 + nominal_int)
    num_payments = math.ceil(log_value)
    over_payment = (payment * num_payments) - principal

    years = num_payments // 12
    months = num_payments % 12

    year_or_years = "year" if years == 1 else "years"
    month_or_months = "month" if months == 1 else "months"

    # figure out the years/months wording here
    if years > 0 and months > 0:
        print(f"It will take {years} {year_or_years} and {months} {month_or_months} to repay this loan!")
    elif years > 0 and months == 0:
        print(f"It will take {years} {year_or_years} to repay this loan!")
    elif years == 0 and months > 0:
        print(f"It will take {months} {month_or_months} to repay this loan!")
    print(f"Overpayment = {over_payment}")


def calculate_differentiated():
    nominal_int = calculate_nominal_interest()
    sum_monthly_payment = 0

    count = 1
    while count <= periods:
        monthly_payment = math.ceil(principal / periods + (nominal_int * (principal - (principal * (count - 1)) /
                                                                          periods)))
        print(f"Month {count}: payment is {monthly_payment}")
        sum_monthly_payment += monthly_payment
        count += 1

    over_payment = sum_monthly_payment - principal
    print()
    print(f"Overpayment is {over_payment}")


parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--payment", default=0, type=int)
parser.add_argument("--principal", default=0, type=int)
parser.add_argument("--periods", default=0, type=int)
parser.add_argument("--interest", default=0.0, type=float)

passed_args = parser.parse_args()

calc_type = passed_args.type
payment = passed_args.payment
principal = passed_args.principal
periods = passed_args.periods
interest = passed_args.interest

# type check
if calc_type == "None" or (calc_type != "annuity" and calc_type != "diff"):
    print("Incorrect parameters")
    exit(1)

if len(sys.argv) != 5:
    print("Incorrect parameters")
    exit(1)


if calc_type == "diff":
    # diff must be this combination
    # principal, periods, interest
    if payment == 0:
        if principal > 0 and periods > 0 and interest > 0:
            calculate_differentiated()
        else:
            print("Incorrect parameters")
    else:
        print("Incorrect parameters")
elif calc_type == "annuity":
    # annuity can be these combinations
    # principal, periods, interest (find annuity/monthly payment + overpayment)
    # payments, periods, interest (find principal + overpayment)
    # principal, payment, interest  (find periods + overpayment)
    if payment == 0:
        if principal > 0 and periods > 0 and interest > 0:
            calculate_annuity()
        else:
            print("Incorrect parameters")
    elif principal == 0:
        if payment > 0 and periods > 0 and interest > 0:
            calculate_principal()
        else:
            print("Incorrect parameters")
    elif periods == 0:
        if principal > 0 and payment > 0 and interest > 0:
            calculate_periods()
        else:
            print("Incorrect parameters")

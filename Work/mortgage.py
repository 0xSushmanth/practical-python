# mortgage.py
#
# Exercise 1.7

def amount_paid(principal: float, interest_rate: float, payment: float, time: int) -> float:
    """
    Calculate the amount to be paid for a mortgage.
    
    Args:
        principal (float): The initial loan amount (principal).
        interest_rate (float): The interest rate.
        payment (float): The monthly payment amount.
        time (int): The time period for repayment (in months).

    Returns:
        float: The total amount paid.
    """
    amount = 0
    while principal > 0:
        principal = principal * (1 + interest_rate / 12) - payment
        amount += payment
    return amount

def main() -> None:
    principal = 500000.0
    rate = 0.05
    payment = 2684.11
    total_paid = 0.0
    month = 0

    extra_payment = 1000.0
    extra_payment_start_month = 61
    extra_payment_end_month = 108

    print("Month   Total Paid   Remaining Principal")
    while principal > 0:
        month += 1
        principal = principal * (1 + rate / 12) - payment
        total_paid += payment

        if extra_payment_start_month <= month <= extra_payment_end_month:
            principal -= extra_payment
            total_paid += extra_payment

        # Using printf style formatting
        print("%-6d %-12.2f %-12.2f" % (month, round(total_paid, 2), round(principal, 2)))

        # Using format method
        # print("{:<6d} {:<12.2f} {:<12.2f}".format(month, round(total_paid, 2), round(principal, 2)))

    print("Total paid: {:.2f}".format(total_paid))
    print("Months:", month)

if __name__ == "__main__":
    main()

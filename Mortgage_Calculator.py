#Q1: Define the mortgage payment function
def mortgage_payments(principal, rate, amortization):
    """
    Calculate mortgage payments based on different payment frequencies.

    Parameters:
        principal (float): Loan amount
        rate (float): Quoted annual interest rate (percentage)
        amortization (int): Amortization period in years

    Returns:
        tuple: Monthly, semi-monthly, bi-weekly, weekly, rapid bi-weekly, and rapid weekly payments
    """
    #convert quoted interest rate to decimal
    rq = rate / 100

    #Calculate periodic interest rates
    r_monthly = (1 + rq / 2) ** (2/12) -1
    r_semi_monthly = (1 + rq / 2) ** (2/24) - 1
    r_bi_weekly = (1 + rq / 2) ** (2/26) - 1
    r_weekly = (1 + rq / 2) ** (2/52) - 1

    #Convert amortization years to total payments
    n_monthly = amortization * 12
    n_semi_monthly = amortization * 24
    n_bi_weekly = amortization * 26
    n_weekly = amortization * 52

    #Present Value of Annuity formula (PVA)
    def calculate_payment(r, n):
        return (principal * r) / (1 - (1 + r) ** -n)

    #Calculate payments
    monthly_payment = calculate_payment(r_monthly, n_monthly)
    semi_monthly_payment = calculate_payment(r_semi_monthly, n_semi_monthly)
    bi_weekly_payment = calculate_payment(r_bi_weekly, n_bi_weekly)
    weekly_payment = calculate_payment(r_weekly, n_weekly)

    #Accelerated payments
    rapid_bi_weekly_payment = monthly_payment / 2
    rapid_weekly_payment = monthly_payment / 4

    return (
        round(monthly_payment, 2),
        round(semi_monthly_payment, 2),
        round(bi_weekly_payment, 2),
        round(weekly_payment, 2),
        round(rapid_bi_weekly_payment, 2),
        round(rapid_weekly_payment, 2),
    )

#Question 2: Prompt the user for input
principal = float(input("Enter the principal amount ($): "))
rate = float(input("Enter the annual interest rate (%): "))
amortization = int(input("Enter the amortization period (years): "))

#Question 3: Call the function and format the output
payments = mortgage_payments(principal, rate, amortization)

#Print the results in the required format
print(f"\nMortgage Payment Breakdown:")
print(f"Monthly Payment: ${payments[0]:.2f}")
print(f"Semi-monthly Payment: ${payments[1]:.2f}")
print(f"Bi-weekly Payment: ${payments[2]:.2f}")
print(f"Weekly Payment: ${payments[3]:.2f}")
print(f"Rapid Bi-weekly Payment: ${payments[4]:.2f}")
print(f"Rapid Weekly Payment: ${payments[5]:.2f}")


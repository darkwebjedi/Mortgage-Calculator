# Get user input
print("=== Mortgage Calculator ===")
P = float(input("Enter the principal amount (loan amount): £"))
annual_rate = float(input("Enter the annual interest rate (%): "))
years = int(input("Enter the loan term (years): "))

# Step 2: Converting interest rate and term
mR = (annual_rate / 100) / 12   # Monthly interest rate
tT = years * 12                 # Total number of payments

# Step 3: Calculating monthly payment (mP) - Fixed formula
mP = P * (mR * (1 + mR) ** tT) / ((1 + mR) ** tT - 1)

# Step 4: Calculating first month's breakdown
iP = P * mR                     # Interest portion of first payment
pP = mP - iP                    # Principal portion
cP = P - pP                     # Remaining balance after first payment

# Step 5: Results
print("\n=== Mortgage Calculation Results ===")
print(f"Principal Amount: £{P:,.2f}")
print(f"Annual Interest Rate: {annual_rate}%")
print(f"Loan Term: {years} years")
print(f"Monthly Payment: £{mP:,.2f}")
print(f"Interest Portion (1st payment): £{iP:,.2f}")
print(f"Principal Portion (1st payment): £{pP:,.2f}")
print(f"Remaining Balance (after 1st payment): £{cP:,.2f}")
print(f"Total Interest over {years} years: £{(mP * tT - P):,.2f}")
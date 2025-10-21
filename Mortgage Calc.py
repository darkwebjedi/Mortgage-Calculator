P = 200000          
annual_rate = 5     # Annual interest rate (%)
years = 30          # Loan term (years)

# Step 2: Convert interest rate and term
mR = (annual_rate / 100) / 12   # Monthly interest rate
tT = years * 12                 # Total number of payments

# Step 3: Calculate monthly payment (mP)
mP = P * (mR * (1 + mR) * tT) / ((1 + mR) * tT - 1)

# Step 4: Calculate first month's breakdown
iP = P * mR                     # Interest portion of first payment
pP = mP - iP                    # Principal portion
cP = P - pP                     # Remaining balance after first payment

# Step 5: Display results
print("Monthly Payment: £", round(mP, 2))
print("Interest Portion: £", round(iP, 2))
print("Principal Portion: £", round(pP, 2))
print("Remaining Balance: £", round(cP, 2))
import csv
from pathlib import Path

"""Part 1: Automate the Calculations.

Automate the calculations for the loan portfolio summaries.

First, let's start with some calculations on a list of prices for 5 loans.
    1. Use the `len` function to calculate the total number of loans in the list.
    2. Use the `sum` function to calculate the total of all loans in the list.
    3. Using the sum of all loans and the total number of loans, calculate the average loan price.
    4. Print all calculations with descriptive messages.
"""
loan_costs = [500, 600, 200, 1000, 450]

total_loans = (len(loan_costs))

print(f"The total number of loans is",{total_loans})

total_sums = (sum(loan_costs))

print(f"The total of all loans is $",{total_sums})

average_loan = total_sums / total_loans

print(f"The average loan amount is $",{average_loan})

"""Part 2: Analyze Loan Data.

Analyze the loan to determine the investment evaluation.

1. Use get() on the dictionary of additional information to extract the **Future Value** and **Remaining Months** on the loan.
    a. Save these values as variables called `future_value` and `remaining_months`.
    b. Print each variable.

2. Use the formula for Present Value to calculate a "fair value" of the loan. Use a minimum required return of 20% as the discount rate.
3. Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
    a. If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
    b. Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

"""

# Given the following loan data, you will need to calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

future_value = (loan.get("future_value"))
remaining_months = (loan.get("remaining_months"))
loan_price = (loan.get("loan_price"))

print(f"The future value is $",{future_value})
print(f"The remaining months for the house is",{remaining_months})
print(f"The loan price is $",{loan_price})

present_value = future_value / (1 + .20/12) ** remaining_months

print(f"The present value is $",{round(present_value,2)})

if present_value >= loan_price:
    print("The loan is worth the cost")
else:
        print("Loan is too expensive and not worth the price")
"""Part 3: Perform Financial Calculations.

Perform financial calculations using functions.

1. Define a new function that will be used to calculate present value.
    a. This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
    b. The function should return the `present_value` for the loan.
2. Use the function to calculate the present value of the new loan given below.
    a. Use an `annual_discount_rate` of 0.2 for this new loan calculation.
"""

new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

def calculate_present_value(future_value, remaining_months, annual_discount_rate):
    pv = future_value / (1 + annual_discount_rate/12) ** remaining_months
    return pv

annual_discount_rate = .2
pv_of_new_loan = calculate_present_value(new_loan["future_value"], new_loan["remaining_months"], annual_discount_rate)

print(f"The present value of the loan is: {round(pv_of_new_loan,2)}")


"""Part 4: Conditionally filter lists of loans.

1. Create a new, empty list called `inexpensive_loans`.
2. Use a for loop to select each loan from a list of loans.
    a. Inside the for loop, write an if-statement to determine if the loan_price is less than 500
    b. If the loan_price is less than 500 then append that loan to the `inexpensive_loans` list.
3. Print the list of inexpensive_loans.
"""

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,

        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

inexpesive_loans = []

for loan in loans :
    if loan['loan_price'] <= 500:
        inexpesive_loans.append(loan)
    


print("This is the inexpensive loans list", inexpesive_loans)

"""Part 5: Save the results.

Output this list of inexpensive loans to a csv file
    1. Use `with open` to open a new CSV file.
        a. Create a `csvwriter` using the `csv` library.
        b. Use the new csvwriter to write the header variable as the first row.
        c. Use a for loop to iterate through each loan in `inexpensive_loans`.
            i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.
"""
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

csvpath = Path("Jose_Medina_Challenge_1.csv")
with open(csvpath, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)
    for row in inexpesive_loans:
        csvwriter.writerow(row.values())
# # Set the output header

# # Set the output file path
output_path = Path("Jose_Medina_Challenge_1.csv")

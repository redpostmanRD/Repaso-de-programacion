"""
Write a program that calculates the future value of 1000 USD with an annual interest rate of 3%,
annual capitalization and a 5-year investment period. Round the result to the nearest cent.

Tip: Use compound capitalization of interest.

Print the result to the console as shown below.

Expected result:

The future value of the investment: 1159.27 USD
"""
irate=3/100
principal_money=1000
year=5
iratepertime=(principal_money*((1+irate)**year))-principal_money
totalwin=iratepertime+principal_money
print(f"The future value of the investment: {totalwin:.2f} USD")

#Solution By book:
#pv = 1000
#r = 0.03
#n = 5
#fv = pv * (1 + r) ** n
#print(f'The future value of the investment: {fv:.2f} USD')


"""
Compound interest = total amount of principal and interest in future (or future value) minus principal amount at present (or present value)
= [P (1 + i)^n] - P
= P [(1 + i)^n - 1]
Where:

P = principal
i = nominal annual interest rate in percentage terms
n = number of compounding periods
"""

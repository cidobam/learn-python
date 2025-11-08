# I start with 1000 Euros
# I will get %1.5 interest per month
# How much money I get in 5 years?

principal = 1000

rate_per_month = 0.015

month = 1


while month <= 60:
    interest = principal * rate_per_month
    principal = principal + interest
    month += 1

print(principal)


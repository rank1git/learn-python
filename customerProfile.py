"""
Customer Profile Generator
Generates a formatted customer profile from raw data.
Includes name formatting, deal value formatting,
tier classification, and tenure messaging.
"""

first_name = input("first name: ")
last_name = input("last name: ")
age = input("age: ")
deal_value = float(input("deal value: "))
years_as_customer = int(input("years as a customer: "))
product = input("product name: ")

heading = "===== CUSTOMER PROFILE ====="
full_name = first_name.capitalize() + " " + last_name.capitalize()
new_deal_value = f"{deal_value:,.2f}"
if deal_value < 10000:
    customer_tier = 'Bronze'
elif 10000 <= deal_value <= 25000:
    customer_tier = 'Gold'
else:
    customer_tier = 'Platinum'

tenure_message = f"{first_name.capitalize()} has been a valued {product.title()} customer for {years_as_customer} years!"

print(f"{heading}\n Name:\t\t {full_name}\n Age:\t\t {int(age)}\n Product:\t {product.title()}\n Deal Value:\t {new_deal_value}\n Customer Tier:\t {customer_tier}\n Tenure Message: \"{tenure_message}\"\n ============================")

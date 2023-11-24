hour = float(input("Please input hours worked "))
wage = float(input("Please input hourly wage "))

# This is based off a one week pay period

if hour > 40:
    reg_hours = 40
    OT = hour - 40
    pay1 = reg_hours * wage
    OTwage = wage * 1.5
    OTpay = OT * OTwage
    total = pay1 + OTpay
else:
    total = hour * wage

total = round(total, 2)

print(f"Before taxes your total pay is ${total}")

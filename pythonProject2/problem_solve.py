'''
loan_amount=1260000
duration 8 year then down payment 300000 and interest rate 10%
when duration 10 year then rate of interest 8% and no down payment required..
EMI=p*r*(1+r)**n/((1+r)**n-1)
p- Principle amount
r- rate of interest
n- time in month
'''
def loan_emi(amount,duration,down_payment=0):
    loan_amount=amount-down_payment
    emi=loan_amount/duration
    return emi
emi1=loan_emi(amount=1260000,duration=8*12,down_payment=300000)
print(emi1)
emi2=loan_emi(1260000,10*12)
print(emi2)
# import math
# help(math.ceil)
def loan_emi(amount,duration,interest,down_payment=0.0):
    loan_amount=amount-down_payment
    try:
        emi=loan_amount*interest*((1+interest)**duration)/((1+interest)**duration-1)
    except ZeroDivisionError:
        emi=loan_amount/duration
    return emi
emi1=loan_emi(
    amount=1260000,
    duration=8*12,
    interest=0.1/12,
    down_payment=300000
)
print(round(emi1,2))
emi2=loan_emi(
    amount=1260000,
    duration=10*12,
    interest=0.08/12
)
print(round(emi2,2))

cost_of_house=800000
house_loan_duration=6*12
house_interest=0.07/12
house_down_payment=0.25*cost_of_house
house_emi=loan_emi(amount=cost_of_house,duration=house_loan_duration,interest=house_interest,down_payment=house_down_payment)
print(round(house_emi,2))
car_price=60000
car_loan_duration=1*12
car_interest=0.12/12
car_emi=loan_emi(amount=car_price,duration=car_loan_duration,interest=car_interest)
print(round(car_emi,2))
print("Shaun,Total monthly ${} payment makes towards loans".format(round((house_emi+car_emi),2)))
emi_with_interest=loan_emi(amount=100000,duration=10*12,interest=0.09/12)
print("EMI with intrest ${}".format(round(emi_with_interest,2)))
emi_without_interest=loan_emi(100000,2*12,0/12)
print("EMI without interest is ${}".format(round(emi_without_interest,2)))

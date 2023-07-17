'''city     return_flight($)    hotel_per_day($)    weekly_car_rent($)
    Paris       200                 20                  200
    London      250                 30                  120
    Dubai       370                 15                  80
    Mumbai      450                 10                  70
if you're planning for 1-week long trip, which city should you visit to spend the least amount of money?
how does answer if you change the duration of the trip 4 days,10 days and 2-week?
if your total budget for trip is $1000 which city should you visit to maximize the duration of your trip? which city for minimize the duration?
how answered if budget is $600,$200 and $1500?
'''
def cost_of_trip(flight_cost,hotel_rate,car_rental_rate,duration_of_the_trip):
    
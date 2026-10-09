#Program that reads how many days did you rented a car and how many km's you drove.
day_cost = 60
km_cost = 0.15
rent_days = (float(input("How many days did you rented the car? ")))
rent_km = (float(input("How many km's did you drove in those days? ")))
days_total = rent_days * day_cost
km_total = rent_km * km_cost

print("The total amount of the rent is ${}. Being ${} for the {:.0f} days and ${} for the {}km's you drove.".format(days_total+km_total, days_total, rent_days, km_total, rent_km))
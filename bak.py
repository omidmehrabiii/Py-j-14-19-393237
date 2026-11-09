





tank_capacity = float(input("Enter fuel tank capacity (liters): "))

fuel_consumption = float(input("Enter fuel consumption per 100 km (liters): "))

distance = (tank_capacity / fuel_consumption) * 100

print("The car can travel", distance, "kilometers with a full tank.")
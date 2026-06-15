cars=["swift","dzire","bmw"]
number_plate=["2328","0002","0001"]

cars.append("audi")
number_plate.append("9921")

print("Cars:",cars)
print("Number_plate:",number_plate)

for i in range(len(cars)):
    print(f"Cars:{cars[i]}, Number_plate:{number_plate[i]}")

# Calculations and comparisons
# Calculate speed for 4 metres over 2 seconds. Decide whether it is at or below a 2 m/s limit, then repeat for 5 metres. Print the speed and comparison for each case.
# Write your attempt below. See the course page for expected results.
distance_m = 4.0
elapsed_s = 2.0
speed = distance_m / elapsed_s
print("speed:", speed, "m/s")
if speed <= 2.0:
    print("The robot is being a good robot")
distance_m = 5.0
speed = distance_m / elapsed_s
print("speed:", speed, "m/s")
if speed > 2.0:
    print("The bot is speeding and is NOT a good robot >:C")
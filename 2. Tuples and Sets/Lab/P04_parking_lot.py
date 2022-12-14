# Write a program that: •	Records a car number for every car that enters the parking lot •	Removes a car number
# when the car leaves the parking lot On the first line, you will receive the number of commands - N. On the
# following N lines, you will receive the direction and car's number in the format: "{direction}, {car_number}". The
# direction could only be "IN" or "OUT". Print the car numbers which are still in the parking lot. Keep in mind that
# all car numbers must be unique. If the parking lot is empty, print "Parking Lot is Empty". Note: The order in which
# we print the result does not matter.

n = int(input())
parking = set()
for _ in range(n):
    direction, license_plate = input().split(', ')
    if direction == "IN":
        parking.add(license_plate)
    elif direction == "OUT":
        parking.remove(license_plate)
if parking:
    print('\n'.join(parking))
else:
    print("Parking Lot is Empty")
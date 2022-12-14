# There is a party at SoftUni. Many guests are invited, and there are two types of them: Regular and VIP. When a guest
# comes, check if they exist on any of the two reservation lists. On the first line, you will receive the number of
# guests – N. On the following N lines, you will be receiving their reservation codes. All reservation codes are 8
# characters long, and all VIP numbers will start with a digit. Keep in mind that all reservation numbers must be
# unique. After that, you will be receiving guests who came to the party until you read the "END" command. In the end,
# print the number of guests who did not come to the party and their reservation numbers: •	The VIP guests must be
# first. •	Both the VIP and the Regular guests must be sorted in ascending order.

n = int(input())
guests = set()

for _ in range(n):
    guest_id = input()
    guests.add(guest_id)
additional_guest = input()

while not additional_guest == "END":
    guests.remove(additional_guest)
    additional_guest = input()
print(len(guests))
sorted_guests = sorted(guests)
for i in sorted_guests:
    print(i)

import os
import pandas as pd
import random as rd
from tabulate import tabulate

max_history_length = 5

filename = "secret_santa.csv"
if os.path.exists(filename):
	history_df = pd.read_csv(filename)
	history_dict = history_df.to_dict(orient='list')
	guests = list(history_dict.keys())
else:
	guests = ["Mathew", "Sarah", "Brendan", "Hannah", "Awkward Waiter", 
			  "Plant Shop Witch", "Metal Market Vendor", "Kiki", "Hal"]
	history_dict = {guest:[] for guest in guests}
	history_df = pd.DataFrame(history_dict)

# for each guest
# get list of valid options which is full guest list minus: 
#	- past choices
#   - the guest's self
#	- guests already chosen

max_attempts = 10000
attempts = 0
current = {}
while attempts < max_attempts and len(current) < len(guests):
	# print("\n" + f"Attempt {attempts}" + "_"*50 + "\n")
	chosen = []
	current = {}
	for guest in guests:

		# print(f"guest: {guest}")
		# print(f"history_dict: {set(history_dict[guest][-max_history_length:])}")
		# print(f"chosen: {set(chosen)}")

		options = set(guests) - {guest} \
				  - set(history_dict[guest][-max_history_length:]) - set(chosen)

		if len(options) > 0:
			# print(f"options: {options}")
			option = rd.choice(list(options))
			current[guest] = option
			chosen.append(option)
		else:
			break

		# print(f"option: {option}")
		# print("\n" + "_"*50 + "\n")

	attempts += 1

assert len(chosen) == len(guests), "Unable to find secret santa choices for \
                                    everyone"
print(f"\nTook {attempts} tries.\n")

for guest, option in current.items():
	history_dict[guest].append(option)

history_df = pd.DataFrame(history_dict)

print("This years Seceret Santa!")
for guest, option in current.items():
	print(f"{guest}: {option}")
	history_dict[guest].append(option)

print("\nPast Seceret Santas!")
print(tabulate(history_df, headers='keys', tablefmt='psql'))

history_df.to_csv("secret_santa.csv", index=False)
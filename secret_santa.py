import random as rd
import pandas as pd
import os

filename = "secret_santa.csv"
if os.path.exists(filename):
	history_df = pd.read_csv(filename)
	history_dict = history_df.to_dict(orient='list')
	guests = list(history_dict.keys())
else:
	guests = ["Mathew", "Sarah", "Brendan", "Hannah", "Awkward Waiter", "Plant Shop Witch", "Metal Market Vendor"]
	history_dict = {guest:[] for guest in guests}
	history_df = pd.DataFrame(history_dict)

current = {}
max_attempts = 0
for guest in guests:
	attempts = 0
	while attempts < 100:
		history = history_dict[guest]
		option = rd.choice(guests)

		if option != guest and option not in history:
			current[guest] = option
			break
		attempts += 1

for guest, option in current.items():
	history_dict[guest].append(option)

history_df = pd.DataFrame(history_dict)

print("This years Seceret Santa!")
for guest, option in current.items():
	print(f"{guest}: {option}")
	history_dict[guest].append(option)

print("\nPast Seceret Santas!")
print(history_df.to_string(index=False))

history_df.to_csv("secret_santa.csv", index=False)
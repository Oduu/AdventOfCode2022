def main():

	max_calories_index = 0
	max_calories = 0
	all_calories = []

	f = open("calories.txt", "r")

	lines = f.readlines()

	current_calories = 0
	current_index = 0

	for line in lines:
		if line.strip() == "":

			print(f"current_calories: {current_calories}")
			print(f"current_index: {current_index}")

			if max_calories < current_calories:
				max_calories = current_calories
				max_calories_index = current_index

			current_index += 1
			all_calories.append(current_calories)
			current_calories = 0
		else:
			current_calories += int(line.strip())

	print(f"The highest elf is carrying: {max_calories}")
	print(f"The highest elf index was: {max_calories_index}")

	print(f"The top 3 elves were carrying: {sorted(all_calories)[-3:]}")
	print(f"The total of the top 3 was {sum(sorted(all_calories)[-3:])}")


main()
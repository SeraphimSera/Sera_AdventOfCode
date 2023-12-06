with open("D7_Data.txt", 'r') as f:
	data = [int(n) for n in f.read().split(',')]

fuel_1 = {}
fuel_2 = {}
for i in data:
	if i not in fuel_1:
		fuel_1[i] = fuel_2[i] = 0
		for j in data:
			n = abs(i-j)
			fuel_1[i] += n
			fuel_2[i] += sum(range(1, n+1))

print(f"The least fuel required for part 1 is {sorted(fuel_1.values())[0]}")
print(f"The least fuel required for part 2 is {sorted(fuel_2.values())[0]}")

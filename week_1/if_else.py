strings = ["2", "6", "9", "1", "18", "11", "3"]

# 1. turn strings into numbers
# 2. find biggest number
# 3. find smallest number
# 4. find average
# time: 20 mins

numbers = [ ]

for n in strings:
    numbers.append(int(n))

max_num = max(numbers)
min_num = min(numbers)

average = int(sum(numbers) / len(numbers))

print("Maximum number is", max_num)
print("Minimum number is", min_num)
print("Average is",average)
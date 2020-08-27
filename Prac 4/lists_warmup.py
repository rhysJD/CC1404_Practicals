"""
Rhys Donaldson 13581558
lists warmup program
"""

numbers = [3, 1, 4, 1, 5, 9, 2]

# numbers[0] == 3
# numbers[-1] == 2
# numbers[3] == 1
# numbers[:-1] == [3, 1, 4, 1, 5, 9]
# numbers[3:4] == [1]
# 5 in numbers == 4
# 7 in numbers == invalid
# "3" in numbers == invalid
# numbers + [6, 5, 3] makes numbers == [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print(numbers[0],
numbers[-1],
numbers[3],
numbers[:-1],
numbers[3:4],
5 in numbers,
7 in numbers,
"3" in numbers,
numbers + [6, 5, 3])

numbers[1] = 'ten'
numbers[len(numbers) - 1] = 1
numbers[2:]
9 in numbers
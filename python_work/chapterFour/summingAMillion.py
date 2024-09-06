# Create an empty list
digits = []

# Create a for loop that builds and appends 1000000 numbers to my empty list
for i in range(1, 1_000_001):
    digits.append(i)

# Print the min, max, and sum of my completed list
print(min(digits))
print(max(digits))
print(sum(digits))

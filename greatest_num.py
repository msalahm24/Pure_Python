numbers=[2,9,8,7]
print(max(numbers))
greatest_is=numbers[0]
for item in numbers:
    if item>greatest_is:
        greatest_is=item
print(greatest_is)


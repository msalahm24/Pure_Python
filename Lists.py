# this ex for removing the duplicate from an list
numbers=[]
while True:
    user_input=input('enter number to add it for the list or p to print your unique list ')
    if user_input.lower()=='p':
        break
    elif user_input.lower() !='p':
        try:
            val=int(user_input)
            numbers.append(val)
        except ValueError:
            print(" i don't understand this")

print(numbers)
uniques=[]
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)




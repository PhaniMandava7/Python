nums = [1, 2, 3, 4, 5]

for num in nums:
    print(num)


# search for particular number in list and stop looping at that number
for num in nums:
    if num == 4:
        print(4,' is found')
        break
    else:
        print(4,' is not found->',num)

print()

# skip a particular number in the loop
for num in nums:
    if num == 4:
        print(4,' is found')
        continue
    else:
        print(4,' is not found ->', num)

print()


for num in nums:
    for letter in 'abc':
        print(num, '->', letter)
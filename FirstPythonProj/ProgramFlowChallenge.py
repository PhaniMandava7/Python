userInput = input("Please enter the IP address.")
sequenceCounter = 1
lengthCounter = 0
if len(userInput) == 0:
    print("Invalid input")
else:
    for char in userInput:
        if char == '.':
            print("{}th sequence has length of {}.".format(str(sequenceCounter), str(lengthCounter)))
            sequenceCounter += 1
            lengthCounter = 0
        else:
            lengthCounter += 1
    else:
        print("{}th sequence has length of {}.".format(str(sequenceCounter), str(lengthCounter)))

itemsList = ["chicken", "salmon", "crab", "beans", "spam"]
for item in itemsList:
    if item == "spam":
        print("Ignore spam")
        continue
    else:
        print(item)

nasty_item = ''
for item in itemsList:
    if item == "spam":
        nasty_item = item
        break
# else here would be useful as a block which would be executed if the break never happen.
else:
    print("I'll have a plate of it then.")
if nasty_item:
    print("Can I have anything else please.")

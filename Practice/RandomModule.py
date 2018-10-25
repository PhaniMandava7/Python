import random

val = random.random()  # --> returns a random value between 0-1.
print(val)

val = random.uniform(1,10)  # --> returns a random float value between specified range
print(val)

val=random.randint(1,6)  # --> returns a random int value between specified range
# print(val)

greetings = ['Hi', 'Hello', 'Hey']
val = random.choice(greetings)  # --> returns a random value from the list of objects.
print('{}, Phani'.format(val))

colors = ['Red','Black', 'White']
results=random.choices(colors,k=10)  # --> returns a list of 'k' randomly picked objects from specified list.
print(results)

results=random.choices(colors, weights=[10,10,4], k=10)  # --> returns the list of values according to weights assigned.
print(results)

deck=list(range(1,53))
random.shuffle(deck)   #  --> shuffles the list in-place
print(deck)

hand=random.sample(deck,k=5)  # --> returns a list of 'k' randomly selected  unique values from the list specified.
print(hand)
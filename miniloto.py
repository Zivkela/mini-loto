import random

lottery_numbers = []
for i in range(0,50):
  while len(lottery_numbers) < 7:
    element = int(input("enter your numbers: "))
    lottery_numbers.append(element)

lucky_numbers = random.sample(range(1,50), 7)
counter = []

print(sorted(lucky_numbers))
print(sorted(lottery_numbers))

for value in lucky_numbers:
  if value in lottery_numbers:
      if value not in counter:
        counter.append(value)

print(counter)

if len(counter) == 3:
  print("You got 3 numbers right")
elif len(counter) == 4:
  print("you got 4 numbers right")
elif len(counter) == 5:
  print("you got 5 numbers right")
elif len(counter) == 6:
  print("you got the 6 numbers right, that is awesome")
elif len(counter) == 7:
  print("Congratulations, you have just won the loterry!")
else:
  print("better luck next time")

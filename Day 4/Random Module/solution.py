import random

random_integer = random.randint(1, 10)
print(random_integer)
#including 1 and 10

random_number_0_to_1 = random.random() * 10
print(random_number_0_to_1)
#including 1 and 10
    #OR
random_float = random.uniform(1, 10)
print(random_float)
#including 1 and 10

random_heads_or_tails = random.randint(0, 1)
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")

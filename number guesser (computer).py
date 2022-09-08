# user sets random number
set_random = 8
while True:
    import random

    list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    random = random.choice(list1)
    print(random)
    if random == set_random:
        print('correct guess made')
        break
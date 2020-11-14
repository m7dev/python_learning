def say(message, times = 1):
    print(message * times)
say ('Привіт, ', 5)
say ('Привіт, ', times = 3)
say ('Hello!!!')

def say2(message):
    import random
    rand = random.randint(1, 10)
    print(message * rand)
say2 ('Wow!')
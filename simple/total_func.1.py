def total(initial = 0, *numbers, **keywords): #initial = 0 - виведе, якщо не буде даних

    for number in numbers:
        initial += number #initial = initial + number
    for key in keywords: #для значень vegetables=20, fruits=100
        initial += keywords[key] #initial = initial + keywords[key]
    return initial 

print(total(10, 1, 2, 3, vegetables=20, fruits=100))

def total(initial = 0, *numbers, **keywords): #initial = 0 - виведе, якщо не буде даних
    count = initial #10, 1, 2, 3,
    for number in numbers:
        count += number #count = count + number
    for key in keywords: #для значень vegetables=20, fruits=100
        count += keywords[key] #count = count + keywords[key]
    return count 

print(total(10, 1, 2, 3, vegetables=20, fruits=100))

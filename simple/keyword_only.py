def total(initial=0, *numbers, extra_number): 
    count = initial
    for number in numbers: #для чисел
        count += number
    count += extra_number #для передачі параметра по ключу
    print(count)

total(10, 1, 2, 3, extra_number=50)
def find_multiples(range_details):
    try:
        s = 0
        for number in range(range_details):
            if (number % 3 == 0 or number % 5 == 0):
                s = s + number
        return s

    except Exception as e:
        return e
#find_multiples(10)

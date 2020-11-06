def sum_of_even_feb_numbers(range_details):
    first_number =  1
    second_number = 1
    total_sum = 0
    try:
        while first_number <= range_details:
            if first_number % 2 == 0:
                total_sum += first_number
            first_number, second_number = second_number, first_number + second_number
        print(total_sum)
        return total_sum
    except Exception as e:
        return e
sum_of_even_feb_numbers(4000000)

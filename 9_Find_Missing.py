def find_missing_number(input_list):
    total_numbers = len(input_list) + 1
    expected_sum = total_numbers * (total_numbers + 1) // 2
    actual_sum = sum(input_list)
    missing_number = expected_sum - actual_sum
    return missing_number

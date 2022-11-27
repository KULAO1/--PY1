list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

index = 0
max_number = 0

for i, number in enumerate(list_numbers):
    if number >= max_number:
        max_number = number
        index = i
list_numbers[index], list_numbers[19] = list_numbers[19], list_numbers[index]


print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]

def get_unique_list_numbers() -> list[int]:
    ...  # TODO написать функцию для получения списка уникальных целых чисел
    import random
    from random import sample
    n = 15
    list_ = []
    for _ in range(n):
        random_ = random.randint(-10, 10)
        if random_ not in list_:
            list_.append(random_)

    return list_


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))

import random


def get_unique_list_numbers(begin_, end_, amount_) -> list[int]:

    list_ = []
    while amount_ > 0:
        random_ = random.randint(begin_, end_)
        if random_ not in list_:
            list_.append(random_)
            amount_ -= 1

    return list_


list_unique_numbers = get_unique_list_numbers(-10, 10, 15)
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))

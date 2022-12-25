import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter) -> list[dict]:
    with open(filename) as file:
        list_headers = file.readline().replace("\n", "").split(delimiter)
        list_values = [line_.replace("\n", "").split(delimiter) for line_ in file]
        list_dict = [dict(zip(list_headers, value)) for value in list_values]

        return list_dict


print(json.dumps(csv_to_list_dict(INPUT_FILE, ","), indent=4))

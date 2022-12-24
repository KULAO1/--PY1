import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter) -> list[dict]:
    with open(filename, encoding='unicode_escape') as file:
        i = 0
        list_dict = []
        for line_ in file:
            line_ = line_.replace("\n", "")
            if i == 0:
                list_headers = line_.split(delimiter)
                i += 1
                continue

            list_values = line_.split(delimiter)
            dict_ = {}
            for key, value in zip(list_headers, list_values):
                dict_[key] = value
            list_dict.append(dict_)
    return list_dict


print(json.dumps(csv_to_list_dict(INPUT_FILE, ","), indent=4))

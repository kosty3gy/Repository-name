import json

json_file = "input.json"


def task() -> float:
    with open(json_file) as f:
        data = json.load(f)
    summa = sum([item["score"] * item["weight"] for item in data])
    return round(summa, 3)


print(task())
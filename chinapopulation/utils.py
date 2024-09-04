import csv


def csv_as_list(fn: str) -> list[list[str]]:
    data_list: list[list[str]] = []
    with open(fn, "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # 跳过标题行
        for row in csv_reader:
            data_list.append(row)
    return data_list

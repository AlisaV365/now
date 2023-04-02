import json
from utils import get_last_operations, format_data


FILE = 'operations.json'


def main():
    with open(FILE, 'r', encoding='utf-8') as file:
        data = json.load(file)

    data = get_last_operations(data)

    for i in range(35):
        print(format_data(data[i]))
        print()


if __name__ == '__main__':
    main()
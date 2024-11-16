# TODO импортировать необходимые модули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task(csv_file: str, delimiter: str = ",", line_terminator: str = "\n") -> str:
    try:
        with open(csv_file, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=delimiter, lineterminator=line_terminator)
            data = [row for row in reader]
        json_data = json.dumps(data, indent=4, ensure_ascii=False)
        with open(OUTPUT_FILENAME, "w", encoding="utf-8") as output_file:
            output_file.write(json_data)
        return OUTPUT_FILENAME
    except FileNotFoundError:
        print(f"Файл '{csv_file}' не найден.")
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    result_file = task(INPUT_FILENAME)
    with open(result_file, "r", encoding="utf-8") as output_f:
        for line in output_f:
            print(line, end="")

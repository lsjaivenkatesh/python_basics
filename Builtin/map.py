number: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def convert_to_string(num: int) -> str:
    return str(num)

numbers_as_strings: list[str] = list(map(convert_to_string, number))

print(numbers_as_strings)
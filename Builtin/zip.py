num: tuple(int) = (1, 2, 3, 4, 5)
names: tuple[str] = ('Alice', 'Bob', 'Charlie', 'David', 'Eve')

zipped: list[tuple[int, str]] = list(zip(num, names))

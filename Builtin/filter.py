prople: list[str,int] = ['marfio', 'lugi',10, 'sofi', 20]

def is_str(element):
    return isinstance(element, str)

filtered_people: list[str] = list(filter(is_str, prople))

print(filtered_people)
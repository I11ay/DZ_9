def change(lst: list) -> list:
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst
a = ['subaru', 'bmw', 'fiat', 'golf', 'mazda', 'nissan']
print(change(a))

def to_dict(lst):
    a = {i:i for i in lst}
    return a


b = ['subaru', 'bmw', 'fiat', 'golf', 'mazda', 'nissan']
print(to_dict(b))

def sum_range(start: int, end: int):
    a = 0
    if start > end:
        start, end = end, start
    for i in range(start, end+1):
        a += i
    return a


print(sum_range(3, 8))

def read_last(lines, file):
    if lines > 0 and lines % 1 == 0:
        a = open(file, 'r')
        strings = a.readlines()[-lines:]
        for i in strings:
            print(i)
        a.close()
    else:
        print("Число должно быть целым и не быть отрицательным")


read_last(4, 'test.txt')

from pprint import pprint

data = [
    {'name': 'Test 1', 'position': 1},
    {'name': 'Test 2', 'position': 2},
    {'name': 'Test 3', 'position': 3},
    {'name': 'Test 4', 'position': 4}
]


def delete_pos(lst, position_number):
    lst.pop(position_number - 1)
    for i, i_value in enumerate(lst):
        i_value['position'] = (i + 1)
    return lst


pprint(delete_pos(data, 2))
print(' ')

data = [
    {'name': 'Test 1', 'position': 1},
    {'name': 'Test 2', 'position': 2},
    {'name': 'Test 3', 'position': 3},
    {'name': 'Test 4', 'position': 4}
]


def add_pos(lst, position_number, text_for_user_pos):
    new_dict = {'name': f'{text_for_user_pos} {len(lst) + 1}', 'position': None}
    lst.insert(position_number - 1, new_dict)

    for i, i_value in enumerate(lst):
        i_value['position'] = (i + 1)
    return lst


pprint(add_pos(data, 2, 'Rubick'))

print(' ')

data = [
    {'name': 'Test 1', 'position': 1},
    {'name': 'Test 2', 'position': 2},
    {'name': 'Test 3', 'position': 3},
    {'name': 'Test 4', 'position': 4}
]


def swap_pos(lst, pos_for_swap_1, pos_for_swap_2):
    if pos_for_swap_1 > pos_for_swap_2:
        pos_for_swap_1, pos_for_swap_2 = pos_for_swap_2, pos_for_swap_1
    lst.insert(pos_for_swap_1 - 1, lst[pos_for_swap_2 - 1])
    lst.pop(pos_for_swap_2)
    lst.insert(pos_for_swap_2, lst[pos_for_swap_1])
    lst.pop(pos_for_swap_1)

    for i, i_value in enumerate(lst):
        i_value['position'] = (i + 1)

    return lst


pprint(swap_pos(data, 1, 4))

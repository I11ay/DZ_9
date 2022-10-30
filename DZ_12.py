# import json
#
# fast_cars = {
#     'Car': 'Subaru',
#     'Speed': '354'
# }
# slow_cars = {
#     'Car': 'BMW',
#     'Price': '2$'
# }
# same_keys = {}
# for key, value in fast_cars.items():
#     for key1, value1 in slow_cars.items():
#         if key == key1:
#             same_keys[key1] = [value, value1]
#         else:
#             break
#
# various_keys = fast_cars | slow_cars
# result = various_keys | same_keys
#
# json_result = json.dumps(result)
# with open('result.json', 'w') as file:
#     file.write(json_result)

import pickle

cars = [
    {
        'car': 'Subaru',
        'speed': '342',
    },
    {
        'car': 'BMW',
        'speed': '256'
    }
]

file = open('car.fast', 'wb')
file.write(pickle.dumps(cars))
file.close()
class Human:
    def __init__(self, name, surname, age, phone, address):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone
        self.address = address

    def get_info(self):
        info = {'name': f'{self.name}', 'surname': f'{self.surname}', 'age': f'{self.age}', 'phone': f'{self.phone}',
                'address': f'{self.address}'}

        return info

    def call(self, phone_number):
        print(f'{self.phone} calls {phone_number}')


a = Human('Илья', 'Панченко', 29, '+38063457564', 'Одесса, Семена Палия 99, 25')
b = Human('Иван', 'Иванович', 43, '+38099564084', 'Одесса, Бочарова 12, 83')
c = Human('Николай', 'Германович', 22, '+38055657485', 'Одесса, Нежинская 43, 93')

print(a.get_info())
print(b.get_info())
print(c.get_info())

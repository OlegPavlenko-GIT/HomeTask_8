# Написать валидации с помощью регулярных выражений:
# 1  мобильный номер телефона (только цифры, возможное наличие плюса, длина номера)
import re
def find_valid_mobile_number(numbers):
    pattern = r'^\+380\d{9}$'
    for number in numbers:
        if re.match(pattern, number):
            return number
    return None
numbers = ['08880-000', '888777-000', '+380501000000', '123456789', '+380502222222', '7024375-5784375', '5999-009']
valid_number = find_valid_mobile_number(numbers)
if valid_number:
    print(f"Found valid mobile number: {valid_number}")
else:
    print("None of the numbers match the format.")
#
# 2 домашний номер телефона (только цифры и длина номера)
import re
def find_valid_home_number(numbers):
    pattern = r'^\d{10}$'
    for number in numbers:
        if re.match(pattern, number):
            return number
    return None
numbers = ['8889-999', '0567781919', '0567700-0', '12345678-90', '0569-881019']
valid_number = find_valid_home_number(numbers)
if valid_number:
    print(f"Found valid home number: {valid_number}")
else:
    print("None of the numbers match the format.")
#
# 3 email (наличие @, домена: gmail.com например, минимальная длина и максимальная на ваш выбор)
import re
def validate_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@gmail\.com$"
    if re.match(pattern, email):
        return True
    else:
        return False
emails = [
    "example@mail.com",
    "test123@uyuytuyf.com",
    "Hillel@gmail.com"
]
valid_emails = [email for email in emails if validate_email(email)]
print("Valid e-mail:")
for email in valid_emails:
    print(email)
#
# 4 ФИО клиента (3 слова, минимальная длина 2 символа, максимальная длина 20)
import re
def validate_client_name(name):
    pattern = r"^[A-Za-z]{2,20}\s[A-Za-z]{2,20}\s[A-Za-z]{2,20}$"
    if re.match(pattern, name):
        return True
    else:
        return False
clients = [
    "Bill Gates Americanovich",
    "M George Washingtonovich",
    "J Ghueorjh Uiu",
    "El Musk GreatSpaceXTeslavich"
]
valid_clients = [client for client in clients if validate_client_name(client)]
print("Valid clients:")
for client in valid_clients:
    print(client)
#
# 5 Пароль (минимально: одна большая буква, одна маленькая буква, одна цифра, один символ, длина пароля
# - от 8 до 16 символов)
import re
def validate_password(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$!%^&*()])[A-Za-z\d@#$!%^&*()]{8,16}$"
    if re.match(pattern, password):
        return True
    else:
        return False
passwords = [
    "somePasswword",
    "QWERTY12345",
    "Super1Password!"
]
valid_passwords = [password for password in passwords if validate_password(password)]
print("Valid password:")
for password in valid_passwords:
    print(password)
# Completed
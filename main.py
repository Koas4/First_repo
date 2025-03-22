import math


def break_password(password_length, num_possible_characters, break_speed):
    # Обчислюємо загальну кількість можливих паролів
    total_passwords = num_possible_characters ** password_length

    # Обчислюємо час у секундах для зламу всіх можливих паролів
    time_seconds = total_passwords / break_speed

    # Переводимо час у роки, місяці, дні, години, хвилини та секунди
    years = math.floor(time_seconds / 31536000)  # 1 рік = 31536000 секунд
    time_seconds %= 31536000
    months = math.floor(time_seconds / 2592000)  # 1 місяць = 2592000 секунд
    time_seconds %= 2592000
    days = math.floor(time_seconds / 86400)  # 1 день = 86400 секунд
    time_seconds %= 86400
    hours = math.floor(time_seconds / 3600)  # 1 година = 3600 секунд
    time_seconds %= 3600
    minutes = math.floor(time_seconds / 60)  # 1 хвилина = 60 секунд
    seconds = math.floor(time_seconds % 60)

    return years, months, days, hours, minutes, seconds


# Вхідні дані для тестування
test_cases = [
    {"password_length": 10, "num_possible_characters": 10, "break_speed": 1},
    {"password_length": 6, "num_possible_characters": 10, "break_speed": 1},
    {"password_length": 6, "num_possible_characters": 10, "break_speed": 4}
]

# Тестування та виведення результатів
for idx, test_case in enumerate(test_cases, start=1):
    years, months, days, hours, minutes, seconds = break_password(**test_case)
    print(
        f"Test Case {idx}: {years} рік(и) {months} місяц(ь) {days} дн(і) {hours} год(ин) {minutes} хв(илин) {seconds} сек(унд)")

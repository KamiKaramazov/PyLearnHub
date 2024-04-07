from datetime import datetime

def days_until_birthday(birthday_month, birthday_day):
    today = datetime.today()
    luffy_birthday = datetime(today.year, birthday_month, birthday_day)

    if luffy_birthday < today:
        luffy_birthday = datetime(today.year + 1, birthday_month, birthday_day)

    time_until_birthday = luffy_birthday - today
    return time_until_birthday

luffy_birthday_month = 5
luffy_birthday_day = 5
days_left = days_until_birthday(luffy_birthday_month, luffy_birthday_day)

print("Days until Luffy's birthday:", days_left)
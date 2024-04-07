from datetime import datetime

def calculate_days_until_birthday(birthdate):
    today = datetime.now()
    next_birthday_year = today.year

    if (today.month, today.day) > (birthdate.month, birthdate.day):
        next_birthday_year += 1

    next_birthday = datetime(next_birthday_year, birthdate.month, birthdate.day)
    days_until_birthday = (next_birthday - today).days
    return days_until_birthday

def calculate_age(birthdate):
    today = datetime.now()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def calculate_zodiac_sign(birthdate):
    zodiac_signs = [
        (1, 20, 'Capricorn'), (2, 19, 'Aquarius'), (3, 20, 'Pisces'), (4, 20, 'Aries'),
        (5, 21, 'Taurus'), (6, 21, 'Gemini'), (7, 22, 'Cancer'), (8, 22, 'Leo'),
        (9, 22, 'Virgo'), (10, 22, 'Libra'), (11, 21, 'Scorpio'), (12, 21, 'Sagittarius')
    ]
    month = birthdate.month
    day = birthdate.day
    for sign_month, sign_day, sign_name in zodiac_signs:
        if (month == sign_month and day <= sign_day) or (month == (sign_month % 12) + 1 and day > sign_day):
            return sign_name
    return None  

def parse_birthdate(birthdate_str):
    try:
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid birthdate format. Please enter in YYYY-MM-DD format.")
    return birthdate

def main():
    birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
    birthdate = parse_birthdate(birthdate_str)

    days_until_birthday = calculate_days_until_birthday(birthdate)
    print("Days until your next birthday:", days_until_birthday)

    age = calculate_age(birthdate)
    print("Your age:", age)

    zodiac_sign = calculate_zodiac_sign(birthdate)
    print("Your zodiac sign:", zodiac_sign)

if __name__ == "__main__":
    main()
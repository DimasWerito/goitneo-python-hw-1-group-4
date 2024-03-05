from datetime import datetime
from collections import defaultdict


def get_birthdays_per_week(users: list[dict]):
    """function that shows users birthdays next 7 days"""
    persons = defaultdict(list)
    today = datetime.today().date()
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year+1)
        delta_days = (birthday_this_year - today).days
        if delta_days < 7:
            week_day_num = birthday_this_year.weekday()
            if week_day_num in [5, 6, 0]:
                persons["Monday"].append(name)
            elif week_day_num == 1:
                persons["Tuesday"].append(name)
            elif week_day_num == 2:
                persons["Wednesday"].append(name)
            elif week_day_num == 3:
                persons["Thursday"].append(name)
            elif week_day_num == 4:
                persons["Friday"].append(name)
    info = ""
    for day, names in persons.items():
        info += f"{day}: {', '.join(names)}\n"
    print(info)


if __name__ == "__main__":
    users = [{"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
             {"name": "Bob Gates", "birthday": datetime(1955, 3, 8)},
             {"name": "Dmytro Krasilnykov", "birthday": datetime(1986, 3, 10)}]
    get_birthdays_per_week(users)
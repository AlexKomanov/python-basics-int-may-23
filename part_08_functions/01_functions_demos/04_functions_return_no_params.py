import datetime


def get_today_date():
    return datetime.date.today()


today = get_today_date()

print(today)

print(get_today_date())

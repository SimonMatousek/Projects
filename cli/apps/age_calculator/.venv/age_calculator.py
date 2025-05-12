from datetime import date


def calculate_age(birthdate) -> tuple[int]:
    today = date.today()
    age_year = today.year - birthdate.year -((today.month, today.day) < (birthdate.month, birthdate.day))
    
    if today.month < birthdate.month or (today.month == birthdate.month and today.day < birthdate.day):
        age_month = 12 - birthdate.month + today.month
    elif age_month == birthdate.month and today.day < birthdate.day:
        age_month = (12 - birthdate.month) + today.month -1
    else:
        age_month = today.month - birthdate.month
        
    if today.day < birthdate.day:
        month_before_today = today.month - 1 if today.month > 1 else 12
        days_in_month = 365 - (date(today.year, today.month, 1) - date(today.year, month_before_today, 1)).days
        age_days = days_in_month - (birthdate.day - today.day) 
    else:
        age_day = today.day - birthdate.day
    
    return(age_year, age_month,age_day)

def run():
    birthday: str = input("Enter your birthday (YYYY-MM-DD)")
    year, month, day = map(int, birthday.split("-"))
    birthdate = date(year, month, day) 
    
    age_year, age_month, age_day = calculate_age(birthdate)
    
    return f"You are {age_year} years, {age_month} months and {age_day} days old"
    
if __name__ == "__main__":
    result = run()
    print(result)
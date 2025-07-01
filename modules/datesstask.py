

# import datetime

# year = int(input("Enter your birth year: "))
# currentyear = datetime.datetime.now().year
# age = currentyear - year
# print("Your age is:", age)


# from datetime import datetime

# def calculate_age():
#     birth_date_str = input("Enter your birthdate (YYYY-MM-DD): ")
#     birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")
#     today = datetime.today()
    
#     # Calculate age
#     age = today.year - birth_date.year
    
#     # Adjust if birthday hasn't occurred yet this year
#     if (today.month, today.day) < (birth_date.month, birth_date.day):
#         age -= 1
    
#     print("Your age is:", age)

# calculate_age()

# import datetime

# year = int(input("Enter your birth year: "))
# month = int(input("Enter your birth month: "))
# day = int(input("Enter your birth day: "))

# birth_date = datetime.date(year, month, day)
# today = datetime.date.today()

# days_lived = (today - birth_date).days

# print("You have lived for", days_lived, "days.")


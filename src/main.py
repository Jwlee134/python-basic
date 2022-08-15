from random import randint
from requests import get

my_name = "Jaewon"
my_age = 26
my_color_eye = "brown"

print(
    f"Hello I'm {my_name} my age is {my_age}, {my_color_eye} is my eye color.")


def make_juice(fruit):
    return f"{fruit}+🥤"


def add_ice(juice):
    return f"{juice}+🧊"


def add_sugar(iced_juice):
    return f"{iced_juice}+🍭"


juice = make_juice("🍎")
iced_juice = add_ice(juice)
sugared_juice = add_sugar(iced_juice)

print(sugared_juice)

winner = 9

if winner > 10:
    print("winner is greater than 10")
elif winner < 10:
    print("winner is less than 10")
else:
    print("winner is 10")

pc_choice = randint(1, 100)

while True:
    user_choice = int(input("Choose a number(1-100): "))

    if user_choice == pc_choice:
        print("You won!")
        break
    elif user_choice > pc_choice:
        print("Lower!")
    elif user_choice < pc_choice:
        print("Higher!")

print("Jaewon".endswith("on"))

weeks = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
weeks.append("Sun")
print(weeks[1:3])  # specific range
print([week for week in weeks if week != "Mon"])  # filter
print([f"{week}-day" for week in weeks])  # map

urls = ["google.com", "naver.com", "https://github.com"]
urls = [url if url.startswith(
    "https://") else f"https://{url}" for url in urls]

results = {}

for url in urls:
    res = get(url)
    if res.status_code == 200:
        results[url] = "Ok"
    else:
        results[url] = "Failed"

print(results)

months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

while True:
    try:
        date = input("Date: ")
        if "/" in date:
            month, day, year = date.split("/")
        elif "," in date:
            month, day, year = date.split(" ")
            day = day.replace(",", "")
            month = months[month.title()]
        break
    except ValueError:
        pass

print(f"{year}-{month:02}-{day:02}")

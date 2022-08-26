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
        date = input("Date: ").strip()
        if "/" in date:
            month, day, year = date.split("/")
            month = int(month)
            month <= 12
            day = int(day)
            day <= 31
            break
        elif "," in date:
            month, day, year = date.split(" ")
            month = int(months[month.title()])
            month <= 12
            day = int(day.replace(",", ""))
            day <= 31
            break
    except (ValueError, KeyError):
        pass

print(f"{year}-{month:02}-{day:02}")
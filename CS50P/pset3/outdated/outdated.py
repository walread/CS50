while True:
    try:
        date = input("Date: ")
        if "/" in date:
            month, day, year = date.split("/")
        elif "," in date:
            month, day, year = date.split(" ")
            day = day.replace(",", "")
        break
    except ValueError:
        pass

print(month)
print(day)
print(year)

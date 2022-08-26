while True:
    try:
        month, day, year = input("Date: ").split("/" or ",")
        break
    except ValueError:
        pass

print(month)
print(day)
print(year)